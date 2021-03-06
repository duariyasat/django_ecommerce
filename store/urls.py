from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),
	path('store1/', views.store1, name="store1"),
	path('logout/', views.logout, name="logout"),
	path('propage/', views.propage, name="propage"),
	path('profile/', views.profile, name="profile"),

]