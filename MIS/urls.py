"""MIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from college import views, HODviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminPage', views.adminPage),
    path('adminLogin', views.adminLogin),
    path('staffLogin', views.staffLogin),
    path('studentLogin', views.studentLogin),
    path('adminRegister', views.adminRegister),
    path('staffRegister', views.staffRegister),
    path('studentRegister', views.studentRegister),
    path('adminLogout', views.adminLogout),
    path('staffLogout', views.staffLogout),
    path('studentLogout', views.studentLogout),
    path('admin_home', HODviews.admin_home),
    path('add_staff', HODviews.add_staff),
    path('add_staff_save', HODviews.add_staff_save),
    path('add_course', HODviews.add_course),
    path('add_course_save', HODviews.add_course_save),
    path('add_student', HODviews.add_student),
    path('add_student_save', HODviews.add_student_save),
    path('add_subject', HODviews.add_subject),
    path('add_subject_save', HODviews.add_subject_save),
    path('manage_staff', HODviews.manage_staff),
    path('manage_student', HODviews.manage_student),
    path('manage_course', HODviews.manage_course),
    path('delete_staff/<int:id>', HODviews.delete_staff),
    path('delete_course/<int:id>', HODviews.delete_course),
    path('delete_subject/<str:id>', HODviews.delete_subject),
    path('manage_subject', HODviews.manage_subject),
    path('edit_staff/<int:id>', HODviews.edit_staff),
    path('edit_student/<int:id>', HODviews.edit_student),
    path('edit_course/<int:id>', HODviews.edit_course),
    path('edit_subject/<str:id>', HODviews.edit_subject),
    path('edit_staff_save', HODviews.edit_staff_save),
    path('edit_student_save', HODviews.edit_student_save),
    path('edit_course_save', HODviews.edit_course_save),
    path('edit_subject_save', HODviews.edit_subject_save),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
