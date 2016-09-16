from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from svsite.forms import UserForm, UserProfileForm
from cars.models import Car, UserProfile, Wishlist, TestDrive, Dealer
from svsite.forms import SearchForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import json
import random

"""
def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        response_data = {}
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username, password)
            user = authenticate(username=username, password=password)

            if user is not None:
                invalid = False
                if user.is_active:
                    login(request, user)
                    response_data['result'] = 'success'
                    response_data['message'] = 'Successfully logged in!'
                else:
                    response_data['result'] = 'failed'
                    response_data['message'] = 'Your account has been deactivated.'
        else:
            response_data['result'] = 'failed'
            response_data['message'] = 'Invalid credentials supplied!'

        return HttpResponse(json.dumps(response_data), content_type="application/json")
"""


def user_login(request):
    invalid = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            invalid = False
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account has been deactivated.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'login.html', {'invalid': invalid, },)
    else:
        return render(request, 'login.html', {})


def dealer_login(request):
    invalid = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            invalid = False
            dealer = Dealer.objects.get(user=user)
            if dealer.user_profile.is_dealer:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dealer-admin/')
                else:
                    return HttpResponse("Your account has been deactivated.")
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
                return render(request, 'dealer_login.html', {'invalid': invalid, },)
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered = True
        else:
            print(user_form.errors, profile_form.errors)
            return render(request, 'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered,
                   'user_form_errors': user_form.errors, 'profile_form_errors': profile_form.errors},
                  )

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
                  )


def search_form(request):
    return render(request, 'search.html')


def search(request):
    errors = []
    suggestions = []
    cars = None
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        else:
            cars = Car.objects.filter(full_name__icontains=q.strip())
            if not cars:
                cars = Car.objects.filter(type__icontains=q.strip())
                if not cars:
                    cars = Car.objects.filter(manufacturer__icontains=q.strip())
                    if not cars:
                        for i in range(4):
                            suggestions.append(Car.objects.get(id=random.randrange(1,100)))
                        return render(request, 'search-results.html', {'cars': cars, 'query': q, 'suggestions': suggestions})
            return render(request, 'search-results.html', {'cars': cars, 'query': q})

    return render(request, 'search-results.html', {'errors': errors})


def car_details(request, manufacturer, slug):
    car = get_object_or_404(Car, manufacturer_slug=manufacturer, slug=slug)
    offset = 300000
    suggestions = []
    i = 1
    for obj in Car.objects.filter(type=car.type):
        if car.price-offset <= obj.price <=car.price+offset and i <= 4 and car != obj:
            suggestions.append(obj)
            i += 1

    if request.method == 'POST' and request.user.is_authenticated():

        # For wishlist
        if 'wishlist' in request.POST.keys():
            add_wishlist = request.POST['wishlist']
            if add_wishlist == 'True':
                try:
                    user_wishlist = Wishlist.objects.get(user=request.user, car=car)
                    if not user_wishlist.is_active:
                        user_wishlist.is_active = True
                        user_wishlist.save()
                except Wishlist.DoesNotExist:
                    user_wishlist = Wishlist()
                    user_wishlist.user = request.user
                    user_wishlist.car = car
                    user_wishlist.save()

            elif add_wishlist == 'False':
                user_wishlist = Wishlist.objects.filter(user=request.user, car=car).update(is_active=False)

        # For testdrive
        elif 'testdrive' in request.POST.keys():
            print('stuff')
            add_testdrive = request.POST['testdrive']
            if add_testdrive == 'True':
                try:
                    user_testdrive = TestDrive.objects.get(user=request.user, car=car)
                    if not user_testdrive.is_active:
                        user_testdrive.is_active = True
                        user_testdrive.save()
                except TestDrive.DoesNotExist:
                    user_testdrive = TestDrive()
                    user_testdrive.user = request.user
                    user_testdrive.car = car
                    user_testdrive.save()

            elif add_testdrive == 'False':
                user_testdrive = TestDrive.objects.filter(user=request.user, car=car).update(is_active=False)

        return HttpResponseRedirect('/cars/'+car.manufacturer_slug+'/'+car.slug)

    # If user is logged in and just retrieving page
    elif request.method == 'GET' and request.user.is_authenticated():
        try:
            add_wishlist = Wishlist.objects.get(user=request.user, car=car)
            if add_wishlist.is_active:
                add_wishlist = True
            else:
                add_wishlist = False
        except Wishlist.DoesNotExist:
            add_wishlist = False

        try:
            add_testdrive = TestDrive.objects.get(user=request.user, car=car)
            if add_testdrive.is_active:
                add_testdrive = True
            else:
                add_testdrive = False
        except TestDrive.DoesNotExist:
            add_testdrive = False

        print(add_testdrive, add_wishlist)
        return render(request, 'car_details.html',
                      {'car': car, 'add_wishlist': add_wishlist, 'add_testdrive': add_testdrive, 'suggestions': suggestions})

    else:
        return render(request, 'car_details.html', {'car': car, 'suggestions': suggestions})


