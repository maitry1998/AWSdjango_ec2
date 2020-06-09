from django.shortcuts import render
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
import json

#
#
# @api_view(['GET', 'POST'])
# def article_list(request):
#     # this methid is used to get or post data
#     if request.method == "GET":
#         data=Article.objects.all()
#         # import pdb;pdb.set_trace()
#         return JsonResponse(ArticleSerializer(data,many=True).data,safe=False)
#     elif request.method == 'POST':
#         data=JSONParser().parse(request)
#         ser=ArticleSerializer(data=data)
#         # import pdb;pdb.set_trace()
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data, status=201)
#         return JsonResponse(ser.errors, status=400)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_int(request,pk):
#     # this methid is used to get or post data
#     try:
#         data = Article.objects.get(pk=pk)
#     except:
#         return HttpResponse( status=404)
#
#     if request.method == "GET":
#         return JsonResponse(ArticleSerializer(data).data)
#
#     elif request.method == 'PUT':
#         data_from_request=JSONParser().parse(request)
#         ser=ArticleSerializer(data,data=data_from_request)
#         # import pdb;pdb.set_trace()
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data, status=201)
#         return JsonResponse(ser.errors, status=400)
#
#     elif request.method == 'DELETE':
#         data.delete()
#         return JsonResponse(ArticleSerializer(data,many=True).data,safe=False)
#
#
#

class ArticleListView(APIView):
    # this methid is used to get or post data
    def get(self,request):
        data=Article.objects.all()
        return JsonResponse(ArticleSerializer(data,many=True).data,safe=False)
    def post(self,request):
        # data=JSONParser().parse(request)
        ser=ArticleSerializer(data=request.data)
        # import pdb;pdb.set_trace()
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)


class ArticleintView(APIView):
    def get_ob(self,pk):
        try:
            return Article.objects.get(pk=pk)
        except:
            return HttpResponse( status=404)

    def get(self,request,pk):
        print(ArticleSerializer(self.get_ob(pk)).data)
        return JsonResponse(ArticleSerializer(self.get_ob(pk)).data)

    def put(self,request,pk):
        ser=ArticleSerializer(instance=self.get_ob(pk),data=request.data)
        # import pdb;pdb.set_trace()
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)

    def delete(self,request,pk):
            self.get_ob(pk=pk).delete()
            return JsonResponse(ArticleSerializer(instance=Article.objects.all(),many=True).data,safe=False)


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)