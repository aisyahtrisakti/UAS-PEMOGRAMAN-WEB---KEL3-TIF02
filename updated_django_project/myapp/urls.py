from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('member_profile/', views.member_profile, name='member_profile'),
    path('message/', views.message, name='message'),
    path('official/', views.official, name='official'),
    path('project_profile/', views.project_profile, name='project_profile'),
    path('proyek/', views.proyek, name='proyek'),
    path('', views.dashboard, name='home'), 
    path('api/setproject/', views.SetProjectView.as_view(), name='api-setproject'),
    path('api/setreadyproject/', views.SetReadyProjectView.as_view(), name='api-setreadyproject'),
    path('api/statuscompletion/ie/', views.StatusCompletionIEView.as_view(), name='api-statuscompletion-ie'),
    path('api/statuscompletion/ic/', views.StatusCompletionICView.as_view(), name='api-statuscompletion-ic'),
    path('api/statuscompletion/imp/', views.StatusCompletionIMPView.as_view(), name='api-statuscompletion-imp'),
]
