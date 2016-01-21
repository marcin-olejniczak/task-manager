from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(BaseModel):
    name = models.CharField(max_length=30)


class UserProfile(BaseModel):
    login = models.CharField(max_length=30)
    role = models.ForeignKey(Role)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Project(BaseModel):
    author = models.ForeignKey(User)
    coauthors = models.ManyToManyField(User, related_name='coauthors_user')
    description = models.TextField()
    end_date = models.DateField()
    members = models.ManyToManyField(User, related_name='members_user')
    name = models.TextField()
    start_date = models.DateField()


class Task(BaseModel):
    PRIORITY_CHOICES = (
        (0, 'Low'),
        (1, 'Normal'),
        (2, 'High'),
        (3, 'Urgent'),
    )
    author = models.ForeignKey(User)
    assignee = models.ForeignKey(User, related_name='assigne_user')
    description = models.TextField()
    end_date = models.DateField()
    priority = models.CharField(
        default=1, choices=PRIORITY_CHOICES, max_length=30)
    project = models.ForeignKey(Project)
    start_date = models.DateField()
    title = models.TextField()


class Change(BaseModel):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Task)


class ChangeDetail(BaseModel):
    change = models.ForeignKey(Change)
    field_name = models.CharField(max_length=255)
    new_value = models.TextField()
    old_value = models.TextField()


class Comment(BaseModel):
    author = models.ForeignKey(User)
    text = models.TextField()

