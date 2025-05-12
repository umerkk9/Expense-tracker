from django.db import models
from django.contrib.auth.models import User

# Descriptive values for expense type
EXPENSE_TYPES = (
    ('income', 'Income'),
    ('expense', 'Expense'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    income = models.FloatField()
    balance = models.FloatField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Expense(models.Model):
    # Make profile nullable to allow adding to existing rows
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=7, choices=EXPENSE_TYPES)  # 'income' or 'expense'
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)  # Let it be null for existing rows

    def __str__(self):
        return f'{self.name} - {self.expense_type}'

