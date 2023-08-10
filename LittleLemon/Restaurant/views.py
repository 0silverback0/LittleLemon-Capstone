from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
        
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# @api_view()
# @permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})