from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1
            if main_count > 1:
                raise ValidationError('Основной раздел должен быть один')
        if main_count == 0:
            raise ValidationError('Задайте основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    fields = ["tag", "is_main"]
    formset = ScopeInlineFormSet


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['tag', 'is_main']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'text', 'published_at', 'image']