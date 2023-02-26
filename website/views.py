from django.shortcuts import render

from website.forms import ContactForm
from website.models import (
    AboutCompany,
    ContactInfo,
    OurTeam,
    Services,
    StaticImages,
    SubServices,
)


def home_view(request, *args, **kwargs):
    context = {}

    services = Services.objects.all()
    context["services"] = services

    members = OurTeam.objects.all()
    context["members"] = members

    about = AboutCompany.objects.all().first()
    context["about"] = about

    about_image = StaticImages.objects.filter(type__icontains="about").first()
    context["about_image"] = about_image

    crousal_images = StaticImages.objects.filter(type__icontains="crousal")[:4]
    context["crousal_images"] = crousal_images

    parallex_image = StaticImages.objects.filter(type__icontains="parallex").first()
    context["parallex_image"] = parallex_image

    return render(request, "website/home_page.html", context)


def about_view(request, *args, **kwargs):
    context = {}

    members = OurTeam.objects.all()
    context["members"] = members

    services = Services.objects.all()
    context["services"] = services

    return render(request, "website/about_page.html", context)


def contact_view(request, *args, **kwargs):
    context = {}

    services = Services.objects.all()
    context["services"] = services

    contact_form = ContactForm(request.POST or None)
    if request.method == "POST":
        if contact_form.is_valid():
            contact_form.save()

    context["form"] = contact_form
    return render(request, "website/contact_page.html", context)


def services_view(request, type=None, id=None, *args, **kwargs):
    context = {}

    if not type:
        context["all"] = True
        services = Services.objects.all()
        context["services"] = services
    elif type == "service":
        service = Services.objects.get(id=id)
        context["service"] = service
        services = Services.objects.all()
        context["services"] = services
    elif type == "sub_service":
        sub_service = SubServices.objects.get(id=id)
        context["sub_service"] = sub_service
        services = Services.objects.all()
        context["services"] = services
    return render(request, "website/services_page.html", context)


def customer_contact_info_view(request, *args, **kwargs):
    context = {}

    services = Services.objects.all()
    context["services"] = services

    contacts = ContactInfo.objects.all()
    context["contacts"] = contacts

    return render(request, "website/customer_contact.html", context)
