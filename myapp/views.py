from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TaskModel
from .forms import Userform

# User Registration View
class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = Userform
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()  # Save user
        login(self.request, user)  # Auto-login after registration
        return super().form_valid(form)


# User Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirect already logged-in users
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url
      
#logout
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login') 


# List View(Read)
class TaskListView(LoginRequiredMixin, ListView):
  model = TaskModel
  template_name = 'index.html'
  context_object_name = 'tasks'
  paginate_by = 5
  ordering = ['-id']
  
  def get_queryset(self):
        return TaskModel.objects.filter(user=self.request.user)


# Create View(add)
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TaskModel
    fields = ['title', 'completed']
    template_name = 'task_form.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set logged-in user
        return super().form_valid(form)
  
# Update View (Edit)
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskModel
    fields = ['title', 'completed']
    template_name = 'task_form.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
       return TaskModel.objects.filter(user=self.request.user)

# Delete View (Delete)
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskModel
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
      return TaskModel.objects.filter(user=self.request.user)
    
# toggle View
class TaskToggleView(LoginRequiredMixin, View):
  login_url = reverse_lazy('login')
  
  def post(self, request, pk):
    task = get_object_or_404(TaskModel, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('index')


  
