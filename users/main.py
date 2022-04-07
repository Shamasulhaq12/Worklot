from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.all()[1]
print(user)
