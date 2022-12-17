from django.db import models
from django.utils.translation import gettext_lazy as _


from users.models import User

# Create your models here.

class Payments(models.Model):
    
    class Services(models.TextChoices):
        NETFLIX = 'NF', _('Neflix')
        AMAZON = 'AZ', _('Amazon Video')
        START = 'ST', _('Start +')
        PARAMAOUNT = 'PM', _('Paramount+')

    service = models.CharField(
        max_length= 2,
        choices= Services.choices,
        default= Services.NETFLIX
    )
    date_payment = models.DateField(auto_now_add= True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'users')
    amount = models.FloatField(default=0.0)