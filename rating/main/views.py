from django.views.generic import DetailView
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from .forms import SignupForm,ReviewAdd
from django.contrib.auth import login,authenticate
from .models import Book,BookReview
from django.db.models import Avg

#Base home 
def home(request):
	data=Book.objects.filter()
	
	# avg_reviews=BookReview.objects.filter(book=product).aggregate(avg_rating=Avg('review_rating'))
	return render(request,'index.html',{'data':data})
	
    
#On click detials page
def product_detail(request,id):
	product=Book.objects.get(id=id)
	reviewForm=ReviewAdd()

	# Check
	canAdd=True
	reviewCheck=BookReview.objects.filter(user=request.user,book=product).count()
	if request.user.is_authenticated:
		if reviewCheck > 0:
			canAdd=False
	# End

	# Fetch reviews
	reviews=BookReview.objects.filter(book=product)
	# End

	# Fetch avg rating for reviews
	avg_reviews=BookReview.objects.filter(book=product).aggregate(avg_rating=Avg('review_rating'))
	# End

	return render(request, 'product_detail.html',{'data':product,'reviewForm':reviewForm,'canAdd':canAdd,'reviews':reviews,'avg_reviews':avg_reviews})

#save reviews 
def save_review(request,pid):
	book=Book.objects.get(pk=pid)
	user=request.user
	review=BookReview.objects.create(
		user=user,
		book=book,
		review_rating=request.POST['review_rating'],
		)
	data={
		'user':user.username,
		'review_rating':request.POST['review_rating']
	}

	# Fetch avg rating for reviews
	avg_reviews=BookReview.objects.filter(book=book).aggregate(avg_rating=Avg('review_rating'))
	# End

	return JsonResponse({'bool':True,'data':data,'avg_reviews':avg_reviews})


# Signup Form
def signup(request):
	if request.method=='POST':
		form=SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			pwd=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=pwd)
			login(request, user)
			return redirect('home')
	form=SignupForm
	return render(request, 'registration/signup.html',{'form':form})


