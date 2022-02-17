from django.contrib import admin

from loans.models import Loan, LoanAmount

# Register your models here.
admin.site.register(LoanAmount)
admin.site.register(Loan)