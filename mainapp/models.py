from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    discourse = models.URLField(null=True, blank=True)
    about = models.TextField()
    profilepic = models.FileField(blank=True,null=True,upload_to='profile_pic')
    github =  models.URLField(null=True, blank=True)
    website = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/u/' + self.user.username + '/'


def create_profile(sender=User, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    authors = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='authors_list')
    duration = models.TimeField()
    level = models.CharField(max_length=20)
    audience = models.CharField(max_length=20)


class Section(models.Model):
    courseId = models.ForeignKey(Course)
    title = models.CharField(max_length=50)
    description = models.TextField()
    authors = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='authors_list')
    duration = models.TimeField()


class CourseItem(models.Model):
    section = models.OneToOneField(Section)
    course = models.OneToOneField(Course)
    title = models.CharField(max_length=50)
    sideLink = models.CharField(max_length=50)
    codeLink = models.CharField(max_length=50)
    textExplanation = models.TextField()


