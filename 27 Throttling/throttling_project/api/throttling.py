from rest_framework.throttling import ScopedRateThrottle
from rest_framework.throttling import UserRateThrottle
from rest_framework.throttling import BaseThrottle
from rest_framework.exceptions import Throttled

class ScopeBasedThrottle(ScopedRateThrottle):
    scope_attr = 'throttle_scope'


# api/throttling.py

class RegularUserRateThrottle(UserRateThrottle):
    scope = 'regular_user'

class PremiumUserRateThrottle(UserRateThrottle):
    scope = 'premium_user'


class GroupBasedThrottle(BaseThrottle):
    def allow_request(self, request, view):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='Premium Users').exists():
                throttle_class = PremiumUserRateThrottle()
            else:
                throttle_class = RegularUserRateThrottle()
            return throttle_class.allow_request(request, view)
        return True  # Non-authenticated users are not throttled by this custom throttle

    def wait(self):
        return None
