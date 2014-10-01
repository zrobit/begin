from django.contrib import admin

from posts.models import Post, Category, Tag, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
