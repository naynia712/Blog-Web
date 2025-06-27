from django import forms
from artikel.models import Kategori, ArtikelBlog, User
from django_ckeditor_5.widgets import CKEditor5Widget

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama',)
        widgets = {
            "nama": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
        }

        # widgets = {
        #     "ruang": forms.Select(
        #         attrs={
        #             'class': 'form-control select2-ruangan',
        #             'type': 'text',
        #             'data-style': 'btn btn-danger btn-block',
        #             'title': 'pilih ruangan',
        #             'data-size': '7',
        #         }
        #     ),
        #     "nama": forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols': '30',
        #             'rows': '10',
        #             'required': True
        #         }
        #     ),
        #     "jumlah": forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols': '30',
        #             'rows': '10',
        #             'required': True
        #         }
        #     ),
        #     "baik": forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols': '30',
        #             'rows': '10',
        #             'required': True
        #         }
        #     ),
        #     "perbaikan": forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols': '30',
        #             'rows': '10',
        #             'required': True
        #         }
        #     ),
        #                 "musnah": forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols': '30',
        #             'rows': '10',
        #             'required': True
        #         }
        #     ),
        # }

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = ArtikelBlog
        fields = ('kategori','judul', 'konten', 'gambar', 'status')
        widgets = {
            "kategori": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'id': "choices-multiple-remove-button",
                    'name': "choices-multiple-remove-button"
                }
            ),
            "judul": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            "konten": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
            # "gambar": forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'required': True
            #     }
            # ),
            # "status": forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'required': True
            #     }
            # ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['konten'].required = False
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff', 'groups']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_staff'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['groups'].widget.attrs.update({'class': 'form-control select2'})

