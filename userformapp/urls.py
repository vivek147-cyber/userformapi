from django.urls import path
from .import views

urlpatterns = [

    path("user-form/", views.CreateView.as_view(), name='user_create'),
    # path("get-user-form-data/",views.getdataView.as_view(),name="get_user_view"),
    # path("show-user-forms/", views.course, name="course"),
    
] 