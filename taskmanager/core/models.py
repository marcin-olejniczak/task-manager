from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True,)
    modified_date = models.DateTimeField(auto_now=True,)

    class Meta:
        abstract = True


class Task(BaseModel):
    PRIORITY_CHOICES = (
        (0, 'Low'),
        (1, 'Normal'),
        (2, 'High'),
        (3, 'Urgent'),
    )
    author = models.ForeignKey(User,)
    assignee = models.ForeignKey(User, related_name='assignee_user',)
    description = models.TextField()
    end_date = models.DateField()
    priority = models.CharField(
        default=1,
        choices=PRIORITY_CHOICES,
        max_length=30,
    )
    project = models.ForeignKey('Project',)
    start_date = models.DateField()
    title = models.TextField()


class Role(BaseModel):
    name = models.CharField(max_length=30,)

    def __unicode__(self):
        return self.name


class UserProfile(BaseModel):
    role = models.ForeignKey(Role)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


class Project(BaseModel):
    description = models.TextField()
    end_date = models.DateField()
    members = models.ManyToManyField(
        User,
        through='ProjectMember',
        through_fields=('project', 'user'),
    )
    name = models.TextField()
    start_date = models.DateField()

    def __unicode__(self):
        return self.name


class ProjectMember(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    is_author = models.BooleanField(" Is author of project?", default=False,)

    def get_user_login(self):
        return self.user.name

    def get_project_name(self):
        return self.project.name


class Change(BaseModel):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Task)


class ChangeDetail(BaseModel):
    change = models.ForeignKey(Change)
    field_name = models.CharField(max_length=255,)
    new_value = models.TextField()
    old_value = models.TextField()


class Comment(BaseModel):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    text = models.TextField()
