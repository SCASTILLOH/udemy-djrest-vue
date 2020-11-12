from django_registration.forms import RegistrationForm
from django_registration.forms import RegistrationFormUniqueEmail
from users.models import CustomUser

# Sin verificacion de email unique, solo usuario.

# class CustomUserForm(RegistrationForm):

#     class Meta(RegistrationForm.Meta):
#         model = CustomUser
#         fields = '__all__'

# Sin verificacion de email unique, solo usuario.

class CustomUserForm(RegistrationFormUniqueEmail):

    class Meta(RegistrationFormUniqueEmail.Meta):
        model = CustomUser
        
