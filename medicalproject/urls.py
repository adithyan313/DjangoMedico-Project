from django.urls import path,include
from medicalstorapp import views

urlpatterns = [
    path('',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login'),
    path('logouts/',views.log_out,name='logout'),
    path('create/',views.medical_create,name='create'),
    path('retrive/',views.retrive_medi,name='retrive'),
    path('update/<int:id>/',views.update_medi,name='update'),
    path('delete/<int:id>/',views.delete_medi,name='delete'),
    path('search/',views.medicine_search,name='medicine_search'),
    path('search/results/<str:query>/',views.search_results,name='search_results'),
    path('medicineapi/',include('medicineapi.urls'))
]
