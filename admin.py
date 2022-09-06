from django.contrib import admin
from news.models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display=('new_title','new_desc','new_image')

admin.site.register(News, NewsAdmin)
