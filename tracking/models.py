from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class PriorityTracking(models.Model):
    priority = models.CharField(unique=True, blank=False, max_length=26, validators=[MinLengthValidator(26)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.priority


class PriorityWithSigTracking(models.Model):
    priority_with_sig = models.CharField(unique=True, blank=False, max_length=26, validators=[MinLengthValidator(26)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.priority_with_sig



class ExpressPriorityTracking(models.Model):
    express_priority = models.CharField(unique=True, blank=False, max_length=26, validators=[MinLengthValidator(26)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.express_priority
        

class ExpressWithSigPriorityTracking(models.Model):
    express_priority_with_sig = models.CharField(unique=True, blank=False, max_length=26, validators=[MinLengthValidator(26)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.express_priority_with_sig
    

