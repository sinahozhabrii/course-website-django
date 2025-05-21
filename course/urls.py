from django.urls import path
from . import views



urlpatterns = [
    path('',views.course_list_view,name='course-list'),
    path('<str:subject>/',views.course_list_subject_view,name='course-list-subject'),
    path('<slug:course_public_id>/',views.course_detail_view,name='course-detail'),
    path('<slug:course_public_id>/lessons/<slug:lesson_public_id>',views.lesson_detail_view,name='lesson-detail')

]