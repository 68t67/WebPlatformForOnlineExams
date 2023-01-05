from django.urls import path

from . import views

app_name = 'exams'

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
    path(
        'exams/',
        views.ExamListView.as_view(),
        name='exam_list'
    ),
    path(
        'exam/<slug:slug>/details/',
        views.ExamDetailView.as_view(),
        name='exam_detail'
    ),
    path(
        'exam/<slug:slug>/progress/<int:pk>/',
        views.ExamProcessView.as_view(),
        name='exam_process'
    ),
]
