from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from loans.models import Loan, LoanAmount

from loans.serializers import LoanAmountSerializer, LoanSerializer
# Create your views here.

class LoanAmountViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = LoanAmountSerializer
    queryset = LoanAmount.objects.all()


class LoanViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = LoanSerializer
    queryset = Loan.objects.filter(is_approved = False).order_by('-date_requested')

class StatsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user_count = User.objects.all().count()
        awarded_loan_count  = Loan.objects.filter(is_approved = True).count()
        data = {
            "total_users":user_count,
            "total_awarded_loans": awarded_loan_count,
        }   
        return Response(data)
