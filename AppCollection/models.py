from django.db import models

# Create your models here.

# user's collections
class UserFavori(models.Model):
    openid = models.CharField(max_length=50, null=True)
    entry_id = models.IntegerField(null=True)
    entry_title = models.CharField(max_length=200, null=True)


# user's collection time token
class UserFavoriToken(models.Model):
    openid = models.CharField(max_length=50, null=True)
    token = models.CharField(max_length=30, null=True)