"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.log,name='login'),
    path('ad',views.admin,name='ad'),
    path('tr',views.teacher,name='tr'),
    path('st',views.student,name='st'),
    path('addtr',views.tradd,name='addtr'),
    path('trview',views.viewtr,name='trview'),
    path('trdel/<int:id>',views.deltr,name='trdel'),
    path('studview',views.viewstud,name='studview'),
    path('studapp/<int:id>',views.apprstud,name='studapp'),
    path('rej/<int:id>',views.rejstud,name='rej'),
    path('logout',views.out,name='logout'),
    path('tredit/<int:id>',views.tredit,name='tredit'),
    path('trprofile',views.viewprofiletr,name='trprofile'),
    path('studviewtr',views.viewstudtr,name='studviewtr'),
    path('editstud/<int:id>',views.editstud,name='editstud'),
    path('trpass',views.trpass,name='trpass'),
    path('stpass',views.studpass,name='stpass'),
    path('stprofile',views.viewstudprof,name='stprofile'),
    path('edit',views.edit,name='edit'),
    path('viewtrstud',views.viewtrstud,name='viewtrstud')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

