from django.shortcuts import render

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
