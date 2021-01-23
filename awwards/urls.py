from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'^$',views.Index_view,name="index_view"),
    re_path(r'^upload/$',views.Upload_Project,name="upload_project"),
    
    re_path(r'^rating/(?P<pk>\d+)$',views.RateProject,name="rate_project"),
    re_path(r'^myprofile/',views.User_Profile,name="my_profile"),
    re_path(r'^devcenter/',views.Dev_center,name="dev_center"),
    re_path('^api/projects/$',views.ProjectList.as_view(),name="all_projects_api"),
    re_path('^ajax/rate/(?P<pk>\d+)',views.AjaxRating,name="ajaxrating"),
]