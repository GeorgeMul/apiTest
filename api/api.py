import common.common
from common.common import *
from step.step_board import *



config = ConfigParser()

# 用來讀取ini檔
# 取得根目錄
BasePath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 取得根目錄中env檔案
AccountSettingPath = os.path.join(BasePath, "config", 'env.ini')
# 如果是用config讀取就讀取上面的路徑
config.read(AccountSettingPath)

# 來自env要有section/key
boards_config = config.get('env_config', 'domain_boards')
card_config = config.get('env_config', 'domain_card')
api_key = config.get('env_config', 'apiKey')
api_token = config.get('env_config', 'apiToken')
header_config = config.get('env_config', 'headers')


# 以下打入所有所需數據的api並傳到step_board做測試
def create_board(name):
    name = name
    params = {
        "name": name,
        "key": api_key,
        "token": api_token
    }
    res = requests.post(url=boards_config, params=params)
    return res

def create_list1(boardId):
    name = "hi1"
    params = {
        "name": name,
        "key": api_key,
        "token": api_token
    }
    url = f"{boards_config}/{boardId}/lists"
    res = requests.post(url=url, params=params)
    return res

def create_list2(boardId):
    name = "hi2"
    params = {
        "name": name,
        "key": api_key,
        "token": api_token
    }
    url = f"{boards_config}/{boardId}/lists"
    res = requests.post(url=url, params=params)
    return res

def create_card(listID1):
    name = "i want to get rich"
    params = {
        "name": name,
        "key": api_key,
        "token": api_token,
        "idList": listID1
    }
    headers = {
        "Accept": "application/json",
    }
    url = f"{card_config}/cards"
    res = requests.post(url=url, params=params, headers=headers)
    return res

def update_card(listID2, cardId):
    name = "very"
    params = {
        "name": name,
        "key": api_key,
        "token": api_token,
        "idList": listID2
    }
    headers = {
        "Accept": "application/json"
    }
    url = f"{card_config}/cards/{cardId}"
    res = requests.put(url=url, params=params, headers=headers)
    return res

def delete_card(cardId):
    params ={
        "key": api_key,
        "token": api_token
    }
    url = f"{card_config}/cards/{cardId}"
    res = requests.delete(url=url, params=params)
    return res

def delete_board(boardId):
    params ={
        "key": api_key,
        "token": api_token
    }
    url = f"{boards_config}/{boardId}"
    res = requests.delete(url, params=params)
    return res

def check_board(boardId):
    params ={
        "key": api_key,
        "token": api_token
    }
    url = f"{boards_config}/{boardId}"
    res = requests.get(url, params=params)
    return res