from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    ''' Form to add a product to the store '''
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        # Update the category field to use friendly names
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 mb-4'
