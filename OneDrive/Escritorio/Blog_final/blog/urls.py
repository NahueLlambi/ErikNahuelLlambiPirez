from django.urls import path
from .views import render_post, post_details, decks_not_available
from . import views

app_name = 'blog'

urlpatterns = [ 
    path('', render_post, name='render_post'), 
    path('<int:post_id>', post_details, name='post_details'),
    path('decks/', decks_not_available, name='deck_not_available'),
    path("registration/", views.UserRegistration.as_view(), name="registration"),
    path("success/", views.success_view, name="success_view"),  
]
