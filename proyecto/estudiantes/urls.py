from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'estudiantes'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create-student', views.CreateStudent.as_view(), name='create-student'),
    path('list-student', views.listStudent, name='list-student'),
    url(r'^edit-student/(?P<pk>\d+)/$', views.EditStudent.as_view(), name="edit-student"),    
    path('delete-student/<int:id>/', views.deleteStudent, name='delete-student'),

]