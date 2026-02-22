from django.conf import settings


def remvoe_old_photos(photos):
    if photos and photos.name != 'user/photos/default.png':
        old_path = settings.MEDIA_ROOT / photos.name