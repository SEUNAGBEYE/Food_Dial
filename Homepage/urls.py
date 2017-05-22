from django.conf.urls import url
from Homepage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^about/', views.about, name = 'about'),
	url(r'^register/', views.registrationView, name = 'register'),
	url(r'^login/', views.loginView, name = 'login'),
	url(r'^product/', views.productView, name = 'product'),
	# url(r'^base/', views.baseView, name = 'base'),
	url(r'^cart/', views.addToCartView, name = 'cart'),
	# url(r'^cart/(?P<food_id>[0-9]+)/$', views.cartView, name = 'cart'),
	url(r'^checkout/', views.checkoutView, name = 'checkout'),
	# url(r'^new/', views.checkoutView, name = 'new'),
	url(r'^success/', views.successView, name = 'success'),


	# url(r'^menu/', views.menuView, name = 'menu'),


]	+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns = [
# 	url(r'^$', views.index, name = 'index'),
# 	url(r'^about/', views.about, name = 'about'),
# 	url(r'^register/', views.registrationView, name = 'register'),
# 	url(r'^login/', views.loginView, name = 'login'),
# 	url(r'^product/', views.productView, name = 'product'),

# 	url(r'^base/', views.baseView, name = 'base'),

# 	url(r'^order/add_to_cart/id=(?P<food_id>[0-9]+)/$', views.addToCart, name = 'add-to-cart'),

# 	url(r'^checkout/', views.checkoutView, name = 'checkout'),
# 	url(r'^new/', views.checkoutView, name = 'new'),
# 	url(r'^success/', views.successView, name = 'success'),

# 	# url(r'^menu/', views.menuView, name = 'menu'),


# ]