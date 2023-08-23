import csv
from difflib import SequenceMatcher
dir = '/home/nomearod/DH work/cite/20230821_csv/'
origin_csv = dir + 'docusky0821.xlsx'
new_csv = dir + '66 DocuSky 數位人文學術研究平台.csv'
write_csv = dir + '66 add.csv'

ori_f = open(origin_csv)
ori_r = csv.reader(ori_f)

new_f = open(new_csv)
new_r = csv.reader(new_f)

write_f = open(write_csv, mode='w', newline='')
write_w = csv.writer(write_f)

ori_lst = list(ori_r)
new_lst = list(new_r)

def comp(new_title, ori_title):
    return SequenceMatcher(None, new_title, ori_title).ratio()

for n_r in new_lst:
    found = False
    for o_r in ori_lst:
        new_title = n_r[3]
        ori_title = o_r[3]

        new_author = n_r[5]
        ori_author = o_r[5]

        new_url = n_r[12]
        ori_url = o_r[12]

        new_system = n_r[1]
        ori_systems = o_r[1]

        # 如果是一樣的論文（名字相似且作者名稱相似）
        if comp(new_title, ori_title) >= 0.8 and comp(new_author, ori_author) >= 0.6:
            found = True
            # print("="*66)
            # print(o_r[0], ori_title)
            """if n_r[0] != o_r[0]:
                print("="*66)
                print(o_r[0], ori_title)
                print(n_r[0])
                print("wrong id!!!")
                """
            # 就算有，也要檢查系統有沒有涵蓋
            if new_system not in ori_systems:
                print("="*66)
                print(o_r[0], ori_title)
                print("有在原資料庫裡，但是少標了資料庫系統：")
                print(new_system)
                print("\n")
            # 就算已經有了，檢查 URL 是否有列入
            if new_url != '' and ori_url == '':
                print("="*66)
                print(o_r[0], ori_title)
                print("有在原資料庫裡，但是缺少 URL:")
                print(new_url)
                o_r[11] = "URL"
                o_r[12] = new_url
                o_r[13] = n_r[13]
                # write_w.writerow(o_r)
            break

    # 沒出現過，加到新清單裡
    if(not found):
        write_w.writerow(n_r)

ori_f.close()
new_f.close()
write_f.close()