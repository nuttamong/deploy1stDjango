from django.db import models

# Create your models here.
class report(models.Model):
    course = models.IntegerField()
    student_id = models.TextField()
    name = models.TextField()
    status = models.IntegerField()
    edu = models.TextField()
    advisor = models.TextField()
    work = models.TextField()
    public = models.IntegerField()
    journal = models.IntegerField()
    implemment = models.TextField()
    meeting = models.TextField()
    from_date = models.TextField()
    to_date = models.TextField()
    year = models.TextField()
