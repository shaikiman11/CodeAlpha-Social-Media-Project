from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Post, Comment, Like, Follow


# =========================
# HOME
# =========================

@login_required
def home(request):

    if request.method == 'POST':

        content = request.POST.get('content')

        if content:
            Post.objects.create(
                user=request.user,
                content=content
            )

        return redirect('home')

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'social/home.html', {
        'posts': posts
    })


# =========================
# REGISTER
# =========================

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            return render(request, 'social/register.html', {
                'error': 'Username already exists.'
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'social/register.html')


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        return render(request, 'social/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'social/login.html')


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect('login')


# =========================
# LIKE POST
# =========================

@login_required
def like_post(request, id):

    post = get_object_or_404(Post, id=id)

    like = Like.objects.filter(
        post=post,
        user=request.user
    ).first()

    if like:
        like.delete()
    else:
        Like.objects.create(
            post=post,
            user=request.user
        )

    return redirect('home')


# =========================
# ADD COMMENT
# =========================

@login_required
def add_comment(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':

        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                post=post,
                user=request.user,
                content=content
            )

    return redirect('home')


# =========================
# PROFILE
# =========================

@login_required
def profile(request, username):

    profile_user = get_object_or_404(
        User,
        username=username
    )

    posts = Post.objects.filter(
        user=profile_user
    ).order_by('-created_at')

    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    is_following = Follow.objects.filter(
        follower=request.user,
        following=profile_user
    ).exists()

    return render(request, 'social/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'followers_count': followers_count,
        'following_count': following_count,
        'is_following': is_following,
    })


# =========================
# FOLLOW USER
# =========================

@login_required
def follow_user(request, username):

    user_to_follow = get_object_or_404(
        User,
        username=username
    )

    if request.user != user_to_follow:

        Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

    return redirect(
        'profile',
        username=username
    )


# =========================
# UNFOLLOW USER
# =========================

@login_required
def unfollow_user(request, username):

    user_to_unfollow = get_object_or_404(
        User,
        username=username
    )

    Follow.objects.filter(
        follower=request.user,
        following=user_to_unfollow
    ).delete()

    return redirect(
        'profile',
        username=username
    )