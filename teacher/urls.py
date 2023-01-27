from django.urls import path, include
from teacher import views

urlpatterns = [
    path('t_list', views.teacher_list,name='teacher_list'),
    path('', views.index,name='home'),
    path('import', views.import_data,name='import'),
    path('simple_upload', views.simple_upload,name='simple_upload'),
    path('/details/<int:pk>', views.teacher_detail,name='details'),
    #path('update_detail/<int:id>', views.update_detail,name='update_detail'),
]

app_name = 'teacher'