from django.db import models

# Create your models here.

# entry
class Entry(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    proof = models.TextField(null=True)
    remark = models.TextField(null=True)
    example = models.TextField(null=True)
    source = models.CharField(max_length=200, null=True)
    chinese = models.CharField(max_length=1000, null=True)
    author = models.TextField(null=True)