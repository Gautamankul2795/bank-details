from django.urls import path, include

from .views import ListBanksView, BanksView2, BanksViewSet

urlpatterns = [
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^branch/', include('ticketapi.urls')),
	re_path(r'^ifsc/', include('ticketapi.urls')),
]



