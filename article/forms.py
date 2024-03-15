from django import forms

from article.models import Article


class ArticleForm(forms.ModelForm):
    """
    Форма для создания и обновления статьи
    """

    class Meta:
        model = Article
        exclude = ('slug', 'status', 'data_created', 'data_published', 'number_views')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["is_published"].widget.attrs['class'] = 'form-check-input'

    def clean_blog_image(self):
        """
        Проверка изображения. Если изображения нет — загружаем пример изображения
        """
        blog_image = self.cleaned_data.get('blog_image')
        if not blog_image:
            blog_image = 'article_example.jpg'
        return blog_image
