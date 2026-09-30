const fs = require('fs');
const path = require('path');

const targetHtml = path.join(__dirname, 'proposal.html');

// We will construct both:
// 1. The rich interactive HTML content
// 2. The full plain-text markdown version for the copyBuffer

const plainMarkdown = `# 【六年級獨立研究專題】《雙北漫遊偵探：都會行蹤》完整遊戲設計企劃書（新版合併深度版）
專案團隊：國小六年級獨立研究小組（三人團隊）
遊戲類型：1:1 雙北開放世界推理探究 RPG (Open-World Detective RPG / Edu-Puzzle)
目標平台：Web 網頁端（靜態託管隨點即玩，支援電腦鍵盤與手機觸控，部署於 GitHub Pages / Itch.io）

============================================================
【⚖️ 重要學術研究、非商業用途與版權合規聲明】
============================================================
1. 非商業學術研究性質：
   本企劃書及後續開發之網頁遊戲，為國小六年級學生「獨立研究」課程之跨學科程式教育與文史科學探究成果，絕無任何商業營利、收費、贊助或販售行為。
2. 虛構榮譽與無官方贊助澄清：
   企劃內所提及之「新北市/台北市政府生活流通金獎勵」、「市警局榮譽顧問勳章」等內容，純屬遊戲世界觀之「虛構劇情榮譽與數值獎勵」，絕非真實政府單位或警察局之官方背書或贊助。
3. 名著機關、商標與音效之合理使用與原創化：
   專案中引用與致敬之《名偵探柯南》、《福爾摩斯探案集》經典密碼與科學手法，以及雙北真實地標與大眾運輸系統（台北捷運、市區公車、YouBike 2.0），皆屬國小課程教學與學術探究之合理使用（Fair Use）。若公開發布上線，所有動漫人物外觀、插畫、UI 貼圖、捷運四語廣播與環境音樂，將全部由團隊原創繪製與錄製，不直接挪用受版權保護之動畫商業素材與官方錄音。
4. 嚴謹求實原則：
   刪除所有「保證全場最高分」等過度保證之宣傳詞，所有科學原理（投影/反射、聲學延遲、弱酸炭化）與在地史實皆通過嚴謹查證與修正。

============================================================
■ 01｜專案基本定位、核心精神與三人團隊深層分工
============================================================
【一句話定位】
《雙北漫遊偵探：都會行蹤》是一款以雙北為舞台的開放式探索推理遊戲：街區是連續的遊戲空間，案件是可選的冒險，學習內容藏在場所與微型互動裡。它不是只有四個封閉關卡、通關即結束的解謎遊戲，而是一座世界隨時持續運轉的城市。

【核心理念與玩家體驗】
- 自由漫遊：玩家在原地操作角色，不必真的到現場；可以辦案，也可以不照主線走，去任何想去的街區探索、進建築、學東西、找彩蛋。
- 案件有結局，世界無終點：即使某個大案被破案歸檔，玩家依然可以繼續在雙北生活、打工、漫遊、拍照、或等待下一批新案件發生。
- 最重要設計原則：玩家自己決定下一站！新手教學不綁死固定動線，故事提供指引但不鎖死城市探索權限。每個可進入的地點至少具備「一項可互動的知識、一個觀察亮點、一個人物對話、一條線索或一個驚喜彩蛋」，絕不做空殼建築。

【三人研究團隊深度職責規劃】
1. 組員 1（組長 / 企劃總監）：
   - 世界觀設定、主支線劇本主筆與對話撰寫。
   - 研讀《名偵探柯南》與《福爾摩斯》經典案件，進行本土化科學與密碼機關改編。
   - 負責每案破案後「名著考據卡」與「微型知識講堂」內容撰寫，確保符合國小自然與社會課綱。
2. 組員 2（美術與圖資總監）：
   - 3D 俯瞰視角街景視覺標準制定，繪製 2D 復古像素角色、NPC 與雙北特色小吃道具。
   - 考察真實雙北地理，使用 OpenStreetMap (OSM) 開放圖資建立 1:1 道路尺度與建築外觀。
   - 負責授權素材清單盤點，確保全專案圖像與符號均符合開源協議（ODbL）與原創規範。
3. 組員 3（技術架構與機制總監）：
   - 規劃 3D/2D 混合引擎、WASD/行動端觸控操作、雙軌經濟數值平衡（破案賞金與生活流通金）。
   - 設計真實大眾交通費率演算法（公車段次緩衝區、捷運真實里程矩陣、YouBike 前 30 分鐘補助）。
   - 規劃伺服器端「共享世界唯一首解原子鎖定」與資料庫存檔規格，主導 AI 協同開發與全班測試。

============================================================
■ 02 & 02A｜雙北連續世界、1:1 地理與真實大眾交通費率建模
============================================================
【1:1 現實地理結構】
- 地圖基礎：基於台北市與新北市真實道路、橋梁、河川、行政區、公車站牌、捷運路網與相對距離建模。
- 連續世界（非傳送門）：跨區不是瞬間切換黑畫面傳送，玩家可以沿著真實道路（如中正橋、台北橋、忠孝西路、新店溪沿岸）跨越行政區界步行，完全不設行政區步行空氣牆。
- 圖資規範：圖資採用 OpenStreetMap (OSM) 道路/建物向量開放資料與交通部公車開放資料（PTX/TDX）。嚴格遵守 ODbL 授權要求，不抓取商業 Google 地圖磚或未授權商業街景。

【多元大眾交通網絡與精確費率】
1. 步行 (Walking)：
   - 免費、無限制！玩家隨時可沿著雙北所有連通街道與人行道跨區漫遊。
2. 市區公車（主要大眾運輸工具）：
   - 走雙北真實路線、站牌與分段點。全票每段次 15 元遊戲內生活金。
   - 跨越分段點或在緩衝區內依現實規則計費（一段票 15 元、跨緩衝區加收 15 元變兩段票 30 元）。
3. 台北捷運 (Taipei Metro)：
   - 按真實站間票價查詢表精確扣款（單程票 20 元～65 元不等），嚴禁使用「直線距離胡亂猜測」。
   - 車站出入口、轉乘動線與到站廣播均忠實呈現。
4. YouBike 2.0 公共自行車：
   - 按租借站點與實際騎乘時間累進扣款：4 小時內每 30 分鐘 10 元；4~8 小時每 30 分鐘 20 元；超過 8 小時每 30 分鐘 40 元（未滿 30 分鐘以 30 分鐘計算）。
   - 會員優惠政策：符合台北市與新北市會員借車「前 30 分鐘免費補助」政策，生活金不足時可善用免費額度短程代步。
5. 交通路徑規劃器：
   - 點擊地圖目的地時，內建手機 App 會自動列出「步行（花費 0 元，耗精力多）」、「公車（花費 15 元，耗時短）」與「捷運（花費 25 元，準點直達）」三種對比方案，由玩家自主抉擇。

【時間、日夜與動態氣象雙軌制】
- 氣象連動：串接中央氣象署（CWA）API 每 15 分鐘更新一次雙北天氣，雨天街道泛起雨絲水窪、NPC 撐傘、地面浮現泥濘鞋印與雨傘滴水等限定線索。
- 雙軌防卡關設計：
  * 「離線預設模式」：API 斷線或本機遊玩時自動進入穩定預設晴天/陰雨循環。
  * 「案件專屬時間軸」：案件內部時間可隨線索調查自由調整（例如推移至嫌犯作案的雨夜），與現實世界時間解耦，防止玩家因為現實連續數天晴天而卡關無法解雨天謎題！

============================================================
■ 03｜玩家遊玩流程：新手前 15 分鐘到長期探索循環
============================================================
【新手前 15 分鐘流暢引導】
1. 醒來與角色創建：玩家在自己的偵探事務所（大稻埕或西門町老街閣樓）甦醒，學會 WASD 走動、調查物件、開啟偵探手機。
2. 門口無門檻失物委託：事務所門口鄰居老爺爺遺失了鑰匙，無任何金錢或精力門檻：
   - 觀察花盆旁的刮痕 ➔ 向兩名路人 NPC 詢問 ➔ 在線索白板連結時間戳 ➔ 找出鑰匙被烏鴉叼到樹上的真相。
3. 獎勵與自由啟航：獲得初始生活金 100 元、第一張「密碼鑑識知識卡」與一張雙北地圖。
4. 自主決定下一站：地圖同時點亮「前往科教館聽講堂」、「前往台北車站接取大案」、或「前往淡水老街吃阿給散步」，由玩家完全自主選擇，絕無強迫推線！

【長期每一次遊玩的循環 (The Gameplay Loop)】
選擇目標（自由漫遊 / 接取委託）➔ 規劃路線（步行 / 公車 / 捷運 / YouBike）➔ 到達現場（觀察環境 / 對話調查 / 進館學習）➔ 整理線索簿（比對時間線 / 破解經典機關）➔ 提交推理獲得獎勵與名著考據卡 ➔ 回到城市繼續慢活、佈置事務所、探索下一個街區。

============================================================
■ 04｜案件、線索簿與四大名著機關（嚴謹科學與史實糾錯升級版）
============================================================
【標準案件設計規範】
- 委託背景：清楚交代人物動機與事件起源，不僅限於重大犯罪，亦涵蓋文物尋寶、歷史誤會、城市怪談。
- 線索簿多軌分類：將「現場證物」、「證人證言」、「監視器時間戳」、「未證實之八卦」分開記錄，玩家可將兩條線索拖曳連線產生新推論。
- 非懲罰性答錯回饋：推理錯誤時給予引導性反思提示（例如「嫌犯若在此時出現，那路口的垃圾車音樂怎麼解釋呢？」），絕不直接遊戲失敗或扣光金錢。

【四大經典機關本土化深度改編與嚴謹糾錯】

1. 淡水紅毛城 ✕ 福爾摩斯〈跳舞的小人〉（密碼替換與港埠文史）：
   - 調查舞台：淡水港近代歷史主題場景（明確標註：紅毛城真實古蹟內部無秘密地牢石室，此為融合淡水海關開港文史之虛構改編場景）。
   - 機關解法：石壁刻有 26 塊不同姿勢的跳舞小人符號（手持旗幟者代表單詞結尾）。玩家調閱淡水海關稅務司公署遺留的英文航海日誌，透過英文字母頻率分析（E 最常出現）並結合上下文單詞拼讀，解出暗格密碼，獲得百年航海懷錶。
   - [名著考據卡]：
     * 原著出處：亞瑟·柯南·道爾 1903 年《福爾摩斯探案集：歸來記》之〈跳舞的人〉(The Dancing Men)。
     * 密碼學原理：單表替換式密碼 (Substitution Cipher) 與字元頻率分析法。
     * 在地歷史：淡水港於 1862 年正式開港通商，英國在此設立領事館，具有濃厚 19 世紀海洋貿易文史背景。

2. 北投溫泉會館 ✕ 名偵探柯南理科加熱顯影（弱酸脫水炭化與安全警語）：
   - 調查舞台：北投溫泉鄉虛構老字號旅店湯屋（明確標註：安全警語！北投天然青磺泉水溫高達 80°C~100°C 具危險性，嚴禁在現實中模仿靠近高溫溫泉槽或操作危險化學品）。
   - 機關解法：現場留下一張看似全白的遺書信紙。玩家使用道具「防熱竹夾」將紙張置於安全溫控的蒸氣顯影槽上方微溫烘烤，紙張上的稀檸檬汁（弱酸）受熱脫水，使纖維素炭化變黑，顯現出隱藏的保管箱號碼。
   - [名著考據卡]：
     * 原著出處：《名偵探柯南》經典理科密室（如第 74 卷「毒與幻的設計」及早期利用溫差顯影手法）。
     * 科學原理：熱敏有機酸脫水反應（稀酸在水分蒸發後濃度升高，在受熱條件下奪取紙張纖維水分使碳析出變褐色）。嚴格區分單一可驗證化學反應，不把酸炭化、氯化鈷吸水變色與硫磺氣體混為一談。
     * 在地特色：北投為台灣知名地熱溫泉之鄉，以此場景引導學生認識地熱能源與日常熱敏化學知識。

3. 台北車站地下街 ✕ 柯南〈霧天狗傳說〉建築聲學（虹吸定時重力傾倒與回聲定位）：
   - 調查舞台：台北車站地下街與三鐵共構連通長廊。
   - 機關解法：嫌犯宣稱案發時自己正在 300 公尺外的商店購物，警衛證實於 14:30 聽到走廊傳來巨響。玩家調查發現嫌犯利用密閉水桶與彎曲軟管製成「虹吸定時蓄水傾倒裝置」，在案發 30 分鐘後蓄水滿溢失衡倒塌製造巨響！
   - [重要科學糾錯]：
     * 造成 30 分鐘不在場證明的是「水力虹吸裝置延遲 30 分鐘才傾倒」，絕非聲波在長廊走了 30 分鐘！（常溫下聲速約 340 m/s，傳播 300 公尺僅需 0.88 秒，不到一秒即達）。
     * 長廊光滑水泥壁造成的「多重聲波反射與回聲」，在案件中是用來「混淆聲音來源方向」，使證人無法精確辨別發聲位置。玩家比對監視器水漬時間戳與物理聲速，徹底粉碎不在場證明！
   - [名著考據卡]：
     * 原著出處：《名偵探柯南》經典特別篇〈霧天狗傳說殺人事件〉（利用水力與虹吸原理製造時間差手法）。
     * 物理學原理：大氣壓力、虹吸原理（Siphon Principle）與建築聲學回聲反射（Acoustic Reflection）。

4. 板橋林家花園 ✕ 福爾摩斯〈馬斯格雷夫禮儀〉（八角漏窗日影投影與幾何比例）：
   - 調查舞台：國定古蹟板橋林本源園邸（汲古書屋與方鑑齋）。
   - 機關解法：尋寶古詩記載「日照方鑑秋水清，八角漏窗投影長」。玩家利用庭園幾何量測儀，根據當季太陽高度角與相似三角形比例（影長 / 物高 = 比例常數），在日影投影至假山石縫的精確焦點處找出暗藏的古銅鑰匙。
   - [重要科學與史實糾錯]：
     * 光線穿過漏窗投在牆面上是「日影幾何投影 (Shadow Projection)」，陽光照在水池上被映照至屋簷則是「反射 (Reflection)」，兩者均非「折射 (Refraction)」。
     * 刪除「午後三刻直接等於 15:00」的不嚴謹古今對應，改以明確的「太陽方位角 240°、高度角 35°」幾何比例方程式進行科學解算。
   - [名著考據卡]：
     * 原著出處：亞瑟·柯南·道爾《福爾摩斯探案集：回憶錄》之〈馬斯格雷夫禮儀〉(The Musgrave Ritual)。
     * 數學幾何原理：相似三角形定理 (Similar Triangles) 與日晷太陽高度角日影幾何測量。
     * 在地美學：林本源園邸為台灣現存最完整的清代江南園林，其花磚漏窗與水榭倒影展現了精湛的傳統建築工藝。

============================================================
■ 04A｜共享世界體系：全服唯一首解、案件生命週期與競速機制
============================================================
【全服唯一首解 (First-Solver Glory)】
- 一個持續運轉的真實雙北：所有玩家登入同一個在線城市，重大疑案以「全伺服器共用狀態」發布。
- 案件生命週期：
  [未公布] ➔ [分批公開/案件發生] ➔ [調查中 (全服競速)] ➔ [被成功解開 / 限時到期] ➔ [結案歸檔 (轉為不計分回顧)]。
- 嚴格原子鎖定防作弊：
  * 首解認定必須是向伺服器提交「完整且正確的推理鏈條（包含作案動機、關鍵物證、手法破解）」，依伺服器時間戳與交易序號判定唯一首解者。
  * 伺服器端採用 Transaction Atomic Lock，若兩名玩家相差數毫秒提交，系統精確判定毫秒先後，絕不產生「雙首解重複發獎」衝突。
  * 首解誕生瞬間，全服發布「號外快訊！知名神探已破獲此案！」，正在查案的其他玩家線索簿自動更新通知。
- 結案後不計分模式：
  * 錯過首解的玩家依然可以在「歷史檔案室」免費載入該案件，親自走訪現場體驗完整的劇本與機關解密，但不再重複發放大量破案獎金與全服首解排位，維護公平性與持續遊玩價值。

============================================================
■ 05｜場所互動、短時微型學習手冊與台味隱藏彩蛋
============================================================
【把學習做成 1~3 分鐘微型互動（拒絕枯燥講義）】
- 規範標準四欄位：每個可進入建築均建立【看見什麼 / 做什麼 / 學到什麼 / 與哪個案件相關】標準規格：
  1. 台灣科學教育館（士林）：
     - 互動：操作安全的虛擬光影折射台與熱敏顯影模擬槽（2 分鐘）。
     - 收穫：解鎖「鑑識物理化學知識卡」，在北投溫泉案件中可直接調出熱敏公式。
  2. 台北市立圖書館總館（大安）：
     - 互動：古典密碼字母頻率分析練習小遊戲（3 分鐘）。
     - 收穫：解鎖「密碼速查表」，淡水紅毛城案件中自動標註字母出現次數。
  3. 淡水海關公署故事館（淡水）：
     - 互動：判讀 1860 年代英國商船航海日誌與海關進出口稅單（2 分鐘）。
     - 收穫：獲得淡水開港歷史知識，解鎖老船長隱藏文史對話。
  4. 新北市立圖書館總館（板橋）：
     - 互動：日晷測時法與相似三角形影子長度測量模擬器（2 分鐘）。
     - 收穫：獲得板橋林家花園日影投影之幾何比例量角器。

【雙北古蹟文史集章冊 (Stamp Rally)】
- 走訪淡水紅毛城、北投溫泉博物館、板橋林家花園、台北北門等古蹟，在虛擬拓印台蓋下復古像素章。
- 集滿 4 枚章解鎖遊戲內虛構榮譽「文史好學者徽章」與虛擬生活金獎勵（清楚標註為遊戲內數值，非政府贊助）。

【四大台味與致敬驚喜彩蛋 (Easter Eggs)】
1. 創作團隊客串彩蛋：台北車站巷弄豆漿店角落，坐著三位六年級獨立研究學生 NPC，筆電螢幕上開著這份企劃書，熱烈討論 AI 程式碼與測試進度！
2. 淡水老街黑貓「阿巧」：在淡水紅磚巷弄餵牠吃一顆魚丸，阿巧會喵喵叫帶你穿過防空洞，指引出牆面上的隱藏經緯度座標。
3. 台北 101 屋頂秘密展望台：完成特定支線後獲得天台鑰匙，夜晚登上 101 俯瞰整座大台北 3D 璀璨燈火與星空。
4. 名著致敬站牌貼紙：某個不起眼的公車站牌下方，悄悄貼著寫有「221B 貝克街」與「米花町五丁目」的復古公車路線貼紙。

============================================================
■ 06｜生活慢活、偵探精力值、雙軌貨幣與無障礙防卡關機制
============================================================
【偵探精力值系統 (Stamina System)】
- 奔跑、搜查現場消耗精力值。精力過低時角色轉為慢速散步、暫時無法進行深度推理解謎，但「絕對不會連回家或求助都做不到」。
- 事務所沙發休息、免費飲水機可免費回滿基本精力；亦可走進小吃店品嚐在地美食回血：
  * 淡水渡船頭小吃：淡水阿給 + 魚丸湯（精力回滿，獲得 3 分鐘海風輕快 Buff）。
  * 北投老街食堂：排骨酥麵 + 溫泉蛋（精力回滿，解謎時出現輔助提示光圈）。
  * 雙北連鎖手搖飲：珍珠奶茶（回補 40% 精力，短時間移速提升 30%）。
  * 台北巷弄早餐店：永和豆漿 + 燒餅夾蛋（平價充飢，隨時補充基礎精力）。

【雙軌貨幣體系 (Dual-Currency Economy)】
1. 貨幣 1：破案委託賞金 (Detective Coins / 偵探徽幣)
   - 獲取途徑：成功偵破主支線大案、解開名著經典機關、達成無提示解謎成就。
   - 專屬用途：在「名偵探高階行」購買永久專業加速裝備（微距放大鏡、紫外光燈、極速滑板）與限定外觀（福爾摩斯風衣、柯南西裝）。
   - 定位：象徵推理破案成就，專門用於永久加速遊戲進程。
2. 貨幣 2：日常生活流通金 (Daily Cash / 悠遊卡現金)
   - 獲取途徑：每日事務所基礎生活津貼、街頭小幫手委託（尋找遺失物/走失寵物）、超商兼職打工、或將破案賞金兌換成生活現金。
   - 專屬用途：支付公車捷運車資、購買超商破案消耗耗材（防熱竹夾、電池組）、吃小吃回精力。
   - 定位：重現真實生活感，體驗現代城市生活的細膩運作。

【無障礙防卡死機制 (Anti-Softlock Design)】
- 絕對不卡死設計：即使生活金花光，玩家依然可以免費步行、在事務所免費休息、或在街頭幫忙做資源回收賺取基礎車資。
- 三階段漸進防卡關提示：
  * 第 1 階（免費）：提示現場關鍵物證觀察方向。
  * 第 2 階：提示邏輯矛盾與破綻（可花費少量生活金，亦可選擇「等待 5 分鐘計時」或「完成指定環境觀察」免費解鎖）。
  * 第 3 階：直接引導具體操作步驟公式（同上，具備免費等待解鎖途徑），徹底避免玩家因沒錢而永久卡死！

【個人基地、相機與在地聲效體驗】
- 事務所生活：擺放案情紅線軟木板、更換偵探服裝、泡茶放空。
- 隨身拍立得相機：按 [C] 鍵隨時開啟取景框拍下街景、夕陽與現場證物，相片可自由釘在事務所案情牆上。
- 復古收音機多頻道：頻道 A【午後淡水 Lo-Fi】、頻道 B【台北雨季白噪音】、頻道 C【警廣虛構即時路況與失物播報】。
- 垃圾車音樂推理結合：嫌疑人電話通話中錄到微弱的《少女的祈禱》垃圾車音樂，比對各里垃圾車時刻表推算出嫌疑人真實所在巷弄！

============================================================
■ 07｜城市動態 NPC 作息、社區信賴度與班級案件工作坊
============================================================
【NPC 動態作息與多時段情報】
- 晨間 (06:00~09:00)：公園晨運長輩、早餐店人潮。
- 午間 (11:30~14:00)：上班族覓食、排隊小吃。
- 夜間 (17:00~21:00)：夜市開張、巡邏巡警、下班人潮。
- 不同時段詢問同一個 NPC 獲得不同零碎證詞，比對時間線拼湊完整拼圖。所有關鍵必要線索均提供替代取得途徑，絕不強迫玩家在現實半夜上線登入。

【社區信賴度善行互動】
- 隨手扶起路邊倒下的 YouBike（+5 信賴度）。
- 在巷弄路口協助長輩安全過馬路。
- 隨手撿起街道丟棄之空寶特瓶投入資源回收桶。
- 信賴度提升後，小吃店阿姨免費請喝冬瓜茶，NPC 會主動透露隱藏八卦。

【班級自製案件工作坊 (Classroom Workshop)】
- 內建極簡案件編輯器：選擇捷運站/公車站 ➔ 放置虛擬密函/寶箱 ➔ 撰寫 3 道提示線索 ➔ 設定通關暗號 ➔ 產生 6 碼大寫英數【案件代碼】（統一格式為 6 碼，如 TP8801）。
- 發表會時評審老師與全班同學只要在遊戲中輸入代碼，即可挑戰同儕設計的自製謎題；無伺服器時亦支援離線字串匯入匯出。

============================================================
■ 08｜跨平台畫面 UI、無障礙操作與後端資料庫架構
============================================================
【介面佈局】
- 中央主視窗：3D 俯瞰立體街景，可互動建築與站牌具備清晰發光標示。
- 畫面邊角 HUD：迷你雷達地圖、當前所在街區與行政區、精力條、現實氣象與遊戲時間。
- 智慧型手機快捷選單：案件簿、線索白板、人物通訊錄、三階提示、知識手冊、拍立得相簿、隨身收音機。每一介面均可一鍵快速返回現場。
- 無障礙設計：支援電腦 WASD/方向鍵 + 行動端虛擬搖桿與點擊移動；全對話皆有繁體中文字幕、支援字體大小調節、高對比度顏色模式、線索符號標註不依賴單一顏色辨識。

【資料與後端存檔架構】
- 本地快取：玩家位置、已解案件進度、手冊知識卡、相簿、事務所裝飾等保存於 LocalStorage / IndexedDB。
- 雲端共享伺服器（首解競賽）：
  * 案件主表：儲存案件狀態（未開放 / 進行中 / 已首解 / 已歸檔）、發布時間、首解玩家 ID、提交答案雜湊值。
  * 併發提交控制：提交答案時走資料庫交易（Database Transaction with Row Lock），確保首解唯一性與時間戳稽核。

============================================================
■ 09｜務實研發策略：第一版「垂直切片 (Vertical Slice)」與專案時程
============================================================
【垂直切片 (Vertical Slice) 敏捷策略】
國小 8 週獨立研究時間有限，若一開始承諾做出 1:1 完整台北與新北所有街道建築將導致專案難產。因此採取業界標準的「垂直切片」策略：
- 第一階段目標（核心跑通）：
  開放 1 條真實街道（台北車站周邊）、2 個公車站點、1 處可進入學習場館（科教館講堂）、1 間可休息小吃店、1 個多人可競速的首解小案。
  完整跑通「自由探索 ➔ 搭乘大眾運輸 ➔ 進館學習 ➔ 現場搜查 ➔ 推理解密 ➔ 獲得考據卡與生活慢活」的完整核心循環！
- 第二階段目標：擴充至 2 個行政區連通（台北車站 ✕ 淡水老街），加入 YouBike 租借與第二個名著機關。
- 第三階段目標：加入北投溫泉與板橋林家花園，實裝全 4 大經典名著機關與班級案件編輯器。
- 第四階段目標：全班試玩、數值微調、部署至 GitHub Pages 與 Itch.io，完成專案發表。

============================================================
■ 10｜決策待辦清單、公平性保障與未來擴充指引
============================================================
【核心待定與決策事項】
1. 建築室內開放排程：決定哪些建築為「完整獨特室內」（如四大古蹟、事務所、科教館），哪些為「共用商店模板」，未開放建築明確掛上「尚未開放探索」標籤，避免玩家誤解為系統故障。
2. 特殊公車票價定義：針對跨區長途公車（如跳蛙公車、快速公車）或段次收費邊界設定清楚的提示選單。
3. 共享案件發布頻率：設定每 2~4 週發布 1 批新案件，限時案件到期後自動轉入「懸案檔案庫」供玩家無期限閱覽。
4. 成果發表會無伺服器備案：若發表會現場展場 Wi-Fi 不穩，遊戲具備完整離線演示模式，確保成果發表 100% 順暢無阻。
`;

