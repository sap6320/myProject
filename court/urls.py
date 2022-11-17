from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='home'),
    path("register/",views.register,name="register"),
	path("login/",views.login,name="login"),
	path("logout/",views.logout,name="logout"),
	path("booking/logout/",views.logout,name="logout"),
	path("aboutus/",views.aboutus,name="aboutus"),
	path("booking/",views.booking_page,name="booking"),
	path("<int:court_id>/court_detail/",views.court_description_page,name="courtdesc"),
	path("<int:user_id>/book_detail/",views.booking_description_page,name="bookdesc"),
	path("status/",views.status_page,name="status"),
	path("<int:court_id>/court_status/",views.court_status_page,name="courtstatus")
]