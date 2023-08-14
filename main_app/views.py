from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widget
from .forms import WidgetForm


def index(request):
  widget_form = WidgetForm()
  return render(request, 'index.html', {'widget_form': widget_form})

def add_widget(request):
  form = WidgetForm((request.POST))


class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'