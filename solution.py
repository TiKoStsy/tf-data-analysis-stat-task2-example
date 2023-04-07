import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 440527813 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return x.max(), (x.max() - 0.086)/(np.power(alpha, 1/len(x))) + 0.086
