from django import forms

# form for user card input 
class MakePaymentForm(forms.Form):

	MONTH_CHOICES = [(i, i) for i in range(1, 13)]
	YEAR_CHOICES = [(i, i) for i in range(2020, 2039)]

	credit_card_number = forms.CharField(label='Credit card number', min_length=16, max_length=16, required=False)
	cvv = forms.CharField(label='Security code (CVV)', min_length=3, max_length=3, required=False)
	expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
	expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
	stripe_id = forms.CharField(widget=forms.HiddenInput, required=False)
