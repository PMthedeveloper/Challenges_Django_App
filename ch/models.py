from django.db import models

# Create your models here.
class Challenges(models.Model):
    sno = models.AutoField(primary_key=True);
    pic = models.URLField();
    title = models.CharField(max_length=10000);
    timeStamp = models.DateTimeField(blank=False);
    active_Solvers = models.IntegerField();
    Tags = models.CharField(max_length=10000);
    price = models.CharField(max_length=15);
    contents = models.TextField();
    slug = models.CharField(max_length=130);

    def __str__(self):
        return self.title;