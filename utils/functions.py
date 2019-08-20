# common functions 

# have username in uploaded image path
def upload_to(instance, filename):
    return "users/%s/%s" % (instance.user.username.lower(), filename)
