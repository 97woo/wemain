from django.db import models

class Actor(models.Model):
    first_name    = models.CharField(max_length=20)
    last_name     = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    # though를 지정해주지 않을시 다른 테이블로 접근하기 힘들어진다고 한다 참고!
   
    movies        = models.ManyToManyField("Movie", through="Actor_Movie")
    
    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title        = models.CharField(max_length=20)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'
        
class Actor_Movie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'
        
        
        #정참조 역참조 개념을 다시 정리하고 many to many를 다시 이해 하고 블로깅 ..