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
        request._jwt_token = token

        return RegisterUser(user=user, token=token)


class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=False)
        email = graphene.String(required=False)
        password = graphene.String(required=True)

    token = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, password, username=None, email=None):
        if not username and not email:
            raise Exception("You must provide either a username or an email.")

        from django.contrib.auth import authenticate

        if email and not username:
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
                username = user.username
            except User.DoesNotExist:
                raise Exception("No user found with this email.")

        user = authenticate(username=username, password=password)

        if user is None:
            raise Exception("Invalid credentials")

        token = get_token(user)
        info.context._jwt_token = token

        return Login(success=True, token=token)


class RefreshToken(graphql_jwt.Refresh):
    @classmethod
    def resolve(cls, root, info, **kwargs):
        result = super().resolve(root, info, **kwargs)

        info.context._jwt_token = result.token

        return result


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


class Logout(graphene.Mutation):
    success = graphene.Boolean()

    def mutate(self, info):
        info.context._jwt_token = ""
        return Logout(success=True)


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    update_user = UpdateUser.Field()
    token_auth = Login.Field(name="tokenAuth")
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = RefreshToken.Field()
    logout = Logout.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
