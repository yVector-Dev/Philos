from django.conf import settings


def site(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_URL": settings.SITE_URL,
        "PLAUSIBLE_DOMAIN": settings.PLAUSIBLE_DOMAIN,
        "GA_MEASUREMENT_ID": settings.GA_MEASUREMENT_ID,
        "canonical_url": settings.SITE_URL + request.path,
    }
