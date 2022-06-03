from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_counter = 0
        print(self.forms)
        print(f'is_main_counter в начале = {is_main_counter}')
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            print(form.cleaned_data.get('tag'))
            print(form.cleaned_data)
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if form.cleaned_data.get('is_main'):
                is_main_counter += 1
                print(f'is_main_counter в середине = {is_main_counter}')
            # else:
            #     is_main_counter = 0
        print(f'is_main_counter в конце = {is_main_counter}')
        if is_main_counter == 0:
            raise ValidationError('Укажите основной раздел')
        elif is_main_counter > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
    #inlines = [ScopeInline,]

