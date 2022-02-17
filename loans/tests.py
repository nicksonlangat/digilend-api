from django.test import TestCase, Client

from accounts.models import User
from .models import  Loan, LoanAmount


# initialize the APIClient app
client = Client()

class LoanTest(TestCase):

    def setUp(self):
        self.test_customer = User(first_name='testuser1',last_name='testuser1l',email='testuser1@test.com', password = '54323543nkl')
        self.test_customer2 = User.objects.create(first_name='testuser1',last_name='testuser1l',email='testuser2@test.com', password = '54323543nkl' )
        # test_customer.save()
        self.loan_amount = LoanAmount(currency = 'KES', loan_interest_rate = 11, loan_value = 10000 )
        self.loan_amount2 = LoanAmount.objects.create(currency = 'KES', loan_interest_rate = 13, loan_value = 20000 )

        self.loan = Loan(customer = self.test_customer2, loan_amount= self.loan_amount2, repayment_period='2' )
        self.loan2 = Loan.objects.create(customer = self.test_customer2, loan_amount= self.loan_amount2, repayment_period='2' )
        
    def test_model_can_create_a_customer(self):
        old_count = User.objects.count()
        self.test_customer.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    def test_model_can_create_a_loan_amount(self):
        old_count =LoanAmount.objects.count()
        self.loan_amount.save()
        new_count = LoanAmount.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_apply_loan(self):
        old_count = Loan.objects.count()
        self.loan.save()
        new_count = Loan.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_customer_string_method(self):
        customer = self.test_customer2
        expected_string = f'{customer.email}'
        self.assertEqual(str(customer), expected_string)
    
    def test_loan_amount_string_method(self):
        loan_amount = self.loan_amount2
        expected_string = f'{loan_amount.currency}-{loan_amount.loan_value}'
        self.assertEqual(str(loan_amount), expected_string)
    
    def test_loan_string_method(self):
        loan = self.loan2
        expected_string = f'{loan.customer} - {loan.loan_amount} - {loan.date_requested}'
        self.assertEqual(str(loan), expected_string)
    
    