from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from letter.views import LetterViewSet, GetPubKeyView

router = SimpleRouter()
router.register('letters', LetterViewSet)

urlpatterns = [
    url(r'^boss-pubkey/$', GetPubKeyView.as_view())
] + router.urls
