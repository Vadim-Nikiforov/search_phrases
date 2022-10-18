from pandas import *
from os import *
from datetime import *


def search_word(phrase, list_of_phrases):
    return all(map(lambda s: any(map(lambda word: word in phrase.lower(), s)), list_of_phrases))


def search_state(responses, state_name):
    return any(map(lambda state: state in responses, state_name))


def search_state_and_phrase(response_data, list_of_phrases, state_name):
    if len(list_of_phrases) > 0 and len(state_name) > 0:
        return search_word(str(response_data[6]), list_of_phrases) and search_state(str(response_data[11]), state_name)
    elif len(list_of_phrases) == 0 and len(state_name) > 0:
        return search_state(str(response_data[11]), state_name)
    elif len(list_of_phrases) > 0 and len(state_name) == 0:
        return search_word(str(response_data[6]), list_of_phrases)
    else:
        print("не верно заданы параметры поиска")


def search(list_of_phrases, state_name):
    start_time = datetime.now()
    files = listdir("logs")
    count = 0
    list_df_search_result = []
    for i in files:
        result_search = []
        logs_list = []
        path = "logs\\" + i
        print(path)
        try:
            df_new = read_excel(path)
            logs_list = list(df_new.values)
        except:
            print("поврежден файл:", path)

        count += len(logs_list)

        for response_data in logs_list:
            if search_state_and_phrase(list(response_data), list_of_phrases, state_name):
                result_search.append(response_data)

        df_end = DataFrame(result_search)
        list_df_search_result.append(df_end)
    done = concat(list_df_search_result)

    file_name_res = "res.xlsx"  # Здесь можно указать любое название вместо "res"

    try:
        done.to_excel(file_name_res, index=False)
    except:
        print()
        print("Открыт файл", file_name_res)
        print("Не возможно сохранить в открытый файл")
        print("Если нужно сохранить существующий файл", file_name_res, ", то перемести его в другую папку")
        print("Закрой или перемести файл и нажми ENTER")
        input("Если файл закрыт или перемещен, поставь курсор в эту строку и нажми ENTER -> ")
        done.to_excel(file_name_res, index=False)

    print("время", datetime.now() - start_time)
    print("Проверено фраз", count)
    print("Найдено фраз", len(done))
