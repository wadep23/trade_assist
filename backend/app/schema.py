import graphene
from graphene_django.types import DjangoObjectType
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
        address_1 = graphene.String()
        address_2 = graphene.String()
        city = graphene.String()
        state = graphene.String()
        postal_code = graphene.String()
        country = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, username, email, password, **kwargs):
        if CustomUser.objects.filter(username=username).exists():
            raise Exception("Username already taken")
        if CustomUser.objects.filter(email=email).exists():
            raise Exception("An account with that email already exists")
        
        user = CustomUser(
            username=username,
            email=email,
            address_1=kwargs.get("address_1", ""),
            address_2=kwargs.get("address_2", ""),
            city=kwargs.get("city", ""),
            state=kwargs.get("state", ""),
            postal_code=kwargs.get("postal_code", ""),
            country=kwargs.get("country", ""),
        )
        user.set_password(password)
        user.save()
        return RegisterUser(user=user)
    
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

