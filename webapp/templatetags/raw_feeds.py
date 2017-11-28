from django import template
import logging
import json
from requests_cache import CachedSession
from django.conf import settings


logger = logging.getLogger(__name__)
requests_timeout = getattr(settings, 'FEED_TIMEOUT', 10)
expiry_seconds = getattr(settings, 'FEED_EXPIRY', 300)

cached_request = CachedSession(
    expire_after=expiry_seconds,
)

register = template.Library()


@register.simple_tag
def get_raw_json_feed(url):
    """
    Get the entries in a JSON feed
    """

    try:
        response = cached_request.get(url, timeout=requests_timeout)
        response.raise_for_status()
    except Exception as request_error:
        logger.warning(
            'Attempt to get feed failed: {}'.format(str(request_error))
        )
        return False

    try:
        content = json.loads(response.text)
    except Exception as parse_error:
        logger.warning(
            'Failed to parse feed from {}: {}'.format(url, str(parse_error))
        )
        return False

    return content
