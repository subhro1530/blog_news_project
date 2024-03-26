import os
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Login successful, redirect to a success page
            return redirect('success_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def home(request):
    if request.user.is_authenticated:
        try:
            news_api_key = os.getenv('API_KEY')
            response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}')
            response.raise_for_status()
            news_articles = response.json()['articles']
        except Exception as e:
            print(f"Error fetching news articles: {e}")
            news_articles = []
        
        return render(request, 'home.html', {'news_articles': news_articles})
    else:
        return redirect('login')

@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Blog.objects.create(title=title, content=content, author=request.user)
        return redirect('home')
    return render(request, 'create_blog.html')

@login_required
def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.user == blog.author:
        blog.delete()
    return redirect('home')
