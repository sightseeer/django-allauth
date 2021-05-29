from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import WzlappProvider

urlpatterns = default_urlpatterns(WzlappProvider)
