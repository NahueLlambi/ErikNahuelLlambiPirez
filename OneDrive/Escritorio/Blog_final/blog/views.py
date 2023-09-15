from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.views.generic.edit import FormView
from .forms import RegisterForm

def render_post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_details.html', {'post': post})

def decks_not_available(request):
    return render(request, 'blog/decks.html')

class UserRegistration(FormView):
    template_name = "blog/registration.html"  
    form_class = RegisterForm
    success_url = reverse_lazy("blog:success_view")


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def success_view(request):
    return render(request, 'blog/success_registration.html')

