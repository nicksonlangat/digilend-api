from rest_framework import serializers
from .models import LoanAmount, Loan

class LoanAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmount
        fields = [
            'id',
            'currency',
            'loan_interest_rate',
            'loan_value'
        ]


class LoanSerializer(serializers.ModelSerializer):
    total_to_pay = serializers.SerializerMethodField(read_only=True)
    monthly_installment = serializers.SerializerMethodField(read_only=True)
    customer_credit_worthiness = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Loan
        fields = [
            'id',
            'customer',
            'loan_amount',
            'repayment_period',
            'total_to_pay',
            'monthly_installment',
            'customer_credit_worthiness',
            'date_requested',
            'is_approved'
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['customer'] = instance.customer.email
        rep['loan_amount'] = instance.loan_amount.loan_value
        return rep
    
    def get_total_to_pay(self, obj):
        interest = obj.loan_amount.loan_interest_rate
        monthly_value = interest * obj.loan_amount.loan_value / 100
        total_accrued_interest = int(monthly_value) * int(obj.repayment_period)
        total_to_pay = total_accrued_interest + obj.loan_amount.loan_value
        
        return total_to_pay
    
    def get_monthly_installment(self, obj):
        return  f'{self.get_total_to_pay(obj) / int(obj.repayment_period):.2f}'
    
    def get_customer_credit_worthiness(self, obj):
        message = ''
        status = obj.customer.credit_status
        if not obj.customer.is_kyc_approved:
            message = "Not Eligible. Needs KYC approval."
        else:
            message = f"{status}"
        
        return message