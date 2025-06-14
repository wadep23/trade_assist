import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.shortcuts import get_token
from graphql_jwt.settings import jwt_settings
from django.contrib.auth import get_user_model
import graphql_jwt
from .models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        exclude = ["password", "is_superuser", "is_staff"]


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required")
        return user


class RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)
    token = graphene.String()

    def mutate(self, info, username, email, password):
        if CustomUser.objects.filter(username=username).exists():
            raise Exception("Username already taken")
        if CustomUser.objects.filter(email=email).exists():
            raise Exception("An account with that email already exists")

        user = CustomUser(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        token = get_token(user)

        request = info.context
        response = request._request

        response.set_cookie(
            key=jwt_settings.JWT_COOKIE_NAME or "accessToken",
            value=token,
            httponly=True,
            samesite="Lax",
            secure=False,
        )

        return RegisterUser(user=user, token=token)


class UpdateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        address_1 = graphene.String()
        address_2 = graphene.String()
        city = graphene.String()
        state = graphene.String()
        postal_code = graphene.String()
        country = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required")

        for key, value in kwargs.items():
            setattr(user, key, value)

        user.save()
        return UpdateUser(user=user)


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    update_user = UpdateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
