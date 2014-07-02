from django.shortcuts import render, get_object_or_404

from booking.models import User, Houses
# Create your views here.

def index(request):
	user_list = User.objects.all() #A line of code here to go get all the users
	return render(request, 'booking/index.html', {'user_list':user_list})

def UserView(request, User_id):
	user = get_object_or_404(User, pk=User_id)
	house = Houses.objects.get(user_id=User_id)
	return render(request, 'booking/user.html', {'user': user}, {'house':house})