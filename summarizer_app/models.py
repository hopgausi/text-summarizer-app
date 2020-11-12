from django.db import models


class Summarized_Data(models.Model):
    raw_text = models.TextField()
    summarized = models.TextField()
