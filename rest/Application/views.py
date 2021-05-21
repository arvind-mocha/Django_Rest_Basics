from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Create your views here.

# View sets

# low code advantages
# best to use when you need usage of all api calls
# all mixins are inherited automatically
# the advantage is can use with rest api router method to display all available routes

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# Generic viewset is like Generic class as the advantage is can use with rest api router method to display all routes
# don't want to define any functions like noremal gerneric class, while using generic viewset you just need the serializer and queryset
# class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

#     lookup_field = 'id'


# Normal viewset is like normal class only as the advantage is can use with rest api router method to display all routes
# class ArticleViewSet(viewsets.ViewSet):
#     def list(self,request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     def create(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self,request,pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def update(self,request,pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Generic Class Based Api

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin): # these mixins represents the api request we are permitted to perform 
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id' # Primary Key

    #authentication_classes = [SessionAuthentication,BasicAuthentication] # Basic Authentication is just your Name and password
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] # for basic authentication

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id = None):
        return self.update(request,id)

    def delete(self, request, id):
        return self.destroy(request, id)

# Class based rest_framework view

class ArticleAPIView(APIView):
    def get(self,requets):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self,id):
        return Article.objects.get(id=id)
    
    def get(self,request,id):
        try:
            article = self.get_object(id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Function Based rest_framework views

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Normal Django Views

# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_detail(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)