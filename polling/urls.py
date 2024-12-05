
from django.urls import path
from polling.views import PolllistView, PollDetailView


urlpatterns = [
    path('', PolllistView.as_view(), name='poll_index'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll_detail')
]