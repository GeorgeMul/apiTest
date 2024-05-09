import time

from api.api import *
from common.common import *

# 以下打入做測試之後傳到最後crud做簡易統整
# 新增看板並且做測試
def step_create_board(name):
    res = create_board(name)
    assert res.status_code == 200
    assert res.json()['name'] == "hello1"
    time.sleep(0.5)
    Id = res.json()["id"]
    return Id

# 新增列表1並且做測試
def step_create_list1(boardId):
    res = create_list1(boardId)
    assert res.status_code == 200
    time.sleep(0.5)
    Id = res.json()["id"]
    return Id

# 新增列表2並且做測試
def step_create_list2(boardId):
    res = create_list2(boardId)
    assert res.status_code == 200
    time.sleep(0.5)
    Id = res.json()["id"]
    return Id

# 新增卡片並且做測試
def step_create_card(listID1):
    res = create_card(listID1)
    assert res.status_code == 200
    time.sleep(0.5)
    Id = res.json()["id"]
    return Id

# 更新卡片並且做測試
def step_update_card(listID2, cardId):
    res = update_card(listID2, cardId)
    assert res.status_code == 200
    time.sleep(0.5)
    return res

# 刪除卡片並且做測試
def step_delete_card(cardId):
    res = delete_card(cardId)
    assert res.status_code == 200
    time.sleep(0.5)
    return res

# 刪除看板並且做測試
def step_delete_board(boardId):
    res = delete_board(boardId)
    assert res.status_code == 200
    time.sleep(0.5)
    return res

# 檢查刊版並且做測試
def step_check_board(boardId):
    res = check_board(boardId)
    assert res.status_code == 404
    time.sleep(0.5)
    return res