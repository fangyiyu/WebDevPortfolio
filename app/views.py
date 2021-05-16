from django.shortcuts import render
from . import predict
import numpy as np
import pandas as pd
import random

# Create your views here.

def index(request):
    MaxLotto_range = range(1,51)
    MaxLotto = predict.lotto(MaxLotto_range, 7)
    MaxLotto = sorted(MaxLotto)

    six49_range = range(1, 50)
    six49 = predict.lotto(six49_range, 6)
    six49 = sorted(six49)


    return render(request, 'app/index.html',{
        "MaxLotto": MaxLotto,
        "six49": six49
    })
