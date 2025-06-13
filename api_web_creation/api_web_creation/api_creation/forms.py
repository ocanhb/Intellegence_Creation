from django import forms
from .models import EngineeringData, DatasetRequest, DatasetResponse, ProjectModel, FinalModel

class EngineeringDataForm(forms.ModelForm):
    class Meta:
        model = EngineeringData
        fields = ['objectives', 'experience', 'implementation']
        widgets = {
            'objectives': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Tujuan'}),
            'experience': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Pengalaman'}),
            'implementation': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Implementasi'}),
        }

class DatasetRequestForm(forms.ModelForm):
    class Meta:
        model = DatasetRequest
        fields = ['kebutuhan', 'deskripsi']
        widgets = {
            'kebutuhan': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Kebutuhan dataset'}),
            'deskripsi': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Deskripsi kebutuhan'}),
        }

class DatasetResponseForm(forms.ModelForm):
    class Meta:
        model = DatasetResponse
        fields = ['nama_dataset', 'jumlah_record', 'status']
        widgets = {
            'nama_dataset': forms.TextInput(attrs={'placeholder': 'Nama dataset'}),
            'jumlah_record': forms.NumberInput(attrs={'placeholder': 'Jumlah record'}),
            'status': forms.TextInput(attrs={'placeholder': 'Status'}),
        }

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['nama_model', 'akurasi', 'metrics_tambahan', 'status_acc']
        widgets = {
            'nama_model': forms.TextInput(attrs={'placeholder': 'Nama model'}),
            'akurasi': forms.NumberInput(attrs={'step': 0.01, 'placeholder': 'Akurasi'}),
            'metrics_tambahan': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Metrics tambahan'}),
            'status_acc': forms.TextInput(attrs={'placeholder': 'Status acc'}),
        }

class FinalModelForm(forms.ModelForm):
    class Meta:
        model = FinalModel
        fields = ['status_project', 'final_model', 'dokumentasi_link']
        widgets = {
            'status_project': forms.TextInput(attrs={'placeholder': 'Status project'}),
            'final_model': forms.TextInput(attrs={'placeholder': 'Final model'}),
            'dokumentasi_link': forms.URLInput(attrs={'placeholder': 'Link dokumentasi'}),
        }
