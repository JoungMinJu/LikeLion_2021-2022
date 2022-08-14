from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json

# Create your views here.
def showmain(request):
    posts=Post.objects.all()
    return render(request,'main/mainpage.html',{'posts':posts})

def showsecond(request):
    return render(request, 'main/second.html')

def showfirst(request):
    return render(request,'main/first.html')

def detail(request,id):
    post=get_object_or_404(Post,pk=id)
    all_comments=post.comments.all().order_by('-created_at')
    return render(request,'main/detail.html',{'post':post, 'comments':all_comments})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_post=Post()
    new_post.title=request.POST['title']
    new_post.writer=request.user
    new_post.pub_date=timezone.now()
    new_post.body=request.POST['body']
    new_post.image=request.FILES.get('image')
    new_post.save()
    return redirect('main:detail',new_post.id)

def edit(request,id):
    edit_post=Post.objects.get(id=id)
    return render(request, 'main/edit.html',{'post': edit_post})

def update(request,id):
    update_post=Post()
    update_post.title=request.POST['title']
    update_post.writer=request.user
    update_post.pub_date=timezone.now()
    update_post.body=request.POST['body']
    update_post.image=request.FILES.get('image')
    update_post.save()
    return redirect('main:detail',update_post.id)

def delete(request, id):
    delete_post=Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:main')

def create_comment(request, post_id):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=post_id)
		current_user = request.user
		comment_content = request.POST.get('content')
		Comment.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('main:detail', post_id)


def edit_comment(request, post_id, comment_id):
    edit_post=Post.objects.get(id=post_id)
    edit_comment=Comment.objects.get(id=comment_id)
    return render(request, 'main/edit_comment.html',{'post': edit_post, 'comment':edit_comment})
    ##edit_comment.html에 수정하고자하는 포스트랑 수정하고자하는 comment값을 보냈슴


def delete_comment(request, comment_id):
    delete_comment=Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect('main:main')


def update_comment(request, post_id,comment_id):
    if request.method=='POST':
        post=get_object_or_404(Post,pk=post_id)
        comment=Comment.objects.filter(pk=comment_id)
        current_user=request.user
        comment_content=request.POST.get('content')
        comment.update(content=comment_content,writer=current_user, post=post)
    return redirect('main:detail', post_id)

@require_POST
@login_required
def like_toggle(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    post_like, post_like_created=Like.objects.get_or_create(user=request.user, post=post)
    #get_or_created는 첫번쨰 인자는 우리가 꺼내려고하는 모델의 인스턴스, 두번쨰 인자는boolean flag
    #True는 인스턴스가 get_or_created메서드에 의해 생성되었다는 것
    #False는 기존에 있던 것이라는 뜻   
    if not post_like_created:
        post_like.delete()
        result='like_cancel'
    else:
        result='like'
    context={
        'like_count':post.like_count,
        'result':result
    }
    return HttpResponse(json.dumps(context), content_type='application/json')

@require_POST
@login_required
def dislike_toggle(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    post_dislike, post_dislike_created=Dislike.objects.get_or_create(user=request.user, post=post)
    if not post_dislike_created:
        post_dislike.delete()
        result="dislike_cancel"
    else:
        result='dislike'
    context={
        "dislike_count":post.dislike_count,
        'result':result
    }
    return HttpResponse(json.dumps(context),content_type="application/json")