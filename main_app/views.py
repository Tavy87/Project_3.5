from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetForm


def index(request):
  widgets = Widget.objects.all()
  add_form = WidgetForm()
  total_quantity = sum(widget.quantity for widget in widgets)
  return render(request, 'index.html', {'widgets': widgets, 'add_form': add_form, 'total_quantity': total_quantity})

def add_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('index')

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'