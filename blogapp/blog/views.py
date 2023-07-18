from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class PostList(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            'title': 'Main Page',
            'posts': post_objs,
        }
        return render(request, 'blog/post_list.html', context)
    

class PostDetail(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        context = {
            'title': 'blog',
            'post': post,
        }
        return render(request, 'blog/post_detail.html', context)
    

class PostWrite(View):
    def get(self, request):
        form = PostForm()
        context = {
            'title': 'write',
            'form': form,
        }
        return render(request, 'blog/post_write.html', context)
        
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:post-list')
        context = {
            'title': 'write',
            'form': form,
        }
        return render(request, 'blog/post_write.html', context)
    

class PostEdit(View):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        form = PostForm(initial=
                        {'title': post.title,
                         'content': post.content, 'category': post.category
                         })
        context = {
            'title': 'Edit',
            'form': form,
            'post': post,
        }
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.category = form.cleaned_data['category']
            post.save()
            return redirect('blog:post-detail', id=id)
        context = {
            'title': 'blog',
            'form': form,
        }
        return render(request, 'blog/post_edit.html', context)
    

class PostDelete(View):
    def post(self, request, id):
        print(id)
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return redirect('blog:post-list')
    

class PostSearch(View):
    def get(self, request, tag):
        print(request.GET)
        post_objs = Post.objects.filter(category=tag)
        print(tag)
        context = {
            'title': 'Main Page',
            'posts': post_objs,
        }
        return render(request, 'blog/post_list.html', context)