
from cloudinary import CloudinaryImage
from django.contrib import admin
from . import models
from django.utils.html import format_html
import helpres

# Register your models here.
class LessonInline(admin.StackedInline):
    model = models.lessonModel
    extra = 0
    readonly_fields = ['public_id','display_image','display_video']
    def display_image(self,obj):
        image_url = helpres.get_cloudinary_image_obj(obj,as_html=False,width=300,field_name='thumbnail',)
        
        return format_html(f"<image src={image_url} />")
    
    def display_video(self,obj):
        video_html = helpres.get_cloudinary_video_obj(obj,as_html=True,field_name='video',width=550 )
        
        return video_html

@admin.register(models.CourseModel)
class CouserAdmin(admin.ModelAdmin):
    list_display = ['title','access','status']
    fields = ['public_id','title','description','subject','image','access','status','display_image']
    list_per_page = 10
    inlines = [LessonInline,]
    readonly_fields = ['display_image','public_id']

    def display_image(self,obj):
        image_url = helpres.get_cloudinary_image_obj(obj,as_html=False,width=300,field_name='image',)
       
        return format_html(f"<image src={image_url} />")
    
@admin.register(models.CourseSubject)
class CourseSubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    