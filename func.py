import requests
import json
import difflib


url = 'https://api-osmosis.imperator.co/pairs/v1/summary'

all_tokens = set()
all_tokens_temp = {'813', '835', '555', '810', '806',
                   '704', '482', '600', '601', '572',
                   '722', '719', '712', '611', '2',
                   '681', '615', '796', '616', '679',
                   '613', '605', '4', '690', '557', '778', '553',
                   '560', '730', '567', '773', '627', '461',
                   '662', '790', '197', '648', '8', '15', '772',
                   '738', '1', '643', '817', '769', '608', '800',
                   '837', '733', '585', '586', '629', '577', '626',
                   '625', '812', '816', '674', '561', '9', '5', '602',
                   '573', '777', '840', '7', '637', '731', '151', '562',
                   '481', '612', '803', '793', '547', '617', '498', '649',
                   '618', '644', '678', '22', '638', '571', '686', '744',
                   '826', '787', '747', '651', '574', '597', '464', '604',
                   '497', '606', '795', '596', '833', '584', '732', '641',
                   '725', '3', '619', '832', '463', '645', '631', '42', '587',
                   '558', '6', '13', '621', '10'}


def check_pools():

    response = requests.get(url)

    if response:
        print('Ответ от сервера успешно получен!')
    else:
        print('В ходе осуществления запроса возникла ошибка.')

    json_response = response.json()

    for elem in json_response['data']:
        all_tokens.add(elem['pool_id'])

    difference = all_tokens.difference(all_tokens_temp)
    pair = ""

    if difference:
        all_tokens_temp.update(all_tokens)

        for elem in difference:
            pair = get_pool_name(elem)
            print(pair)

    return pair


def get_pool_name(pool_id):
    response = requests.get(f'https://api-osmosis.imperator.co/pools/v2/{pool_id}')

    if response:
        print('Ответ от сервера успешно получен!')
    else:
        print('В ходе осуществления запроса возникла ошибка.')

    json_response = response.json()
    pair = f"{json_response[0]['symbol']} / {json_response[1]['symbol']}"
    return pair


if __name__ == '__main__':
    check_pools()
