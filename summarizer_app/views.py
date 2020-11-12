from django.shortcuts import render
from .text_summarizer import Summarizer
from .models import Summarized_Data


def index(request):
    template_name = 'summarizer_app/index.html'
    context = {

    }
    return render(request, template_name, context)


def get_data(request):
    template_name = 'summarizer_app/get_data.html'
    context = {
        'title': 'Get data to summarize',
    }
    return render(request, template_name, context)


def summarize_data(request):
    if request.method == 'POST':
        summarizer = Summarizer()
        try:
            saved_data = Summarized_Data.objects.first()
            saved_data.delete()

            data = request.POST['txtdata']
            # if data.is_valid:
            summarized_text = summarizer.summarize(data)
            saved_data = Summarized_Data(raw_text=data, summarized=summarized_text)
            saved_data.save()

        except:
            data = request.POST['txtdata']
            # if data.is_valid:
            summarized_text = summarizer.summarize(data)
            saved_data = Summarized_Data(raw_text=data, summarized=summarized_text)
            saved_data.save()

    context = {
        'title': 'Summarized Data',
        'summarized': summarized_text,
        'raw_text': data,
    }

    template_name = 'summarizer_app/summarize.html'
    return render(request, template_name, context)


def prev_summarize_data(request):
    try:
        saved_data = Summarized_Data.objects.first()
        context = {
            'title': 'Summarized Data',
            'summarized': saved_data.summarized,
            'raw_text': saved_data.raw_text,
        }
    except:
        context = {
            'title': 'Summarized Data',
        }
    template_name = 'summarizer_app/summarize.html'
    return render(request, template_name, context)
