from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TaskModel
from .forms import Userform
from django.contrib import messages

# User Registration View
class RegistrationView(View):
    def get(self, request):
        form = Userform()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = Userform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user automatically
            return redirect("index")  # Redirect to the home page
        else:
            messages.error(request, "❌ Registration failed. Please correct the errors below.")
        return render(request, "register.html", {"form": form})


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
  login_url = 'login' # redirects unauthenticated users
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


  
