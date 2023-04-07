import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 440527813 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return uniform.ppf(1 - alpha, loc=0.086, scale=x.max()-0.086), x.max()
