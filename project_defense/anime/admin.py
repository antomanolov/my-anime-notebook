from django.contrib import admin


from project_defense.anime.models import AnimeTorrent


@admin.register(AnimeTorrent)
class AppUserAdmin(admin.ModelAdmin):
    fields = ('name', 'genre')