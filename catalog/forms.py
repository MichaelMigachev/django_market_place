from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError


forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа',
             'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name_product', 'description', 'image', 'category', 'price',)
        # fields = "__all__"                       # если нужны все поля
        # exclude = ("created_at", "updated_at",)  # исключить поля

    def clean_name_product(self):
        name_product = self.cleaned_data.get('name_product')
        if any(word in name_product.lower() for word in forbidden):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return name_product

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in forbidden):
            raise ValidationError("Описание не должно содержать запрещенные слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Неверная цена")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1025:
                raise ValidationError("Файл больше 5МБ")
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise ValidationError("Файл не допустимого формата")
        return image
