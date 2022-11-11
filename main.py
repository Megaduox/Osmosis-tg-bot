import requests
import json
import difflib


url = 'https://api-osmosis.imperator.co/pairs/v1/summary'


def create_first_file():
    all_tokens = list()
    response = requests.get(url)

    if response:
        print('Ответ от сервера успешно получен!')
    else:
        print('В ходе осуществления запроса возникла ошибка.')

    json_response = response.json()

    for elem in json_response['data']:
        all_tokens.append(elem['pool_id'])

    file_object = open('firstFile.txt', 'w')
    for item in all_tokens:
        file_object.write("%s\n" % item)
    file_object.close()


def compare_files():
    result = list()
    with open('firstFile.txt') as file_1:
        file_1_text = file_1.readlines()

    with open('secondFile.txt') as file_2:
        file_2_text = file_2.readlines()

    for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile='firstFile.txt',
            tofile='secondFile.txt', lineterm=''):
        print(line)
        result.append(line)
    breakpoint()


def check_new_tokens():
    all_tokens = list()
    response = requests.get(url)

    if response:
        print('Ответ от сервера успешно получен!')
    else:
        print('В ходе осуществления запроса возникла ошибка.')

    json_response = response.json()

    for elem in json_response['data']:
        # print(i['quote_symbol'],'/',i['base_symbol'], sep = '')
        # print('Цена:',round(i['price'],2))
        # print('Ликвидность:',round(i['liquidity'],2),'\n')
        # print('pool_address:', i['pool_address'],'\n')
        # print(elem['pool_id'])
        # if 'TORI' in elem['base_symbol']:
        all_tokens.append(elem['pool_id'])

    with open('secondFile.txt', 'w') as file_object:
        for item in all_tokens:
            file_object.write("%s\n" % item)
        print('Done')


if __name__ == '__main__':
    # create_first_file()
    # check_new_tokens()
    compare_files()
