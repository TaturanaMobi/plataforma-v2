from functools import lru_cache
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Email(TimeStampedModel):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    html = models.TextField()
    text = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @lru_cache(maxsize=4)
    def get_email_template_for_film(self, film):
        """
        Given a film instance return it's EmailTemplate

        :param film: Film instance
        :type film: movies.models.Film
        :rtype: EmailTemplate
        :return: EmailTemplate
        """
        try:
            tpl = EmailTemplate.objects.get(email=self, film=film, active=True)
        except EmailTemplate.DoesNotExist:
            tpl = None

        return tpl

    def _get_field_from_tpl_or_email_for_film(self, film, field_name) -> str:
        """
        Get field value from EmailTemplate if it exists, and if not from Email

        :param film: Film instance
        :type film: movies.models.Film
        :param field_name: name of field to retrieve
        :type field_name: str
        :return: str
        :raise: ValueError
        """
        if field_name not in ['subject', 'html', 'text']:
            raise ValueError("field_name must be one of 'subject', 'html' or 'text'.")

        tpl = self.get_email_template_for_film(film)

        try:
            return getattr(tpl, field_name) or getattr(self, field_name)
        except AttributeError:
            return getattr(self, field_name)

    def get_subject_for_film(self, film):
        return self._get_field_from_tpl_or_email_for_film(film, 'subject')

    def get_html_for_film(self, film):
        return self._get_field_from_tpl_or_email_for_film(film, 'html')

    def get_text_for_film(self, film):
        return self._get_field_from_tpl_or_email_for_film(film, 'text')


class EmailTemplate(TimeStampedModel):
    # movie_id is the object_id in mongo
    film = models.ForeignKey('movies.Film', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    html = models.TextField(blank=True)
    text = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    email = models.ForeignKey(
        Email, on_delete=models.CASCADE,
        related_name='templates'
    )

    def __str__(self):
        return "{} - {}".format(self.email, self.film)
