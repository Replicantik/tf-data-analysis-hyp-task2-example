import pandas as pd
import numpy as np


chat_id = 359238083 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import ks_2samp
    stat, p = ks_2samp(x, y)
    if p <= 0.07:
        return False
    else:
        return True
        
