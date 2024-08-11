from django.contrib import admin
from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import BlogRecordCreate, BlogRecordIndexView, BlogRecordDeatilView, BlogRecordUpdate, \
    BlogRecordDeleteView, toggle_published

app_name = BlogConfig.name


urlpatterns = [
    path('create/', BlogRecordCreate.as_view(), name='create'),
    path('view/<int:pk>/', BlogRecordDeatilView.as_view(), name='view'),
    path('', BlogRecordIndexView.as_view(), name='list'),
    path('edit/<int:pk>/', BlogRecordUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogRecordDeleteView.as_view(), name='delete'),
    path('published/<int:pk>/', toggle_published, name='is_published'),
]