from PIL import Image, ImageOps
from django.core.files.storage import default_storage as storage

# common functions 

# have username in uploaded image path
def upload_to(instance, filename):
    return "users/%s/%s" % (instance.user.username.lower(), filename)

# save function, resize image
def resize_image(context, model, image_field, size_px, *args, **kwargs):
    """
    Installed 'django-cleanup' to auto-remove old image.
    Installed 'pillow' to resize larger images.
    Arguments are: 
    - self
    - model the save is referencing
    - name of ImageField in model
    - size of desired resize in pixels (one value for equal size)
    - mandatory *args and **kwargs
    """
    super(model, context).save(*args, **kwargs)
    if image_field:
        img = Image.open(image_field)
        size = size_px
        thumb = (size, size)
        method = Image.ANTIALIAS
        center = (0.5, 0.5)
        extension = 'jpeg'
        # if greater than 300px on any side, then resize it to 300x300
        if img.height > size or img.width > size:
            img.thumbnail((size, size), method)
            new = ImageOps.fit(img, thumb, method, centering=center)
            temp = storage.open(image_field.name, "w")
            new.save(temp, extension)
            temp.close()
            super(model, context).save(*args, **kwargs)