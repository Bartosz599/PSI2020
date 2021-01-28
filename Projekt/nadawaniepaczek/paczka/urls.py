from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('dostawcy/', views.DostawcaList.as_view(), name=views.DostawcaList.name),
    path('dostawcy/<int:pk>', views.DostawcaDetails.as_view(), name=views.DostawcaDetails.name),
    path('madawcy/', views.NadawcaList.as_view(), name=views.NadawcaList.name),
    path('nadawcy/<int:pk>', views.NadawcaDetails.as_view(), name=views.NadawcaDetails.name),
    path('odbiorcy/', views.OdbiorcaList.as_view(), name=views.OdbiorcaList.name),
    path('odbiorcy/<int:pk>', views.OdbiorcaDetails.as_view(), name=views.OdbiorcaDetails.name),
    path('paczki/', views.PaczkaList.as_view(), name=views.PaczkaList.name),
    path('paczki/<int:pk>', views.PaczkaDetails.as_view(), name=views.PaczkaDetails.name),
    path('zamowienia/', views.ZamowienieList.as_view(), name=views.ZamowienieList.name),
    path('zamowienia/<int:pk>', views.ZamowienieDetails.as_view(), name=views.ZamowienieDetails.name),
    path('harmonogramypracy/', views.HarmonogrampracyList.as_view(), name=views.HarmonogrampracyList.name),
    path('harmonogramypracy/<int:pk>', views.HarmonogrampracyDetails.as_view(), name=views.HarmonogrampracyDetails.name)

]

