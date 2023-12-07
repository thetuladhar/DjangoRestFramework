from django.db import models



class SocialMediaHandleModel(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class AuthorModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    hashtags=models.ManyToManyField(SocialMediaHandleModel,null=True)

    def __str__(self):
        return self.name

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')
    SocialMediaHandles = models.ForeignKey(SocialMediaHandleModel, on_delete=models.CASCADE, related_name='handles',null=True)
    publication_date = models.DateField()
    def __str__(self):
        return self.title