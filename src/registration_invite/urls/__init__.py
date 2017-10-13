"""
Default URL conf for the ng-utils invite registration backend.
This URL conf simply includes the URLs for both invitation and activation functionality.
If the default behavior of these views is acceptable to you, simply use a line like this
in your root URLconf to set up the default URLs for registration::
    url(r'^', include('registration_invite.urls')),
If you'd like to customize registration behavior, feel free to set up
your own URL patterns for these views instead.
"""

from . import activation, invitation


urlpatterns = activation.urlpatterns + invitation.urlpatterns
