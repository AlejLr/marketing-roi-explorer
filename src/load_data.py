import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    
    
    data = pd.read_csv(file_path)
    return data

df = load_data('../data/marketing_data.csv')