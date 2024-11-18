from django.db.models import Sum
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PaymentForm
from .models import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"
    context_object_name = "home"


class LoanListView(ListView):
    model = Loan
    context_object_name = "loan_list"
    template_name = "loan_list.html"

class LoanDetailView(DetailView):
    model = Loan
    context_object_name = "loan_detail"
    template_name = "loan_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loan = self.get_object()
        total_payments = Payment.objects.filter(loan=loan).aggregate(total=Sum('payment_amount'))['total'] or 0
        context['total_payments'] = total_payments
        return context

class LoanCreateView(CreateView):
    model = Loan
    context_object_name = "loan_create"
    fields = ['user','loan_amount','description', 'due_date']
    template_name = "loan_create.html"
    success_url = reverse_lazy("loan_list")

class LoanUpdateView(UpdateView):
    model = Loan
    context_object_name = "loan_update"
    template_name = "loan_update.html"
    fields = ['user','loan_amount','description', 'due_date']
    success_url = reverse_lazy("loan_list")


class LoanDeleteView(DeleteView):
    model = Loan
    context_object_name = "loan_delete"
    template_name = "loan_confirm_delete.html"
    success_url = reverse_lazy("loan_list")


class PaymentListView(ListView):
    model = Payment
    context_object_name = "payment_list"
    template_name = "payment_list.html"


class PaymentDetailView(DetailView):
    model = Payment
    context_object_name = "payment_detail"
    template_name = "payment_detail.html"

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    context_object_name = "payment_create"
    template_name = "payment_create.html"
    success_url = reverse_lazy("payment_list")


class PaymentUpdateView(UpdateView):
    model = Payment
    context_object_name = "payment_update"
    template_name = "payment_update.html"
    fields = ['loan','payment_amount']
    success_url = reverse_lazy("payment_list")

class PaymentDeleteView(DeleteView):
    model = Payment
    context_object_name = "payment_delete"
    template_name = "payment_confirm_delete.html"


class LimitCreateView(CreateView):
    model = Limit
    context_object_name = "limit_create"
    fields = ['user','amount']
    template_name = "limit_create.html"
    success_url = reverse_lazy("limit_list")

class LimitUpdateView(UpdateView):
    model = Limit
    context_object_name = "limit_update"
    template_name = "limit_update.html"
    fields = ['user','amount']
    success_url = reverse_lazy("limit_list")

class CompletedLoanListView(ListView):
    model = Loan
    context_object_name = "completed_loan_list"
    template_name = "completed_loan_list.html"

    def get_queryset(self):
        return Loan.objects.filter(status="completed")

class UpcomingDueDateLoanListView(ListView):
    model = Loan
    context_object_name = "upcoming_due_date_loan_list"
    template_name = "upcoming_due_date_loan_list.html"

    def get_queryset(self):
        return Loan.objects.filter(status='pending').order_by('due_date')
