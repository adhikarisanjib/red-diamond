from django.contrib import admin

from website.models import (
    AboutCompany,
    ContactInfo,
    OurTeam,
    ServiceImages,
    Services,
    StaticImages,
    SubServices,
)

admin.site.register(AboutCompany)
admin.site.register(ContactInfo)
admin.site.register(Services)
admin.site.register(SubServices)
admin.site.register(ServiceImages)
admin.site.register(OurTeam)
admin.site.register(StaticImages)
