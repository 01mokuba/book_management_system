from django.urls import path

from .models import Book
from .views import BookFilterView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

# アプリケーションのルーティング設定

urlpatterns = [
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
    path('', BookFilterView.as_view(), name='index'),
]
