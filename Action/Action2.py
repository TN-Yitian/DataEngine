import pandas as pd
import numpy as np

df = pd.DataFrame([[68, 65, 30],
                  [95, 76, 98],
                  [98, 86, 88],
                  [90, 88, 77],
                   [80, 90, 90]],
                  columns=['语文', '数学', '英语'],
                  index=['张飞', '关羽', '刘备', '典韦', '许褚'])
print(df)

Chinese_mean = np.mean(df['语文'])
Chinese_min = np.min(df['语文'])
Chinese_max = np.max(df['语文'])
Chinese_std = np.std(df['语文'])
Chinese_var = np.var(df['语文'])
print(Chinese_mean, Chinese_max, Chinese_min, Chinese_std, Chinese_var)

# print(df.loc['张飞'])
ZF_sum = sum(df.loc['张飞'])
GY_sum = sum(df.loc['关羽'])
LB_sum = sum(df.loc['刘备'])
DW_sum = sum(df.loc['典韦'])
XC_sum = sum(df.loc['许褚'])

df_sum = pd.DataFrame([ZF_sum, GY_sum, LB_sum, DW_sum, XC_sum], index=['张飞', '关羽', '刘备', '典韦', '许褚'])
print(df_sum.sort_values)