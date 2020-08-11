from django.shortcuts import render
from django.core.mail import send_mail
from .models import HomeCarousel, TextPost, VideoPost
from .forms import ContactForm

def index(request):
    images = HomeCarousel.objects.all()
    new_posts = TextPost.objects.order_by('-id')[:2]
    new_video = VideoPost.objects.order_by('-id').first()
    context = {
        'title': 'LIFT Church - Home',
        'images': images,
        'posts': new_posts,
        'video': new_video
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
