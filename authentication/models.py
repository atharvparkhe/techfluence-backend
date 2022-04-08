from django.db import models
from django.forms import FileField
from base.models import *
from .validators import *


class OrganisersModel(BaseUser):
    photo = models.ImageField(upload_to="organiser", height_field=None, width_field=None, max_length=None, null=True)
    token = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name


class CollegeModel(BaseModel):
    college_name = models.CharField(max_length=50)
    def __str__(self):
        return self.college_name


class AddOrganiserModel(BaseModel):
    file = models.FileField(upload_to="organiser_excel", max_length=100)


class ParticipantsModel(BaseUser):
    college = models.ForeignKey(CollegeModel, related_name="student_college", on_delete=models.CASCADE)
    vaccination = models.FileField(upload_to="vaccination", max_length=100, null=True, blank=True, validators=[validate_file_extension_2, validate_file_size])
    aadhar = models.FileField(upload_to="aadhar", max_length=100, null=True, blank=True, validators=[validate_file_extension_2, validate_file_size])
    def __str__(self):
        return self.name


class TeamModel(BaseModel):
    name = models.CharField(max_length=50)
    size = models.PositiveSmallIntegerField()
    members = models.ManyToManyField(ParticipantsModel)