// Now let's generate the complete HTML file
const htmlContent = `<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>《雙北漫遊偵探：都會行蹤》完整遊戲設計企劃書（新版合併深度版）- 六年級獨立研究專題</title>
  <style>
    :root {
      --primary: #1d4ed8;
      --primary-dark: #1e3a8a;
      --primary-light: #eff6ff;
      --conan-red: #dc2626;
      --holmes-gold: #b45309;
      --accent: #f59e0b;
      --success: #059669;
      --purple: #7c3aed;
      --bg: #f1f5f9;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #475569;
      --border: #cbd5e1;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.04);
      --radius: 12px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", "Noto Sans TC", sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.7;
      padding: 24px 16px 120px;
    }

    .container {
      max-width: 980px;
      margin: 0 auto;
    }

    /* 頂部操作列 */
    .top-action-bar {
      position: sticky;
      top: 16px;
      z-index: 100;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 12px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.1);
      margin-bottom: 24px;
    }

    .project-tag {
      font-size: 13px;
      font-weight: 800;
      color: var(--primary);
      background: var(--primary-light);
      padding: 5px 12px;
      border-radius: 20px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .btn-group {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    button, .btn-link {
      cursor: pointer;
      font-family: inherit;
      font-size: 14px;
      font-weight: 700;
      padding: 8px 18px;
      border-radius: 8px;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .btn-primary {
      background-color: var(--primary);
      color: white;
    }

    .btn-primary:hover {
      background-color: var(--primary-dark);
      transform: translateY(-1px);
    }

    .btn-secondary {
      background-color: #f8fafc;
      color: var(--text);
      border: 1px solid var(--border);
    }

    .btn-secondary:hover {
      background-color: #e2e8f0;
    }

    /* 大標題卡片 */
    .header-card {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%);
      color: white;
      border-radius: var(--radius);
      padding: 38px 34px;
      margin-bottom: 26px;
      box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.3);
    }

    .header-card h1 {
      font-size: 28px;
      font-weight: 800;
      margin-bottom: 12px;
      letter-spacing: -0.5px;
      line-height: 1.35;
    }

    .header-card .subtitle {
      font-size: 15.5px;
      opacity: 0.94;
      margin-bottom: 22px;
      line-height: 1.6;
    }

    .meta-badges {
      display: flex;
      gap: 9px;
      flex-wrap: wrap;
    }

    .meta-badge {
      background: rgba(255, 255, 255, 0.18);
      border: 1px solid rgba(255, 255, 255, 0.35);
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    /* 免責聲明卡片 */
    .disclaimer-card {
      background: #fff1f2;
      border: 2px solid #f43f5e;
      border-radius: var(--radius);
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
    }

    .disclaimer-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 800;
      font-size: 16px;
      color: #be123c;
      margin-bottom: 10px;
    }

    .disclaimer-text {
      font-size: 13.5px;
      color: #881337;
      margin-bottom: 8px;
      line-height: 1.65;
    }

    /* 內容卡片 */
    .card {
      background: var(--card-bg);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      padding: 30px;
      margin-bottom: 26px;
      box-shadow: var(--shadow);
    }

    .card h2 {
      font-size: 21px;
      color: #0f172a;
      margin-bottom: 18px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .card h3 {
      font-size: 17px;
      color: #1e293b;
      margin: 22px 0 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    p {
      margin-bottom: 14px;
      color: #334155;
      font-size: 15px;
      line-height: 1.7;
    }

    ul, ol {
      margin-left: 22px;
      margin-bottom: 16px;
      color: #334155;
    }

    li {
      margin-bottom: 8px;
      font-size: 14.5px;
      line-height: 1.65;
    }

    /* 表格樣式 */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 18px 0;
      font-size: 14px;
    }

    th, td {
      border: 1px solid var(--border);
      padding: 11px 13px;
      text-align: left;
      vertical-align: top;
    }

    th {
      background-color: #f8fafc;
      font-weight: 700;
      color: #1e293b;
    }

    /* 團隊角色卡片 */
    .team-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 18px 0;
    }

    .team-card {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
      border-top: 4px solid var(--primary);
    }

    .team-role {
      font-size: 12px;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 4px;
      letter-spacing: 0.5px;
    }

    .team-name {
      font-size: 16px;
      font-weight: 800;
      margin-bottom: 10px;
      color: #0f172a;
    }

    .team-duty {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.65;
    }

    /* 機關案例文獻卡片 */
    .case-container {
      display: flex;
      flex-direction: column;
      gap: 22px;
      margin: 20px 0;
    }

    .case-card {
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      background: #ffffff;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      overflow: hidden;
      border-left: 6px solid var(--primary);
    }

    .case-card.conan { border-left-color: var(--conan-red); }
    .case-card.holmes { border-left-color: var(--holmes-gold); }

    .case-header {
      padding: 16px 20px;
      background: #f8fafc;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .case-title {
      font-size: 16.5px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .case-badge {
      font-size: 12px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 20px;
    }

    .badge-conan { background: #fee2e2; color: var(--conan-red); border: 1px solid #fca5a5; }
    .badge-holmes { background: #fef3c7; color: var(--holmes-gold); border: 1px solid #fcd34d; }

    .case-body { padding: 20px; }
    .case-section { margin-bottom: 12px; font-size: 14.5px; }
    .case-label { font-weight: 700; color: #1e293b; font-size: 14px; margin-bottom: 4px; display: inline-flex; align-items: center; gap: 6px; }

    .codex-card {
      background: #fdf6ec;
      border: 1px dashed #d97706;
      border-radius: 8px;
      padding: 14px 16px;
      margin-top: 12px;
      font-size: 13.5px;
      color: #78350f;
      line-height: 1.65;
    }

    .codex-header {
      font-weight: 800;
      font-size: 14px;
      color: #92400e;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* 亮點提示區塊 */
    .callout {
      background-color: var(--primary-light);
      border-left: 4px solid var(--primary);
      padding: 16px 20px;
      border-radius: 0 8px 8px 0;
      margin: 18px 0;
      font-size: 14.5px;
      line-height: 1.65;
    }

    .callout.tip { background-color: #ecfdf5; border-left-color: var(--success); }
    .callout.accent { background-color: #fffbeb; border-left-color: var(--accent); }
    .callout.purple { background-color: #f5f3ff; border-left-color: var(--purple); }

    .callout-title {
      font-weight: 800;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* 網格系統 */
    .feature-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 18px 0;
    }

    .feature-box {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
    }

    .feature-box h4 {
      font-size: 15.5px;
      color: #0f172a;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Toast 浮動提示 */
    #toast {
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #0f172a;
      color: #fff;
      padding: 14px 28px;
      border-radius: 30px;
      font-size: 15px;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
      transition: transform 0.3s cubic-bezier(0.18, 0.89, 0.32, 1.28), opacity 0.3s;
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
      pointer-events: none;
      opacity: 0;
    }

    #toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    @media print {
      body { background: white; padding: 0; }
      .top-action-bar, #toast { display: none !important; }
      .card { box-shadow: none; border: 1px solid #bbb; page-break-inside: avoid; margin-bottom: 18px; padding: 18px; }
      .header-card { background: #1e3a8a !important; color: white !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    }
  </style>
</head>
<body>

  <div class="container">

    <!-- 頂部快速操作列 -->
    <div class="top-action-bar">
      <div class="project-tag">
        <span>🔍</span> 六年級獨立研究深度企劃書（新版合併深度版）
      </div>
      <div class="btn-group">
        <a href="index.html" class="btn-secondary btn-link">
          <span>🎮</span> 進入遊戲展示
        </a>
        <button class="btn-primary" onclick="copyFullProposal()">
          <span>📋</span> 一鍵複製企劃書全文
        </button>
        <button class="btn-secondary" onclick="window.print()">
          <span>🖨️</span> 列印 / 存為 PDF
        </button>
      </div>
    </div>

    <!-- 標題大卡片 -->
    <div class="header-card">
      <h1>《雙北漫遊偵探：都會行蹤》完整遊戲設計企劃書</h1>
      <div class="subtitle">
        1:1 連續雙北開放地圖 ✕ 名著經典機關科學考據 ✕ 真實大眾交通費率 ✕ 共享世界唯一首解競速 ✕ 《動物森友會》式慢活日常
      </div>
      <div class="meta-badges">
        <span class="meta-badge">👥 專案團隊：國小六年級獨立研究小組（三人團隊）</span>
        <span class="meta-badge">🗺️ 地理架構：1:1 連續雙北（OpenStreetMap 開放圖資基礎）</span>
        <span class="meta-badge">🎨 視覺表現：3D 空中俯瞰街景 + 2D 復古像素主角</span>
        <span class="meta-badge">🚌 交通費率：公車 15 元、捷運里程計費、YouBike 前 30 分鐘補助</span>
        <span class="meta-badge">🏆 核心競技：全伺服器共享世界與唯一首解原子鎖定</span>
        <span class="meta-badge">💰 經濟雙軌：高階破案賞金 vs 生活流通金</span>
      </div>
    </div>

    <!-- ⚖️ 學術研究與非商業用途免責聲明 -->
    <div class="disclaimer-card">
      <div class="disclaimer-title">
        <span>⚖️</span>【重要法規與合規聲明】國小六年級獨立研究學術專案與非商業聲明
      </div>
      <p class="disclaimer-text">
        1. <strong>非商業性質</strong>：本企劃書及後續開發之遊戲專案，為<strong>國小六年級學生「獨立研究」課程之學術成果與跨學科程式教育專案</strong>，完全<strong>不具備任何商業營利、收費、贊助或販售行為</strong>。
      </p>
      <p class="disclaimer-text">
        2. <strong>名著、地標商標與公共音效原創規範</strong>：專案中所引述致敬之《名偵探柯南》、《福爾摩斯探案集》經典密碼與科學手法，以及台灣真實大眾運輸（台北捷運、市區公車、YouBike）、真實地標景點名稱，皆僅作為國小教學研究、科學物理探究與遊戲體驗設計之<strong>合理使用（Fair Use）</strong>。公開發布時，所有美術立繪、像素角色、UI、捷運廣播與背景音樂，皆採<strong>原創繪製與自製錄音</strong>，不直接套用版權動畫素材。
      </p>
      <p class="disclaimer-text" style="margin-bottom:0;">
        3. <strong>虛構榮譽與無官方贊助澄清</strong>：企劃內提及之「雙北文史生活金獎勵」、「市警局榮譽顧問勳章」等內容，純屬遊戲世界觀之<strong>「虛構劇情榮譽與數值獎勵」</strong>，絕非真實台北市或新北市政府、警局之官方背書或真實贊助。
      </p>
    </div>

    <!-- 01｜專案基本定位與三人小組深度分工 -->
    <div class="card">
      <h2>📌 01｜專案基本定位、核心精神與三人團隊深層分工</h2>
      
      <div class="callout tip">
        <div class="callout-title">💡 一句話定位</div>
        《雙北漫遊偵探：都會行蹤》是一款以雙北為舞台的開放式探索推理遊戲：<strong>街區是連續的遊戲空間，案件是可選的冒險，學習內容藏在場所與微型互動裡</strong>。它不是只有四個封閉關卡、通關即結束的解謎遊戲，而是一座世界隨時持續運轉的城市！
      </div>

      <h3>🎯 核心體驗與玩家可做的事</h3>
      <ul>
        <li><strong>人不用真的到現場</strong>：玩家在電腦前用鍵盤或手機搖桿操作角色，在虛擬的台北市與新北市街頭奔馳，身歷其境。</li>
        <li><strong>自主漫遊與生活</strong>：可以辦案，也可以完全不照主線走。跨區散步、搭乘公車、進店家吃小吃回體力、在事務所整理線索、或是坐在便利超商看雨景放空。</li>
        <li><strong>深度調查與科學解密</strong>：調查現場物件、訪問不同時段出沒的居民 NPC、比對時間線、解開經典物理化學機關，提交完整推理。</li>
        <li><strong>案件有結局，世界無終點</strong>：破案後世界依然持續運作，玩家可繼續探索新街區、尋找隱藏彩蛋、或等待下一批案件分批發布。</li>
        <li><strong>最核心設計原則</strong>：<strong>玩家自己決定下一站！</strong>教學不綁死順序，故事提供方向但不鎖死整座城市。每個可進入地點至少有一件值得做的事（一段知識、一個觀察、一個人物、一條線索或一個彩蛋）。</li>
      </ul>

      <h3>👥 三人研究團隊詳細職責規劃</h3>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-role">組員 1（組長 / 企劃總監）</div>
          <div class="team-name">世界觀設定、劇本與知識編寫</div>
          <div class="team-duty">
            • 統籌專案整體目標與進度。<br>
            • 研讀《名偵探柯南》與《福爾摩斯》，改編經典物理/化學/密碼機關。<br>
            • 編寫雙北生活圈委託、NPC 對話、破案後的「名著考據卡」與「微型知識講堂」文案，緊扣國小課綱。
          </div>
        </div>
        <div class="team-card">
          <div class="team-role">組員 2（美術與圖資總監）</div>
          <div class="team-name">視覺風格、街區尺度與授權清單</div>
          <div class="team-duty">
            • 制定 45°~60° 3D 俯瞰視角立體街景美學與 2D 復古像素主角/NPC 造型。<br>
            • 考察真實雙北地理，使用 OpenStreetMap (OSM) 開放圖資建立 1:1 道路尺度與建築外觀。<br>
            • 盤點圖資與圖片開源協議（ODbL），繪製在地小吃（阿給、排骨酥麵、珍奶）道具圖示。
          </div>
        </div>
        <div class="team-card">
          <div class="team-role">組員 3（技術架構與機制總監）</div>
          <div class="team-name">引擎架構、經濟平衡與 AI 協同</div>
          <div class="team-duty">
            • 規劃「3D 俯瞰街道 + 2D 像素小人」移動手感、手機觸控操作與鍵盤支援。<br>
            • 建立真實大眾交通費率演算法（公車站牌段次緩衝區、捷運票價矩陣、YouBike 租借補助）。<br>
            • 設計伺服器端「唯一首解原子鎖定」與資料表架構，為 AI（志炫等）提供規格並主導全班測試。
          </div>
        </div>
      </div>
    </div>

    <!-- 02 & 02A｜雙北連續世界、1:1 地理與真實大眾交通費率建模 -->
    <div class="card">
      <h2>🏙️ 02 & 02A｜雙北連續世界、1:1 地理與真實大眾交通費率建模</h2>

      <h3>1. 1:1 現實地理與無縫連續城市</h3>
      <p>
        雙北地圖以台北市與新北市的真實道路、橋梁、河川、行政區、公車站點、捷運站與相對距離為基礎。<strong>這是一座連續的城市，絕不把區域濃縮成幾個互不相連的關卡傳送門！</strong>
      </p>
      <ul>
        <li><strong>沿道路跨區步行</strong>：即使穿越行政區界（例如台北市中正區跨越中正橋進入新北市永和區、或是跨越大漢溪進入板橋），玩家都能沿著現實街道步行前進，不得以行政區邊界限制玩家步行漫遊。</li>
        <li><strong>圖資來源與開源合規</strong>：地圖底層採用 OpenStreetMap（OSM）道路與建物圖資，搭配政府交通開放資料平台（TDX/PTX）。嚴格遵守 ODbL 開源協議與署名規範，絕不未授權抓取商業街景或商業地圖磚。</li>
      </ul>

      <h3>2. 公車為主，捷運、YouBike 與步行四軌並行</h3>
      <table>
        <thead>
          <tr>
            <th style="width: 20%;">交通方式</th>
            <th style="width: 30%;">真實雙北費率與計算規則</th>
            <th style="width: 30%;">遊戲內運作與機制表現</th>
            <th style="width: 20%;">防卡死與特色</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>🚶 步行 (Walking)</strong></td>
            <td><strong>完全免費 ($0)</strong></td>
            <td>沿街道與騎樓前進，耗費現實操作時間與少量精力值。</td>
            <td><strong>永不卡死</strong>：沒錢時隨時可走回事務所或下個現場。</td>
          </tr>
          <tr>
            <td><strong>🚌 市區公車 (Bus)<br><span style="font-size:12px; color:var(--primary); font-weight:700;">★ 核心大眾運輸</span></strong></td>
            <td><strong>全票每段次 15 元</strong><br>依真實路線站牌、分段點與緩衝區計費（跨緩衝區加收 15 元變兩段票 30 元）。</td>
            <td>走雙北真實路線（如 307、299、紅 26 等），站牌清楚標示起迄站、抵達出口與扣除生活金金額。</td>
            <td>網絡最密、深入大街小巷，短程跨區最具生活代入感！</td>
          </tr>
          <tr>
            <td><strong>🚇 台北捷運 (MRT)</strong></td>
            <td><strong>按起迄站官方票價表計費</strong><br>單程票 $20 ~ $65（嚴禁以直線距離胡亂猜測票價）。</td>
            <td>高架與地下軌道穿梭，速度極快、固定班次準點，進站出站播放經典四語廣播音效。</td>
            <td>長途跨區首選（如台北車站直奔淡水或板橋）。</td>
          </tr>
          <tr>
            <td><strong>🚲 YouBike 2.0</strong></td>
            <td>• 4 小時內每 30 分鐘 10 元<br>• 4~8 小時每 30 分鐘 20 元<br>• <strong>雙北會員前 30 分鐘免費補助</strong></td>
            <td>在街頭 YouBike 租借站借還車，騎乘速度比步行快 1.8 倍，精力消耗大幅降低。</td>
            <td>活用前 30 分鐘免費補助，短程接駁省錢無負擔。</td>
          </tr>
        </tbody>
      </table>

      <h3>3. 時間、日夜與動態氣象雙軌制</h3>
      <div class="feature-grid">
        <div class="feature-box">
          <h4>🌦️ 串接中央氣象署 API（自然科跨領域）</h4>
          <p style="font-size:13.5px; color:var(--text-muted);">
            串接 CWA API 每 15 分鐘同步雙北即時天候。下雨天 3D 俯瞰街道泛起細密雨絲與水窪，街頭 NPC 撐傘；泥濘草地會留下未乾鞋印、屋簷落水聲掩蓋犯罪撞擊、雨傘滴水成為推算嫌犯進門時刻的線索！
          </p>
        </div>
        <div class="feature-box">
          <h4>⚖️ 雙軌防卡關：離線預設與案件時間軸解耦</h4>
          <p style="font-size:13.5px; color:var(--text-muted);">
            若網路中斷或 API 異常，自動啟用預設穩定天氣；更重要的是：<strong>將「世界現實同步時間」與「案件內部可調整的時間軸」分開</strong>，絕不讓玩家因現實中等不到連續陰雨天而卡死無法解案！
          </p>
        </div>
      </div>
    </div>

    <!-- 03｜玩家遊玩流程：新手前 15 分鐘到長期探索循環 -->
    <div class="card">
      <h2>🔄 03｜玩家遊玩流程：新手前 15 分鐘到長期探索循環</h2>

      <h3>1. 新手的前 15 分鐘（零門檻上手）</h3>
      <ol>
        <li><strong>事務所誕生</strong>：在充滿懷舊氛圍的西門町/大稻埕老街事務所甦醒，學會 WASD / 手機虛擬搖桿走動、觀察周圍物件、開啟手機線索簿。</li>
        <li><strong>門口無門檻失物小委託</strong>：事務所樓下雜貨店老闆遺失了一串鑰匙（花費門檻為 0 元）：
          <ul>
            <li>在巷口盆栽旁發現金屬刮痕（現場搜查）。</li>
            <li>向兩名 NPC（早餐店老闆與郵差）打聽線索（訪談證詞）。</li>
            <li>把線索放進線索簿時間軸連線，推論出鑰匙被樹上的喜鵲叼至屋簷鳥巢。</li>
          </ul>
        </li>
        <li><strong>首戰獎勵與自由啟程</strong>：破案獲得初始生活金 100 元、第一張「密碼鑑識知識卡」與雙北地圖。</li>
        <li><strong>地圖全面解鎖</strong>：地圖顯示「前往科教館上課」、「前往台北車站接取大案」、或是「搭捷運去淡水吃阿給散步」，由玩家自主決定下一步！</li>
      </ol>

      <h3>2. 長期每一次遊玩的循環 (The Gameplay Loop)</h3>
      <div class="callout tip">
        <strong>【無限漫遊核心迴路】</strong>：<br>
        自主選擇目的地或接案 ➔ 步行散步或搭乘公車/捷運 ➔ 抵達街區觀察街景、拍照、進館學習 ➔ 收集物件證詞並破解名著經典機關 ➔ 提交推理獲得原理解析、考據卡與獎金 ➔ 自由選擇去下一區、接下一案、或是回事務所裝飾房間泡茶慢活。
      </div>
      <ul>
        <li><strong>案件任務有始有終，城市生活永不停歇</strong>：主線大案有明確的真相調查與收尾；但雙北城市的街道、商店、小委託與學習館舍永不落幕。</li>
        <li><strong>已結案共享案件轉為回顧</strong>：已被全服首解的案件自動歸檔為「歷史不計分檔案」，後續玩家仍可體驗劇情但無法重複領首解大獎，世界持續運轉！</li>
      </ul>
    </div>

    <!-- 04｜案件、線索簿與四大名著機關（嚴謹科學與史實糾錯升級版） -->
    <div class="card">
      <h2>🔍 04｜案件、線索簿與四大名著機關（嚴謹科學與史實糾錯升級版）</h2>
      <p>
        在雙北各名勝現場調查時，會觸發精心設計的原創機關。成功破案後，畫面會彈出充滿成就感的<strong>【名著考據解密卡】</strong>，介紹小說出處、科學物理化學原理與雙北文史結合：
      </p>

      <div class="case-container">

        <!-- 案例 1：淡水跳舞小人 -->
        <div class="case-card holmes">
          <div class="case-header">
            <div class="case-title">
              <span>🏰</span> 案例 1：淡水港文史主題場景 ——「跳舞小人密碼磚」
            </div>
            <span class="case-badge badge-holmes">致敬：福爾摩斯探案集</span>
          </div>
          <div class="case-body">
            <div class="case-section">
              <div class="case-label">📍 調查舞台：</div>
              淡水老街與海關碼頭歷史場景（<strong>★ 史實嚴謹標註</strong>：淡水紅毛城古蹟實體並無地下秘密地牢暗室，本案為結合淡水開港文史之虛構主題場景改編，避免誤導學生）。
            </div>
            <div class="case-section">
              <div class="case-label">⚙️ 機關形式與玩家互動：</div>
              石壁上刻有 26 塊不同姿態的火柴小人符號（手持旗幟者代表單詞結尾）。玩家調閱淡水海關公署遺留的英文航海日誌，使用「英文字母頻率分析（E 最常出現）」結合單字上下文替換破解密碼磚，解鎖暗格獲得百年航海懷錶。
            </div>
            <div class="codex-card">
              <div class="codex-header">📜 【破案解密考據卡：柯南·道爾《跳舞的人》】</div>
              • <strong>原著出處</strong>：亞瑟·柯南·道爾 1903 年《福爾摩斯探案集：歸來記》之〈跳舞的人〉（The Adventure of the Dancing Men）。<br>
              • <strong>密碼學原理</strong>：單表替換式密碼（Substitution Cipher）與字母頻率分析法。<br>
              • <strong>在地文史結合</strong>：淡水港於 1862 年正式開港通商，曾設英國領事館，具有濃厚 19 世紀海洋貿易文史背景。
            </div>
          </div>
        </div>

        <!-- 案例 2：北投溫泉顯影 -->
        <div class="case-card conan">
          <div class="case-header">
            <div class="case-title">
              <span>♨️</span> 案例 2：北投溫泉會館 —— 蒸氣加熱「弱酸脫水顯影遺書」
            </div>
            <span class="case-badge badge-conan">致敬：名偵探柯南</span>
          </div>
          <div class="case-body">
            <div class="case-section">
              <div class="case-label">📍 調查舞台：</div>
              北投溫泉博物館旁的虛構老字號旅店湯屋（<strong>★ 現實安全警語</strong>：北投天然青磺泉高達 80°C~100°C 具危險性，嚴禁在現實中靠近高溫湧泉槽或進行危險化學模仿）。
            </div>
            <div class="case-section">
              <div class="case-label">⚙️ 機關形式與玩家互動：</div>
              案發現場留下一張空白泛黃信紙。玩家使用道具「防熱竹夾」將紙張置於安全溫控蒸氣上方微溫烘烤，紙張上的稀有機酸（檸檬酸）受熱脫水，使纖維素炭化變褐，浮現出保管箱密碼。
            </div>
            <div class="codex-card">
              <div class="codex-header">📜 【破案解密考據卡：柯南理科加熱顯影與有機化學】</div>
              • <strong>原著出處</strong>：《名偵探柯南》經典理科密室（如第 74 卷「毒與幻的設計」、早期加熱顯影手法）。<br>
              • <strong>科學原理糾錯</strong>：<strong>嚴格鎖定單一可驗證之弱酸高溫脫水炭化反應</strong>，不把酸、氯化鈷吸水變色與硫磺氣體混為一談。<br>
              • <strong>在地特色</strong>：北投為天然地熱溫泉之鄉，以此場景引導學生認識地熱能源與生活有機化學。
            </div>
          </div>
        </div>

        <!-- 案例 3：台北車站水力延時聲學 -->
        <div class="case-card conan">
          <div class="case-header">
            <div class="case-title">
              <span>🚇</span> 案例 3：台北車站地下街 —— 水力虹吸延時「不在場證明」
            </div>
            <span class="case-badge badge-conan">致敬：名偵探柯南 & 經典本格推理</span>
          </div>
          <div class="case-body">
            <div class="case-section">
              <div class="case-label">📍 調查舞台：</div>
              台北車站三鐵共構連通長廊與地下街通道。
            </div>
            <div class="case-section">
              <div class="case-label">⚙️ 機關形式與玩家互動：</div>
              嫌犯利用虹吸管與水桶製成水力重力延時裝置，在案發 30 分鐘後蓄水滿溢倒塌製造巨響，利用長廊多重聲音反射使目擊者誤判案發時間製造不在場證明。玩家比對地下街監視器時間戳與物理聲學破案。
            </div>
            <div class="codex-card">
              <div class="codex-header">📜 【破案解密考據卡：柯南〈霧天狗傳說〉與建築聲學糾錯】</div>
              • <strong>原著出處</strong>：《名偵探柯南》動畫第 52 集〈霧天狗傳說殺人事件〉（水流蓄力延遲手法）。<br>
              • <strong>★ 關鍵科學糾錯</strong>：
                <strong>造成 30 分鐘不在場證明的是「水力虹吸裝置延遲 30 分鐘傾倒」</strong>，絕非聲波在長廊傳播花了 30 分鐘（空氣聲速約 340 m/s，300 公尺長廊不到 0.9 秒即抵達！）。長廊水泥壁的多次回聲反射在案情中是負責「混淆發聲方向」，使證人無法精準判別聲源位置。<br>
              • <strong>物理學原理</strong>：流體虹吸原理（Siphon Principle）與建築聲學回聲反射（Acoustic Reflection）。
            </div>
          </div>
        </div>

        <!-- 案例 4：板橋日影幾何投影 -->
        <div class="case-card holmes">
          <div class="case-header">
            <div class="case-title">
              <span>🏮</span> 案例 4：板橋林家花園 —— 八角漏窗「秋分日影幾何投影」
            </div>
            <span class="case-badge badge-holmes">致敬：福爾摩斯探案集</span>
          </div>
          <div class="case-body">
            <div class="case-section">
              <div class="case-label">📍 調查舞台：</div>
              國定古蹟板橋林本源園邸（汲古書屋與方鑑齋）。
            </div>
            <div class="case-section">
              <div class="case-label">⚙️ 機關形式與玩家互動：</div>
              古詩記載「秋分午後，八角漏窗見金光」。玩家調整遊戲內幾何量測儀，根據秋分太陽高度角（35°）與相似三角形比例，計算日影投影至假山暗縫的焦點，找出暗藏的古銅鑰匙。
            </div>
            <div class="codex-card">
              <div class="codex-header">📜 【破案解密考據卡：福爾摩斯〈馬斯格雷夫禮儀〉與幾何光學糾錯】</div>
              • <strong>原著出處</strong>：柯南·道爾《福爾摩斯探案集：回憶錄》之〈馬斯格雷夫禮儀〉（The Musgrave Ritual）。<br>
              • <strong>★ 關鍵光學糾錯</strong>：
                光線穿過八角漏窗投在牆面上是<strong>「日影幾何投影 (Shadow Projection)」</strong>；水池水面映射是<strong>「反射 (Reflection)」</strong>，兩者皆非「折射 (Refraction)」。<br>
              • <strong>數學幾何原理</strong>：相似三角形定理（物高比影長）與日影高度角幾何方程式。
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- 04A｜共享世界體系：全服唯一首解、案件生命週期與競速機制 -->
    <div class="card">
      <h2>🌐 04A｜共享世界體系：全服唯一首解、案件生命週期與競速機制</h2>

      <div class="callout purple">
        <div class="callout-title">🏆 一案只有一個結局與唯一首解！</div>
        所有玩家登入同一個持續運轉的雙北城市。每起重大案件在雲端伺服器均有全服同步的<strong>生命週期狀態</strong>：
        <div style="font-weight:700; margin-top:6px; color:#5b21b6;">
          【未公布】 ➔ 【分批公開】 ➔ 【可接 / 全服競速調查中】 ➔ 【首解破案 / 限時到期】 ➔ 【結案歸檔 (轉為不計分回顧)】
        </div>
      </div>

      <h3>1. 唯一首解公平性與伺服器原子鎖定 (Atomic Lock)</h3>
      <ul>
        <li><strong>客觀判定標準</strong>：首解判定必須由玩家向伺服器提交<strong>「完整且正確的推理鏈條」</strong>（包含動機、手法、物證與機關解鎖），伺服器依交易時間戳（精確至毫秒）判定全服第一名。</li>
        <li><strong>並發防衝突</strong>：採用資料庫原子交易鎖（Transaction Row Lock），杜絕多名玩家同時提交時的「重複發獎」與爭議。首解誕生瞬間，全服彈出快訊，案件狀態立即鎖定。</li>
        <li><strong>首解榮譽榜</strong>：首解神探將永久銘刻於雙北偵探總署「全服名人堂」，並獲得豐厚破案賞金！</li>
      </ul>

      <h3>2. 結案後不計分歷史回顧模式</h3>
      <p>
        若某個大案已被其他同學首解破獲，正在調查中的其他玩家會收到即時結案簡訊。<strong>已結案的案件會自動移入「歷史案件檔案室」，後續玩家依然可以完整閱讀案情、前往現場解謎與收集知識卡，但不再發放首解大獎</strong>。這樣既保障了競速刺激感，又不會破壞其他玩家的探究樂趣！
      </p>
    </div>

    <!-- 05｜場所互動、短時微型學習手冊與台味隱藏彩蛋 -->
    <div class="card">
      <h2>🏛️ 05｜場所互動、短時微型學習手冊與台味隱藏彩蛋</h2>

      <h3>1. 把學習做成 1~3 分鐘微型互動（拒絕一整頁枯燥講義）</h3>
      <p>
        每個可進入地點均遵循【看見什麼 / 做什麼 / 學到什麼 / 與哪個案件相關】四欄標準規範：
      </p>
      <table>
        <thead>
          <tr>
            <th style="width: 22%;">學習場館與地點</th>
            <th style="width: 38%;">1~3 分鐘微型互動形式</th>
            <th style="width: 40%;">收穫知識卡與案件助益</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>台灣科學教育館<br>(士林科教館)</strong></td>
            <td>操作安全的光影折射台與熱敏顯影模擬槽，調整溫度觀察變色過程。</td>
            <td>獲得「熱敏顯影鑑識卡」，在北投溫泉案件中自動提示受熱脫水原理。</td>
          </tr>
          <tr>
            <td><strong>台北市立圖書館總館<br>(大安區)</strong></td>
            <td>英文字母頻率分佈比對小遊戲（拖曳字母方塊還原被遮蓋的英文單字）。</td>
            <td>獲得「密碼速查字典」，在淡水紅毛城案件中直接提供字母頻率參考線索。</td>
          </tr>
          <tr>
            <td><strong>淡水海關公署故事館<br>(淡水紅毛城旁)</strong></td>
            <td>判讀 1860 年代英國領事館商船航海日誌與海關驗貨稅單字跡。</td>
            <td>獲得台灣海洋開港史知識，與淡水老船長 NPC 對話時可觸發特殊文史選項。</td>
          </tr>
          <tr>
            <td><strong>新北市立圖書館總館<br>(板橋貴興路)</strong></td>
            <td>日晷測時法與相似三角形影子長度測量模擬器。</td>
            <td>獲得幾何測量儀，在板橋林家花園日影機關中直接顯示太陽方位角與高度角。</td>
          </tr>
        </tbody>
      </table>

      <h3>2. 雙北街頭四大特色彩蛋 (Easter Eggs)</h3>
      <div class="feature-grid">
        <div class="feature-box">
          <h4>🎮 彩蛋 1：創作團隊三人組客串</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            台北車站巷弄小吃店角落，坐著三名六年級獨立研究學生 NPC，筆電上正開著這本企劃書與 AI 程式碼，幽默感謝所有玩家試玩！
          </p>
        </div>
        <div class="feature-box">
          <h4>🐱 彩蛋 2：淡水老街黑貓「阿巧」</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            在淡水老街紅磚後巷買魚丸餵牠，黑貓阿巧會領著你穿過神秘防空洞，指引出牆面上的隱藏經緯度座標暗號！
          </p>
        </div>
        <div class="feature-box">
          <h4>🔭 彩蛋 3：台北 101 屋頂秘密展望台</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            完成特定支線後獲得天台鑰匙，在晴朗夜間可登上 101 屋頂飽覽大台北 3D 星空與萬家燈火全景。
          </p>
        </div>
        <div class="feature-box">
          <h4>🚏 彩蛋 4：名著致敬彩蛋站牌貼紙</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            雙北某個公車站牌角落，悄悄貼著「221B 貝克街」與「米花町五丁目」的復古公車路線貼紙，向柯南與福爾摩斯致敬！
          </p>
        </div>
      </div>
    </div>

    <!-- 06｜生活慢活、偵探精力值、雙軌貨幣與無障礙防卡關機制 -->
    <div class="card">
      <h2>☕ 06｜生活慢活、偵探精力值、雙軌貨幣與無障礙防卡關機制</h2>

      <h3>1. 偵探精力值系統 (Stamina System) 與小吃回血</h3>
      <ul>
        <li><strong>精力消耗</strong>：奔跑與深度現場搜查消耗精力。低精力時角色轉為慢走散步，但<strong>「絕對不會連回家或求助都做不到」</strong>。</li>
        <li><strong>免費與小吃回復</strong>：在事務所沙發休息、便利超商飲水機皆可免費回滿基本精力；進店品嚐台灣小吃回血：
          <ul>
            <li><strong>淡水阿給 + 魚丸湯</strong>：精力回滿 100%，獲得 3 分鐘「海風輕快」奔跑無消耗 Buff。</li>
            <li><strong>北投排骨酥麵 + 溫泉蛋</strong>：精力回滿，解謎時出現額外提示光圈。</li>
            <li><strong>連鎖手搖飲珍奶</strong>：快速回補 40% 精力，短時間移速提升 30%。</li>
            <li><strong>台北巷弄豆漿油條</strong>：平價實惠，隨時隨地補滿基礎體力。</li>
          </ul>
        </li>
      </ul>

      <h3>2. 雙軌貨幣體系與商城機制</h3>
      <table>
        <thead>
          <tr>
            <th style="width: 22%;">貨幣類型</th>
            <th style="width: 28%;">獲取途徑 (How to Earn)</th>
            <th style="width: 32%;">專屬用途 (Where to Spend)</th>
            <th style="width: 18%;">定位與原則</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong style="color:var(--primary); font-size:15px;">🏅 破案委託賞金</strong><br>
              <span style="font-size:12px; color:var(--text-muted);">(Detective Coins / 偵探徽幣)</span>
            </td>
            <td>
              • 成功破獲主線與支線大案。<br>
              • 解開名著經典物理/密碼機關。<br>
              • 達成全服首解或零提示成就。
            </td>
            <td>
              • <strong>永久專業加速裝備</strong>：<br>
                - 改裝極速滑板（移速 +60%）<br>
                - 高倍微距放大鏡（隱密證物高光）<br>
                - 便攜紫外光燈（暗處螢光顯影）<br>
              • <strong>限定外觀</strong>（風衣、變聲西裝）。
            </td>
            <td>
              <strong>榮譽與破關成就！</strong><br>
              專門用於永久加速遊戲進程，不可直接由日常打工取得。
            </td>
          </tr>
          <tr>
            <td>
              <strong style="color:var(--success); font-size:15px;">💳 日常生活流通金</strong><br>
              <span style="font-size:12px; color:var(--text-muted);">(Daily Cash / 悠遊卡現金)</span>
            </td>
            <td>
              • 每日事務所基本生活津貼。<br>
              • 街頭鄰里小委託（找走失小狗/失物）。<br>
              • 超商或店家短暫兼職打工。<br>
              • 將破案賞金兌換成生活現金。
            </td>
            <td>
              • <strong>大眾運輸搭乘</strong>：公車每段 $15、捷運 $20~$65、YouBike 租借。<br>
              • <strong>現場破關必備耗材</strong>：超商防熱竹夾 ($35)、電池組 ($50)、試紙。<br>
              • <strong>小吃吃飯回體力</strong>：購買阿給、排骨酥麵補滿精力。
            </td>
            <td>
              <strong>生活代入感！</strong><br>
              體現真實城市生活的運作邏輯，進店吃飯搭車皆需生活金。
            </td>
          </tr>
        </tbody>
      </table>

      <h3>3. 絕對不卡死 (Anti-Softlock) 與無障礙三階提示</h3>
      <div class="callout tip">
        <strong>🛡️ 零死局保證</strong>：即使生活金與精力降為 0，玩家依然可以免費漫遊步行、在事務所免費休息回滿精力、或在街頭做資源回收賺取基礎車資，絕不會卡死無法動彈！
      </div>
      <ul>
        <li><strong>第 1 階提示（完全免費）</strong>：給予現場關鍵物證的觀察重點。</li>
        <li><strong>第 2 階提示</strong>：給予邏輯推論方向（可花費 $10 生活金，<strong>亦可選擇「等待 5 分鐘冷卻」或「完成指定環境觀察」免費解鎖</strong>）。</li>
        <li><strong>第 3 階提示</strong>：直接引導具體操作公式（同上，提供無障礙免費等待途徑），確保所有同學都能順利破案通關！</li>
      </ul>

      <h3>4. 事務所慢活、隨身拍立得與環境音效</h3>
      <ul>
        <li><strong>事務所基地</strong>：自由佈置案情白板（紅線連結關係圖）、古董咖啡機與沙發，享受都會慢活。</li>
        <li><strong>拍立得相機 [C] 鍵</strong>：隨時拍下街景、夕陽與現場證物，拍立得卡片可自由<strong>釘在事務所案情軟木板上</strong>留念。</li>
        <li><strong>垃圾車音樂推理</strong>：嫌犯通話錄到了微弱的《少女的祈禱》音樂，查詢雙北清潔隊各里清運時刻表，精準推算嫌犯案發當時所在的真實巷弄！</li>
      </ul>
    </div>

    <!-- 07｜城市動態 NPC 作息、社區信賴度與班級案件工作坊 -->
    <div class="card">
      <h2>👥 07｜城市動態 NPC 作息、社區信賴度與班級案件工作坊</h2>

      <h3>1. NPC 動態生活作息與多時段證詞</h3>
      <p>
        雙北居民擁有逼真的生活作息：晨間阿公阿嬤在公園運動、午後上班族湧入捷運地下街覓食、黃昏夜市開張。同一案件在不同時段訪談同一個 NPC 會獲得不同零碎證詞，比對時間軸才能拼湊真相。<strong>關鍵必要線索均提供替代取得途徑，絕不要求同學在現實中半夜上線登入！</strong>
      </p>

      <h3>2. 社區信賴度善行互動</h3>
      <ul>
        <li>🚲 隨手扶起路邊倒下的 YouBike（+5 信賴度）。</li>
        <li>👵 在無號誌巷弄路口協助長輩安全過馬路。</li>
        <li>🧴 隨手撿起街道丟棄之寶特瓶投入資源回收桶換取零錢。</li>
        <li>🎁 信賴度滿分後，小吃店阿姨免費請喝冬瓜茶，NPC 會主動透露深層八卦！</li>
      </ul>

      <h3>3. 班級自製案件工作坊 (Classroom Workshop)</h3>
      <p>
        內建極簡案件編輯器：選擇站點 ➔ 放置虛擬失物 ➔ 撰寫 3 條提示 ➔ 設定暗號 ➔ 產生統一 6 碼大寫英數【案件代碼】（例如 <code>TP8801</code>）。在學校發表會上，台下同學拿起手機輸入代碼，即可挑戰同儕設計的尋寶案件！
      </p>
    </div>

    <!-- 08｜跨平台畫面 UI、無障礙操作與後端資料庫架構 -->
    <div class="card">
      <h2>📱 08｜跨平台畫面 UI、無障礙操作與後端資料庫架構</h2>
      <ul>
        <li><strong>中央主畫面</strong>：3D 俯瞰立體街區，可互動店家與站牌具備發光標籤。</li>
        <li><strong>邊角 HUD</strong>：迷你雷達地圖、當前地點行政區、精力值、氣象與遊戲時間。</li>
        <li><strong>偵探手機快捷頁</strong>：案件簿、線索白板、人物通訊錄、三階提示、知識圖鑑、拍立得相簿，每一頁均可一秒返回現場。</li>
        <li><strong>跨平台與無障礙</strong>：支援電腦鍵盤 WASD + 手機觸控搖桿與點擊；支援繁體中文大字幕、色盲輔助標籤、不依賴顏色辨識之符號系統。</li>
        <li><strong>資料庫架構</strong>：本地 LocalStorage 保存探索進度，雲端資料庫（首解競賽）採用交易鎖防雙首解，確保公平公正。</li>
      </ul>
    </div>

    <!-- 09｜務實研發策略：第一版「垂直切片 (Vertical Slice)」與專案時程 -->
    <div class="card">
      <h2>🚀 09｜務實研發策略：第一版「垂直切片 (Vertical Slice)」與專案時程</h2>
      
      <div class="callout tip">
        <div class="callout-title">📐 什麼是垂直切片 (Vertical Slice)？</div>
        國小 8 週獨立研究時間有限，若一開始承諾做出 1:1 完整雙北所有街區將導致專案難產。因此先製作一個小規模但<strong>系統完整</strong>的精華切片：
        <strong>「1 條真實街道（台北車站周邊）+ 2 個公車站 + 1 個可進入學習場館 + 1 家小吃店 + 1 個多人可競速首解小案」</strong>，完整跑通核心循環！
      </div>

      <h3>📅 專案推進里程碑</h3>
      <ul>
        <li><strong>第一階段（第 1 ~ 2 週 / 目前進度）</strong>：企劃定案、三人小組分工、1:1 地理圖資規範確立與首解機制設計。</li>
        <li><strong>第二階段（第 3 ~ 4 週）</strong>：找 AI（志炫等）製作第一版垂直切片原型（街景移動、吃小吃回體力、第一個跳舞小人機關與後端首解驗證）。</li>
        <li><strong>第三階段（第 5 ~ 6 週）</strong>：公車捷運轉乘、四大機關完整實裝、雙軌商城與考據百科圖鑑上線。</li>
        <li><strong>第四階段（第 7 ~ 8 週）</strong>：邀請全班同學試玩與同儕編輯器測試，正式部署至 GitHub Pages 與 Itch.io，完成成果發表會！</li>
      </ul>
    </div>

    <!-- 10｜決策待辦清單、公平性保障與未來擴充指引 -->
    <div class="card">
      <h2>📋 10｜決策待辦清單、公平性保障與未來擴充指引</h2>
      <div class="feature-grid">
        <div class="feature-box">
          <h4>🗺️ 建築室內開放排程</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            四大古蹟、事務所與科教館建立獨特室內；一般商店採用共用模板。尚未開放之建築一律清楚標註「尚未開放探索」，避免玩家以為功能異常。
          </p>
        </div>
        <div class="feature-box">
          <h4>⚖️ 共享案件更新節奏</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            每 2~4 週發布 1 批新案件，限時案件到期後自動轉入「歷史懸案檔案庫」供玩家無限次回顧。
          </p>
        </div>
        <div class="feature-box">
          <h4>📶 發表會離線安全備案</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            若成果發表會現場 Wi-Fi 不穩，遊戲支援全離線預演模式，確保向評審老師與全班展示時 100% 穩定順暢！
          </p>
        </div>
        <div class="feature-box">
          <h4>🎨 原創美術與音效審查</h4>
          <p style="font-size:13px; color:var(--text-muted);">
            所有動漫致敬角色造型由組員進行原創像素重繪，環境音效採自製擬音或開源授權音庫，保障合法合規。
          </p>
        </div>
      </div>
    </div>

  </div>

  <!-- Toast 提示元件 -->
  <div id="toast">✅ 完整企劃書已複製到剪貼簿！可直接貼上至 LINE、Word 或 Google Docs！</div>

  <!-- 隱藏的超詳細純文字複製緩衝區 -->
  <textarea id="copyBuffer" style="position: absolute; left: -9999px; top: -9999px;"></textarea>

  <script>
    // Inject the complete plain-text markdown into the copyBuffer
    document.getElementById('copyBuffer').value = ${JSON.stringify(plainMarkdown.trim())};

    function copyFullProposal() {
      const buffer = document.getElementById('copyBuffer');
      const text = buffer.value.trim();

      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(showToast).catch(fallbackCopy);
      } else {
        fallbackCopy();
      }

      function fallbackCopy() {
        buffer.select();
        buffer.setSelectionRange(0, 99999);
        try {
          document.execCommand('copy');
          showToast();
        } catch (err) {
          alert('複製失敗，請手動全選複製。');
        }
      }
    }

    function showToast() {
      const toast = document.getElementById('toast');
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 3500);
    }
  </script>
</body>
</html>
`;

fs.writeFileSync(targetHtml, htmlContent, 'utf-8');
console.log('Successfully generated merged proposal.html! File size:', fs.statSync(targetHtml).size, 'bytes');
