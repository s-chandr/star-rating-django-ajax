
from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name='home'),
    path('accounts/signup',views.signup,name='signup'),
    path('book/<int:id>', views.product_detail,name='product_detail'),
    path('save-review/<int:pid>', views.save_review,name='save-review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)