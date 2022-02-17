import json
from django.views import View
from django.http import JsonResponse
from .models import Movie, Actor
# Create your views here.

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []
        
        for actor in actors:
            movies = actor.movies.all()
            movie_lists =[]
            
            for movie in movies:
                movie_results=({
                        "title" : movie.title
                    })
                movie_lists.append(movie_results)
            actor_result=({
                  "first_name" : actor.first_name,
                  "last_name"  : actor.last_name,
                  "movie"      : movie_lists   
                 })
            result.append(actor_result)
        return JsonResponse({"result":result}, status=200)

class MovieView(View):
    def get(self,request):
        movies = Movie.objects.all()
        result = []
        
        for movie in movies:
            actor_lists = []
            actors      = movie.actors_sets.all()
            for actor in actors:
                actor_result=({
                    "name" : actor.last_name 
                })
                actor_lists.append(actor_result)
                actor_result=({
                    "title"         : movie.title,
                    "runnning_time" : movie.running_time,
                    "release_date"  : movie.release_date,
                    "actor"         : actor_lists
                })
                result.append(actor_result)
            return JsonResponse({'result': result},status =200)