from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core import serializers
from django.contrib.auth import logout, login, authenticate
from .models import HomeCarousel, TextPost, VideoPost, HomeCarouselText
from .forms import ContactForm, CreateTextPost, CreateVideoPost, CreateCarousel, CreateCarouselText

import stripe
stripe.api_key = "sk_test_51HEkuTLZInSgn8lOO6oYl4c7GoX5OThsVniX0YgJ6sFG3tVPCbRaZygsRNNUTosOE9nSsAxrQYcehXJaCw8pHvgi00P2AvPECA"


# Site Views

def index(request):
    images = HomeCarousel.objects.all()
    new_posts = TextPost.objects.order_by('-id')[:2]
    new_video = VideoPost.objects.order_by('-id').first()
    text = HomeCarouselText.objects.all()

    text = serializers.serialize('json', text)

    context = {
        'title': 'LIFT Church - Home',
        'images': images,
        'posts': new_posts,
        'video': new_video,
        'text': text
    }

    return render(request, 'index.html', context)

def about(request):
    context = {
        'title': 'LIFT Church - About'
    }

    return render(request, 'about-us.html', context)

def sermens(request):
    posts = TextPost.objects.all().order_by('-id')
    videos = VideoPost.objects.all().order_by('-id')

    context = {
        'title': 'LIFT Church - Sermens',
        'posts': posts,
        'videos': videos
    }

    return render(request, 'sermens.html', context)

def sermen_detail(request, id):
    post = TextPost.objects.get(id=id)
    context = {
        'title': 'LIFT Church - Sermen',
        'post': post
    }

    return render(request, 'sermen-details.html', context)

def video_detail(request, id):
    video = VideoPost.objects.get(id=id)
    context = {
        'title': 'LIFT Church - Video Sermen',
        'video': video
    }

    return render(request, 'sermen-video.html', context)

def ministries(request):
    context = {
        'title': 'LIFT Church - Ministries'
    }

    return render(request, 'ministries.html', context)

def our_mission(request):
    context = {
        'title': 'LIFT Church - Our Mission'
    }

    return render(request, 'our-mission.html', context)

def our_vision(request):
    context = {
        'title': 'LIFT Church - Our Vision'
    }

    return render(request, 'our-vision.html', context)

def our_beliefs(request):
    context = {
        'title': 'LIFT Church - Our Beliefs'
    }

    return render(request, 'our-beliefs.html', context)

def core_values(request):
    context = {
        'title': 'LIFT Church - Core Values'
    }

    return render(request, 'core-values.html', context)

def roman_road(request):
    context = {
        'title': 'LIFT Church - Roman Road'
    }

    return render(request, 'roman-road.html', context)

def donate(request):
    context = {
        'title': 'LIFT Church - Donation'
    }

    return render(request, 'donate.html', context)

def charge(request):
    if request.method == 'POST':
        print(request.POST)

        customer = stripe.Customer.create(
            name = request.POST['name']
        )

 #       charge = stripe.Charge.create(
 #           customer = customer,
 #           amount = (request.POST['amount'] * 100),
 #           currency= 'usd',
 #           description = 'Donation'
 #       )

    return render(request, 'thankyou.html')

def team(request):
    context = {
        'title': 'LIFT Church - Team'
    }

    return render(request, 'team.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                message,
                email,
                ['emoore13@ycp.edu']
            )

            context = {
                'title': 'LIFT Church - Message Received',
                'form': ContactForm(),
                'message': 'Message Sent'
            }

            return render(request, 'contact.html', context)
    else:
        form = ContactForm()
        context = {
            'title': 'LIFT Church - Contact',
            'form': form
        }

    return render(request, 'contact.html', context)


# Admin views

def adminHome(request):
    if request.user.is_authenticated:
        return render(request, 'admin_home.html')

    return redirect('/admin_login/')

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/lift-admin/')

    return render(request, 'admin_login.html')

def adminLogout(request):
    logout(request)
    return redirect('/')

def allPosts(request):
    posts = TextPost.objects.all()

    context = {
        "title": "Text Posts",
        "posts": posts
    }

    return render(request, 'admin_posts.html', context)

