
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class AuthenticatedGenericAPIView(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]