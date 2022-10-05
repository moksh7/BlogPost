from django.contrib import admin
import main.models as m
# Register your models here.

admin.site.register(m.BlogPost)
admin.site.register(m.PostComment)
admin.site.register(m.Relation)
admin.site.register(m.PostLikes)