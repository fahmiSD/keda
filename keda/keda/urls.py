"""
URL configuration for keda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website.views import *
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('solution/', solution, name='solution'),
    path('consultation/', consultation, name='consultation'),
    path('processOverview/', processOverview, name='processOverview'),
    path('processBrief/', processBrief, name='processBrief'),
    path('processScope/', processScope, name='processScope'),
    path('processEstimation/', processEstimation, name='processEstimation'),
    path('processDevelopment/', processDevelopment, name='processDevelopment'),
    path('processSupport/', processSupport, name='processSupport'),
    path('processNextSteps/', processNextSteps, name='processNextSteps'),
    path('aboutCareer/', aboutCareer, name='aboutCareer'),
    path('aboutTechnologies/', aboutTechnologies, name='aboutTechnologies'),
    path('detailBlog/<slug:slug_blog>', detailBlog, name='detailBlog'),
    path('project/', project, name='project'),
    path('detailProject/', detailProject, name='detailProject'),
    path('aboutStory/', aboutStory, name='aboutStory'),
    path('aboutTeam/', aboutTeam, name='aboutTeam'),
    path('detailCareer/<slug:slug_career>', detailCareer, name='detailCareer'),
    path('processOverview/', process, name='processOverview'),
    path('blog/', blog, name="blog"),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
