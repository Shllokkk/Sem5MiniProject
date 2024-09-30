
from django.db import models
from datetime import date

# Create your models here.
class Querry(models.Model):
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    desc = models.TextField()
    date = models.DateField(default=date.today)
    Cat = models.CharField(max_length=20, default='Other')

    def __str__(self):
        return f"{self.query_id}"

class Signup(models.Model):
    name = models.CharField(max_length=30,default='xyz')
    password = models.CharField(max_length=15,default='123')
    email = models.EmailField(max_length=40, default='sample@gmail.com')
    Year = models.CharField(max_length=10, default='2')
    Branch = models.CharField(max_length=20, default='IT')  
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Answers(models.Model):
    answer_id = models.AutoField(primary_key=True)
    query = models.ForeignKey(Querry,related_name='answers', on_delete=models.CASCADE)
    response = models.TextField()
    rating = models.FloatField(default=0.0)
    date = models.DateField(default=date.today)

    def __str__(self):
        return (
            f"Answer ID:- {self.answer_id},\n"
            f"Query ID:- {self.query},\n"
            f"Date:- {self.date},"
        )

class Rating(models.Model):
    rating = models.FloatField()  
    answer = models.ForeignKey(Answers, related_name='ratings', on_delete=models.CASCADE)  
    user_rated = models.ForeignKey(Signup, related_name='user_rated', on_delete=models.CASCADE) 
    user_rater = models.EmailField() 
    date = models.DateField(default=date.today)  

    def __str__(self):
        return (
            f"Rating: {self.rating_value} for Answer ID: {self.answer.answer_id} "
            f"by User: {self.user_rater}"
        )
    
       
