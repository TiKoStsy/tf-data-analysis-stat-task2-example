import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 440527813 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return (x.mean() - 0.086*alpha)/(1 - alpha), \
           (x.mean() - 0.086*(1 - alpha))/(alpha)
