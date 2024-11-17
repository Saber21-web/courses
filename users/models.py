from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name="enrolled_users")
    progress = models.JSONField(default=dict)  

    def __str__(self):
        return self.user.username

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)
