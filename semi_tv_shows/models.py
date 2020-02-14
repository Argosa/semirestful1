from django.db import models

# Create your models here.
class Network(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.name} {self.created_at} {self.updated_at}"

class Show(models.Model):
    name = models.CharField(max_length=255)
    network = models.ForeignKey(Network, related_name= "networks", on_delete = models.CASCADE)
    release_date = models.DateField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.name} {self.network} {self.release_date} {self.desc} {self.created_at} {self.updated_at}"