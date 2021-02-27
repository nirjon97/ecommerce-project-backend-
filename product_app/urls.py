from django.urls import path
from product_app.views import Comment_Add

urlpatterns = [
    path('comment_add/<int:id>/', Comment_Add, name='comment_add'),
]