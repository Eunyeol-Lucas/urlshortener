from ctypes.wintypes import SIZE
from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, 'MAXIMUN_URL_CHARS', 7)
AVAILABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAILABLE_CHARS):
    return ''.join([choice(chars) for _ in range(SIZE)])


def create_shortend_url(models_instance):
    random_code = create_random_code()

    models_class = models_instance.__class__
    if models_class.objects.filter(short_url=random_code).exists():
        return create_shortend_url(models_instance)
    
    return random_code