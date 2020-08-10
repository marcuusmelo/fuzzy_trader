from django.urls import path
from trader_simulator.views import new_investment, my_wallet

app_name = 'trader_simulator'

urlpatterns = [
    path('new_investment', new_investment, name='new_investment'),
    path('my_wallet', my_wallet, name='my_wallet'),
]
