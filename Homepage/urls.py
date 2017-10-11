from django.conf.urls import url
from Homepage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^video_call/$', views.start_video_call, name = 'video_call'),
	url(r'^register/', views.registrationView, name = 'register'),
	url(r'^login/', views.loginView, name = 'login'),
	url(r'^logout/', views.logoutView, name = 'logout'),
	url(r'^order/(?P<food_id>[0-9]+)/$', views.orderView, name='order'),

]	+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

