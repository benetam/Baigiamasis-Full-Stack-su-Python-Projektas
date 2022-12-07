from django import forms
from django.forms import ModelForm
from .models import Post, Category
from django.core.exceptions import ValidationError

# choises = Category.objects.all().values_list('name','name')
# choise_list = []
# for item in choises:
#     choise_list.append(item)

class CreateViewForm(forms.ModelForm):

    title = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    category = forms.Select()


    class Meta:
        model = Post
        fields = ['title','content','category', 'date_posted','image']

    def clean(self):
        cleaned_data = super(CreateViewForm, self).clean()

        input_field_1 = cleaned_data.get('title')
        input_field_2 = cleaned_data.get('content')
        input_field_3 = cleaned_data.get('category')

        if input_field_1 is not None and input_field_2 is not None:
            if len(input_field_2)<3:
                self.add_error('content', ValidationError('Parašykite kažką daugiau :)'))



class UpdateViewForm(forms.ModelForm):

    title = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    image_clear = forms.BooleanField(required=False)
    category = forms.Select()

    class Meta:
        model = Post
        fields = ['title','content','category','date_posted','image']

    def clean(self):
        cleaned_data = super(UpdateViewForm, self).clean()

        input_field_1 = cleaned_data.get('title')
        input_field_2 = cleaned_data.get('content')
        input_field_3 = cleaned_data.get('date_posted')

        if input_field_1 is not None and input_field_2 is not None:
            if len(input_field_2)<3:
                self.add_error('content', ValidationError('Žinutė per trumpa'))
