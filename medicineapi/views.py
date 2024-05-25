from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from medicalstorapp.forms import medicalform
from medicalstorapp.models import medicalstore
from .serializer import medicalserializers
from django.shortcuts import get_object_or_404

@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        form.save()
        return Response('account creater successfully', status=HTTP_201_CREATED)
    return Response(form.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'erroe': 'please provide both username and password'}, status=HTTP_400_BAD_REQUEST )
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error':'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsADirectoryError,))
def create_data(request):
    form = medicalform(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=HTTP_201_CREATED)
    return Response(form.error, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def retrive_data(request):
    product = medicalstore.objects.all()
    serializer = medicalserializers(product, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_data(request, id):
    product = get_object_or_404(medicalstore, pk=id)
    form = medicalform(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = medicalserializers(product)
        return Response(serializer.data)
    else:
        return Response(form.error, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_data(request, id): 
    try:
        product = medicalstore.objects.get(pk=id)

    except medicalstore.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response('data deleate sucessfully')

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def search_data(request, query):
    medicines = medicalstore.objects.filter(name__istartswith=query)
    serializer = medicalserializers(medicines, many=True)
    
    if medicines.exists():
        return Response(serializer.data)
    else:
        return Response({'message': 'Medicine not found'}, status=HTTP_404_NOT_FOUND)