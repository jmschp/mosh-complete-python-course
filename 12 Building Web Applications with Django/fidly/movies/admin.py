from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_created")


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "genre", "number_in_stock", "relase_year", "daily_rate", "date_created")
    exclude = ("date_created", )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

# Register your models here.
