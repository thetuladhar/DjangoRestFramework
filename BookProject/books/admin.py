from django.contrib import admin
from .models import BookModel,AuthorModel,SocialMediaHandleModel

admin.site.register(BookModel)
admin.site.register(AuthorModel)
admin.site.register(SocialMediaHandleModel)
