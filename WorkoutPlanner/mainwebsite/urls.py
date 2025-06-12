from django.urls import path  # Import the path function to define URL patterns
from . import views  # Import views from the current app to link URLs to view functions
 
urlpatterns = [
    # Define URL patterns here to route specific requests to corresponding view functions.
    # Example:
    # path('home/', views.home, name='home')  # This would route 'yourwebsite.com/home/' to the home view.
 
    #website homepage
    path("", views.index, name="index"),  # Root URL for the app
    path("signup", views.signup, name="signup"),  # Root URL for the app
    path("dashboard", views.dashboard, name="dashboard")
]

