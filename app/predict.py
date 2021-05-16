import numpy as np
import pandas as pd
import random

def lotto(target, n):
  res = []
  while n>0:
    target = list(target)
    random_num = random.choice(target)
    res.append(random_num)
    target.remove(random_num)
    n = n-1
  return res

