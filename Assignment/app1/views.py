# myfeedapp/views.py
from django.shortcuts import render,get_object_or_404, redirect,HttpResponse
from .models import Message
from django.contrib.auth.decorators import login_required

from .models import Message, Comment,Like
from .forms import MessageForm, CommentForm

from django.http import JsonResponse

@login_required
def feed(request):
    return render(request, 'app1/feed.html',)


@login_required
def post_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(user=request.user, content=content)
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'app1/feeds.html',{'messages': messages})



def message_list(request):
    messages = Message.objects.all()
    return render(request, 'app1/message_list.html', {'messages': messages})




def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()

    return render(request, 'app1/create_message.html', {'form': form})
    # return HttpResponse("Hello")




def create_comment(request, message_id):
    message = Message.objects.get(id=message_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.message = message
            comment.save()
            return redirect('message_list')
    else:
        form = CommentForm()

    return render(request, 'app1/create_comment.html', {'form': form, 'message': message})







@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, user=request.user)

    if request.method == 'POST':
        message.delete()
        return redirect('message_list')  # Redirect to your messages list view

    return render(request, 'app1/delete_message_confirm.html', {'message': message})





@login_required
def like_message(request, message_id):
    user = request.user
    message = Message.objects.get(pk=message_id)

    # Check if the user has already liked the message
    if not Like.objects.filter(user=user, message=message).exists():
        like = Like(user=user, message=message)
        like.save()

    return JsonResponse({'likes': message.like_set.count()})

@login_required
def like_comment(request, comment_id):
    user = request.user
    comment = Comment.objects.get(pk=comment_id)

    # Check if the user has already liked the comment
    if not Like.objects.filter(user=user, comment=comment).exists():
        like = Like(user=user, comment=comment)
        like.save()

    return JsonResponse({'likes': comment.like_set.count()})
