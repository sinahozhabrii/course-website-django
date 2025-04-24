from typing import Iterable
from django.db import models
from cloudinary.models import CloudinaryField
import helpres
import uuid
from django.utils.text import slugify

helpres.cloudinary_init()

class AccessRequirements(models.TextChoices):
    ANYONE = 'any','anyone'
    EMAIL_REQUIRED = 'email','email_required'

class PublishStatus(models.TextChoices):
    PUBLISHED = 'publish','published'
    COMING_SOON = 'soon','coming soon'
    DRAFT = 'draft','Draft'
# Create your models here.
def gen_public_id(instance):
    title = instance.title
    unique_id = str(uuid.uuid4()).replace('-','')
    if not title:
        return unique_id
    slug = slugify(title)
    unique_id_short = unique_id[:5]
    return f'{title}-{unique_id_short}'


class CourseModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    public_id = models.CharField(max_length=130)
    image = CloudinaryField('image',blank=True,null=True,public_id_prefix=)
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
    def save(self):
        if self.public_id == '' or self.public_id == None:
            self.public_id = gen_public_id(self)
        super().save()
    
class lessonModel(models.Model):
    course = models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = CloudinaryField('image',blank=True,null=True,)
    video = CloudinaryField('video',blank=True,null=True,resource_type='video')
    can_preview = models.BooleanField(default=False,help_text='if user do not have access to course can they see this?')
    status = models.CharField(max_length=7,choices=PublishStatus.choices,default=PublishStatus.DRAFT)
    ordering = models.IntegerField(default=0)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['ordering','-datetime_updated']