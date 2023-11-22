from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    ppt_completed = models.BooleanField(default=False)
    notes_completed = models.BooleanField(default=False)
    end_term_completed = models.BooleanField(default=False)
    mid_term_completed = models.BooleanField(default=False)
    lab_files_completed = models.BooleanField(default=False)
