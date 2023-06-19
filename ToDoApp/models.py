from django.db import models


class CategoryMaster(models.Model):
    category_name = models.CharField(max_length=1000, null = False, blank = False)
    def __str__(self):
        return f"Category : {self.category_name}"

class StatusMaster(models.Model):
    status_name = models.CharField(max_length=1000, null = False, blank = False)
    def __str__(self):
        return f"Status : {self.status_name}"

# Create your models here.
class Task(models.Model):
    sr_no = models.IntegerField(null = False, blank = False)
    title = models.CharField(null = False, blank = False, max_length=500)
    category = models.ForeignKey(CategoryMaster, null = True, blank = True, on_delete=models.SET_NULL)
    description = models.TextField()
    status = models.ForeignKey(StatusMaster, null = True, blank = True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sr_no} - {self.title}"


