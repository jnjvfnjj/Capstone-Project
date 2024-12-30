from django.shortcuts import render, get_object_or_404
from .models import University

# Главная страница
def home(request):
    return render(request, 'index.html')

# Страница поиска
def search(request):
    return render(request, 'search.html')

# Результаты поиска
def results(request):
    if request.method == "GET":
        country = request.GET.get("country")
        specialization = request.GET.get("specialization")
        budget = request.GET.get("budget")
        
        universities = University.objects.all()

        if country:
            universities = universities.filter(country__icontains=country)
        if specialization:
            universities = universities.filter(specialization__icontains=specialization)
        if budget:
            universities = universities.filter(tuition_fee__lte=budget)

        return render(request, 'results.html', {'universities': universities})

    return render(request, 'search.html', {'error': 'Invalid request method. Please use GET.'})

# Детали университета
def university_detail(request, id):
    university = get_object_or_404(University, id=id)
    return render(request, 'university.html', {'university': university})
