from django.http import JsonResponse
from django.shortcuts import redirect, render
from . import services
from . import models
import helpres
from django.core.paginator import Paginator

# Create your views here.
def course_list_view(request):
    courses,subjects = services.get_course_list()
    
    # return JsonResponse({'id':[x.path for x in courses]})
    paginator = Paginator(courses, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'course/course_list.html',{'courses':page_obj,"subjects":subjects,'courses_count':courses.count()})

def course_list_subject_view(request,subject):
    courses,subjects = services.get_course_subject_list(subject)
    paginator = Paginator(courses, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'course/course_list.html',{'courses':page_obj,'subjects':subjects,'courses_count':courses.count()})
    
    # return JsonResponse({'id':[x.path for x in courses]})
    paginator = Paginator(courses, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'course/course_list.html',{'courses':page_obj})


def course_detail_view(request,course_public_id):
    course_obj = services.get_course_detail(course_public_id)
    lessons = services.get_course_lessons(course_obj)
    template = 'course/course_detail.html'
    if course_obj.email_required and not request.session.get('email_id'):
        request.session['next_url'] = course_obj.path
        template = 'course/course_email_req.html'
    # return JsonResponse({'course_id':course_obj.id,'lesson_path':[x.id for x in lessons]},safe=False)

    return render(request,template,{'course':course_obj,'lessons':lessons})

def lesson_detail_view(request,course_public_id,lesson_public_id):
    lesson_obj = services.get_lesson_detail(course_public_id,lesson_public_id)

    if lesson_obj.email_required and not request.session.get('email_id'):
        request.session['next_url'] = lesson_obj.path
        return redirect('/login')

    template_name= 'course/lesson_detail_comingsoon.html'

    if lesson_obj.status == models.PublishStatus.PUBLISHED:
        template_name = 'course/lesson_detail.html'
   
    # return JsonResponse({'id':lesson_obj.id})
    video_html = helpres.get_cloudinary_video_obj(lesson_obj,as_html=True,field_name='video',width=1035 )
    return render(request,template_name,{'lesson':lesson_obj,'video_html':video_html})


