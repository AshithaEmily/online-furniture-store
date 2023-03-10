from django.urls import path
from furnitureweb import views


urlpatterns=[
    path('', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('discategory/<itemcatg>', views.discategory, name="discategory"),
    path('coffeedetails/<int:dataid>/', views.coffeedetails, name="coffeedetails"),
    path('pagelogin/', views.pagelogin, name="pagelogin"),
    path('logindata/', views.logindata, name="logindata"),
    path('registerdata', views.registerdata, name="registerdata"),
    path('logoutp/', views.logoutp, name="logoutp"),
    path('contactsave/',views.contactsave,name="contactsave")


]