from asyncio import proactor_events
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
    return f'{slug}-{unique_id_short}'

def get_public_id_prefix(instance):
    if hasattr(instance,'path'):
        path = instance.path
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        return path
    public_id = instance.public_id
    instance_class = instance.__class__
    instance_class_name = instance_class.__name__
    model_name_slug = slugify(instance_class_name)
    if not public_id:
        return f'{model_name_slug}'
    return f'{model_name_slug}/{public_id}'


def get_display_name(instance):
    if hasattr(instance,'get_display_name'):
        return instance.get_display_name()
    elif hasattr(instance,'title'):
        return instance.title
    instance_class = instance.__class__
    instance_class_name = instance_class.__name__
    return f'{instance_class_name}-upload'

class CourseSubject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title
class CourseModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    subject = models.ForeignKey(CourseSubject,on_delete=models.PROTECT,related_name='courses',)
    public_id = models.CharField(max_length=130,blank=True,null=True)
    image = CloudinaryField('image',blank=True,null=True,
                            
                            public_id_prefix=get_public_id_prefix,

                            display_name=get_display_name,

                            tags=['course','thumbnail'])
    
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
  
    def get_display_name(self):

        return f'{self.title}-course'
    @property
    def path(self):
        return f'/course/{self.public_id}'
    
    def get_absolute_url(self):
        return self.path
    
    @property
    def display_image(self):
        image_url = helpres.get_cloudinary_image_obj(self,as_html=False,field_name='image')
       
        return image_url
    @property
    def email_required(self):
        return self.access == AccessRequirements.EMAIL_REQUIRED


    def save(self,*args, **kwargs):
        if self.public_id == '' or self.public_id == None:
            self.public_id = gen_public_id(self)
        super().save(*args, **kwargs)
    
class lessonModel(models.Model):
    course = models.ForeignKey(CourseModel,on_delete=models.CASCADE,related_name='lesson_set')
    title = models.CharField(max_length=120)
    description = models.TextField()
    public_id = models.CharField(max_length=130,blank=True,null=True)
    thumbnail = CloudinaryField('image',blank=True,null=True,
                            
                            public_id_prefix=get_public_id_prefix,

                            display_name=get_display_name,
                            
                            tags=['lesson','thumbnail'])
    
    video = CloudinaryField('video',blank=True,null=True,resource_type='video',
                            
                            public_id_prefix=get_public_id_prefix,

                            display_name=get_display_name,

                            type = 'private'
                            
                            )
    
    can_preview = models.BooleanField(default=False,help_text='if user do not have access to course can they see this?')
    status = models.CharField(max_length=7,choices=PublishStatus.choices,default=PublishStatus.DRAFT)
    access = models.CharField(max_length=5,choices=AccessRequirements.choices,default=AccessRequirements.EMAIL_REQUIRED)
    ordering = models.IntegerField(default=0)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['ordering','-datetime_updated']
    
    def save(self,*args, **kwargs):
        if self.public_id == '' or self.public_id == None:
            self.public_id = gen_public_id(self)
        super().save(*args, **kwargs)

    def get_display_name(self):

        return f'{self.title}-{self.course.get_display_name()}'
    @property
    def path(self):
        course_path = self.course.path
        if course_path.endswith('/'):
            course_path = course_path[:-1]
        return f'{course_path}/lessons/{self.public_id}'
    
    def get_absolute_url(self):
        return self.path
    
    @property
    def email_required(self):
        return self.access == AccessRequirements.EMAIL_REQUIRED
    @property
    def display_image(self):
        image_url = helpres.get_cloudinary_image_obj(self,as_html=False,field_name='thumbnail',width=200,height=200)
       
        return image_url