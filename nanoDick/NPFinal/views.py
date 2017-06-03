from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_list(request):
    srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'NPFinal/index.html', {'srcs':srcs})

# return login html
def login(request):
    srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'NPFinal/login.html', {})

# return register html
def register(request):
    srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'NPFinal/register.html', {})

def upload(request):
    if request.method == 'POST':
        # store file
        #print(settings.IMAGES_ROOT+request.FILES['image'].name)
        file_exten = request.FILES['image'].name.split('.')[-1]
        destination_path = open(settings.IMAGES_ROOT+request.FILES['image'].name, "wb+")
        image = request.FILES['image']
        for chunk in image.chunks():
            destination_path.write(chunk)
        destination_path.close()
        Post.objects.create(
            title = "test title",
            img_src = settings.IMAGES_ROOT+request.FILES['image'].name,
            text = "test text",
            hash_tag = ['1','2','3'],
        )
        
        #handle_uploaded_file(request.FILES['file'])
        return HttpResponse(status=200)

def post(request):
    return render(request, 'NPFinal/demo.html', {})






