from django.db import models

from accounts.models import User

# Create your models here.
PERIOD_CHOICES = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
]

class LoanAmount(models.Model):
    currency = models.CharField(max_length=20, default='KES')
    loan_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_value = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.currency}-{self.loan_value}'


class Loan(models.Model):
    customer = models.ForeignKey(User,on_delete=models.PROTECT)
    loan_amount = models.ForeignKey(LoanAmount,on_delete=models.PROTECT)
    date_requested = models.DateTimeField(auto_now_add=True)
    repayment_period = models.CharField(choices=PERIOD_CHOICES, max_length=250)
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.customer} - {self.loan_amount} - {self.date_requested}'


