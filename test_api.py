# 引入模塊
from wsgiref import headers

import requests
import pytest

# ENV
domain_boards = "https://api.trello.com/1/boards"
domain_card = "https://api.trello.com/1"
apiKey = "5381a5e1cc832bee54b23d4b0d800376"
apiToken = "ATTA40817ab1c421b154cb67b4d308541767ca71f9f60471bef8b72d59616e22300fC6D216A4"


# pytest 指定執行方法需使用function
def create_board():
    name = "e04"
    params = {
        "name": name,
        "key": apiKey,
        "token": apiToken
    }
    res = requests.post(url=domain_boards, params=params)
    assert res.status_code == 200
    assert res.json()["name"] == name
    id = res.json()["id"]
    return id


# 新增List1
def create_list1(board_id):
    name = "fuk"
    params = {
        "name": name,
        "key": apiKey,
        "token": apiToken
    }
    url = f"{domain_boards}/{board_id}/lists"
    res = requests.post(url=url, params=params)
    assert res.status_code == 200
    assert res.json()["name"] == name
    listId1 = res.json()["id"]
    return listId1

# 新增list2
def create_list2(board_id):
    name = "fuk2"
    params = {
        "name": name,
        "key": apiKey,
        "token": apiToken
    }
    url = f"{domain_boards}/{board_id}/lists"
    res = requests.post(url=url, params=params)
    assert res.status_code == 200
    Id = res.json()["id"]
    return Id

#新增卡片
def create_card(list_id):
    name = "i want to get rich"
    params = {
        "name": name,
        "key": apiKey,
        "token": apiToken,
        "idList": list_id
    }
    headers = {
        "Accept": "application/json",
    }
    url = f"{domain_card}/cards"
    res = requests.post(url=url, params=params, headers=headers)
    assert res.status_code == 200
    Id = res.json()["id"]
    return Id

# 更換卡片位置
def update_card(list_id2, card_id):
    name = "very"
    params = {
        "name": name,
        "key": apiKey,
        "token": apiToken,
        "idList": list_id2
    }
    headers = {
        "Accept": "application/json"
    }
    url = f"{domain_card}/cards/{card_id}"
    res = requests.put(url=url, params=params, headers=headers)
    assert res.status_code == 200

# 刪除卡片
def delete_card(card_Id):
    params ={
        "key": apiKey,
        "token": apiToken
    }
    url = f"{domain_card}/cards/{card_Id}"
    res = requests.delete(url, params=params)
    assert res.status_code == 200

# 刪除看板

def delete_board(board_id):
    params ={
        "key": apiKey,
        "token": apiToken
    }
    url = f"{domain_boards}/{board_id}"
    res = requests.delete(url, params=params)
    assert res.status_code == 200

#檢查看板
def check_board(board_id):
    params ={
        "key": apiKey,
        "token": apiToken
    }
    url = f"{domain_boards}/{board_id}"
    res = requests.get(url, params=params)
    assert res.status_code == 404

# 最終執行
def test_exceute():
    board_id = create_board()
    list_id = create_list1(board_id)
    list_id2 = create_list2(board_id)
    card_id = create_card(list_id)
    update_card(list_id2, card_id)
    delete_card(card_id)
    delete_board(board_id)
    check_board(board_id)