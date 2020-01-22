from PIL import Image, ImageOps
from django.core.files.storage import default_storage as storage
from io import BytesIO

# common functions 

# have username in uploaded image path
def upload_to(instance, filename):
    return "users/%s/%s" % (instance.user.username.lower(), filename)
