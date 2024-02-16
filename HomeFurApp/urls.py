from .views import LoginView, RegisterView, AlldataView, AdminView, GetAllFurView, GetFurbyCategoryView
from django.urls import path 





urlpatterns = [
    path('data', AlldataView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('category', AdminView.as_view()),
    path('furnitures/', GetAllFurView.as_view()),
    path('furnitures/<str:category>', GetFurbyCategoryView.as_view())
]

