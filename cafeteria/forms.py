from django import forms
from .models import Opinion, Contacto

from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['nombre', 'comentario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu opinión'}),
        }

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Tu nombre',
                'id': 'id_nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'tu@correo.com',
                'id': 'id_email'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Asunto',
                'id': 'id_asunto'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Escribe tu mensaje...',
                'rows': 5,
                'id': 'id_mensaje'
            }),
        }