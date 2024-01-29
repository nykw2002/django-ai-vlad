from django.shortcuts import render
import openai

open_ai_key = "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"
client = openai.OpenAI(api_key=open_ai_key)

# Create your views here.
def home(request):
    client.fine_tuning.jobs.create(
        trainint_file="knowledge.pdf",
        model="gpt-3.5-turbo",
    )
        


    context = {'data': "test returned data"}
    return render(request, 'home.html')