from django.shortcuts import render, redirect
from django.views import View
from info.models import Product, Customer, Card, OrderPlaced
from info.forms import RegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
# def home(request):
#      return render(request, 'Shop/home.html')


# Productview
class Productview(View):
     def get(self, request):
          total_item = 0
          gentpants = Product.objects.filter(category = 'GP')
          borkas = Product.objects.filter(category = 'BK')
          babyfashions = Product.objects.filter(category = 'BF')
          if request.user.is_authenticated:
              total_item =len(Card.objects.filter(user=request.user))
          return render(request, 'Shop/home.html', {'gentpants':gentpants, 'borkas': borkas, 'babyfashions':babyfashions, 'total_item' :total_item})
     
     

# def product_detail(request):
#  return render(request, 'Shop/productdetail.html')


# productdetail
class productdetail(View):
     def get(self, request, pk ):
          total_item= 0
          product = Product.objects.get(pk=pk)
          item_already_in_card = False
          if request.user.is_authenticated:
              item_already_in_card = Card.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
          product.brand = product.brand.replace('_', ' ')
          if request.user.is_authenticated:
              total_item =len(Card.objects.filter(user=request.user))
          return render(request, 'Shop/productdetail.html',{'product':product, 'item_already_in_card':item_already_in_card, 'total_item':total_item})
          

      
#  add_to_cart
@login_required               
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Card(user=user, product=product).save()
 return redirect('/cart')


# buy_now
def buy_now(request):
 total_item =0
 if request.user.is_authenticated:
     total_item =len(Card.objects.filter(user=request.user))
     
     data = {
         'total_item':total_item
     }
 return render(request, 'Shop/buynow.html', data)


# Customerprofileview
@method_decorator(login_required, name='dispatch')
class Customerprofileview(View):
     def get(self,request):
          form = CustomerProfileForm()
          return render(request, 'Shop/profile.html',{'form':form, 'active':'btn-outline-primary', 'actives':'btn-outline-danger'})

     def post(self, requset):

          form = CustomerProfileForm(requset.POST)
          if form.is_valid():
               use = requset.user
               name = form.cleaned_data['name']
               division = form.cleaned_data['division'] 
               district = form.cleaned_data['district']
               thana = form.cleaned_data['thana'] 
               villprroad = form.cleaned_data['villprroad'] 
               zipcode = form.cleaned_data['zipcode'] 
               register = Customer(user=use, name=name, division=division, district=district, thana=thana, villprroad=villprroad, zipcode=zipcode)
               register.save()
               messages.success(requset, "Congratulation Registration Successfully")

          return render(requset, 'Shop/profile.html',{'form':form, 'active':'btn-outline-primary', })


# address
@login_required
def address(request):
  addres = Customer.objects.filter(user=request.user)
  total_item=0
  if request.user.is_authenticated:
     total_item =len(Card.objects.filter(user=request.user))
  return render(request, 'Shop/address.html',{'addres':addres,'active':'btn-outline-danger', 'total_item':total_item})



# change_password
def change_password(request):
 return render(request, 'Shop/changepassword.html')


# lehenga
def lehenga(request, data = None):
     total_item=0
     if request.user.is_authenticated:
       total_item =len(Card.objects.filter(user=request.user))
     if data == None:
          lehenga = Product.objects.filter(category='L')
     elif data == 'Kalkis'  or data == 'Kalki':
          lehenga = Product.objects.filter(category='L').filter(brand=data)
     elif data == 'below':
          lehenga = Product.objects.filter(category='L').filter(discounted_price__lte=20000)
     elif data == 'above':
          lehenga = Product.objects.filter(category='L').filter(discounted_price__gte=20000)     
     return render(request, 'Shop/lehenga.html', {'lehenga': lehenga, 'total_item':total_item})


# Saree
def Saree(request, data = None):
     total_item=0
     if request.user.is_authenticated:
          total_item =len(Card.objects.filter(user=request.user))
     if data == None:
          saree = Product.objects.filter(category='S')
     elif data == 'jamdani'  or data == 'muslim':
          saree = Product.objects.filter(category='S').filter(brand=data)
     elif data == 'below':
          saree = Product.objects.filter(category='S').filter(discounted_price__lte=2500)
     elif data == 'above':
          saree = Product.objects.filter(category='S').filter(discounted_price__gte=2500)      
     return render(request, 'Shop/sarees.html', {'saree': saree, 'total_item':total_item})


# Borkha
def Borkha(request, data = None):
     total_item=0
     if request.user.is_authenticated:
          total_item =len(Card.objects.filter(user=request.user))
     if data == None:
          borkha = Product.objects.filter(category='BK')
     elif data == 'Short_Abaya'  or data == ('The_Hijab_Lady'):
          borkha = Product.objects.filter(category='BK').filter(brand=data)
     elif data == 'below':
          borkha = Product.objects.filter(category='BK').filter(discounted_price__lte=2500)
     elif data == 'above':
          borkha = Product.objects.filter(category='BK').filter(discounted_price__gte=2500)      
     return render(request, 'Shop/borkhas.html', {'borkha':borkha, 'total_item':total_item})


# Gents_Pants
def Gents_Pants(request, data = None):
     total_item=0
     if request.user.is_authenticated:
          total_item =len(Card.objects.filter(user=request.user))
     if data == None:
          gents_Pant = Product.objects.filter(category='GP')
     elif data == 'Armani'  or data == 'Denim':
          gents_Pant = Product.objects.filter(category='GP').filter(brand=data)
     elif data == 'below':
          gents_Pant = Product.objects.filter(category='GP').filter(discounted_price__lte=2500)
     elif data == 'above':
          gents_Pant = Product.objects.filter(category='GP').filter(discounted_price__gte=2500)     
     return render(request, 'Shop/gents_Pant.html', {'gents_Pant': gents_Pant, 'total_item':total_item})

