from django.db import models

class EngineeringData(models.Model):
    objectives = models.TextField()
    experience = models.TextField()
    implementation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Menambahkan auto_now_add=True

class DatasetRequest(models.Model):
    kebutuhan = models.TextField()
    deskripsi = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Menambahkan auto_now_add=True

class DatasetResponse(models.Model):
    nama_dataset = models.CharField(max_length=100)
    jumlah_record = models.IntegerField()
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)  # Menambahkan auto_now_add=True

class ProjectModel(models.Model):
    nama_model = models.CharField(max_length=100)
    akurasi = models.FloatField()
    metrics_tambahan = models.TextField()
    status_acc = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)  # Menambahkan auto_now_add=True

class FinalModel(models.Model):
    status_project = models.CharField(max_length=50)
    final_model = models.CharField(max_length=100)
    dokumentasi_link = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Menambahkan auto_now_add=True
