from django.db import models

# Create your models here.
class Event(models.Model):
    EVENT_TYPES = (
        ("arangu", "Arangu"),
        ("kalolsavam", "Kalolsavam"),
    )

    type = models.CharField(max_length=30, choices=EVENT_TYPES, null=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    reg_fee = models.FloatField(blank=False, null=False, default=0)
    rules = models.TextField()

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False)    
    events = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name="contacts")

    def __str__(self) -> str:
        return self.name