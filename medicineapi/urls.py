from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='sign_up'),
    path('login',views.login,name='log_in'),
    path('create',views.create_data,name='createdata'),
    path('retrive',views.retrive_data,name='retrivedata'),
    path('<int:id>/update',views.update_data,name='updatedata'),
    path('<int:id>/delete',views.delete_data,name='deletedata'),
    path('search/<str:query>/', views.search_data, name='searchdata'),
]