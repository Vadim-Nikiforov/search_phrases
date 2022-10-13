from pandas import *
from os import *
from datetime import *
from fun_search import *

start_time = datetime.now()

files = listdir("logs")

count = 0

df_res = []
for i in files:
    s_res = []
    s = []
    path = "logs\\" + i
    print(path)
    try:
        df_new = read_excel(path)
        s = list(df_new.values)
    except:
        print("поврежден файл:", path)

    count += len(s)

    for j in s:
        if search_word(str(list(j)[6])):
            s_res.append(j)

    df_end = DataFrame(s_res)
    df_res.append(df_end)
done = concat(df_res)
done.to_excel("res.xlsx", index=False) # Здесь можно указать любое название вместо "res"
print("время", datetime.now() - start_time)
print("Проверено фраз", count)
print("Найдено фраз", len(done))
