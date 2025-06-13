from django.shortcuts import render, redirect
from .forms import CreationEntryForm 
from .models import CreationEntry, ModelEntry
import requests
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt 
from django.views.decorators.http import require_http_methods

API_BASE = "http://127.0.0.1:8000/api" 

def index_view(request):
    return render(request, 'index.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')
def modeling_view(request):
    models = ModelEntry.objects.all().order_by('-id')
    data = [
        {
            "id": idx + 1,
            "title": m.title,
            "target": m.target,
            "accuracy": m.accuracy,
            "status": m.status,
            "from": "Dataset Upload",
            "features": m.features,
            "jenis": "Numerical",  # bisa kamu sesuaikan kalau ada field aslinya
            "category": m.category,
            "input": m.input,
            "process": m.process,
            "output": m.output,
            "algorithm": m.algorithm,
            "start": m.start.strftime("%Y-%m-%d") if m.start else '',
            "end": m.end.strftime("%Y-%m-%d") if m.end else '',
            "deployment": "no",  # bisa disesuaikan jika kamu punya field ini
            "activity": m.activity,
        }
        for idx, m in enumerate(models)
    ]
    return render(request, 'modeling.html', {'entries_json': data})

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_model_entry(request, model_id):
    try:
        model = ModelEntry.objects.get(id=model_id)
        model.delete()
        return JsonResponse({'status': 'success'})
    except ModelEntry.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Model tidak ditemukan'}, status=404)

def modeling_api_view(request):
    models = ModelEntry.objects.all().order_by('-id')
    data = [m.to_dict() for m in models]
    return JsonResponse(data, safe=False)


@csrf_exempt
def creation_entry_api(request):
    if request.method == 'POST':
        try:
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()

            model = ModelEntry.objects.create(
                title=request.POST.get('problem_name'),
                features=request.POST.get('features'),
                target=request.POST.get('output'),
                category=request.POST.get('dataset_type'),
                accuracy=request.POST.get('accuracy') or '0%',
                status=request.POST.get('training_status'),
                input=request.POST.get('features'),
                process=request.POST.get('refining_strategy'),
                output=request.POST.get('output'),
                algorithm = request.POST.get('algorithm'),
                activity=request.POST.get('data_activity'),
                start=start_date,
                end=end_date
            )
            return JsonResponse({'status': 'success', 'data': model.to_dict()})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})

def creation_entry(request):
    if request.method == 'POST':
        entry = CreationEntry(
            problem_name = request.POST.get('problem_name'),
            features = request.POST.get('features'),
            output = request.POST.get('output'),
            objective = request.POST.get('objective'),
            dataset_type = request.POST.get('dataset_type'),
            training_status = request.POST.get('training_status'),
            accuracy = request.POST.get('accuracy'),
            refining_strategy = request.POST.get('refining_strategy'),
            refining_status = request.POST.get('refining_status'),
            data_activity = request.POST.get('data_activity'),
            start_date = request.POST.get('start_date'),
            end_date = request.POST.get('end_date'),
            upload_csv = request.FILES.get('upload_csv')
        )
        entry.save()
        return redirect('modeling')  # redirect ke halaman modeling setelah submit
    return render(request, 'creation_entry.html')


def integrasi_view(request):
    engineering = requests.get(f"{API_BASE}/engineering-data/").json()
    dataset_request = requests.get(f"{API_BASE}/dataset-request/").json()
    dataset_response = requests.get(f"{API_BASE}/dataset-response/").json()
    project_models = requests.get(f"{API_BASE}/project-model/").json()
    final_models = requests.get(f"{API_BASE}/final-model/").json()

    context = {
        'engineering': engineering,
        'dataset_request': dataset_request,
        'dataset_response': dataset_response,
        'project_models': project_models,
        'final_models': final_models,
    }

    return render(request, 'integrasi.html', context)
