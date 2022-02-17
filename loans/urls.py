from django.urls import path
from rest_framework import routers

from loans.views import LoanAmountViewset, LoanViewset, StatsData

router = routers.DefaultRouter()

router.register(r'loan/amount', LoanAmountViewset, basename='loan_amount')
router.register(r'loans', LoanViewset, basename='loans')

urlpatterns = [
     path('stats',StatsData.as_view(),name='stats'),
]+router.urls