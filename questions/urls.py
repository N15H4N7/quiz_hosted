from django.urls import path
from .views import calculate_marks, marks_page		

urlpatterns = [
    path('marks/', calculate_marks, name = 'marks'),
    path('marks-page/', marks_page, name = 'marks-page'),
]
