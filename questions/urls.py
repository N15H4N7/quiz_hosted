from django.urls import path
from .views import calculate_marks, marks_page, export_answers_xls

urlpatterns = [
    path('marks/', calculate_marks, name = 'marks'),
    path('marks-page/', marks_page, name = 'marks-page'),
    path('export-answers/', export_answers_xls, name = 'export'),
]
