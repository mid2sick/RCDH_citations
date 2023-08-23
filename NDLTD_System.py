class System:
    def __init__(self, id, name, req, csv_name):
        self.id = id
        self.name = name
        self.req = req
        self.csv_name = csv_name
        self.done = False
        pass

    def get_id(self):       # ex. 1
        return self.id

    def get_name(self):     # ex. "臺灣歷史數位圖書館"
        return self.name

    def get_req(self):      # ex. '("thdl" or "台灣歷史數位圖書館" or "臺灣歷史數位圖書館" or "Taiwan History Digital Library").rf'
        return self.req
    
    def get_csv_name(self): # ex. thdl
        return self.csv_name
    
    def set_done(self):
        self.done = True
    
    def is_done(self):
        return self.done

class Systems:
    def __init__(self):
        thdl = System(1, '臺灣歷史數位圖書館', '("thdl.ntu.edu.tw/THDL" or "台灣歷史數位圖書館" or "臺灣歷史數位圖書館" or "Taiwan History Digital Library").rf', '01 臺灣歷史數位圖書館')
        leis = System(2, '藝文類聚‧太平御覽', '("leishukis.digital.ntu.edu.tw" or "藝文類聚‧太平御覽").rf', '02 藝文類聚‧太平御覽')
        darc = System(4, '臺灣大學典藏數位化計畫', '("www.darc.ntu.edu.tw" or "臺灣大學典藏數位化計畫" or "台灣大學典藏數位化計畫").rf', '04 臺灣大學典藏數位化計畫')
        newnrch = System(5, '新版國家文化資料庫', '("newnrch.digital.ntu.edu.tw" or "新版國家文化資料庫").rf', '05 新版國家文化資料庫')
        tecom = System(6, '海外博物館臺灣民族學藏品資料', '("tecom.digital.ntu.edu.tw" or "海外博物館臺灣民族學藏品資料" or "Taiwan Ethnological Collection in Overseas Museums").rf', '06 海外博物館臺灣民族學藏品資料')
        leishu = System(7, '類書對應查詢系統', '("leishucis.digital.ntu.edu.tw" or "類書對應查詢系統").rf', '07 類書對應查詢系統')
        shakespeare = System(9, '臺灣莎士比亞資料庫', '("shakespeare.digital.ntu.edu.tw" or "臺灣莎士比亞資料庫" or "台灣莎士比亞資料庫" or "Taiwan Shakespeare Database").rf', '09 臺灣莎士比亞資料庫')
        cspis = System(10, '乾隆朝大清會典與則例對照檢索系統', '("cspis.digital.ntu.edu.tw" or "乾隆朝大清會典與則例對照檢索系統").rf', '10 乾隆朝大清會典與則例對照檢索系統')
        ssop = System(11, '清季職官表查詢系統', '("ssop.digital.ntu.edu.tw" or "清季職官表查詢系統").rf', '11 清季職官表查詢系統')
        ahonline = System(12, '國史館檔案史料文物查詢系統', '("ahonline.drnh.gov.tw" or "國史館檔案史料文物查詢系統").rf', '12 國史館檔案史料文物查詢系統')
        drtpa = System(13, '臺灣省議會史料總庫', '("drtpa.th.gov.tw" or "臺灣省議會史料總庫" or "台灣省議會史料總庫").rf', '13 臺灣省議會史料總庫')
        journal = System(14, '中華民國地方議會議事錄總庫', '("journal.th.gov.tw" or "中華民國地方議會議事錄總庫").rf', '14 中華民國地方議會議事錄總庫')
        buddhism = System(15, '佛學數位圖書館暨博物館', '("buddhism.lib.ntu.edu.tw" or "enlight.lib.ntu.edu.tw" or "ccbs.ntu.edu.tw" or "佛學數位圖書館").rf', '15 佛學數位圖書館暨博物館')
        kmt = System(16, '中國國民黨史料資料庫', '("中國國民黨史料資料庫").rf', '16 中國國民黨史料資料庫')
        chilin = System(17, '慈林教育基金會典藏臺灣社運史料資料庫', '("chilin.lib.ntu.edu.tw" or "慈林教育基金會典藏臺灣社運史料資料庫").rf', '17 慈林教育基金會典藏臺灣社運史料資料庫')
        tccra = System(18, '日治法院檔案資料庫', '("tccra.lib.ntu.edu.tw" or "日治法院檔案資料庫").rf', '18 日治法院檔案資料庫')
        tcsd = System(19, '臺灣日治時期統計資料庫', '("tcsd.lib.ntu.edu.tw" or "臺灣日治時期統計資料庫").rf', '19 臺灣日治時期統計資料庫')
        dl_photo = System(20, '臺灣舊照片資料庫', '("dl.lib.ntu.edu.tw/s/photo" or "臺灣舊照片資料庫").rf', '20 臺灣舊照片資料庫')
        ntur = System(21, '國立臺灣大學機構典藏', '("ntur.lib.ntu.edu.tw" or "國立臺灣大學機構典藏").rf', '21 國立臺灣大學機構典藏')
        ntu_archive = System(22, '臺灣大學網站典藏庫', '("webarchive.lib.ntu.edu.tw" or "臺灣大學網站典藏庫").rf', '22 臺灣大學網站典藏庫')
        thtc = System(25, '臺灣曆法查詢系統', '("thdl.ntu.edu.tw/datemap" or "臺灣曆法查詢系統" or "台灣曆法查詢系統").rf', '25 臺灣曆法查詢系統')
        sino_cloud = System(28, '古今圖書集成', '("www.sino-cloud.com.tw").rf', '28 古今圖書集成')
        judical = System(30, '司法院文化走廊', '("www2.judicial.gov.tw/culture/index.html" or "司法院文化走廊").rf', '30 司法院文化走廊')
        ming_qing = System(33, '明清婦女著作檢索系統', '("140.112.30.238/wws_test/view_poet.php" or "明清婦女著作檢索系統").rf', '33 明清婦女著作檢索系統')
        pingdong = System(35, '屏東縣志進階閱讀與標註系統', '("屏東縣志進階閱讀與標註系統").rf', '35 屏東縣志進階閱讀與標註系統')
        weight_measure = System(36, '度量衡單位換算系統', '("thdl.ntu.edu.tw/thdl_tool/weight_measure" or "度量衡單位換算系統").rf', '36 度量衡單位換算系統')
        crise = System(37, '教務雜誌索引檢索系統 CRISE', '("www.airiticri.com/index.php" or "140.112.114.9/cri/" or "Chinese Recoder Index Search Engine" or "教務雜誌索引檢索系統 CRISE").rf', '37 教務雜誌索引檢索系統 CRISE')
        ntu_acis = System(45, '臺灣大學人類學系藏品資料查詢系統', '("ntuacis.digital.ntu.edu.tw" or "臺灣大學人類學系藏品資料查詢系統").rf', '45 臺灣大學人類學系藏品資料查詢系統')
        ntu_museum = System(46, '臺灣大學博物館群', '("museum.ntu.edu.tw" or "臺灣大學博物館群").rf', '46 臺灣大學博物館群')
        itdels = System(48, '臺灣法實證研究資料庫—法律文件資料庫', '("itdels.digital.ntu.edu.tw" or "臺灣法實證研究資料庫—法律文件資料庫" or "臺灣法實證研究資料庫，法律文件資料庫").rf', '48 臺灣法實證研究資料庫—法律文件資料庫')
        tadels_image = System(49, '臺灣法實證研究資料庫—法律影像資料庫', '("tadels.law.ntu.edu.tw/image-info" or "臺灣法實證研究資料庫—法律影像資料庫" or "臺灣法實證研究資料庫，法律影像資料庫").rf', '49 臺灣法實證研究資料庫—法律影像資料庫')
        core = System(50, '臺灣核心文獻資料庫', '("臺灣核心文獻資料庫").rf', '50 臺灣核心文獻資料庫')
        suzhou = System(59, '蘇州碼轉換器', '("thdl.ntu.edu.tw/suzhou/").rf', '59 蘇州碼轉換器')
        ctb = System(60, '清代臺灣文官官職表查詢系統', '("ctb.digital.ntu.edu.tw/" or "清代文官官職表查詢系統" or "清代臺灣文官官職表查詢系統").rf', '60 清代臺灣文官官職表查詢系統')
        thdl_termpat = System(61, 'THDL 前後綴詞分析工具', '("thdl.ntu.edu.tw/SimpleTools/TermPat/TermPatSimpleUI.php" or "THDL前後綴詞分析工具").rf', '61 THDL 前後綴詞分析工具')
        danxin = System(65, '淡新檔案訴訟關係圖', '("淡新檔案訴訟關係圖").rf', '65 淡新檔案訴訟關係圖')
        docusky = System(66, 'DocuSky 數位人文學術研究平台', '("docusky.org.tw" or "DocuSky 數位人文學術研究平台").rf', '66 DocuSky 數位人文學術研究平台')
        self.elements = [thdl, leis, darc, newnrch, tecom, leishu, shakespeare, cspis, 
                        ssop, ahonline, drtpa, journal, buddhism, kmt, chilin, tccra, tcsd,
                        dl_photo, ntur, ntu_archive, thtc, sino_cloud, judical, ming_qing,
                        pingdong, weight_measure, crise, ntu_acis, ntu_museum, itdels, tadels_image,
                        core, suzhou, ctb, thdl_termpat, danxin, docusky]

    
    def set_done_by_names(self, *system_names):
        for system_name in system_names:
            for sys in self.elements:
                if(sys.get_name() == system_name):
                    sys.set_done()
                    print("yes: ", sys.get_name())
                else:
                    print("nope: ", sys.get_name())
    
    def set_done_by_ids(self, *system_ids):
        for system_id in system_ids:
            for sys in self.elements:
                if(sys.get_id() == system_id):
                    sys.set_done()