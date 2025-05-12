from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Profile, Expense

@login_required
def home(request):
    # Use .get() to get a single profile
    profile = Profile.objects.get(user=request.user)
    expenses = Expense.objects.filter(profile=profile).order_by('-date')

    # Calculating total income and expenses
    total_expenses = sum(exp.amount for exp in expenses if exp.expense_type == 'expense')
    total_income = sum(exp.amount for exp in expenses if exp.expense_type == 'income')
    balance = total_income - total_expenses

    # Handling form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = float(request.POST.get('amount'))

        expense_type = 'income' if amount >= 0 else 'expense'

        # Create new Expense
        Expense.objects.create(
            profile=profile,
            name=name,
            amount=abs(amount),
            expense_type=expense_type
        )

        return redirect('home')  # refresh page

    context = {
        'profile': profile,
        'expenses': expenses,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance
    }

    return render(request, 'tracker/home.html', context)
