from django.contrib import admin
from .models import BookInfo1,HeroInfo1
# Register your models here.
class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo1
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title','pub_data')
    list_filter = ('title','pub_data')
    list_per_page = 20
    inlines = [HeroInfoInlines]



admin.site.register(BookInfo1,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('name','content')
    list_filter = ('name',)
    search_fields = ('name','content')
admin.site.register(HeroInfo1,HeroInfoAdmin)

