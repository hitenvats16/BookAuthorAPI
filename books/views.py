from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

# Like book with given id (for authenticated user only)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def LikeABook(request, id):
    book = Book.objects.get(pk=id)
    user = request.user
    if user in book.likes.all():
        return Response('Already Liked', status=status.HTTP_400_BAD_REQUEST)
    book.no_of_likes = book.no_of_likes + 1
    book.likes.add(request.user)
    book.save()
    return Response('Liked', status=status.HTTP_202_ACCEPTED)

# Unlike book with given id (for authenticated user only)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UnlikeABook(request, id):
    book = Book.objects.get(pk=id)
    user = request.user
    if user not in book.likes.all():
        return Response('Already not Liked', status=status.HTTP_400_BAD_REQUEST)
    book.likes.remove(request.user)
    book.no_of_likes = book.no_of_likes - 1
    book.save()
    return Response('Unliked', status=status.HTTP_202_ACCEPTED)

# Return details of book with given id to authenticated user


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def GetDetails(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

# Return a paginated response of all books to authenticated user


class ListBooks(ListAPIView):
    queryset = Book.objects.all().order_by('-no_of_likes', 'id')
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
