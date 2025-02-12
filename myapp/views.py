from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TaskModel

# List View(Read)
class TaskListView(ListView):
  model = TaskModel
  template_name = 'index.html'
  context_object_name = 'tasks'


# Create View(add)
class TaskCreateView(CreateView):
  model = TaskModel
  fields = ['title', 'completed']
  template_name = 'task_form.html'
  success_url = reverse_lazy('index')
  
# Update View (Edit)
class TaskUpdateView(UpdateView):
    model = TaskModel
    fields = ['title', 'completed']
    template_name = 'task_form.html'
    success_url = reverse_lazy('index')

# Delete View (Delete)
class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('index')
