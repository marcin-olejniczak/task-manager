from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True,)
    modified_date = models.DateTimeField(auto_now=True,)

    class Meta:
        abstract = True


class Task(BaseModel):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )
    STATUS_CHOICES = (
        ('new', 'New'),
        ('closed', 'Closed'),
        ('feedback', 'Feedback'),
        ('in_progress', 'In Progress'),
    )
    author = models.ForeignKey(User,)
    assignee = models.ForeignKey(User, related_name='assignee_user',)
    description = models.TextField()
    end_date = models.DateField()
    priority = models.CharField(
        default='normal',
        choices=PRIORITY_CHOICES,
        max_length=30,
    )
    status = models.CharField(
        default='new',
        choices=STATUS_CHOICES,
        max_length=30,
    )
    project = models.ForeignKey('Project',)
    start_date = models.DateField()
    title = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_preview', kwargs={'pk': self.id})


class Role(BaseModel):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name


class UserProfile(BaseModel):
    role = models.ForeignKey(Role)
    tracked_tasks = models.ManyToManyField(
        Task,
        related_name='tracked_tasks',
        blank=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return self.user.username


class Project(BaseModel):
    description = models.TextField()
    end_date = models.DateField()
    members = models.ManyToManyField(
        User,
        through='ProjectMember',
        blank=True,
    )
    start_date = models.DateField()
    title = models.CharField(max_length=255, unique=True,)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_preview', kwargs={'pk': self.id})


class ProjectMember(BaseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_member',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='project_member',
    )
    is_author = models.BooleanField(" Is author of project?", default=False,)

    def __unicode__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'project')


class Change(BaseModel):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Task)

    def __unicode__(self):
        return self.task.title


class ChangeDetail(BaseModel):
    change = models.ForeignKey(Change)
    field_name = models.CharField(max_length=255,)
    new_value = models.TextField()
    old_value = models.TextField()

    def __unicode__(self):
        return self.change.task.title


class Comment(BaseModel):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    text = models.TextField()

    def __unicode__(self):
        return self.task.title
