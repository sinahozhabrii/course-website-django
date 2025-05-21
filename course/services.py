from django.shortcuts import get_object_or_404
from . import models
def get_course_list():
    course_q_list = models.CourseModel.objects.filter(status__in=[models.PublishStatus.PUBLISHED,models.PublishStatus.COMING_SOON])
    subjects = models.CourseSubject.objects.all()
    return course_q_list,subjects

def get_course_subject_list(subject):
    course_q_list = models.CourseModel.objects.select_related('subject').filter(status__in=[models.PublishStatus.PUBLISHED,models.PublishStatus.COMING_SOON],subject__title=subject)
    subjects = models.CourseSubject.objects.all()
    return course_q_list,subjects

def get_course_detail(course_public_id):
    if not course_public_id:
        return None
    course_obj = get_object_or_404(models.CourseModel.objects.prefetch_related('lesson_set'),public_id=course_public_id)
    return course_obj

def get_course_lessons(course_obj):
    # if not course_obj:
    #     return None
    lessons_qlist = course_obj.lesson_set.filter(status__in=[models.PublishStatus.PUBLISHED,models.PublishStatus.COMING_SOON])
    return lessons_qlist

def get_lesson_detail(course_public_id,lesson_public_id):
    if not course_public_id and lesson_public_id:
        return None
    lesson_obj = get_object_or_404(models.lessonModel,course__public_id=course_public_id,public_id=lesson_public_id)
    return lesson_obj
