from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from ..helpers import jwt_decode_handler

class JWTMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/login") or request.path.startswith("/admin"):
            return

        jwt = request.META.get("HTTP_AUTHORIZATION", None)
        if not jwt:
            return HttpResponseForbidden()
        
        try:
            user = jwt_decode_handler(jwt)
            if not user:
                return HttpResponseForbidden()
        except Exception:
            return HttpResponseForbidden()
