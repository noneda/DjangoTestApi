from django.db import models
class Users(models.Model):

    state = {
        "Onl" : "Online",
        "Ofl" : "Ofline",
        "Ban" : "Banned"
    }
    
    name = models.CharField(max_length = 50)
    pasw = models.CharField(max_length = 50)
    status = models.CharField(max_length =  3, choices = state)