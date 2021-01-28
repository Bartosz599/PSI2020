from django.contrib import admin
from .models import Dostawca, Nadawca, Odbiorca, Paczka, Harmonogrampracy, Zamowienie

admin.site.register(Dostawca)
admin.site.register(Nadawca)
admin.site.register(Odbiorca)
admin.site.register(Paczka)
admin.site.register(Harmonogrampracy)
admin.site.register(Zamowienie)
