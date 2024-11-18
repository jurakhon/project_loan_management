from django import forms
from .models import Payment, Loan


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['loan', 'payment_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['loan'].queryset = Loan.objects.filter(status='pending')
