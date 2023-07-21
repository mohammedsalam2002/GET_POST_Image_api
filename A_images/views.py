from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Images
from .serializer import ImagesSerializer
from rest_framework.authentication import BasicAuthentication ,TokenAuthentication
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

#use BVF
@api_view(['GET','POST'])
def get_image(request):
    # GET 
    if request.method == 'GET':
        guests = Images.objects.all()
        serializer = ImagesSerializer(guests, many=True) # ان وضع (مني يساوي صح ) لانه يتعامل مع اكثر من عنصر
        return Response(serializer.data)
    elif request.method == 'POST':

        serailizer = ImagesSerializer(data = request.data)
        if serailizer.is_valid():
            serailizer.save()
            # نرجع الداتا الذي تم تكوينه
            return Response(serailizer.data)
        return Response(serailizer.data)
    

# use generic
class Images_List(generics.ListCreateAPIView):
    queryset =Images.objects.all()
    serializer_class = ImagesSerializer

    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']




