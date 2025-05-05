from pickle import FALSE
from . import models
from django.core.mail import send_mail
from config import settings
from django.utils import timezone

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

def email_verification_event(email):
    email_obj,created = models.Email.objects.get_or_create(
                email=email
            )
    email_event_obj = models.EmailVerificationEvent.objects.create(
        parent=email_obj,email=email
    )
    subject = 'verifi your email'
    text_msg = verifiction_email_msg(email_event_obj)
    to_user_email = email

    did_send =send_mail(
    subject,
    text_msg,
    EMAIL_HOST_USER,
    [to_user_email],
    fail_silently=False,
)
    return email_event_obj,did_send

def verifiction_email_msg(obj,as_html=False):
    if not isinstance(obj,models.EmailVerificationEvent):
        return None
    
    if as_html:
        return f"<h1>{obj.verifey_link}</h1>"
    return f"pls click on this link to verify\n{obj.verifey_link}"

def verifey_token(token,max_attempts=5):
    qs = models.EmailVerificationEvent.objects.filter(token=token)
    if not qs.exists() or not qs.count() ==1:
        return False, 'invalid token'
    
    has_token_expired = qs.filter(expired=True)
    if has_token_expired.exists():
        return False, 'token expired, try again'
    
    max_attempts_reached = qs.filter(attempts__gte=max_attempts)
    if max_attempts_reached.exists():
        return False, 'token expired, max attempts reached'
    
    obj = qs.first()
    if obj is None:
        return None
    obj.attempts += 1
    obj.last_attempt_at = timezone.now()
    if obj.attempts > max_attempts:
        obj.expired = True
        obj.expired_at = timezone.now()
    obj.save()

    return True, 'welcome'
    