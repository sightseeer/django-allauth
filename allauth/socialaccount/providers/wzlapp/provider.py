from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class WzlappAccount(ProviderAccount):
    def get_avatar_url(self):
        return self.account.extra_data.get('user').get('image_192', None)

    def to_str(self):
        dflt = super(WzlappAccount, self).to_str()
        return '%s (%s)' % (
            self.account.extra_data.get('name', ''),
            dflt,
        )


class WzlappProvider(OAuth2Provider):
    id = 'wzlapp'
    name = 'wzlapp'
    account_class = WzlappAccount

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(username=data['email'],
                    email=data['email'],
                    first_name=data['firstname'],
                    last_name=data['lastname'])

    def get_default_scope(self):
        return ['read']


providers.registry.register(WzlappProvider)
