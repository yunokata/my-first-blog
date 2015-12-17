from django.db import models
from django.utils import timezone
#from pyuploadcare.dj import ImageField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(upload_to="images/art/")



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def generate_path(instance, filename):
        ext = filename.rsplit('.', 1)[-1]
        h = md5(instance.user.username.encode()).hexdigest()
        result = 'photos/%s/%s/%s.%s' % (h[:2], h[2:4], h[4:], ext)
        path = os.path.join(settings.MEDIA_ROOT, result)
        if os.path.exists(path):
            os.remove(path)
        return result
