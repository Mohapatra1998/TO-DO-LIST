from django.urls import path
from TO_DO_APP import views

# app_name='Auth_App'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('work', views.workFilter, name='work'),
    path('add-work', views.workAdd, name="workadd"),
    path('update-work', views.workUpdate, name="workupdate"),
     path('delete', views.deleteWork, name='delete'),
    path('work-details', views.workDetails, name='workdetails'),

]