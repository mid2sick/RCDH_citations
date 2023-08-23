from NDLTD_System import Systems
from functions import *
import os

csvDir = './20230821_csv/'
if not os.path.isdir(csvDir):
    os.mkdir(csvDir)

my_systems = Systems()
# my_systems.set_done_by_names('臺灣歷史數位圖書館', '臺灣大學典藏數位化計畫', '新版國家文化資料庫')
# my_systems.set_done_by_ids(1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 28, 30, 33, 35, 36, 37, 45, 46, 48, 49, 50, 59, 60, 61, 65, 66)
cnt_all = 0

for system in my_systems.elements:
    if system.is_done():
        continue
    cnt_all = crawlOneSystem(system, csvDir, cnt_all)
    print("crawled: ", cnt_all)