from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.views.generic import ListView, DetailView
from django.db.models import Count
from django.contrib import messages
from blog.models import Post, Comment, Favorite, Like
from blog.forms import PostForm, ContactForm
from registration.backends.simple.views import RegistrationView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    post_list = Post.objects.all().annotate(num_likes=Count('likes')).order_by('-num_likes', '-created')
    all_posts = Post.objects.all().order_by('-created')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {
        'all_posts': all_posts,
        'posts': posts,
        'post_list': post_list,

    })

def post_detail(request, slug):
    all_posts = Post.objects.all().order_by('-created')
    post = Post.objects.get(slug=slug)
    fav_posts = posts.annotate(num_favorites=Count('favorites'))

    return render(request, 'posts/post_detail.html', {
        'fav_posts': fav_posts,
        'all_posts': all_posts,
        'post': post,
    })

@login_required
def edit_post(request, slug):
    posts = Post.objects.all().order_by('-created')
    post = Post.objects.get(slug=slug)
    # if post.user != request.user:
    #     raise Http404
    form_class = PostForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts/post_detail', slug=post.slug)
    else:
        form = form_class(instance=post)

    return render(request, 'posts/edit_post.html', {
        'posts': posts,
        'post': post,
        'form': form,
    })

def create_post(request):
    posts = Post.objects.all().order_by('-created')
    form_class = PostForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            message = f"Your comment has been added to '{post.title}'!"
            messages.add_message(request, messages.SUCCESS, message)

            return redirect('post_detail', slug=post.slug)
    else:
        form = form_class()

    return render(request, 'posts/create_post.html', {
        'posts': posts,
        'form': form,
    })

def contact(request):
    form_class = ContactForm

    if request.method == "POST":
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')

            content = template.render({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website <h1@example.com>',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'nav/contact.html', {
        'form': form_class,
    })

class MyRegistrationView(RegistrationView):
    success_url = 'registration_create_post'

def get_post_list(request, header, posts):
    posts = Post.objects.all().order_by('-created')
    fav_posts = posts.annotate(num_favorites=Count('favorites'))
    # {{ fav_posts.num_favorites }}
    favorite_posts = []
    if request.user.is_authenticated:
        favorite_posts = request.user.favorite_posts.all()
    return render(request, 'index.html', {
        'posts': posts,
        'fav_posts': fav_posts,
        'favorite_posts': favorite_posts
    })

@login_required
def favorites_view(request):
    posts = request.user.favorite_posts.all().order_by('-created')
    return get_post_list(request, 'Your Favorite Posts', posts)

def toggle_favorite(request, slug):
    post = Post.objects.get(slug=slug)

    if post in request.user.favorite_posts.all():
        post.favorites.get(user=request.user).delete()
        message = f"{post} has been unfavorited."
    else:
        post.favorites.create(user=request.user)
        message = f"{post} has been favorited"

    messages.add_message(request, messages.INFO, message)
    return redirect('home')


def toggle_like(request, slug):
    post = Post.objects.get(slug=slug)

    if post in request.user.liked.all():
        post.likes.get(user=request.user).delete()
    else:
        post.likes.create(user=request.user)

    return redirect('home')
