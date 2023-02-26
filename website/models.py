from distutils.command.upload import upload

from django.db import models


class AboutCompany(models.Model):
    heading = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return self.heading


class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=14)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


def set_image_name(self, filename):
    return f"{self.service.id}/{filename}"


class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SubServices(models.Model):
    service = models.ForeignKey(
        Services,
        on_delete=models.CASCADE,
        related_name="services",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceImages(models.Model):
    service = models.ForeignKey(
        SubServices,
        on_delete=models.CASCADE,
        related_name="sub_services",
    )
    image = models.ImageField(
        upload_to=set_image_name,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.service.name


STATIC_IMAGE_TYPE = (
    ("parallex", "parallex"),
    ("crousal", "crousal"),
    ("about", "about"),
)


def get_static_image(self, filename):
    return f"ststic_images/{filename}"


class StaticImages(models.Model):
    heading = models.CharField(max_length=125, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=15, choices=STATIC_IMAGE_TYPE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.type}-{self.image}"


def get_team_image(self, filename):
    return f"ourteam/{filename}"


DEPT_CHOICES = (
    ("construction", "construction"),
    ("info", "info"),
)


class OurTeam(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    department = models.CharField(max_length=15, choices=DEPT_CHOICES, null=True)
    position = models.CharField(max_length=31, blank=True, null=True)
    image = models.ImageField(upload_to=get_team_image)

    def __str__(self):
        return self.name
