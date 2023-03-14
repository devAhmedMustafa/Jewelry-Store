from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','email']