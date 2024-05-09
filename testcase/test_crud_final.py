from step.step_board import *
from common.common import *

# 讀取 YAML 檔案並將其轉換為 Python 對象
file_path = os.path.join(os.path.dirname(__file__), "../data/data.yaml")
with open(file_path, 'r') as stream:
    data = yaml.safe_load(stream)

# 從 Python 對象中獲取需要的測試參數
list = data['board_name']


# 用pytest裝飾器導入看板名稱做以下測試,執行下列即可全部測試
@pytest.mark.parametrize("name", list)
def test_list(name):
    boardId = step_create_board(name)
    listID1 = step_create_list1(boardId)
    listID2 = step_create_list2(boardId)
    cardId = step_create_card(listID1)
    step_update_card(listID2, cardId)
    step_delete_card(cardId)
    step_delete_board(boardId)
    step_check_board(boardId)
# 將得到的數據給一個變數回傳到api做後續測試



