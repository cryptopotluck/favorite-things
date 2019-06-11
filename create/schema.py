import graphene
from graphene_django import DjangoObjectType
from .models import Create
from django.db.models import Q


class CreateType(DjangoObjectType):
    class Meta:
        model = Create


class Query(graphene.ObjectType):
    favorites = graphene.List(CreateType, search=graphene.String())

    def resolve_tracks(self, info, search=None):
        if search:

            filter = (
                Q(title__icontains=search) |
                Q(body__icontains=search) |
                Q(author__exact=search)
            )
            Create.objects.filter(filter)
        return Create.objects.all()


class CreateFavorite(graphene.Mutation):
    favorite = graphene.Field(CreateType)

    class Arguments:
        title = graphene.String()
        body = graphene.String()
        pub_date = graphene.DateTime()
        category = graphene.String()
        rank = graphene.Int()
        metadata = graphene.String()
        modified_date = graphene.DateTime()

    def mutate(self, info, title, body, pub_date, category, rank, metadata, modified_date):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Login to Create Favorite')

        fav =Create(title=title, body=body, pub_date=pub_date, category=category, rank=rank,
               metadata=metadata, modified_date=modified_date, posted_by=user)
        fav.save()

        return CreateFavorite(fav=fav)


class UpdateFavorite(graphene.Mutation):
    favorite_U = graphene.Field(CreateType)

    class Arguments:
        favorite_id = graphene.Int(required=True)
        title = graphene.String()
        body = graphene.String()
        pub_date = graphene.DateTime()
        category = graphene.String()
        rank = graphene.Int()
        metadata = graphene.String()
        modified_date = graphene.DateTime()

    def mutate(self,  info, favotie_id, title, body, pub_date, category, rank, metadata, modified_date):

        user = info.context.user
        favorite = Create.objects.get(id=favotie_id)

        if favorite.posted_by != user:
            raise Exception("Not permitted to update other peoples Favorites.")

        Create.title = title
        Create.body = body
        Create.pub_date = pub_date
        Create.category = category
        Create.rank = rank
        Create.metadata = metadata
        Create.modified_date = modified_date

        favorite.save()

        return UpdateFavorite(favorite=favorite)


class DeleteFavorite(graphene.Mutation):
    favorite_id = graphene.Int()

    class Arguments:
        favorite_id = graphene.Int(required=True)

    def mutate(self, info, favorite_id):
        user = info.context.user
        favorite = Create.objects.get(id=favorite_id)

        if Create.author != user:
            raise Exception('You are not allowed to delete other peoples Favorites!')

        favorite.delete()

        return DeleteFavorite(favorite_id=favorite)


class Mutation(graphene.ObjectType):
    create_favorite = CreateFavorite.Field()
    update_favorite = UpdateFavorite.Field()
    delete_favorite = DeleteFavorite.Field()