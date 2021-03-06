
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FishJournal_detail, name='fj2'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('listview/', views.listView, name="listview"),
    path('<str:id>', views.detailView, name="detailview"),
    path('<str:id>/update', views.updateView, name="updateview"),
    path('<str:id>/delete', views.delete, name="delete"),
    # path('map/', views.plotting, name="map"),
    # path('', views.total, name="total"),
]
