from django.urls import path
from . import views
from .views import login_view, home_view, logout_view

urlpatterns = [
    path('', login_view, name="login"),  # Login como página principal
    path('home/', home_view, name="home"),  # Página principal después del login
    path('registrarCurso/', views.registrarCurso),
    path('home/edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('home/eliminarCurso/<codigo>', views.eliminarCurso),
    path("logout/", logout_view, name="logout"),
]