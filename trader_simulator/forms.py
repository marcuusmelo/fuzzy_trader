from django.forms import forms, IntegerField

class InvestmentInputForm(forms.Form):
    """
    Form to get amount to invest from user
    """
    investment_amount = IntegerField()
