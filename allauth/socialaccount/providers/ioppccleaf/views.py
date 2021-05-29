import requests
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)
from allauth.socialaccount.providers.oauth2.client import OAuth2Error

from .provider import IoppccLeafProvider


class IoppccLeafOAuth2Adapter(OAuth2Adapter):
    provider_id = IoppccLeafProvider.id

    base_url = 'http://192.168.1.51:3000/'
    access_token_url = base_url + 'oauth/token'
    authorize_url = base_url + 'oauth/authorize'
    identity_url = base_url + 'api/user'

    supports_state = True

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.identity_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)

    # def get_data(self, token):
    #     # Verify the user first
    #     resp = requests.get(
    #         self.identity_url,
    #         params={'token': token}
    #     )
    #     resp = resp.json()
    #
    #     if not resp.get('ok'):
    #         raise OAuth2Error()
    #
    #     # Fill in their generic info
    #     info = {
    #         'user': resp.get('user'),
    #         'team': resp.get('team')
    #     }
    #
    #     return info


oauth2_login = OAuth2LoginView.adapter_view(IoppccLeafOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(IoppccLeafOAuth2Adapter)
