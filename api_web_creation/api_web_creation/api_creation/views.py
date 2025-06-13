from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.request import Request
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EngineeringDataForm, DatasetRequestForm, DatasetResponseForm, ProjectModelForm, FinalModelForm
from .models import EngineeringData, DatasetRequest, DatasetResponse, ProjectModel, FinalModel
from .serializers import (
    EngineeringDataSerializer, DatasetRequestSerializer, DatasetResponseSerializer,
    ProjectModelSerializer, FinalModelSerializer
)

class EngineeringDataAPIView(APIView):
    def get(self, request):
        data = EngineeringData.objects.all().order_by('-timestamp')
        serializer = EngineeringDataSerializer(data, many=True)
        return Response(serializer.data)

class DatasetRequestAPIView(APIView):
    def get(self, request):
        data = DatasetRequest.objects.all().order_by('-timestamp')
        serializer = DatasetRequestSerializer(data, many=True)
        return Response(serializer.data)

class DatasetResponseAPIView(APIView):
    def get(self, request):
        data = DatasetResponse.objects.all().order_by('-timestamp')
        serializer = DatasetResponseSerializer(data, many=True)
        return Response(serializer.data)

class ProjectModelAPIView(APIView):
    def get(self, request):
        data = ProjectModel.objects.all().order_by('-timestamp')
        serializer = ProjectModelSerializer(data, many=True)
        return Response(serializer.data)

class FinalModelAPIView(APIView):
    def get(self, request):
        data = FinalModel.objects.all().order_by('-timestamp')
        serializer = FinalModelSerializer(data, many=True)
        return Response(serializer.data)

class APIRootView(APIView):
    def get(self, request: Request):
        base_url = request.build_absolute_uri('/')[:-1]  # dapetin http://127.0.0.1:5000

        return Response({
            "engineering_data": base_url + "/api/engineering-data/",
            "dataset_request": base_url + "/api/dataset-request/",
            "dataset_response": base_url + "/api/dataset-response/",
            "project_model": base_url + "/api/project-model/",
            "final_model": base_url + "/api/final-model/",
        })

def integrasi_view(request):
    context = {
        'engineering_form': EngineeringDataForm(),
        'dataset_request_form': DatasetRequestForm(),
        'dataset_response_form': DatasetResponseForm(),
        'project_model_form': ProjectModelForm(),
        'final_model_form': FinalModelForm()
    }
    return render(request, 'integrasi.html', context)

def submit_engineering(request):
    if request.method == 'POST':
        form = EngineeringDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')  # redirect ke laporan_integrasi
        else:
            # kalau error, render form dengan error (bisa sesuaikan)
            return render(request, 'integrasi.html', {'engineering_form': form})
    else:
        form = EngineeringDataForm()
        return render(request, 'integrasi.html', {'engineering_form': form})
    
def submit_dataset_request(request):
    if request.method == 'POST':
        form = DatasetRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
        else:
            return render(request, 'integrasi.html', {'dataset_request_form': form})
    else:
        form = DatasetRequestForm()
        return render(request, 'integrasi.html', {'dataset_request_form': form})

def submit_dataset_response(request):
    if request.method == 'POST':
        form = DatasetResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
        else:
            return render(request, 'integrasi.html', {'dataset_response_form': form})
    else:
        form = DatasetResponseForm()
        return render(request, 'integrasi.html', {'dataset_response_form': form})

def submit_project_model(request):
    if request.method == 'POST':
        form = ProjectModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
        else:
            return render(request, 'integrasi.html', {'project_model_form': form})
    else:
        form = ProjectModelForm()
        return render(request, 'integrasi.html', {'project_model_form': form})

def submit_final_model(request):
    if request.method == 'POST':
        form = FinalModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
        else:
            return render(request, 'integrasi.html', {'final_model_form': form})
    else:
        form = FinalModelForm()
        return render(request, 'integrasi.html', {'final_model_form': form})


def laporan_integrasi_view(request):
    context = {
        'engineering': EngineeringData.objects.all().order_by('-timestamp'),
        'dataset_requests': DatasetRequest.objects.all().order_by('-timestamp'),
        'project_models': ProjectModel.objects.all().order_by('-timestamp'),
        'final_models': FinalModel.objects.all().order_by('-timestamp'),
    }
    return render(request, 'laporan_integrasi.html', context)

# EDIT views
def edit_engineering(request, pk):
    obj = get_object_or_404(EngineeringData, pk=pk)
    if request.method == "POST":
        form = EngineeringDataForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
    else:
        form = EngineeringDataForm(instance=obj)
    return render(request, 'edit_form.html', {'form': form, 'title': 'Edit Engineering Data'})

def edit_dataset(request, pk):
    obj = get_object_or_404(DatasetRequest, pk=pk)
    if request.method == "POST":
        form = DatasetRequestForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
    else:
        form = DatasetRequestForm(instance=obj)
    return render(request, 'edit_form.html', {'form': form, 'title': 'Edit Dataset Request'})

def edit_project_model(request, pk):
    obj = get_object_or_404(ProjectModel, pk=pk)
    if request.method == "POST":
        form = ProjectModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
    else:
        form = ProjectModelForm(instance=obj)
    return render(request, 'edit_form.html', {'form': form, 'title': 'Edit Project Model'})

def edit_final_model(request, pk):
    obj = get_object_or_404(FinalModel, pk=pk)
    if request.method == "POST":
        form = FinalModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('laporan_integrasi')
    else:
        form = FinalModelForm(instance=obj)
    return render(request, 'edit_form.html', {'form': form, 'title': 'Edit Final Model'})

# DELETE views
def delete_engineering(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(EngineeringData, pk=pk)
        obj.delete()
        return redirect('laporan_integrasi')
    return redirect('laporan_integrasi')


def delete_dataset(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(DatasetRequest, pk=pk)
        obj.delete()
        return redirect('laporan_integrasi')
    return redirect('laporan_integrasi')


def delete_project_model(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(ProjectModel, pk=pk)
        obj.delete()
        return redirect('laporan_integrasi')
    return redirect('laporan_integrasi')


def delete_final_model(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(FinalModel, pk=pk)
        obj.delete()
        return redirect('laporan_integrasi')
    return redirect('laporan_integrasi')