"""
Collection of tests for the Trader Simulator App
"""
from django.test import TestCase, Client
from django.urls import reverse

from trader_simulator.forms import InvestmentInputForm
from trader_simulator.models import InvestmentLog


class TestTraderSimulator(TestCase):
    """
    Trader Simulator App Test Class
    """

    def setUp(self):
        """
        Test preparation to run before each test case
        """
        self.client = Client()

    def test_user_investment_numeric_amount(self):
        """
        Check if the user form is valid when it gets a number as input
        """
        data = {'investment_amount': 1000}
        form = InvestmentInputForm(data=data)
        self.assertTrue(form.is_valid())

    def test_user_investment_empty(self):
        """
        Check if the user for is not valid when it gets nothing as input
        """
        data = {'investment_amount': None}
        form = InvestmentInputForm(data=data)
        self.assertFalse(form.is_valid())

    def test_user_investment_bad_value(self):
        """
        Check if the user used a string as input
        """
        data = {'investment_amount': 'One thousand dolars'}
        form = InvestmentInputForm(data=data)
        self.assertFalse(form.is_valid())

    def test_investment_selection(self):
        """
        Check if selected investment gets to InvestmentLog table
        """
        test_username = 'test_user_0000'
        self.client.login(username=test_username, password='secretpw0000')
        investment_data = {
            'investment_amount': 1000,
            'investment_selection': 'AAPL',
        }

        url = reverse('trader_simulator:new_investment')
        response = self.client.post(url, investment_data)
        selected_investment = InvestmentLog.objects.all().filter(username__exact=test_username)
        self.assertEqual(len(selected_investment), 1)

    def test_investment_consolidation(self):
        """
        Check if the sum of the investments added matches the expected result
        """
        test_username = 'test_user_0001'
        self.client.login(username=test_username, password='secretpw0001')

        investment_entry = {
            'username': test_username,
            'investment_symbol': 'AAPL',
            'quantity': 7
        }

        for _ in range(3):
            InvestmentLog(**investment_entry).save()

        url = reverse('trader_simulator:my_wallet')
        response = self.client.get(url)

        self.assertEqual(response.context['investments'][0]['total_quantity'], 21)
