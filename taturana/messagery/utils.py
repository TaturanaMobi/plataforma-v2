from django.template import Context, engines


def get_movie_context(film, screening) -> Context:
    """

    :param film: Film instance
    :type film: movies.models.Film
    :param screening: Screening instance
    :type screening: movies.models.Screening
    :rtype: django.template.Context
    :return: context instance
    """
    return {
        "film": film,
        "screening": screening
    }


def render_movie_email(email, film, screening) -> (str, str, str):
    """
    Render any email instance

    :param email: Email instance
    :type email: messagery.models.Email
    :param film: Film instance
    :type film: movies.models.Film
    :param screening: Screening instance
    :type screening: movies.models.Screening
    :return: (str, str, str)
    """
    engine = engines['django']
    context = get_movie_context(film, screening)
    subject_tpl = engine.from_string(email.get_subject_for_film(film))
    html_tpl = engine.from_string(email.get_html_for_film(film))
    text_tpl = engine.from_string(email.get_text_for_film(film))

    subject_rendered = subject_tpl.render(context)
    html_rendered = html_tpl.render(context)
    text_rendered = text_tpl.render(context)

    return subject_rendered, html_rendered, text_rendered