# Baby_Fashion

def Baby_Fashion(request, data = None):
     total_item=0
     if request.user.is_authenticated:
      total_item =len(Card.objects.filter(user=request.user))
     if data == None:
          baby_fashion = Product.objects.filter(category='BF')
     elif data == 'Easy'  or data == 'Vocabulary':
          baby_fashion = Product.objects.filter(category='BF').filter(brand=data)
     elif data == 'below':
          baby_fashion = Product.objects.filter(category='BF').filter(discounted_price__lte=2500)
     elif data == 'above':
          baby_fashion = Product.objects.filter(category='BF').filter(discounted_price__gte=2500)     
     return render(request, 'Shop/baby_fashion.html', {'baby_fashion': baby_fashion, 'total_item':total_item})

# def login(request):
#      return render(request, 'Shop/login.html')


# registrationforms

class registrationforms(View):
     def get(self, request):
          info = RegistrationForm()
          return render(request, 'Shop/registration.html', {'form':info})



     def post(self, request):
          info = RegistrationForm(request.POST)
          if info.is_valid():
               messages.success(request, "Congratulation Registration Successfully")
               info.save()
              
          return render(request, 'Shop/registration.html', {'form':info}) 
        


#  checkout    
@login_required           
def checkout(request):
 total_item=0
 if request.user.is_authenticated:
     total_item =len(Card.objects.filter(user=request.user))
 user = request.user
 add = Customer.objects.filter(user=user)
 card_member = Card.objects.filter(user=user)
 amount = 0.0
 shoppimg_amount = 100.0
 total_amount = 0.0
 card_amount = [p for p in Card.objects.all() if p.user == user]
 if  card_amount:
     for p in card_amount:
          temproraryamount = (p.quntity * p.product.discounted_price)
          amount += temproraryamount
          total_cost = amount + shoppimg_amount

          data = {
              'add':add,
              'card_member':card_member,
              'total_cost':total_cost,
              'total_item':total_item
          }

 return render(request, 'Shop/checkout.html', data)


# payment_dine
def payment_dine(request):
    user = request.user
    customerid = request.GET.get('customerid')
    customer = Customer.objects.get(id=customerid)
    carts = Card.objects.filter(user=user)
    for c in carts:
        OrderPlaced(user= user, customer=customer, product=c.product, quantity=c.quntity).save()
        c.delete()

    return redirect('orders')    



# orders
@login_required
def orders(request):
 total_item=0
 if request.user.is_authenticated:
     total_item =len(Card.objects.filter(user=request.user))
 order_place = OrderPlaced.objects.filter(user = request.user)
 return render(request, 'Shop/orders.html', {'order_place':order_place, 'total_item':total_item})




# show Card 
@login_required
def show_cards(request):
     total_item=0
     if request.user.is_authenticated:
          total_item =len(Card.objects.filter(user=request.user))
     if request.user.is_authenticated:
        user = request.user
        card = Card.objects.filter(user=user)
        amount = 0.0
        shoppimg_amount = 100.0
        total_amount = 0.0
        card_amount = [p for p in Card.objects.all() if p.user == user]
        if  card_amount:
             for p in card_amount:
                temproraryamount = (p.quntity * p.product.discounted_price)
                amount += temproraryamount
                total_cost = amount + shoppimg_amount
             return render(request, 'Shop/addtocart.html',{'card':card, 'amount':amount, 'total_cost':total_cost,'total_item':total_item})
        else:
          return render(request, 'Shop/emtycart.html')
        



#Plus cart
def plus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Card.objects.get(Q(product=prod_id) & Q(user=request.user))

    c.quntity += 1
    c.save()
    amount = 0.0
    shipping_amount = 100.0
    cart_product = [p for p in Card.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quntity * p.product.discounted_price)
      amount += tempamount
      total_cost = amount + shipping_amount

    data={
      'quntity': c.quntity,
      'amount': amount,
      'total_cost':total_cost
     }
    return JsonResponse(data)
  


  #minus cart
def minus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Card.objects.get(Q(product=prod_id) & Q(user=request.user))

    c.quntity -= 1
    c.save()
    amount = 0.0
    shipping_amount = 100.0
    cart_product = [p for p in Card.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quntity * p.product.discounted_price)
      amount += tempamount
      total_cost = amount + shipping_amount

    data={
      'quntity': c.quntity,
      'amount': amount,
      'total_cost':total_cost
    }
    return JsonResponse(data)
  




  #remove cart
def remove_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Card.objects.get(Q(product=prod_id) & Q(user=request.user))

    c.delete()
    amount = 0.0
    shipping_amount = 100.0
    cart_product = [p for p in Card.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quntity * p.product.discounted_price)
      amount += tempamount
      total_cost = amount + shipping_amount

    data={
      'amount': amount,
      'total_cost':total_cost
    }
    return JsonResponse(data)




#  search 
def search(requset):
     total_item=0
     if requset.user.is_authenticated:
        total_item =len(Card.objects.filter(user=requset.user))
     if requset.method == 'GET':
        quary = requset.GET.get('quary')
        if quary:
          product = Product.objects.filter(title__icontains=quary)
          data = {
              'product':product,
              'total_item':total_item
          }
          return render(requset, 'Shop/search.html', data)
     else:
        return render(requset, 'Shop/search.html', data)       
   