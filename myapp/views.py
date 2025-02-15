from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
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
    
# toggle View
class TaskToggleView(View):
  def post(self, request, pk):
    task = get_object_or_404(TaskModel, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('index')
  
