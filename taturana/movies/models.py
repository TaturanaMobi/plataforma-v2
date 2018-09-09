from datetime import datetime

from django.utils.timezone import make_aware
from djongo import models as djongo_models
from django.db import models

class MongoScreening(djongo_models.Model):
    _id = djongo_models.CharField(max_length=24, primary_key=True)
    date = djongo_models.DateTimeField()
    team_member = djongo_models.BooleanField()
    activity = djongo_models.CharField(max_length=250)
    activity_theme = djongo_models.TextField()
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
    draft = djongo_models.CharField(max_length=15)
    real_quorum = djongo_models.CharField(max_length=250)
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
    technical_information = djongo_models.TextField()
    site = djongo_models.CharField(max_length=250)
    facebook = djongo_models.CharField(max_length=250)
    twitter = djongo_models.CharField(max_length=250)
    instagram = djongo_models.CharField(max_length=250)
    youtube = djongo_models.CharField(max_length=250)
    createdAt = djongo_models.DateTimeField()
    slug = djongo_models.CharField(max_length=250)
    poster_thumb_path = djongo_models.CharField(max_length=250)
    press_kit_path = djongo_models.CharField(max_length=250)
    screening = djongo_models.ArrayModelField(
        model_container=MongoScreening
    )
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
    technical_information = models.TextField(null=True, blank=True)
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

        screenings_status = {'updated': 0, 'created': 0}
        for mongo_src in mongo_film.screening or []:
            try:
                scr = Screening.objects.get(_id=mongo_src._id)
                screenings_status['updated'] += 1
            except Screening.DoesNotExist:
                scr = Screening(_id=mongo_src._id, film=film)
                screenings_status['created'] += 1

            try:
                for field in Screening._meta.fields:
                    if field.name == 'film':
                        continue
                    value = getattr(mongo_src, field.name)
                    if isinstance(field, models.BooleanField):
                        value = value or False
                    if isinstance(value, datetime):
                        value = make_aware(value)
                    field.validate(value, scr)
                    setattr(scr, field.name, value)

                scr.full_clean()
            except Exception as exc:
                print("Error on screening {} movie {}: {} {}".format(mongo_src._id, film._id, field.name, exc))
                print(vars(exc))
            else:
                scr.save()
        print(screenings_status)

class Screening(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
    date = models.DateTimeField()
    team_member = models.BooleanField(default=True)
    activity = models.CharField(max_length=250, null=True, blank=True)
    activity_theme = models.TextField(null=True, blank=True)
    quorum_expectation = models.CharField(max_length=250, null=True, blank=True)
    comments = models.TextField(max_length=250, null=True, blank=True)
    accept_terms = models.BooleanField()
    place_name = models.CharField(max_length=250, null=True, blank=True)
    cep = models.CharField(max_length=250, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    number = models.CharField(max_length=250, null=True, blank=True)
    complement = models.CharField(max_length=250, null=True, blank=True)
    zone = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    public_event = models.BooleanField(default=True)
    uf = models.CharField(max_length=250, null=True, blank=True)
    s_country = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    user_id = models.CharField(max_length=250, null=True, blank=True)
    draft = models.CharField(max_length=15, null=True, blank=True)
    real_quorum = models.CharField(max_length=250, null=True, blank=True)
    report_description = models.TextField(null=True, blank=True)
    report_image_1 = models.CharField(max_length=250, null=True, blank=True)
    report_image_2 = models.CharField(max_length=250, null=True, blank=True)
    report_image_3 = models.CharField(max_length=250, null=True, blank=True)
    author_1 = models.CharField(max_length=250, null=True, blank=True)
    author_2 = models.CharField(max_length=250, null=True, blank=True)
    author_3 = models.CharField(max_length=250, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='screenings')
