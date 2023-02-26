from django.urls import path

from website.views import (
    about_view,
    contact_view,
    customer_contact_info_view,
    home_view,
    services_view,
)

app_name = "website"

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("services/", services_view, name="services"),
    path("services/<str:type>/<int:id>/", services_view, name="services"),
    path("customer_info/", customer_contact_info_view, name="customer-info"),
]
