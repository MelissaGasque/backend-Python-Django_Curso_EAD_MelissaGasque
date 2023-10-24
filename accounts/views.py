from rest_framework.generics import CreateAPIView
from accounts.serializers import AccountSerializer


class AccountView(CreateAPIView):
    serializer_class = AccountSerializer
