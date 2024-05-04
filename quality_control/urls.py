from django.urls import path, re_path
from quality_control import views


app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bug_list, name='bug_list'), 
    path('features/', views.feature_list, name='feature_list'), 
    path('bugs/<int:bug_id>/',views.bug_detail,),
    path('features/<int:feature_id>/',views.feature_id_detail,),


    # path('',views.IndexView.as_view(), name = "index")
]