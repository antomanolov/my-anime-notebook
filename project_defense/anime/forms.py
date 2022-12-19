from django import forms

from project_defense.anime.models import AnimeTorrent


class AnimeCreateForm(forms.ModelForm):
    class Meta:
        model = AnimeTorrent
        exclude = ('date_of_upload', 'date_of_last_download', 'uploader', 'download_count')
