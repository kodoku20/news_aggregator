from django.db import models


class HeadLine(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    # source = models.CharField(max_length=50)

    def __str__(self):
        return self.title
