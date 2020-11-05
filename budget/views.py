import sys
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import BudgetEntry
from .models import Main

#View for submit button, enters data into Postgres and redirects back to same page
def EnterData(request):
    if request.method == 'POST':
        form = BudgetEntry(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            new_entry = Main(item_name=item_name, price=price, category=category)
            new_entry.save()

            return HttpResponseRedirect('/budget/')

    else:
        form = BudgetEntry()
    return render(request, 'budget/input.html', {'form': form})


