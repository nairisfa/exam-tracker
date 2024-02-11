from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Naila Nursa Krisnazulfa',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)