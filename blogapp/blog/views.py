from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            'title': '블로그',
            'posts': post_objs
        }
        return render(request, 'blog/post_list.html', context)
    

class PostDetail(View):
    def get(self, request, id):
        post = Post.objects.prefetch_related('comment_set').get(pk=id)
        post.count += 1
        post.save()

        comments = post.comment_set.all()
        comment_form = CommentForm()

        recomments = []
        for comment in comments:
            recomment = Recomment.objects.filter(comment=comment.pk)
            recomments += recomment
        recomment_form = RecommentForm()

        context = {
            'title': '상세페이지',
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'recomments': recomments,
            'recomment_form': recomment_form
        }
        return render(request, 'blog/post_detail.html', context)
    

class PostWrite(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            'title': '글작성',
            'form': form
        }
        return render(request, 'blog/post_write.html', context)
        
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:post-list')
        context = {
            'title': '글작성',
            'form': form
        }
        return render(request, 'blog/post_write.html', context)
    

class PostEdit(LoginRequiredMixin, View):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        form = PostForm(initial=
                        {'title': post.title,
                         'content': post.content,
                         'imgfile': post.imgfile,
                         'category': post.category
                         })
        context = {
            'title': '수정',
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.category = form.cleaned_data['category']
            if form.cleaned_data['imgfile'] == None:
                post.save()
                return redirect('blog:post-detail', id=id)
            post.imgfile = form.cleaned_data['imgfile']
            post.save()
            return redirect('blog:post-detail', id=id)
        context = {
            'title': '상세페이지',
            'form': form
        }
        return render(request, 'blog/post_edit.html', context)
    

class PostDelete(LoginRequiredMixin, View):
    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return redirect('blog:post-list')
    

class PostSearch(View):
    def get(self, request, tag):
        if tag == "*":
            post_objs = Post.objects.all()
        else:
            post_objs = Post.objects.filter(category=tag)
        context = {
            'title': '블로그',
            'posts': post_objs
        }
        return render(request, 'blog/post_list.html', context)
    

class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user
            comment = Comment.objects.create(post=post, content=content, writer=writer)
            return redirect('blog:post-detail', id=id)
        
        comments = post.comment_set.all()

        recomments = []
        for comment in comments:
            recomment = Recomment.objects.filter(comment=comment.pk)
            recomments += recomment
        recomment_form = RecommentForm()
        
        context = {
            'title': "상세보기",
            'post': post,
            'comments': comments,
            'comment_form': form,
            'recomments': recomments,
            'recomment_form': recomment_form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(LoginRequiredMixin, View):
    def post(self, request, id):
        comment = get_object_or_404(Comment, pk=id)
        post_id = comment.post.pk
        comment.delete()
        return redirect('blog:post-detail', id=post_id)
    

class RecommentWrite(LoginRequiredMixin, View):
    def post(self, request, id):
        form = RecommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            content = form.cleaned_data['content']
            writer = request.user
            recomment = Recomment.objects.create(comment=comment, content=content, writer=writer)
            return redirect('blog:post-detail', id=id)
        
        post = Post.objects.prefetch_related('comment_set').get(pk=id)
        comments = post.comment_set.all()

        recomments = []
        for comment in comments:
            recomment = Recomment.objects.filter(comment=comment.pk)
            recomments += recomment
        recomment_form = RecommentForm()
        
        context = {
            'title': "상세보기",
            'post': post,
            'comments': comments,
            'comment_form': form,
            'recomments': recomments,
            'recomment_form': recomment_form
        }
        return render(request, 'blog/post_detail.html', context)
        

class RecommentDelete(LoginRequiredMixin, View):
    def post(self, request, id):
        recomment = get_object_or_404(Recomment, pk=id)
        post_id = recomment.comment.post.pk
        recomment.delete()
        return redirect('blog:post-detail', id=post_id)