def search_type(request):
    return render(request, 'search_type.html')


def search_type_results(request):
    errors = []
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            if form.data['manufacturer'] and form.data['type']:
                cd = form.cleaned_data
                print(cd)
                cars = Car.objects.filter(manufacturer=cd['manufacturer'], type=cd['type'])
                return render(request, 'search-results.html', {'cars': cars},)
            else:
                errors.append('Please make sure you select both the type and manufacturer.')
                return render(request, 'home.html', {'errors': errors})
        else:
            return render(request, 'search_type.html', {'form_errors': form.errors})


def search_price_range(request):
    cars = []
    if request.method == 'GET':
        car_objs = Car.objects.all()
        price_range = request.GET['price_range']
        if price_range == '1lakh-5lakh':
            for car in car_objs:
                if 100000 <= car.price < 500000:
                    cars.append(car)

        elif price_range == '5lakh-10lakh':
            for car in car_objs:
                if 500000 <= car.price < 1000000:
                    cars.append(car)

        elif price_range == '10lakh-20lakh':
            for car in car_objs:
                if 1000000 <= car.price < 2000000:
                    cars.append(car)

        elif price_range == '20lakh-50lakh':
            for car in car_objs:
                if 2000000 <= car.price < 5000000:
                    cars.append(car)

        elif price_range == '50lakh-1crore':
            for car in car_objs:
                if 5000000 <= car.price < 10000000:
                    cars.append(car)

        elif price_range == 'above1crore':
            for car in car_objs:
                if car.price >= 10000000:
                    cars.append(car)

        else:
            cars = False
            return render(request, 'search-results.html', {'invalid_price': True},)

        return render(request, 'search-results.html', {'cars': cars},)


# @staff_member_required
def dealer_admin(request):
    count = TestDrive.objects.all().count()
    approved = []
    pending = []
    testdrives = TestDrive.objects.all()
    for td in testdrives:
        if td.confirmed:
            approved.append(td)
        else:
            pending.append(td)
    return render(request, 'dealer-admin.html', {'approved': approved, 'pending': pending, 'count': count})


def dealer_approve(request):
    print('Pass')
    if request.method == 'POST' and request.user.is_authenticated():
        print('Pass')
        id_val = request.POST['val_id']
        print(id_val)
        obj = TestDrive.objects.get(id=id_val)
        obj.confirmed = True
        obj.save()
        return HttpResponseRedirect('/dealer-admin/')
    else:
        return HttpResponse('Some shit!')


@login_required
def wishlist_display(request):
    cars = []
    for obj in Wishlist.objects.filter(user=request.user):
        if obj.is_active:
            cars.append(obj.car)
            print(obj.car.full_name)
    return render(request, 'wishlist.html', {'cars': cars})


def about(request):
    return render(request, 'about.html')

