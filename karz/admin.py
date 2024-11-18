from django.contrib import admin
from .models import User, Limit, Loan, Payment
# Register your models here.
# admin.site.register(User)
# admin.site.register(Limit)
# admin.site.register(Loan)
# admin.site.register(Payment)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number']
    list_filter = ['username','email', 'first_name', 'last_name', 'phone_number']


@admin.register(Limit)
class LimitAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'limit_amount']
    list_display = ['user__username', 'limit_amount']
    list_filter = ['user__username', 'limit_amount']


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'loan_amount', 'created_at', 'due_date']
    list_display = ['user__username', 'loan_amount', 'created_at', 'due_date']
    list_filter = ['user__username', 'loan_amount', 'created_at', 'due_date']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['loan__loan_amount', 'payment_amount','payment_date']
    list_display = ['loan__loan_amount', 'payment_amount','payment_date']
    list_filter = ['loan__loan_amount', 'payment_amount','payment_date']