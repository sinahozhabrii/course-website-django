
from cloudinary import CloudinaryImage
from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
class LessonInline(admin.StackedInline):
    model = models.lessonModel
    extra = 0
    readonly_fields = ['public_id']
    
@admin.register(models.CourseModel)
class CouserAdmin(admin.ModelAdmin):
    list_display = ['title','access','status']
    fields = ['public_id','title','description','image','access','status','image_perview']
    list_per_page = 10
    inlines = [LessonInline,]
    readonly_fields = ['image_perview','public_id']

    def image_perview(self,obj):
        image_url = obj.image.url
        cloudinary_id = str(obj.image)
        cloudinary_html = CloudinaryImage(cloudinary_id).image(width=500)
        print(image_url)
        return format_html(cloudinary_html)