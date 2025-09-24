from django.shortcuts import render, get_object_or_404
from .models import SpecialOffer, Category, Course, PopularSearch

# Create your views here.
def home(request):
    offers = SpecialOffer.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    popular_courses = Course.objects.order_by('-views')[:4]  # top 4 par vues
    recent_courses = Course.objects.order_by('-created_at')[:4]  # 4 plus récents
    
    context = {
        "offers": offers,
        "categories": categories,
        "popular_courses": popular_courses,
        "recent_courses": recent_courses,
    }
    return render(request, "core/home.html", context)

def dash(request):
    return render(request, 'core/dashboard.html')

def search_view(request):
    query = request.GET.get("q")  # ce qui est tapé dans la barre de recherche
    results = []

    if query:
        results = Course.objects.filter(
            title__icontains=query
        ) | Course.objects.filter(
            description__icontains=query
        ) | Course.objects.filter(
            category__name__icontains=query
        )

    categories = Category.objects.all()

    context = {
        "query": query,
        "results": results,
        "categories": categories,
    }
    return render(request, "core/recherche.html", context)



def search_result(request):
    query = request.GET.get('q', '').strip()
    results = []
    
    if query:
        # Enregistrer/mettre à jour la recherche populaire
        search_term, created = PopularSearch.objects.get_or_create(term=query)
        search_term.count += 1
        search_term.save()
        
        # Votre logique de recherche existante
        results = Course.objects.filter(title__icontains=query)
    
    # Récupérer les catégories et recherches populaires
    categories = Category.objects.all()
    popular_searches = PopularSearch.objects.order_by('-count')[:9]
    
    context = {
        'query': query,
        'results': results,
        'categories': categories,
        'popular_searches': popular_searches,
    }
    return render(request, 'core/search_result.html', context)



def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    courses = category.courses.all()  # grâce à related_name="courses"
    return render(request, "core/category_detail.html", {"category": category, "courses": courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "core/course_detail.html", {"course": course})

def search(request):
    query = request.GET.get("q")
    courses = Course.objects.filter(title__icontains=query) if query else []
    return render(request, "search.html", {"query": query, "courses": courses})
