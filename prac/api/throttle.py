from rest_framework.throttling import UserRateThrottle

class MustafaThrottle(UserRateThrottle):
    scope = "musu"