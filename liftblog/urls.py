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
    path('charge/', views.charge, name="Charge"),
    path('error/', views.donateError),
    path('team/', views.team, name="Lift Team"),
    path('contact/', views.contact, name="Lift Contact"),
    # admin paths
    path('admin_login/', views.adminLogin, name="Lift Login"),
    path('admin_logout/', views.adminLogout, name="Lift Logout"),
    path('lift-admin/', views.adminHome, name="Lift Admin"),
    path('lift-admin/posts/', views.allPosts, name="All Posts"),
    path('lift-admin/posts/add-post/', views.createPost, name="Add Post"),
    path('lift-admin/posts/<int:id>/edit/', views.editPost, name="Edit Post"),
    path('lift-admin/posts/<int:id>/delete/', views.deletePost, name="Delete Post"),
    path('lift-admin/videos/', views.allVideos, name="All Videos"),
    path('lift-admin/videos/add-video/', views.createVideo, name="Add Video"),
    path('lift-admin/videos/<int:id>/edit/', views.editVideo, name="Edit Video"),
    path('lift-admin/videos/<int:id>/delete/', views.deleteVideo, name="Delete video"),
    path('lift-admin/carousel/', views.allCarousel, name="All Images"),
    path('lift-admin/carousel/add-image/', views.addCarousel, name="Add Image"),
    path('lift-admin/carousel/<int:id>/delete/', views.deleteImage, name="Delete Image"),
    path('lift-admin/carousel-text/', views.allCarouselText, name="Carousel Text"),
    path('lift-admin/carousel-text/add-text/', views.addCarouselText, name="Add Text"),
    path('lift-admin/carousel-text/<int:id>/edit/', views.editCarouselText, name="Edit text"),
    path('lift-admin/carousel-text/<int:id>/delete/', views.deleteText, name="Delete Text"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
