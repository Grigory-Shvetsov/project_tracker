from django.db import models
from tasks.models import Project, Task    

# Create your models here.

# STATUS_CHOICES = {
#     "e": "edit",
#     "f": "fixed"
# } 

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New','Новая'),
        ('In proccess','В работе'),
        ('Completed','Завершена')
        ]
    PRIORITY_CHOICES = [
        '5',
        '4',
        '3',
        '2',
        '1'
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='project_as_bugreport',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='task_as_bugreport',
        on_delete=models.SET_NULL,
        null =True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )    
    priority = PRIORITY_CHOICES
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Consideration','Рассмотрение'),
        ('Accepted','Принято'),
        ('Rejected','Отклонено')
    ]
    PRIORITY_CHOICES = [
            '5',
            '4',
            '3',
            '2',
            '1'
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='project_as_featurerequest',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='task_as_featurerequest',
        on_delete=models.SET_NULL,
        null =True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )    
    priority = PRIORITY_CHOICES
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
