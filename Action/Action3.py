import pandas as pd
import os

cwd = os.getcwd()
df = pd.read_csv(cwd + '\\car_complain.csv')

############用isin找出特定字符的行，再用df.shape[0]来计算行数