from django.shortcuts import render, redirect
from keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.models import load_model
import numpy as np
from .sustain import tokenizer


def handler(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        result = predict(title, desc)
        fina = label_reverse(result[0])
        print(fina)
    else:
        result = [None]
        fina = 'error'
    return render(request, "index.html", {'response': fina})


def predict(title, desc):
    # Max number of words in each complaint.
    MAX_SEQUENCE_LENGTH = 50
    data_for_lstms = []
    data_for_lstms.append(' '.join([title, desc]))
    # Convert the data to padded sequences
    X = tokenizer.texts_to_sequences(data_for_lstms)
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
    model = load_model('polls/video_classification-model.h5')
    predict_x = model.predict(X)
    classes_x = np.argmax(predict_x, axis=1)
    return classes_x


def label_reverse(result):
    if result == 0:
        return 'art and music'
    elif result == 1:
        return 'food'
    if result == 2:
        return 'history'
    if result == 3:
        return 'manufacturing'
    if result == 4:
        return 'science and technology'
    else:
        return 'travel'
