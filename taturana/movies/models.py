from djongo import models as djongo_models
from django.db import models

class MongoScreening(djongo_models.Model):
    _id = djongo_models.CharField(max_length=24, primary_key=True)
    date = djongo_models.DateTimeField()
    team_member = djongo_models.BooleanField()
    activity = djongo_models.CharField(max_length=250)
    activity_theme = djongo_models.CharField(max_length=250)
    quorum_expectation = djongo_models.CharField(max_length=250)
    comments = djongo_models.CharField(max_length=250)
    accept_terms = djongo_models.BooleanField()
    place_name = djongo_models.CharField(max_length=250)
    cep = djongo_models.CharField(max_length=250)
    street = djongo_models.CharField(max_length=250)
    number = djongo_models.CharField(max_length=250)
    complement = djongo_models.CharField(max_length=250)
    zone = djongo_models.CharField(max_length=250)
    city = djongo_models.CharField(max_length=250)
    public_event = djongo_models.BooleanField()
    uf = djongo_models.CharField(max_length=250)
    s_country = djongo_models.CharField(max_length=250)
    created_at = djongo_models.DateTimeField()
    user_id = djongo_models.CharField(max_length=250)
    draft = djongo_models.CharField(max_length=5)
    real_quorum = djongo_models.CharField(max_length=10)
    report_description = djongo_models.TextField()
    report_image_1 = djongo_models.CharField(max_length=250)
    report_image_2 = djongo_models.CharField(max_length=250)
    report_image_3 = djongo_models.CharField(max_length=250)
    author_1 = djongo_models.CharField(max_length=250)
    author_2 = djongo_models.CharField(max_length=250)
    author_3 = djongo_models.CharField(max_length=250)
    updated_at = djongo_models.DateTimeField()

    class Meta:
       abstract = True


class MongoFilm(djongo_models.Model):
    _id = djongo_models.CharField(max_length=24, primary_key=True)
    poster_path = djongo_models.CharField(max_length=250)
    poster_home_path = djongo_models.CharField(max_length=250)
    link_for_download = djongo_models.CharField(max_length=250)
    password_for_download = djongo_models.CharField(max_length=250)
    sequence_number = djongo_models.CharField(max_length=250)
    status = djongo_models.CharField(max_length=250)
    title = djongo_models.CharField(max_length=250)
    synopsis = djongo_models.CharField(max_length=250)
    trailer_url = djongo_models.CharField(max_length=250)
    genre = djongo_models.CharField(max_length=250)
    year = djongo_models.CharField(max_length=250)
    length = djongo_models.CharField(max_length=250)
    country = djongo_models.CharField(max_length=250)
    age_rating = djongo_models.CharField(max_length=250)
    production_company = djongo_models.CharField(max_length=250)
    director = djongo_models.CharField(max_length=250)
    technical_information = djongo_models.CharField(max_length=250)
    site = djongo_models.CharField(max_length=250)
    facebook = djongo_models.CharField(max_length=250)
    twitter = djongo_models.CharField(max_length=250)
    instagram = djongo_models.CharField(max_length=250)
    youtube = djongo_models.CharField(max_length=250)
    createdAt = djongo_models.DateTimeField()
    slug = djongo_models.CharField(max_length=250)
    poster_thumb_path = djongo_models.CharField(max_length=250)
    press_kit_path = djongo_models.CharField(max_length=250)
    # screening = djongo_models.ArrayModelField(
    #     model_container=MongoScreening
    # )
    class Meta:
        managed = False
        db_table = 'films'


class Film(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
    poster_path = models.CharField(max_length=250, null=True, blank=True)
    poster_home_path = models.CharField(max_length=250, null=True, blank=True)
    link_for_download = models.CharField(max_length=250, null=True, blank=True)
    password_for_download = models.CharField(max_length=250, null=True, blank=True)
    sequence_number = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    trailer_url = models.CharField(max_length=250, null=True, blank=True)
    genre = models.CharField(max_length=250, null=True, blank=True)
    year = models.CharField(max_length=250, null=True, blank=True)
    length = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    age_rating = models.CharField(max_length=250, null=True, blank=True)
    production_company = models.CharField(max_length=250, null=True, blank=True)
    director = models.CharField(max_length=250, null=True, blank=True)
    technical_information = models.CharField(max_length=250, null=True, blank=True)
    site = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    twitter = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    youtube = models.CharField(max_length=250, null=True, blank=True)
    createdAt = models.DateTimeField()
    slug = models.CharField(max_length=250, null=True, blank=True)
    poster_thumb_path = models.CharField(max_length=250, null=True, blank=True)
    press_kit_path = models.CharField(max_length=250, null=True, blank=True)

    @classmethod
    def sync_from_mongo(cls, hash):
        mongo_film = MongoFilm.objects.get(_id=hash)
        try:
            film = Film.objects.get(_id=hash)
            update = True
        except Film.DoesNotExist:
            film = Film(_id=hash)
            update = False

        for field in Film._meta.fields:
            value = getattr(mongo_film, field.name)
            setattr(film, field.name, value)
            field.validate(value, film)
        film.full_clean()
        film.save()
        if update:
            print("Film {._id} updated.".format(film))
        else:
            print("Film {._id} created.".format(film))



class Screening(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
    date = models.DateTimeField()
    team_member = models.BooleanField()
    activity = models.CharField(max_length=250)
    activity_theme = models.CharField(max_length=250)
    quorum_expectation = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)
    accept_terms = models.BooleanField()
    place_name = models.CharField(max_length=250)
    cep = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    complement = models.CharField(max_length=250)
    zone = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    public_event = models.BooleanField()
    uf = models.CharField(max_length=250)
    s_country = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    user_id = models.CharField(max_length=250)
    draft = models.CharField(max_length=5)
    real_quorum = models.CharField(max_length=10)
    report_description = models.TextField()
    report_image_1 = models.CharField(max_length=250)
    report_image_2 = models.CharField(max_length=250)
    report_image_3 = models.CharField(max_length=250)
    author_1 = models.CharField(max_length=250)
    author_2 = models.CharField(max_length=250)
    author_3 = models.CharField(max_length=250)
    updated_at = models.DateTimeField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='screenings')
