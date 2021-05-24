from django.shortcuts import render



def guito_page_view(request):
    context = {
        'raca': "Yorkshire Terrier"
    }
    return render(request, 'website/guito.html', context)

def home_page_view(request):
    context = {
        'data': "24/08/2019",
        'cor': "Preto e Castanho",
        'porte': "Pequeno",
        'carat': "Fotogénico"
    }
    return render(request, 'website/home.html', context)


def fotos_page_view(request):

    return render(request, 'website/fotos.html')


# Create your views here.
