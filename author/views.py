# Views for the user API

from rest_framework import generics, authentication, permissions
from .serializers import AuthorSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


class ManageUserView(generics.RetrieveUpdateAPIView):
    # Manage the authenticated user
    serializer_class = AuthorSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retrieve and return the authenticated user
        user = self.request.user
        return user

# Return a List of authors to authenticated user


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AuthorList(request):
    user = get_user_model().objects.all()
    serializer = AuthorSerializer(user, many=True)
    return Response(serializer.data)
