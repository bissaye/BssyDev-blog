from django.db import models
from ckeditor.fields import RichTextField


class Categorie (models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name

class Posts(models.Model):

    thumbnail = models.ImageField(null=True, blank=True, upload_to='img/thumbnail/', default='img/thumbnail/thumb.jpg')
    image = models.ImageField(null=True, blank=True, upload_to='img/post/', default='img/post/post.png')
    titre = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    body = RichTextField()
    date = models.DateField(auto_now_add=True)
    comments = models.IntegerField(blank=False, null=False, default=0)
    categorie = models.ManyToManyField(to=Categorie)

    def __str__(self):
        return self.titre

class Suscribers(models.Model):
    adresse = models.EmailField(null=False, blank=False)
    def __str__(self):
        return self.adresse

class Commentaires(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    adresse = models.EmailField(null=False, blank=False)
    commentaire = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        post = Posts.objects.filter(pk = self.post.id)
        if len(post)>0:
            post.update(comments = post[0].comments +1)
            super(Commentaires, self).save(*args, **kwargs)
    def __str__(self):
        return self.adresse


class Email(models.Model):

    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email