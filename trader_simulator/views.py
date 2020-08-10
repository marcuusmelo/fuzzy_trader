from django.shortcuts import render, redirect
from django.db.models import Sum
from trader_simulator.forms import InvestmentInputForm
from trader_simulator.models import InvestmentLog
from django.contrib.auth.forms import UserCreationForm
from trader_simulator.external_data.exchange_apis import MarketData
from trader_simulator.external_data.exchange_apis_config import AVAILABLE_INVESTMENTS
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trader_simulator:my_wallet')
    else:
        form = UserCreationForm()
        context = {'form': form}

        return render(request, 'registration.html', context=context)


@login_required(login_url='/login')
def new_investment(request):
    available_investments = AVAILABLE_INVESTMENTS

    form = InvestmentInputForm()

    if request.method == 'GET' and 'investment_amount' in request.GET:
        market_data = MarketData()
        investment_amount = float(request.GET['investment_amount'])
        investment_data = market_data.get_all_data(investment_amount=investment_amount)
        investments = {'data': investment_data}
        return render(request, 'investment_select.html', context=investments)

    elif request.method == 'POST':
        username = request.user.username
        investment_symbol = request.POST['investment_symbol']
        quantity = request.POST['quantity']
        InvestmentLog(
            username=username,
            investment_symbol=investment_symbol,
            quantity=quantity
        ).save()
        return redirect('trader_simulator:my_wallet')

    context = {'form': form}
    return render(request, 'investment_form.html', context=context)


@login_required(login_url='/login')
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
