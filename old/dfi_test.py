import dataframe_image as dfi
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_x =[[1,'a',3,4,5,6,7,True],[11,'b',13,14,15,16,17,True]]
df = pd.DataFrame(data_x)
df.columns=('ts','link','Stock Max', 'Price', 'Stock Selected',
            'Delivery Price','Total Price', 'Data Correct')

df.to_csv('a.csv')