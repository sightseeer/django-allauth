from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import WzlappLocalProvider

urlpatterns = default_urlpatterns(IoppccLeafProvider)
