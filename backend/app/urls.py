from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .views import hello_world

urlpatterns = [
    path('hello/', hello_world),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]