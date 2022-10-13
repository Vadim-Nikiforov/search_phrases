import pandas as pd
import os
from datetime import *

start_time = datetime.now()
directory = 'logs/'
phrase_search = 'арест'
done = pd.DataFrame()
list_file = os.listdir(directory)

for filename in list_file:
    if '.xlsx' in filename:
        directory_f = f'{directory}{filename}'
        print(directory_f)
        try:
            d = pd.read_excel(directory_f)
            d = d[d.question.notna()]
            done = pd.concat([done, d[d['question'].str.contains(phrase_search)]])
        except:
            print("поврежден файл:", directory_f)

done.to_excel('res.xlsx')
print("время", datetime.now() - start_time)
print("Проверено фраз", len(list_file))
print("найдено фраз", len(done))
