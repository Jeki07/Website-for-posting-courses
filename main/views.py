from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView
from mysite.settings import STATIC_ROOT
from django.contrib.auth import authenticate


def index(request):
    post = Post.objects.order_by('id')
    return render(request, 'main/index.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail_view.html'
    context_object_name = 'post_view'
    
    
def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Запись неверно заполнено'
        
    form = PostForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    post = Post.objects.order_by('id')
    return render(request, 'main/about.html', {'post': post})

def login(request):
    return render(request, 'main/login.html')

        
