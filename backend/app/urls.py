from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .views import hello_world, login_view, logout_view
from .schema import schema

COOKIE_NAME = 'accessToken'

class CustomGraphQLView(GraphQLView):
    def parse_body(self, request):
        token = request.COOKIES.get(COOKIE_NAME)
        if token:
            request.META['HTTP_AUTHORIZATION'] = f'JWT {token}'
        return super().parse_body(request)

urlpatterns = [
    path("graphql/", csrf_exempt(CustomGraphQLView.as_view(schema=schema, graphiql=True))),
    path("login/", csrf_exempt(login_view)),
    path("logout/", csrf_exempt(logout_view)),
    path('hello/', csrf_exempt(hello_world)),
]