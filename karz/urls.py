from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('loanlist/', LoanListView.as_view(), name='loan_list'),
    path('loandetail/<int:pk>', LoanDetailView.as_view(), name='loan_detail'),
    path('loancreate/', LoanCreateView.as_view(), name='loan_create'),
    path('loanupdate/<int:pk>', LoanUpdateView.as_view(), name='loan_update'),
    path('loandelete/<int:pk>', LoanDeleteView.as_view(), name='loan_delete'),
    path('loans/completed/', CompletedLoanListView.as_view(), name='completed_loan_list'),
    path('loans/upcoming/', UpcomingDueDateLoanListView.as_view(), name='upcoming_due_date_loan_list'),
         path('paymentlist/', PaymentListView.as_view(), name='payment_list'),
    path('paymentdetail/<int:pk>', PaymentDetailView.as_view(), name='payment_detail'),
    path('paymentcreate/', PaymentCreateView.as_view(), name='payment_create'),
    path('paymentupdate/<int:pk>', PaymentUpdateView.as_view(), name='payment_update'),
    path('paymentdelete/<int:pk>', PaymentDeleteView.as_view(), name='payment_delete'),
    path('limitcreate/', LimitCreateView.as_view(), name='limit_create'),
    path('limitupdate/<int:pk>', LimitUpdateView.as_view(), name='limit_update'),
    path('userlist/', UserListView.as_view(), name='user_list'),
    path('userdetail/<int:pk>', UserDetailView.as_view(), name='user_detail'),



]