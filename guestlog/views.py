from django.shortcuts import render, redirect
#need to import the Comment from models to be able to use it
from .models import Comment 
from .forms import CommentForm

# Create your views here.
def index(request):
    comments = Comment.objects.order_by('-date_added')#the - sign in front of the date is so the sorting would be from the latest comment 

    context = {'comments' : comments}
    return render(request, 'guestbook/index.html', context)

def sign(request):
    if request.method == 'POST':
        #Method 1 used to save details to the database
        #  name = request.POST['name']
        #  comment = request.POST['comment']
        #  new_comment = Comment(name=name, comment=comment)
        #  new_comment.save()
        #  return redirect('index')

        #below code is another method we can use to save the details in our database
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    context = {'form' : form}
    return render(request, 'guestbook/sign.html', context)
