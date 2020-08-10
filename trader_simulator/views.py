from django.shortcuts import render
from django.db.models import Sum
from trader_simulator.models import InvestmentLog
from trader_simulator.external_data.exchange_apis import MarketData

def new_investment(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

def my_wallet(request):
    username = request.user.username
    user_investments = list(
        InvestmentLog.objects.values('investment_symbol').\
        filter(username__exact=username).\
        annotate(total_quantity=Sum('quantity'))
    )

    market_data = MarketData()

    total_value = 0
    for index, investment in enumerate(user_investments):
        symbol = investment['investment_symbol']
        quantity = investment['total_quantity']
        value = market_data.get_value(symbol, quantity)
        user_investments[index]['value'] = value

        total_value += value

    context = {
        'investments': user_investments,
        'total_value': total_value
    }

    return render(request, 'my_wallet.html', context=context)
