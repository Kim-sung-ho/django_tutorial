import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name": '족발',"price":30000}, 
             {"name": '햄버거',"price":5000}, 
             {"name": '치킨',"price":20000}, 
             {"name": '초밥',"price":15000},
             ]
    pick = random.choice(menus)
    #딕셔너리의 key로 사용할 변수명을 만들고, value로 딕셔너리에 넣어준다.
    context ={
        'pick' : pick,
        'name': name,
        'menus': menus,
    }
    return render(request, 'dinner.html',context)