
from django.shortcuts import render
from .models import Roles,Users
from .serializers import RoleSerializer,UserSerializer
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.core import serializers
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
import bcrypt
from . validators import *




class RoleAPI(APIView):
	def get(self,request,*args,**kwargs):
		try:
			obj=Roles.objects.all()
			serializer=RoleSerializer(obj,many=True)
			return Response(serializer.data)
		except Roles.DoesNotExist:
			raise Http404

	def post(self,request,format=None):
		try:
			serializer=RoleSerializer(data=request.data,partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response({"success":True,"data":serializer.data})
			return Response({"message":serializer.errors})
		except Http404:
			return Response({"message":"data not added"})


class getUpdateDeleteRole(APIView):
    def get_object(self,id):
        try:
            return Roles.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=RoleSerializer(get)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"listings not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=RoleSerializer(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
            return JsonResponse({"message":serializer.errors})
        except Http404:
            return JsonResponse({"message":"data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return Response({"message":"data  deleted"})
        except Http404:
            return JsonResponse({"message":"data not deleted"})




class UserAPI(APIView):
	def get(self,request,*args,**kwargs):
		try:
			obj=Users.objects.all()
			serializer=UserSerializer(obj,many=True)
			return Response(serializer.data)
		except Users.DoesNotExist:
			raise Http404

	def post(self,request,format=None):
		try:
			serializer=RoleSerializer(data=request.data,partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response({"success":True,"data":serializer.data})
			return Response({"message":serializer.errors})
		except Http404:
			return Response({"message":"data not added"})


class getUpdateDeleteUser(APIView):
    def get_object(self,id):
        try:
            return Users.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=UserSerializer(get)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"listings not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=UserSerializer(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
            return JsonResponse({"message":serializer.errors})
        except Http404:
            return JsonResponse({"message":"data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return Response({"message":"data  deleted"})
        except Http404:
            return JsonResponse({"message":"data not deleted"})



class UserSignupAPI(APIView):

	def post(self,request,format=None):

            obj = request.data
            password = obj["password"]
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password, salt)

            #hashed_pwd = make_password("password")
            request.data["password"]= hashed
            serializer=UserSerializer(data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"success":True,"data":serializer.data})
            return Response({"message":serializer.errors})
        #except Http404:
			#return Response({"message":"data not added"})



class UserSigin(APIView):
	def post(self,request,format=None):
            obj = request.data
            email = obj["email"]
            password = obj["password"]
            email_check = Users.objects.filter(email=requesst.data["email"]).first()
            if email_check is not None:
                hashed_password = email_check.password
                print(hashed_password)
                if bcrypt.checkpw(password,hashed_password):
                    return Response ({"success":True,
                        'message': 'logined successfully'
                        })
                else:
                    return Response({"success":False,"message": "Invalid password"})
            else:
                return Response({"success":False,"message": "Invalid UserName"})



class FileUploadView(APIView):
    permission_classes = []
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class Signup(APIView):

	def post(self,request,format=None):

            obj = request.data
            password = obj["password"]

            if len(password) < 8 or password.lower() == password or password.upper() == password or password.isalnum()\
                    or not any(i.isdigit() for i in password):
                return Response({"message":"The password must week"})
            else:
                salt = bcrypt.gensalt()
                hashed = bcrypt.hashpw(password, salt)

                #hashed_pwd = make_password("password")
                request.data["password"]= hashed
                serializer=UserSerializer(data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"success":True,"data":serializer.data})
                return Response({"message":serializer.errors})
