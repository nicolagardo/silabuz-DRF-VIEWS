from django.db import models
from django.utils.translation import gettext_lazy as _


from users.models import User

# Create your models here.
# Payments model
class Payments(models.Model):
    
    class Services(models.TextChoices):
        NETFLIX = 'NF', _('Neflix')
        AMAZON = 'AZ', _('Amazon Video')
        START = 'ST', _('Start +')
        PARAMAOUNT = 'PM', _('Paramount+')

    service = models.ForeignKey(Services, on_delete= models.CASCADE, related_name= 'services')
    date_payment = models.DateField(auto_now_add= True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'users')
    amount = models.FloatField(default=0.0)
    """ Payment_user
    - Id
    - User_id
    - Service_id
    - Amount
    - PaymentDate
    - ExpirationDate"""
    
    # Services Model
    class Services(models.Model):
        name = models.CharField()
        description = models.TextField()
        logo = models.CharField()

    """Expired_payments
    - Id
    - Pay_user_id
    - Penalty_fee_amount
    """
    
class ExipiredPayments(models.Model):
    pay_user_id = models.ForeignKey(Payments, on_delete= models.CASCADE, related_name= 'services')
    penalty_fee_amount = models.FloatField()