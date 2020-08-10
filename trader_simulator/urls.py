from django.urls import path
from trader_simulator.views import new_investment, my_wallet, home, registration
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'trader_simulator'

urlpatterns = [
    path('', home, name='home'),
    path('new_investment', new_investment, name='new_investment'),
    path('my_wallet', my_wallet, name='my_wallet'),
    path('login', LoginView.as_view(template_name='login.html')),
    path('logout', LogoutView.as_view(template_name='logout.html')),
    path('registration', registration, name='registration')
]
