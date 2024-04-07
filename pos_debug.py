import cv2
import numpy as np

from GameHelper import GameHelper

img_path = "D:/work/git/DouZero_For_HLDDZ_FullAuto/Snipaste/Snipaste_2024-04-02_13-49-38.png"

capture_pos = [
            #    (180, 530, 1050, 90,'MyHandCardsPos'),    # 我的手牌截图区域
            #    (180, 390, 1050, 90,'MPlayedCardPos'),  # 我的截图区域
            #    (225, 240, 400, 120,'LPlayedCardsPos'),    # 玩家上家区域
            #    (820, 240, 400, 120,'RPlayedCardsPos'),   # 玩家下家区域
            #    (112, 248, 22, 61,'LLandlordFlagPos'),   # 地主标志区域(玩家上家)
            #    (111, 705, 22, 61,'MLandlordFlagPos'),    # 地主标志区域(玩家)
            #    (1300, 248, 22, 61,'RLandlordFlagPos'),    # 地主标志区域(玩家下家)
            #    (700, 53, 110, 53, 'ThreeLandlordCardsPos'),      # 地主底牌区域
            #    (230, 270, 115, 52, 'LPassPos'),                    #左边不出截图区域
            #    (1110, 270, 115, 52, 'RPassPos'),                    #右边不出截图区域
            #    (659, 449, 115, 52, 'MPassPos'),                    #我的不出截图区域
            #    (200, 390, 1000, 120, 'PassBtnPos'),                 #要不起截图区域
            #    (200, 390, 1000, 120, 'GeneralBtnPos'),               #叫地主、抢地主、加倍按钮截图区域
            #    (145, 365, 30, 36, 'Lblue_cards_num'),               #加倍阶段上家和下家的牌数显示区域
            #    (1267, 365, 30, 36, 'Rblue_cards_num'),               #加倍阶段上家和下家的牌数显示区域

               (700, 53, 110, 53, 'LandlordCardsPos'),
               (1275, 758, 99, 33, 'chat'),
               (670, 190, 97, 125, 'laotou'),
               (502, 437, 150, 38, 'LimitStartBtn')
               ]

# 窗口截图
# helper = GameHelper()
# image, _ = helper.Screenshot()
# image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)

# 加载截图
image = cv2.imread(img_path)

for pos in capture_pos:
    image = cv2.rectangle(image, pos[0:2], (pos[0] + pos[2], pos[1] + pos[3]), (0, 0, 255), 3)
    image = cv2.putText(image, pos[4], pos[0:2], cv2.FONT_HERSHEY_COMPLEX, 1, (128, 128, 128), 2, cv2.LINE_AA)

# cv2.namedWindow("test", 0)
cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()