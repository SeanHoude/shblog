from django.contrib import admin
from blog.models import Post, Comment, Favorite, Like

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'description', 'slug', 'created', 'updated', 'image', )
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('user', 'post', 'comment', 'created', 'updated', )

class FavoriteAdmin(admin.ModelAdmin):
    model = Favorite
    list_display = ('user', 'post', 'created', 'updated', )

class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ('user', 'post', 'created', 'updated', )

# class UploadAdmin(admin.ModelAdmin):
#     model = Upload
#     list_display = ('post', 'image', 'created', 'updated', )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Like, LikeAdmin)
# admin.site.register(Upload, UploadAdmin)
