from django import  forms

QUESTIONS = (
    ('', 'Select a Question'),
    ('First elementary school I attended?', 'First elementary school I attended?'),
    ('The high school I graduated from?', 'The high school I graduated from?'),
    ("Mother's city of birth?", "Mother's city of birth?"),
    ("Father's city of birth?", "Father's city of birth?"),
    ('Your city of birth?', 'Your city of birth?'),
    ("Name of your first pet?", "Name of your first pet?"),
    ("Best friend in high school?", "Best friend in high school?"),
    ('Model of your first car?', 'Model of your first car?'),
    ("Name of your first pet?", "Name of your first pet?"),
    ("Your favorite sports team?", "Your favorite sports team?"),
    ('Your first employer (company name)?', 'Your first employer (company name)?'),
)

class Registration_form(forms.Form):
    username =  forms.CharField(max_length=30)
    password = forms.PasswordInput(min_length=6)
    confirm_password = forms.PasswordInput(min_length=6)
    email = forms.EmailField()
    secretQ = forms.Select(choices=QUESTIONS)
    answer = forms.CharField(max_length=30)