def createPost(request):
    if request.method == 'POST':
        form = CreateTextPost(request.POST, request.FILES)

        if form.is_valid():
            post = TextPost.objects.create(
                title = form.cleaned_data['title'],
                post_image = request.FILES['post_image'],
                content = form.cleaned_data['content'],
                author = request.user
            )

            post.save()
            return redirect('/lift-admin/posts/')
    else:
        form = CreateTextPost()
        
    return render(request, 'add-post.html', {"form": form})

def editPost(request, id):
    post = TextPost.objects.get(id=id)

    if request.method == 'POST':
        form = CreateTextPost(request.POST, request.FILES)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            if len(request.FILES) != 0:
                post.post_image = request.FILES['post_image']
            else:
                post.post_image = post.post_image
            post.content = form.cleaned_data['content']

            post.save()
            return redirect('/lift-admin/posts/')
    else:
        form = CreateTextPost(initial = {
            'title': post.title,
            'post_image': post.post_image,
            'content': post.content
        })

    return render(request, 'edit-post.html', {"form": form, "post": post})

def deletePost(request, id):
    post = TextPost.objects.get(id=id)
    post.delete()

    return redirect('/lift-admin/posts/')

def allVideos(request):
    videos = VideoPost.objects.all()

    context = {
        "title": "Video Posts",
        "videos": videos
    }

    return render(request, "admin_videos.html", context)

def createVideo(request):
    if request.method == 'POST':
        form = CreateVideoPost(request.POST, request.FILES)

        if form.is_valid():
            video = VideoPost.objects.create(
                title = form.cleaned_data['title'],
                post_video = request.FILES['post_video'],
                description = form.cleaned_data['description'],
                author = request.user
            )

            video.save()
            return redirect('/lift-admin/videos')
    else:
        form = CreateVideoPost()

    return render(request, 'add-video.html', {"form": form})

def editVideo(request, id):
    video = VideoPost.objects.get(id=id)

    if request.method == 'POST':
        form = CreateVideoPost(request.POST, request.FILES)

        if form.is_valid():
            video.title = form.cleaned_data['title']
            if len(request.FILES) != 0:
                video.post_video = request.FILES['post_video']
            else:
                video.post_video = video.post_video
            video.description = form.cleaned_data['description']

            video.save()
            return redirect('/lift-admin/videos/')
    else:
        form = CreateVideoPost(initial = {
            'title': video.title,
            'post_video': video.post_video,
            'description': video.description
        })

    return render(request, 'edit-video.html', {"form": form, "video": video})


def deleteVideo(request, id):
    video = VideoPost.objects.get(id=id)
    video.delete()

    return redirect('/lift-admin/videos/')

def allCarousel(request):
    images = HomeCarousel.objects.all()

    context = {
        "title": "Carousel Images",
        "images": images
    }

    return render(request, 'admin_images.html', context)

def addCarousel(request):
    if request.method == 'POST':
        form = CreateCarousel(request.POST, request.FILES)

        if form.is_valid():
            image = HomeCarousel(
                image = request.FILES['image']
            )

            image.save()
            return redirect('/lift-admin/carousel/')
    else:
        form = CreateCarousel()

    return render(request, 'add-image.html', {"form": form})

def deleteImage(request, id):
    image = HomeCarousel.objects.get(id=id)
    image.delete()

    return redirect('/lift-admin/carousel/')

def allCarouselText(request):
    text = HomeCarouselText.objects.all()
    context = {
        "title": "Carousel Text",
        "text": text
    }

    return render(request, "admin_text.html", context)

def addCarouselText(request):
    if request.method == 'POST':
        form = CreateCarouselText(request.POST)

        if form.is_valid():
            text = HomeCarouselText(
                text = form.cleaned_data['text']
            )

            text.save()
            return redirect('/lift-admin/carousel-text/')
    else:
        form = CreateCarouselText()

    return render(request, 'add-text.html', {"form": form})

def editCarouselText(request, id):
    text = HomeCarouselText.objects.get(id=id)

    if request.method =='POST':
        form = CreateCarouselText(request.POST)
        if form.is_valid():
            text.text = form.cleaned_data['text']
            text.save()
            return redirect('/lift-admin/carousel-text/')
    else:
        form = CreateCarouselText(initial= {
            'text': text.text
        })
    return render(request, 'edit-text.html', {"form": form, 'text': text})

def deleteText(request, id):
    text = HomeCarouselText.objects.get(id=id)
    text.delete()

    return redirect('/lift-admin/carousel-text/')
