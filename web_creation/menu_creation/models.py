from django.db import models
from datetime import date, datetime

class CreationEntry(models.Model):
    problem_name = models.CharField(max_length=255)
    features = models.TextField()
    output = models.CharField(max_length=255)
    objective = models.TextField()

    dataset_type = models.CharField(max_length=50, choices=[
        ('regresi', 'Regresi'),
        ('klasifikasi', 'Klasifikasi'),
        ('forecasting', 'Forecasting'),
    ])

    training_status = models.CharField(max_length=50, choices=[
        ('belum', 'Belum Dilatih'),
        ('proses', 'Proses'),
        ('sudah', 'Sudah Dilatih'),
    ])

    accuracy = models.CharField(max_length=50, blank=True, null=True)
    refining_strategy = models.CharField(max_length=255, blank=True, null=True)

    refining_status = models.CharField(max_length=50, choices=[
        ('belum', 'Belum'),
        ('proses', 'Proses'),
        ('sudah', 'Sudah'),
    ])

    data_activity = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    upload_csv = models.FileField(upload_to='uploads/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.problem_name

class History(models.Model):
    title = models.CharField(max_length=200)
    from_field = models.CharField(max_length=200)
    target = models.CharField(max_length=100)
    features = models.TextField()
    jenis_data = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    accuracy = models.CharField(max_length=20)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    deployment = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Engineering(models.Model):
    objectives = models.TextField()
    experience = models.TextField()
    implementation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class DatasetRequest(models.Model):
    kebutuhan = models.CharField(max_length=255)
    deskripsi = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class DatasetResponse(models.Model):
    nama_dataset = models.CharField(max_length=255)
    jumlah_record = models.IntegerField()
    status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

class ProjectModel(models.Model):
    nama_model = models.CharField(max_length=100)
    akurasi = models.FloatField()
    metrics_tambahan = models.TextField()
    status_acc = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

class FinalModel(models.Model):
    status_project = models.CharField(max_length=100)
    final_model = models.CharField(max_length=100)
    dokumentasi_link = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class ModelEntry(models.Model):
    title = models.CharField(max_length=200)
    features = models.TextField()
    target = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    accuracy = models.CharField(max_length=20)
    status = models.CharField(max_length=100)
    input = models.TextField()
    process = models.TextField()
    output = models.CharField(max_length=100)
    algorithm = models.TextField()
    activity = models.TextField()
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "features": self.features,
            "target": self.target,
            "category": self.category,
            "accuracy": self.accuracy,
            "status": self.status,
            "input": self.input,
            "process": self.process,
            "output": self.output,
            "algorithm": self.algorithm,
            "activity": self.activity,
            "start": self.start.strftime('%Y-%m-%d') if self.start else '',
            "end": self.end.strftime('%Y-%m-%d') if self.end else '',
            "from": "Dataset Upload",
            "jenis": "Numerical",  # ubah sesuai kebutuhan
            "deployment": "no"     # default sementara
        }
