from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275632',
        'name': 'Regina Meilani Aruan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)