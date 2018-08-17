from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def counter(request):
    entered_text = request.GET['fulltext']
    split_text = entered_text.split()

    words = len(split_text)

    word_dict = {}

    for word in split_text:
        if word in word_dict:
            word_dict[word] += 1
        else: word_dict[word] = 1

    sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'entered_text':entered_text, 'count':len(split_text), 'word_dict':sorted_dict})

def aboutme(request):
    return render(request, 'aboutme.html')
