from django.shortcuts import render

from booking.models import User
# Create your views here.

def index(request):
	user_list = User.objects.all()
	context = {'user_list':user_list}
	return render(request, 'booking/index.html', context)