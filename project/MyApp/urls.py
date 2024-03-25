from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Home , name='Home'),
    path('books/' , views.Books , name="Books"),
    path('update/<int:id>/' , views.Update , name='Update'),
    path('delete/<int:id>/' , views.Delete , name="Delete")
]