# 引用資料爬蟲程式
## 1. crawl_NDLTD.py
- 爬博碩士論文網的資料，會得到 csv 檔
- 使用方法
```bash=
python3 crawl_NDLTD.py
```
- 如果有些資料庫已經爬過了，可以用下列其中一個 function 去紀錄，這樣爬的時候就會跳過這些資料庫。
```bash=
my_systems.set_done_by_names('System name')
my_systems.set_done_by_ids(1, 2, ...)
```

## 2. find_new_records.py
- 爬完博碩士論文網後（csv 檔），要跟現有的引用資料（xlsx 檔）比對，留下爬出來的資料裡面的新的部份（得到 add.csv 這個檔案）
- 使用方法
```bash=
python3 find_new_records.py
```
至於 find_new_records_old.py 跟這個很像，只是引用資料也是 csv 檔，然後是只有針對指定系統去比對

## 3. createCitation.py
- 如果「metadata/title引用」一欄為空，自動生出該欄
- 使用方法
```bash=
python3 createCitation.py
```
- 沒有依照 APA 、MLA、CHICAGO 等標準引用格式去 format 出這欄