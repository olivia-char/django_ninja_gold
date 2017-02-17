from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.

def index(request):
	if "gold" not in request.session:
		request.session["gold"] = 0 
	if "result" not in request.session:
		request.session["result"] = " "	

	return render (request, 'golds/index.html')

def process_money(request):
	if request.POST["building"] == "farm": 
		addgold = random.randrange(10,20)
		request.session["gold"] += addgold 
		request.session["result"] += "You earned" + str(request.session["gold"]) + " from the farm"
	if request.POST["building"] == "cave":
		addgold = random.randrange(5,10)
		request.session["gold"] += addgold
		request.session["result"] += str("You earned" + str(request.session["gold"]) + " from the cave")
	if request.POST["building"] == "house":
		addgold = random.randrange(2,5)
		request.session["gold"] += addgold
		request.session["result"] += str("You earned" + str(request.session["gold"]) + " from the house")
	if request.POST["building"] == "casino":
		addgold = random.randrange(-50,50)
		request.session["gold"] += addgold
		request.session["result"] += str("You earned" + str(request.session["gold"]) + " from the casino")
	return redirect('/')
