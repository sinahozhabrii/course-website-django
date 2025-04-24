from django.db import models
from cloudinary.models import CloudinaryField
import helpres

helpres.cloudinary_init()

class AccessRequirements(models.TextChoices):
    ANYONE = 'any','anyone'
    EMAIL_REQUIRED = 'email','email_required'

class PublishStatus(models.TextChoices):
    PUBLISHED = 'publish','published'
    COMING_SOON = 'soon','coming soon'
    DRAFT = 'draft','Draft'
# Create your models here.
class CourseModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    image = CloudinaryField('image',null=True)
    access = models.CharField(max_length=5,choices=AccessRequirements.choices,default=AccessRequirements.EMAIL_REQUIRED)
    status = models.CharField(max_length=7,choices=PublishStatus.choices,default=PublishStatus.DRAFT)
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
    def iamge_admin(self):
        if  not self.image:
            return ''
        image_options = {
            'width':200
        }
        url = self.image.build_url(**image_options)
        return url
    def get_image_thumbnail(self,as_html=False,width=500):
        if not self.image:
            return ""
        image_options = {
            'width':width
        }
        if as_html:
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options)
        return url
    
