import pandas as pd

df = pd.read_excel("docusky0821.xlsx")
df = df.reset_index()

for index, row in df.iterrows():
    # 如果此欄不為空，跳過
    if not pd.isna(row['metadata/title引用']):
        continue

    authors = row['metatags/author作者']
    year = row['metadata/year_for_grouping出版時間']
    title = row['paper title研究文獻題名']
    source = row['metadata/doc_source出版項/學校']
    compilation = row['metadata/compilation_vol卷期,頁次']
    url = row['metadata/URL.href']
    language = row['metadata/language文種']
    citation = ''

    # 根據語言來決定是哪種 citation 的格式
    if language in ["中文", "日文", "韓文"]:
        authors = authors.replace(";", "、")
        citation = authors + "（" + str(int(year)) + "）。" + title + "。" + source + "。"
        if not pd.isna(compilation):
            citation = citation + str(compilation) + "。"
        if not pd.isna(url):
            citation = citation + "取自網址：" + str(url)
    else:
        authors = authors.replace(";", ", ")
        citation = authors + "(" + str(int(year)) + "). " + title + ". " + source + "."
        if not pd.isna(compilation):
            citation = citation + " " + str(compilation) + "."
        if not pd.isna(url):
            citation = citation + " Retrieved from " + str(url)
    
    df.at[index, 'metadata/title引用'] = citation
    print(citation)
df.to_excel('docusky0821_with_citation.xlsx', sheet_name="sheet1", index=False)