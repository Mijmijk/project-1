from django.shortcuts import render
import random


def signup(request):
    return render (request, "firstapp/index.html")
def magic_number(request):
    if request.method == "POST": 
        number = int(request.POST['number'])
        random_number = random.randint (1,10)
        if number==random_number: 
            return render(request, "firstapp/magic_number.html", {'result': "УРА ПОБЕДА"} )
        else :
            return render(request, "firstapp/magic_number.html", {'result': " гг )))"} )
    else : 
        return render(request, "firstapp/magic_number.html")