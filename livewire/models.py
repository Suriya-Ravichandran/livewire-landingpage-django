from django.db import models

class Enroll(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)

    course = models.CharField(max_length=50)

    adhaarcard = models.FileField(upload_to="adhaar_cards/",null=True, blank=True)
    photo = models.ImageField(upload_to="student_photos/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course}"


class StudentProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="project_thumbnails/")
    project_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)