from django.contrib import admin
from .models import University

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'specialization', 'tuition_fee', 'image',"description")  # Отображаем поле изображения в списке
    search_fields = ('name', 'country', 'specialization')  # Добавляем поиск по полям

admin.site.register(University, UniversityAdmin)
