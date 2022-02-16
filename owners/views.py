from django.shortcuts import render
from .models import Owner, Dog
from django.http import JsonResponse
from django.views import View
import json
#Create your views here.

class OwnerView(View):
    def post(self, request):
        #print(request.body) json -> python 
        
        data   = json.loads(request.body)
        owners = Owner.objects.create(
                                name=data['name'],  
                                email=data['email'],
                                age=data['age']
                                   )
        return JsonResponse({"result":"created"},status=201)

    def get(self, request):
        owners  = Owner.objects.all()
        results = []
        
        
        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list = []
            
            for dog in dogs:
                dog_result = {
                    "name" : dog.name,
                    "age"  : dog.age
                }    
                dog_list.append(dog_result)
            
            owner_result = {
                    "name"      : owner.name,
                    "email"     : owner.email,
                    "age"       : owner.age,
                    "dog_list"  : dog_list 
                 }
            results.append(owner_result)
            
        return JsonResponse({"result":results}, status=200)
        
        
       

class DogView(View):
    def post(self, request):
        
        #print(request.body) json -> python 
        
        data = json.loads(request.body)
        dogs = Dog.objects.create(owner_id = data['owner_id'], name=data['name'],age=data['age'])
      
        return JsonResponse({"result":"created"},status=201)
    
    def get(self,request):
        
       dogs = Dog.objects.all()
       results = []
       
       for dog in dogs:
        result = {
                    "name"  : dog.name,
                    "age"   : dog.age,
                    "owner" : dog.owner_id
                    
                 }
        results.append(result)
        
        return JsonResponse({"result":result}, status=200)
        
        