from django import forms
from budget.models import Main

#budgetcategories = ['Personal', 'Groceries', 'Health',]

class BudgetEntry(forms.ModelForm):
    class Meta:
        model = Main
        fields = ['item_name', 'price', 'category']