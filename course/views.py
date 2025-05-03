from django.http import JsonResponse
from django.shortcuts import render
from . import services
from . import models
import helpres

# Create your views here.
def course_list_view(request):
    courses = services.get_course_list()
    
    # return JsonResponse({'id':[x.path for x in courses]})
    return render(request,'course/course_list.html',{'courses':courses})

def course_detail_view(request,course_public_id):
    course_obj = services.get_course_detail(course_public_id)
    lessons = services.get_course_lessons(course_obj)

    # return JsonResponse({'course_id':course_obj.id,'lesson_path':[x.id for x in lessons]},safe=False)

    return render(request,'course/course_detail.html',{'course':course_obj,'lessons':lessons})

def lesson_detail_view(request,course_public_id,lesson_public_id):
    lesson_obj = services.get_lesson_detail(course_public_id,lesson_public_id)

    template_name= 'course/lesson_detail_comingsoon.html'

    if lesson_obj.status == models.PublishStatus.PUBLISHED:
        template_name = 'course/lesson_detail.html'

    # return JsonResponse({'id':lesson_obj.id})
    video_html = helpres.get_cloudinary_video_obj(lesson_obj,as_html=True,field_name='video',width=1250 )
    return render(request,template_name,{'lesson':lesson_obj,'video_html':video_html})