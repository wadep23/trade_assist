from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

# from .views import hello_world, login_view, logout_view
from .schema import schema

COOKIE_NAME = "accessToken"
COOKIE_MAX_AGE = 60 * 60 * 24 * 7


class CustomGraphQLView(GraphQLView):
    def parse_body(self, request):
        token = request.COOKIES.get(COOKIE_NAME)
        if token:
            request.META["HTTP_AUTHORIZATION"] = f"JWT {token}"
        return super().parse_body(request)

    def execute_graphql_request(self, request, *args, **kwargs):
        self._jwt_token = None  # default
        result = super().execute_graphql_request(request, *args, **kwargs)
        self._jwt_token = getattr(request, "_jwt_token", None)
        return result

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if hasattr(self, "_jwt_token"):
            if self._jwt_token:
                response.set_cookie(
                    key=COOKIE_NAME,
                    value=self._jwt_token,
                    httponly=True,
                    samesite="Strict",
                    secure=True,
                    max_age=COOKIE_MAX_AGE,
                )
            else:
                response.delete_cookie(COOKIE_NAME)
        return response


urlpatterns = [
    path(
        "graphql/", csrf_exempt(CustomGraphQLView.as_view(schema=schema, graphiql=True))
    ),
    # path("login/", csrf_exempt(login_view)),
    # path("logout/", csrf_exempt(logout_view)),
    # path("hello/", csrf_exempt(hello_world)),
]
