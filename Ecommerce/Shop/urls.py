from django.urls import path
from Shop import views
from django.conf import settings
from django.conf.urls.static import static
from info.forms import loginForms, PasswordChangeForm, myPasswordresetForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Productview.as_view(), name= 'home'),
    path('product-detail/<int:pk>', views.productdetail.as_view(), name='product-detail'),
    path('add-to-card/', views.add_to_cart, name='add-to-card'),

    path('cart/', views.show_cards, name='show_cards'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.Customerprofileview.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name= 'Shop/passwordchange.html', form_class = PasswordChangeForm, success_url = '/changedone/'),name= 'changepassword'),
    
    path('changedone/', auth_views.PasswordChangeView.as_view(template_name = 'Shop/changedone.html') ),
    
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'Shop/password_reset.html', form_class= myPasswordresetForm), name= 'password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'Shop/password_reset_done.html'), name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Shop/password_reset_confirm.html'),name='password_reset_confirm'),
    
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'Shop/password_reset_complete.html'), name='password_reset_complete'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Shop/login.html', authentication_form=loginForms), name= 'login'),
    

    path('lehenga/', views.lehenga, name='lehenga'),
    path('lehenga/<slug:data>', views.lehenga, name= 'lehengaitems'),
    
    path('saree/', views.Saree, name='saree'),
    path('saree/<slug:data>', views.Saree, name= 'Sareeitems'),
    
    path('borkha/', views.Borkha, name='borkha'),
    path('borkha/<slug:data>', views.Borkha, name= 'Borkhaitems'),
    
    path('gents_Pant/', views.Gents_Pants, name='gents_Pant'),
    path('gents_Pant/<slug:data>', views.Gents_Pants, name= 'gents_Pantitems'),
    
    path('baby_fashion/', views.Baby_Fashion, name='baby_fashion'),
    path('baby_fashion/<slug:data>', views.Baby_Fashion, name= 'baby_fashionitems'),
    
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    
    path('registration/', views.registrationforms.as_view(), name='registration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name= 'logout'),
    
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_dine, name='paymentdone'),
    path("search/",views.search, name="search")
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)