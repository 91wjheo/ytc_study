from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from django.utils import timezone

# Create your views here.
def test(request):
    return HttpResponse("Hello World")

def map(request):
    return render(request, 'restaurantApp/map.html')

def map_add(request):
    # request객체에서 POST로 넘어온 파라미터를 가져옴.
    name = request.POST['name']
    phone = request.POST['phone']
    address = request.POST['address']
    lat = request.POST['lat']
    lng = request.POST['lng']

    print(name, phone, address, lat, lng)

    # restaurant객체 생성
    restaurant_info = Restaurant(name=name, phone=phone, address=address, lat=lat, lng=lng)
    restaurant_info.save() #db에 insert

    return render(request, 'restaurantApp/map.html')



def map_list_all(request):
    # QuerySet을 가져옴 -> 이걸 템플릿 컨텍스트에 전달할거임.
    restaurants = Restaurant.objects.filter(created__lte=timezone.now()).order_by('created')

    # render메서드를 호출하여 'first/post_list.html'템플릿을 보여줍니다.
    # 이때 위에서 가져온 QuerySet인 posts를 템플릿에 'posts'라는 문자열로 같이 넘겨줌.!
    return render(request, 'restaurantApp/map_list.html', {'restaurants':restaurants})

