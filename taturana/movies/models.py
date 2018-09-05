from djongo import models as djongo_models


class Screening(djongo_models.Model):
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


class Film(djongo_models.Model):
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
    screening = djongo_models.ArrayModelField(
        model_container=Screening
    )
    class Meta:
       managed = False
       db_table = 'films'
