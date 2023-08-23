from NDLTD_System import Systems
import pandas as pd
from difflib import SequenceMatcher
import csv

dir = "./20230821_csv/"

# Iterate through all the systems' csv
# in each system's csv, iterate through each row
# iterate through each row in the original excel
# check if current row matches any of the row in the original excel (title and author should be similar)
# if no row matches, record this current row in a new excel

def comp(new_title, ori_title):
    return SequenceMatcher(None, new_title, ori_title).ratio()

my_systems = Systems()

df = pd.read_excel(dir + "docusky0821_with_citation.xlsx")
df = df.reset_index()

write_csv = dir + "add.csv"

write_f = open(write_csv, mode='w', newline='')
write_w = csv.writer(write_f)

for system in my_systems.elements:
    crawl_csv = dir + system.csv_name + ".csv"
    add_xlsx = dir + "add_" + system.csv_name + ".xlsx"
    crawl_f = open(crawl_csv)
    crawl_r = csv.reader(crawl_f)

    crawl_lst = list(crawl_r)

    for crawl_row in crawl_lst:
        found = False
        for df_index, df_row in df.iterrows():
            crawl_title = crawl_row[3]
            crawl_author = crawl_row[5]
            crawl_system = crawl_row[1]
            crawl_url = crawl_row[12]

            if comp(crawl_title, df_row['paper title研究文獻題名']) >= 0.8 and comp(crawl_author, df_row['metatags/author作者']) >= 0.6:
                found = True
                # 就算有，也要檢查系統有沒有涵蓋
                if crawl_system not in df_row['metatags/docclass中心系統']:
                    print("="*66)
                    print(df_row['filename'], df_row['paper title研究文獻題名'])
                    print("有在原資料庫裡，但是少標了資料庫系統：")
                    print(crawl_system)
                    print("\n")
                # 就算已經有了，檢查 URL 是否有列入
                if crawl_url != '' and df_row['metadata/URL.href'] == '':
                    print("="*66)
                    print(df_row["filename"], df_row['paper title研究文獻題名'])
                    print("有在原資料庫裡，但是缺少 URL:")
                    print(crawl_url)
                break
        if not found:
            write_w.writerow(crawl_row)

    crawl_f.close()

write_f.close()