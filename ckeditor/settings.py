from django.conf import settings


"""
Allows you to enable (or not) the user to browse the
images he has uploaded to the server. If it's set to False, no thumbs are created
for the images.
When setting this variable to False you have to remove the `browse` button
from all the ckeditor dialogs where it appears through the config.js file.
"""
CKEDITOR_BROWSEABLE_UPLOADED_IMAGES = getattr(
    settings, 'CKEDITOR_BROWSEABLE_UPLOADED_IMAGES', False)

CKEDITOR_IMAGE_MAX_WIDTH = getattr(settings, 'CKEDITOR_IMAGE_MAX_WIDTH', None)

CKEDITOR_IMAGE_MAX_HEIGHT = getattr(settings, 'CKEDITOR_IMAGE_MAX_HEIGHT', None)

"""
When setting CKEDITOR_IMAGE_MAX_WIDTH or CKEDITOR_IMAGE_MAX_HEIGHT,
you have to provide a callable function that does the resizing you need.
This function takes as a parameter the absolute path to the image and
modifies its dimensions as you need.
It must be a procedure (not a function) so no return value will be used.
"""
CKEDITOR_IMAGE_AUTORESIZE_FUNCTION = getattr(settings, 'CKEDITOR_IMAGE_AUTORESIZE_FUNCTION', None)
