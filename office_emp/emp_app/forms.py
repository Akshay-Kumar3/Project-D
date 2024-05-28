#accounts/forms.py
from django import forms
from .models import Employee
class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)  # Storing passwords securely requires hashing, consider using Django's built-in authentication system
    confirm_password =forms.CharField(max_length=128)

    class Meta:
        model = Employee
        fields = ['username','password','confirm_password']

# forms.py
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # def validate_password(self, password):
    #     if not re.search(r'[A-Za-z]', password):
    #         raise ValidationError("Password must contain at least one alphabet.")
    #     if not re.search(r'[0-9]', password):
    #         raise ValidationError("Password must contain at least one digit.")
    #     if not re.search(r'[!@#$%^&*()_+=-]', password):
    #         raise ValidationError("Password must contain at least one special character.")
    #     if not re.search(r'[A-Z]', password):
    #         raise ValidationError("Password must contain at least one uppercase letter.")
    # def clean_password1(self):
    #     password1 = self.cleaned_data.get("password1")
    #     self.validate_password(password1)
    #     return password1
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')





