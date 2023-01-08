from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Book,BookReview
from .serializers import ItemSerializer,RatingSerializer

@api_view(['GET'])
def getData(request):
    books = BookReview.objects.all()
    serializer = RatingSerializer(books, many =True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = RatingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("Invalid")
    return Response(serializer.data)

