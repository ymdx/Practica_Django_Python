from django.contrib import admin

# Register your models here.

from Wordplease.models import Blog
from Wordplease.models import Post
from Wordplease.models import User

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(User)
