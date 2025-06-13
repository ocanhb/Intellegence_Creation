from django import forms
from .models import CreationEntry

class CreationEntryForm(forms.ModelForm):
    class Meta:
        model = CreationEntry
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'problem_name': forms.TextInput(attrs={'placeholder': 'Contoh: Prediksi Harga Rumah'}),
            'features': forms.TextInput(attrs={'placeholder': 'Contoh: Luas, Lokasi'}),
            'output': forms.TextInput(attrs={'placeholder': 'Contoh: Harga Rumah'}),
            'objective': forms.Textarea(attrs={'placeholder': 'Contoh: Prediksi harga rumah berdasarkan luas dan lokasi'}),
            'accuracy': forms.TextInput(attrs={'placeholder': 'Contoh: 92.5%'}),
            'refining_strategy': forms.TextInput(attrs={'placeholder': 'Contoh: Feature Tuning'}),
            'data_activity': forms.Textarea(attrs={'placeholder': 'Deskripsikan aktivitas pemrosesan data...'}),
        }
