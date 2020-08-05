from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='Lift Home'),
    path('about-us/', views.about, name="Lift About"),
    path('sermens/', views.sermens, name="Lift Sermens"),
    path('sermens/<int:id>/', views.sermen_detail, name="Lift Sermen Details"),
    path('sermens/videos/<int:id>', views.video_detail, name="Lift Sermen Video"),
    path('ministries/', views.ministries, name="Lift Ministries"),
    path('our-mission/', views.our_mission, name="Lift Mission"),
    path('our-vision/', views.our_vision, name="Lift Vision"),
    path('our-beliefs/', views.our_beliefs, name="Lift Beliefs"),
    path('core-values/', views.core_values, name="Lift Values"),
    path('roman-road/', views.roman_road, name="Lift Roman Road"),
    path('donate/', views.donate, name="Lift Donation"),
    path('team/', views.team, name="Lift Team"),
    path('contact/', views.contact, name="Lift Contact"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
