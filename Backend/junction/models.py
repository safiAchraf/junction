from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class user(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=False)
    # Add your custom fields for instructors here

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class category(models.Model):
    category_name = models.CharField(max_length = 20)
    category_description = models.CharField(max_length = 100)

class user_category(models.Model):
    user_id = models.ForeignKey(user, on_delete = models.CASCADE)
    category_id = models.ForeignKey(category, on_delete = models.CASCADE)

class course(models.Model):
    instructor_id = models.ForeignKey(user, on_delete = models.CASCADE)
    course_name = models.CharField(max_length = 20)
    course_description = models.CharField(max_length = 100)
    rating = models.IntegerField(default=0)
    course_duration = models.IntegerField()
    course_price = models.IntegerField()
    acheivement = models.CharField(max_length = 20 , null=True)
    category = models.ForeignKey(category, on_delete = models.CASCADE , null=True)
class learner(models.Model):
    user_id = models.ForeignKey(user, on_delete = models.CASCADE)
    streak = models.IntegerField()
    score = models.IntegerField()
    current_course = models.ForeignKey(course, on_delete = models.CASCADE)

class chapitres(models.Model):
    course_id = models.ForeignKey(course, on_delete = models.CASCADE)
    chapitre_name = models.CharField(max_length = 20)
    chapitre_description = models.CharField(max_length = 100)
    chapitre_duration = models.IntegerField()

class videos(models.Model):
    course_id = models.ForeignKey(chapitres, on_delete = models.CASCADE)
    video_url = models.CharField(max_length = 100)
    video_title = models.CharField(max_length = 20)

class tasks(models.Model):
    course_id = models.ForeignKey(chapitres, on_delete = models.CASCADE)
    learner_id = models.ForeignKey(user, on_delete = models.CASCADE)
    task_title = models.CharField(max_length = 20)
    task_description = models.CharField(max_length = 100)
    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 20)
    done = models.BooleanField(default=False)

class child_learner(models.Model):
    parent_id = models.ForeignKey(user, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    level = models.IntegerField(default=0)
    last_achievement = models.CharField(max_length = 20 , null=True)

class child_enrolled(models.Model):
    child_id = models.ForeignKey(child_learner, on_delete = models.CASCADE)
    course_id = models.ForeignKey(course, on_delete = models.CASCADE)
    course_progress = models.IntegerField()

class adult_enrolled(models.Model):
    learner_id = models.ForeignKey(user, on_delete = models.CASCADE)
    course_id = models.ForeignKey(course, on_delete = models.CASCADE)
    course_progress = models.IntegerField()




