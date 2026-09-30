# -*- coding: utf-8 -*-
import json
import os
import sys

from generate_proposal import cases_50, detailed_10_cases

output_html_path = os.path.join(os.path.dirname(__file__), 'proposal.html')

# 1. Build 50-Case Table HTML
case_rows_html = []
for c in cases_50:
    tag_color = "#dc2626" if "突發" in c["category"] else "#1d4ed8"
    case_rows_html.append(f"""
    <tr>
      <td style="font-weight:700; color:#1e293b;">{c['id']}</td>
      <td>
        <strong style="font-size:14.5px; color:#0f172a;">{c['title']}</strong><br>
        <span style="font-size:12px; color:{tag_color}; font-weight:700;">● {c['category']}</span>
      </td>
      <td style="font-size:13.5px; color:#334155;">{c['location']}</td>
      <td style="font-size:13px; color:#475569;">
        <strong>{c['homage']}</strong><br>
        <span style="color:#0284c7;">【科學原理】{c['science']}</span>
      </td>
      <td style="font-size:13px; color:#334155;">{c['synopsis']}</td>
    </tr>
    """)

cases_table_html = "\n".join(case_rows_html)

# 2. Build 10 Detailed Cases Cards HTML
detailed_cards_html = []
for d in detailed_10_cases:
    card_border_class = "conan" if "conan" in d["badge_class"] else "holmes"
    detailed_cards_html.append(f"""
    <div class="case-card {card_border_class}">
      <div class="case-header">
        <div class="case-title">
          <span>🔍</span> {d['id']}：{d['title']}
        </div>
        <span class="case-badge {d['badge_class']}">{d['homage_author']}</span>
      </div>
      <div class="case-body">
        <div class="case-section">
          <div class="case-label">📍 調查舞台與標記：</div>
          {d['stage']}
        </div>
        <div class="case-section">
          <div class="case-label">⚡ 觸發機制與現場狀態：</div>
          {d['trigger']}
        </div>
        <div class="case-section">
          <div class="case-label">⚙️ 調查互動、物證與機關解鎖：</div>
          {d['interact']}
        </div>
        <div class="codex-card">
          <div class="codex-header">📜 【名著與科學考據卡：{d['codex_title']}】</div>
          • <strong>原著出處</strong>：{d['codex_origin']}<br>
          • <strong>科學物理化學原理</strong>：{d['codex_science']}<br>
          • <strong>雙北在地文史結合</strong>：{d['codex_local']}
        </div>
      </div>
    </div>
    """)

detailed_cases_html_rendered = "\n".join(detailed_cards_html)

# 3. Build plainMarkdown for copyBuffer
case_md_list = []
for c in cases_50:
    case_md_list.append(f"- 【{c['id']}】{c['title']}（{c['category']}）| 地點：{c['location']} | 致敬/原理：{c['homage']}（{c['science']}）| 梗概：{c['synopsis']}")
cases_50_markdown = "\n".join(case_md_list)

detailed_10_markdown_list = []
for d in detailed_10_cases:
    detailed_10_markdown_list.append(f"""
### 【{d['id']}】{d['title']}（{d['type']}）
- 致敬來源：{d['homage_author']}
- 調查舞台：{d['stage']}
- 觸發情境：{d['trigger']}
- 調查解密：{d['interact']}
- 考據與科學原理：{d['codex_title']} | 出處：{d['codex_origin']} | 原理：{d['codex_science']} | 在地結合：{d['codex_local']}
""")
detailed_10_markdown = "\n".join(detailed_10_markdown_list)

plainMarkdown = f"""# 【六年級獨立研究專題】《雙北漫遊偵探：都會行蹤》完整遊戲設計企劃書（50宗大案 ✕ 10精選案例 ✕ AI生成模組 ✕ 實體到店 ✕ 突發事件 ✕ 共享世界競速 深度升級版）
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
   專案中引用與致敬之《名偵探柯南》、《福爾摩斯探案集》、《口袋神探》經典密碼與科學手法，以及雙北真實地標與大眾運輸系統（台北捷運、市區公車、YouBike 2.0），皆屬國小課程教學與學術探究之合理使用（Fair Use）。若公開發布上線，所有動漫人物外觀、插畫、UI 貼圖、捷運四語廣播與環境音樂，將全部由團隊原創繪製與錄製，不直接挪用受版權保護之動畫商業素材與官方錄音。
4. 嚴謹求實原則：
   刪除所有「保證全場最高分」等過度保證之宣傳詞，所有科學原理（光學投影/反射、聲學延遲、弱酸炭化、慣性定律、天平力矩）與在地史實皆通過嚴謹查證與修正。

============================================================
■ 01｜專案基本定位、核心精神與三人團隊深層分工
============================================================
【一句話定位】
《雙北漫遊偵探：都會行蹤》是一款以雙北為舞台的開放式探索推理遊戲：街區是連續的遊戲空間，案件是可選的冒險，學習內容藏在場所與微型互動裡。它不是只有四個封閉關卡、通關即結束的解謎遊戲，而是一座世界隨時持續運轉、案件不斷發生的無盡城市！

【核心理念與玩家體驗】
- 自由漫遊（動森式慢活）：玩家在原地操作角色，不必真的到現場；可以辦案，也可以完全不辦案，單純在雙北街區漫步、去淡水看夕陽、在超商喝飲料看雨景、回事務所整理相片佈置房間。
- 案件有結局，世界無終點：即使某個大案被全服首解破案歸檔，玩家依然可以繼續在雙北生活、打工、漫遊、拍照、或等待下一批新案件發生。
- 玩家自己決定下一站：新手教學不綁死固定動線，故事提供指引但不鎖死城市探索權限。每個可進入的地點至少具備「一項可互動的知識、一個觀察亮點、一個人物對話、一條線索或一個驚喜彩蛋」，絕不做空殼建築。

【三人研究團隊深度職責規劃】
1. 組員 1（組長 / 企劃總監）：
   - 世界觀設定、主支線劇本主筆與對話撰寫。
   - 研讀《名偵探柯南》、《福爾摩斯》與《口袋神探》，改編 50 宗科學與密碼機關，規劃未來 AI 提示詞工程。
   - 負責每案破案後「名著考據卡」與「微型知識講堂」內容撰寫，確保符合國小自然與社會課綱。
2. 組員 2（美術與圖資總監）：
   - 3D 俯瞰視角街景視覺標準制定，繪製 2D 復古像素角色、NPC 與雙北特色小吃道具。
   - 考察真實雙北地理，使用 OpenStreetMap (OSM) 開放圖資建立 1:1 道路尺度與建築外觀。
   - 制定建築進出發光標記圖案（門形、咖啡杯、小吃、超商、五金行、書本、博物館等）。
3. 組員 3（技術架構與機制總監）：
   - 規劃 3D/2D 混合引擎、WASD/行動端觸控操作、雙軌經濟數值平衡（破案賞金與生活流通金）。
   - 設計真實大眾交通費率演算法（公車段次緩衝區、捷運真實里程矩陣、YouBike 前 30 分鐘補助）。
   - 設計實體商店到店購買機制、伺服器端「共享世界唯一首解原子鎖定」與 AI 案件自動生成模組架構。

============================================================
■ 02 & 02A｜雙北連續世界、1:1 地理、建築進出圖案標記與大眾交通費率
============================================================
【1:1 現實地理結構】
- 地圖基礎：基於台北市與新北市真實道路、橋梁、河川、行政區、公車站牌、捷運路網與相對距離建模。
- 連續世界（非傳送門）：跨區不是瞬間切換黑畫面傳送，玩家可以沿著真實道路（如中正橋、台北橋、忠孝西路、新店溪沿岸）跨越行政區界步行，完全不設行政區步行空氣牆。

【★ 建築進出發光圖案標記系統（Enterable Building Markers）】
雙北包含數萬棟建築，為了兼顧 1:1 真實比例與清晰引導，遊戲嚴格區分建築類型：
1. 可進入建築（Enterable Buildings）：
   建築上方會浮現發光的動態圖案標籤：
   - 🚪 門形：偵探事務所、民宅、長廊入口
   - ☕ 咖啡杯：連鎖咖啡店（休憩、隨機觸發中毒突發事件）
   - 🍜 麵碗：台灣小吃店、餐廳（進店吃飯補滿精力值）
   - 🏪 超商：7-11/全家便利商店（實體購買電池、竹夾等現場耗材）
   - 🛠️ 板手螺絲：在地五金行、電子商場（實體購買手電筒、紫外光儀等工具）
   - 📚 書本：市立圖書館、書店（參與 1~3 分鐘微型知識講堂）
   - 🏛️ 神殿柱：博物館、古蹟展館（歷史探究、蓋紀念拓印章）
   靠近時畫面出現提示按鍵 [E] 或手機觸控點擊，即可推門進入專屬 2D/3D 室內場景。
2. 不可進入建築（Exterior Only）：
   建築上方無任何圖案標示，純作為真實雙北街景立面，不可進入，避免玩家盲目碰壁以為系統故障。

【多元大眾交通網絡與精確費率】
1. 步行 (Walking)：免費、無限制！玩家隨時可沿著雙北街道跨區漫遊。
2. 市區公車（主要大眾運輸工具）：走雙北真實路線與站牌，全票每段次 15 元生活金，按真實分段點與緩衝區計費。
3. 台北捷運 (Taipei Metro)：按起迄站官方票價查詢表扣款（$20 ~ $65），捷運站內播放經典四語廣播。
4. YouBike 2.0 公共自行車：4 小時內每 30 分鐘 10 元，雙北會員享有前 30 分鐘免費補助政策。

【時間、日夜與動態氣象雙軌制】
- 串接中央氣象署（CWA）API 每 15 分鐘同步天氣；雨天草地留下泥濘鞋印、屋簷落水聲掩蓋撞擊、雨傘滴水成為破案線索。
- 雙軌防卡關：提供離線預設模式，並將案件時間軸與現實解耦，防止玩家因現實中等不到下雨天而卡關。

============================================================
■ 03｜玩家遊玩流程：自由漫遊、動森式慢活與新手前 15 分鐘
============================================================
【★ 玩法自由原則：不必一直破案，放鬆慢活也是一種玩法】
- 不設死線：玩家完全不必有破案壓力，可以花一整天在淡水河岸看夕陽、坐在超商落地窗前喝珍奶看雨景。
- 居家天地：玩家也可以整天待在自己的偵探事務所/家裡，整理線索白板、更換服裝、泡茶放空。

【新手前 15 分鐘流暢引導】
1. 事務所誕生：在老街閣樓甦醒，熟悉 WASD 走動與手機線索簿操作。
2. 門口無門檻失物委託：事務所門口老爺爺鑰匙遺失案（花費 0 元，觀察刮痕、訪談鄰居、推論喜鵲叼走鑰匙）。
3. 獎勵與自由啟程：獲得初始生活金 100 元、密碼鑑識知識卡與雙北地圖，自主決定下一站。

============================================================
■ 04｜案件體系重大擴充：50 宗大案全景矩陣、10 大精選深度案例與 AI 案件生成模組
============================================================
【50 宗雙北推理案件主題分類全景矩陣】
{cases_50_markdown}

【10 宗精選深度案例完整檔案（含致敬、科學考據與在地結合）】
{detailed_10_markdown}

【★ 未來 AI 案件生成模組架構（AI Case Generator Engine）】
為了實現「永不結束的推理世界」，系統設計了標準化 AI 案件生成介面：
1. 標準 JSON 案件資料格式（Schema）：
   {{
     "case_id": "CASE-AI-0101",
     "title": "大稻埕布莊消失的藍染布",
     "type": "dynamic_event | shared_speedrun | personal_quest",
     "location": {{
       "name": "迪化街一段傳統布莊",
       "district": "大同區",
       "coordinates": [25.0565, 121.5098],
       "enterable_marker": "store"
     }},
     "trigger_condition": {{
       "event_type": "enter_store | walk_nearby | server_broadcast",
       "probability": 0.35,
       "cooldown_minutes": 60
     }},
     "npcs": [
       {{"id": "npc_01", "name": "布莊老闆娘", "dialogue": "這塊布原本浸在染缸裡，怎麼突然變成白色了？"}},
       {{"id": "npc_02", "name": "路過染工", "dialogue": "我剛才聞到一股微弱的雙氧水味道..."}}
     ],
     "clues": [
       {{"id": "clue_01", "type": "physical", "name": "白色染布纖維", "science_note": "氧化還原褪色反應"}},
       {{"id": "clue_02", "type": "testimony", "name": "監視器時間戳", "science_note": "14:15 有人攜帶噴霧瓶進入"}}
     ],
     "reasoning_graph": {{
       "motive": "盜取隱藏在布料纖維中的高價染料",
       "method": "利用還原劑使靛藍暫時無色化",
       "contradiction": "嫌犯衣服口袋殘留雙氧水試劑瓶"
     }},
     "verification_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
   }}
2. AI 自動生成工作流（AI Generation Pipeline）：
   - 由 AI Agent（如志炫 / 雲端大模型）根據雙北 OSM 地理圖資、台灣中小學自然科學課綱概念、與名著推理核心手法自動組合。
   - 經邏輯自洽性驗證後，由後端動態注入案件資料庫，實現定期甚至每日自動推出全新突發與全服案件！

============================================================
■ 04A｜共享世界體系：突發事件、全服搶案同步結束 vs 個人晉升任務
============================================================
【★ 突發事件觸發機制（Dynamic Events）】
- 不定時隨機觸發：案件不一定全數事先標在地圖上。當玩家在咖啡店用餐、搭公車、逛超商時，可能突發意外（例如客人咖啡被下毒、公車急煞調包）。
- 現場即時封鎖：觸發瞬間門窗拉下封鎖，進入 20~25 分鐘限時現場調查，身歷其境宛如柯南附體！

【★ 全服共享公開案件（Shared Public Cases）】
- 全體玩家在同一世界同步看到。
- 支援組隊合作與全服首解競速搶案。
- 【全服同步結束機制】：一旦任何玩家成功提交完整推理驗證，或限時倒數結束，伺服器立即發布全服快訊，所有玩家畫面上的該案件「同步結束」，自動歸檔至「歷史檔案室（不計分回顧模式）」。

【★ 個人專屬晉升任務（Personal Milestone Quests）】
- 專屬每位玩家的個人成就與能力進階（例如新手任務：破獲任意 3 個案件晉升階級、取得特定道具）。
- 解鎖條件：需要累積「個人人際信賴度（與特定 NPC 熟識）」或「觸發特定街道彩蛋（如遇見黑貓阿巧）」。
- 【無搶任務機制】：每位玩家的個人任務進度完全獨立，人人平等，自己按節奏一個一個往上解，絕不會被其他玩家搶走！

============================================================
■ 05｜場所互動、短時微型學習手冊與台味隱藏彩蛋
============================================================
【1~3 分鐘微型學習講堂（拒絕枯燥講義）】
1. 士林科教館：操作光影折射與熱敏顯影模擬槽，解鎖「熱敏鑑識知識卡」。
2. 北市圖總館：英文字母頻率對照練習小遊戲，解鎖「密碼速查字典」。
3. 淡水海關故事館：判讀 1860 年代英國商船航海日誌，解鎖老船長文史對話。
4. 新北市圖總館：日晷測時法與相似三角形影子長度測量模擬器，解鎖日影幾何量角器。

【雙北街頭四大特色彩蛋 (Easter Eggs)】
1. 創作團隊客串彩蛋：台北車站巷弄豆漿店角落，坐著三位六年級獨立研究學生 NPC，筆電上正開著這本企劃書與 AI 程式碼，幽默感謝所有玩家試玩！
2. 淡水老街黑貓「阿巧」：在淡水紅磚巷弄餵牠吃一顆魚丸，阿巧會喵喵叫帶你穿過防空洞，指引出牆面上的隱藏經緯度座標暗號！
3. 台北 101 屋頂秘密展望台：完成特定支線後獲得天台鑰匙，在晴朗夜間可登上 101 屋頂飽覽大台北 3D 星空與萬家燈火全景。
4. 名著致敬彩蛋站牌貼紙：雙北某個公車站牌角落，悄悄貼著「221B 貝克街」與「米花町五丁目」的復古公車路線貼紙，向柯南與福爾摩斯致敬！

============================================================
■ 06｜生活慢活、真實實體商店到店購買機制、雙軌貨幣與無障礙防卡關
============================================================
【★ 真實實體商店到店購買機制（Real In-Store Shopping）】
- 拒絕隔空網購直送！偵探必須親自走到街道真實存在的實體店面推門進去購買：
  1. 便利超商（7-11 / 全家 / 萊爾富）：加長竹夾 ($35)、3號電池組 ($50)、小包食鹽 ($15)、石蕊試紙 ($30)、礦泉水 ($20)、熱拿鐵 ($45)。
  2. 在地五金行 / 雜貨店（太原路 / 萬華五金街）：高精度鋼捲尺 ($80)、高流明 LED 手電筒 ($120)、防靜電鑷子 ($45)、棉線與滑輪組 ($65)。
  3. 大稻埕百年中藥行（迪化街）：紫甘藍萃取試劑 ($50)、天然白芷粉末 ($40)、精密天平免費借用。
  4. 光華數位新天地 / 三創園區：便攜紫外光鑑識筆 (400 偵探幣)、改裝高扭力滑板 (500 偵探幣)、高靈敏定向降噪錄音筆 (350 偵探幣)。
  5. 捷運站服務處 / 悠遊卡加值機：悠遊卡查詢與生活金加值、購買捷運一日票 ($150)。

【偵探精力值系統與台灣小吃回血】
奔跑與調查消耗精力值；在事務所沙發休息、超商飲水機皆可免費回滿精力；進店品嚐淡水阿給魚丸湯、北投排骨酥麵、珍奶、永和豆漿油條回血。

【雙軌貨幣體系】
1. 破案委託賞金 (Detective Coins)：破獲主支線大案、解開名著經典機關獲得，用於購買永久加速裝備與外觀。
2. 日常生活流通金 (Daily Cash)：每日生活津貼、街頭小委託、超商打工獲得，用於搭車、實體店買材料、小吃吃飯。

【絕對不卡死 (Anti-Softlock) 與無障礙三階提示】
生活金花光依然可以免費步行、事務所免費休息、街頭做資源回收賺車資。第 1 階提示免費；第 2、3 階提示提供「等待 5 分鐘冷卻」或「完成指定環境觀察」之免費解鎖管道。

============================================================
■ 07｜城市動態 NPC 作息、社區信賴度與班級案件工作坊
============================================================
- NPC 動態作息：晨運長輩、午後上班族、黃昏夜市攤販，不同時段訪談獲不同零碎線索。
- 社區信賴度互動：隨手扶起倒下的 YouBike、協助長輩過馬路、隨手做資源回收，提升信賴度獲得小吃店阿姨免費招待與隱藏八卦。
- 班級案件工作坊：內建極簡案件編輯器，產生 6 碼大寫英數代碼（如 TP8801），全班同學輸入代碼即可挑戰彼此設計的自製案件！

============================================================
■ 08｜跨平台畫面 UI、無障礙操作與後端資料庫架構
============================================================
- 3D 俯瞰街道 + 2D 像素主角 + 邊角 HUD + 智慧型手機多功能選單（案件簿、線索白板、通訊錄、三階提示、相簿）。
- 支援電腦鍵盤 WASD + 手機觸控搖桿與點擊；支援繁中大字幕、色盲輔助標籤。
- 伺服器端採用 Transaction Row Lock 防止雙首解，保障全服競賽絕對公平。

============================================================
■ 09｜務實研發策略：第一版「垂直切片 (Vertical Slice)」與專案時程
============================================================
- 垂直切片策略：先開放 1 條真實街道（台北車站周邊）+ 2 個公車站 + 1 個可進入學習館舍 + 1 家小吃店 + 1 個多人可競速首解小案，完整跑通核心循環。
- 8 週推進里程碑：第 1~2 週企劃定案與圖資規範 ➔ 第 3~4 週垂直切片原型製作 ➔ 第 5~6 週交通轉乘、四大機關與實體商店實裝 ➔ 第 7~8 週全班試玩與成果發表會。

============================================================
■ 10｜決策待辦清單、公平性保障與未來擴充指引
============================================================
- 建築室內開放排程（獨特室內 vs 共用模板，未開放明確標記「尚未開放」）。
- 共享案件發布頻率（每 2~4 週發布 1 批，到期轉入歷史懸案檔案庫）。
- 發表會離線安全備案（若展場 Wi-Fi 不穩，支援全離線預演模式）。
- 原創美術與音效審查（動漫致敬元素全部原創繪製，合法合規）。
"""

# Now build the full HTML document string
html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>《雙北漫遊偵探：都會行蹤》完整遊戲設計企劃書（50大案 ✕ AI生成 ✕ 實體到店 ✕ 突發事件 深度升級版）- 六年級獨立研究專題</title>
  <style>
    :root {{
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
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", "Noto Sans TC", sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.7;
      padding: 24px 16px 120px;
    }}

    .container {{
      max-width: 1000px;
      margin: 0 auto;
    }}

    /* 頂部操作列 */
    .top-action-bar {{
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
    }}

    .project-tag {{
      font-size: 13px;
      font-weight: 800;
      color: var(--primary);
      background: var(--primary-light);
      padding: 5px 12px;
      border-radius: 20px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .btn-group {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}

    button, .btn-link {{
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
    }}

    .btn-primary {{
      background-color: var(--primary);
      color: white;
    }}

    .btn-primary:hover {{
      background-color: var(--primary-dark);
      transform: translateY(-1px);
    }}

    .btn-secondary {{
      background-color: #f8fafc;
      color: var(--text);
      border: 1px solid var(--border);
    }}

    .btn-secondary:hover {{
      background-color: #e2e8f0;
    }}

    /* 大標題卡片 */
    .header-card {{
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%);
      color: white;
      border-radius: var(--radius);
      padding: 38px 34px;
      margin-bottom: 26px;
      box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.3);
    }}

    .header-card h1 {{
      font-size: 27px;
      font-weight: 800;
      margin-bottom: 12px;
      letter-spacing: -0.5px;
      line-height: 1.35;
    }}

    .header-card .subtitle {{
      font-size: 15px;
      opacity: 0.94;
      margin-bottom: 20px;
      line-height: 1.6;
    }}

    .meta-badges {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .meta-badge {{
      background: rgba(255, 255, 255, 0.18);
      border: 1px solid rgba(255, 255, 255, 0.35);
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}

    /* 免責聲明卡片 */
    .disclaimer-card {{
      background: #fff1f2;
      border: 2px solid #f43f5e;
      border-radius: var(--radius);
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
    }}

    .disclaimer-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 800;
      font-size: 16px;
      color: #be123c;
      margin-bottom: 10px;
    }}

    .disclaimer-text {{
      font-size: 13.5px;
      color: #881337;
      margin-bottom: 8px;
      line-height: 1.65;
    }}

    /* 內容卡片 */
    .card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      padding: 30px;
      margin-bottom: 26px;
      box-shadow: var(--shadow);
    }}

    .card h2 {{
      font-size: 21px;
      color: #0f172a;
      margin-bottom: 18px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .card h3 {{
      font-size: 17px;
      color: #1e293b;
      margin: 22px 0 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    p {{
      margin-bottom: 14px;
      color: #334155;
      font-size: 15px;
      line-height: 1.7;
    }}

    ul, ol {{
      margin-left: 22px;
      margin-bottom: 16px;
      color: #334155;
    }}

    li {{
      margin-bottom: 8px;
      font-size: 14.5px;
      line-height: 1.65;
    }}

    /* 表格樣式 */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 18px 0;
      font-size: 14px;
    }}

    th, td {{
      border: 1px solid var(--border);
      padding: 10px 12px;
      text-align: left;
      vertical-align: top;
    }}

    th {{
      background-color: #f8fafc;
      font-weight: 700;
      color: #1e293b;
    }}

    /* 團隊角色卡片 */
    .team-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 18px 0;
    }}

    .team-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
      border-top: 4px solid var(--primary);
    }}

    .team-role {{
      font-size: 12px;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 4px;
      letter-spacing: 0.5px;
    }}

    .team-name {{
      font-size: 16px;
      font-weight: 800;
      margin-bottom: 10px;
      color: #0f172a;
    }}

    .team-duty {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.65;
    }}

    /* 機關案例文獻卡片 */
    .case-container {{
      display: flex;
      flex-direction: column;
      gap: 22px;
      margin: 20px 0;
    }}

    .case-card {{
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      background: #ffffff;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      overflow: hidden;
      border-left: 6px solid var(--primary);
    }}

    .case-card.conan {{ border-left-color: var(--conan-red); }}
    .case-card.holmes {{ border-left-color: var(--holmes-gold); }}

    .case-header {{
      padding: 16px 20px;
      background: #f8fafc;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .case-title {{
      font-size: 16.5px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .case-badge {{
      font-size: 12px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 20px;
    }}

    .badge-conan {{ background: #fee2e2; color: var(--conan-red); border: 1px solid #fca5a5; }}
    .badge-holmes {{ background: #fef3c7; color: var(--holmes-gold); border: 1px solid #fcd34d; }}

    .case-body {{ padding: 20px; }}
    .case-section {{ margin-bottom: 12px; font-size: 14.5px; }}
    .case-label {{ font-weight: 700; color: #1e293b; font-size: 14px; margin-bottom: 4px; display: inline-flex; align-items: center; gap: 6px; }}

    .codex-card {{
      background: #fdf6ec;
      border: 1px dashed #d97706;
      border-radius: 8px;
      padding: 14px 16px;
      margin-top: 12px;
      font-size: 13.5px;
      color: #78350f;
      line-height: 1.65;
    }}

    .codex-header {{
      font-weight: 800;
      font-size: 14px;
      color: #92400e;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* 亮點提示區塊 */
    .callout {{
      background-color: var(--primary-light);
      border-left: 4px solid var(--primary);
      padding: 16px 20px;
      border-radius: 0 8px 8px 0;
      margin: 18px 0;
      font-size: 14.5px;
      line-height: 1.65;
    }}

    .callout.tip {{ background-color: #ecfdf5; border-left-color: var(--success); }}
    .callout.accent {{ background-color: #fffbeb; border-left-color: var(--accent); }}
    .callout.purple {{ background-color: #f5f3ff; border-left-color: var(--purple); }}

    .callout-title {{
      font-weight: 800;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* 網格系統 */
    .feature-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 18px 0;
    }}

    .feature-box {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
    }}

    .feature-box h4 {{
      font-size: 15.5px;
      color: #0f172a;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* 程式碼區塊 */
    pre {{
      background: #0f172a;
      color: #f8fafc;
      padding: 16px;
      border-radius: 8px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 13px;
      overflow-x: auto;
      line-height: 1.5;
      margin: 14px 0;
    }}

    /* Toast 浮動提示 */
    #toast {{
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
    }}

    #toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    @media print {{
      body {{ background: white; padding: 0; }}
      .top-action-bar, #toast {{ display: none !important; }}
      .card {{ box-shadow: none; border: 1px solid #bbb; page-break-inside: avoid; margin-bottom: 18px; padding: 18px; }}
      .header-card {{ background: #1e3a8a !important; color: white !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    }}
  </style>
</head>
<body>

  <div class="container">

    <!-- 頂部快速操作列 -->
    <div class="top-action-bar">
      <div class="project-tag">
        <span>🔍</span> 六年級獨立研究深度企劃書（50宗大案 ✕ AI生成 ✕ 實體到店 深度升級版）
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
        1:1 連續雙北地圖 ✕ 50宗推理案件庫 ✕ AI自動擴充架構 ✕ 實體到店購買 ✕ 突發事件 ✕ 共享世界競速 ✕ 《動物森友會》式慢活
      </div>
      <div class="meta-badges">
        <span class="meta-badge">👥 專案團隊：國小六年級獨立研究小組（三人團隊）</span>
        <span class="meta-badge">🗺️ 地理架構：1:1 連續雙北（OpenStreetMap + 建築進出發光標記）</span>
        <span class="meta-badge">🔍 案件庫規模：50 宗大案全景矩陣 ＋ 10 宗精選深度案例</span>
        <span class="meta-badge">🤖 擴充機制：未來 AI Agent 自動生成案件模組（永不結束）</span>
        <span class="meta-badge">⚡ 觸發體驗：不定時突發事件（如咖啡店下毒密室）</span>
        <span class="meta-badge">🌐 雙軌體系：全服同步結束搶案機制 vs 個人專屬晉升任務（無搶奪）</span>
        <span class="meta-badge">🏪 實體商店：親自走到真實街道店家購買耗材與高階裝備</span>
        <span class="meta-badge">🎨 視覺美學：3D 空中俯瞰街景 + 2D 復古像素主角</span>
        <span class="meta-badge">💰 經濟雙軌：破案委託賞金 vs 日常生活流通金</span>
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
        2. <strong>名著、地標商標與公共音效原創規範</strong>：專案中所引述致敬之《名偵探柯南》、《福爾摩斯探案集》、《口袋神探》經典密碼與科學手法，以及台灣真實大眾運輸（台北捷運、市區公車、YouBike）、真實地標景點名稱，皆僅作為國小教學研究、科學物理探究與遊戲體驗設計之<strong>合理使用（Fair Use）</strong>。公開發布時，所有美術立繪、像素角色、UI、捷運廣播與背景音樂，皆採<strong>原創繪製與自製錄音</strong>，不直接套用版權動畫素材。
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
        《雙北漫遊偵探：都會行蹤》是一款以雙北為舞台的開放式探索推理遊戲：<strong>街區是連續的遊戲空間，案件是可選的冒險，學習內容藏在場所與微型互動裡</strong>。它不是只有四個封閉關卡、通關即結束的解謎遊戲，而是一座世界隨時持續運轉、案件源源不絕的無盡城市！
      </div>

      <h3>🎯 核心體驗與玩家可做的事</h3>
      <ul>
        <li><strong>人不用真的到現場</strong>：玩家在電腦前用鍵盤或手機搖桿操作角色，在虛擬的台北市與新北市街頭奔馳，身歷其境。</li>
        <li><strong>自主漫遊與生活（動森式慢活）</strong>：可以辦案，也可以完全不照主線走。跨區散步、搭乘公車、進店家吃小吃回體力、在事務所整理線索相片、或是坐在便利超商看雨景放空。</li>
        <li><strong>案件永不結束</strong>：遊戲內建 50 宗大案全景矩陣，並預留未來 AI 自動生成模組介面，打破「破完 4 個案子就沒得玩」的遺憾！</li>
        <li><strong>不定時突發狀況</strong>：打破常規「接單再破案」，走進咖啡店用餐時，隔壁桌客人可能突然中毒，秒變柯南突發密室調查現場！</li>
        <li><strong>深度調查與科學解密</strong>：調查現場物件、訪問不同時段出沒的居民 NPC、比對時間線、解開經典物理化學機關，提交完整推理。</li>
        <li><strong>最核心設計原則</strong>：<strong>玩家自己決定下一站！</strong>教學不綁死順序，故事提供方向但不鎖死整座城市。每個可進入地點至少有一件值得做的事。</li>
      </ul>

      <h3>👥 三人研究團隊詳細職責規劃</h3>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-role">組員 1（組長 / 企劃總監）</div>
          <div class="team-name">世界觀設定、劇本與知識編寫</div>
          <div class="team-duty">
            • 統籌專案整體目標與進度。<br>
            • 研讀《名偵探柯南》、《福爾摩斯》與《口袋神探》，編寫 50 宗大案劇本，規劃未來 AI 案件提示詞工程。<br>
            • 編寫雙北生活圈委託、NPC 對話、破案後的「名著考據卡」與「微型知識講堂」文案，緊扣國小課綱。
          </div>
        </div>
        <div class="team-card">
          <div class="team-role">組員 2（美術與圖資總監）</div>
          <div class="team-name">視覺風格、街區尺度與建築標記</div>
          <div class="team-duty">
            • 制定 45°~60° 3D 俯瞰視角立體街景美學與 2D 復古像素主角/NPC 造型。<br>
            • 考察真實雙北地理，使用 OpenStreetMap (OSM) 開放圖資建立 1:1 道路尺度與建築外觀。<br>
            • 繪製建築進出發光標記（門形 🚪、咖啡 ☕、小吃 🍜、超商 🏪、五金行 🛠️ 等）與小吃道具圖示。
          </div>
        </div>
        <div class="team-card">
          <div class="team-role">組員 3（技術架構與機制總監）</div>
          <div class="team-name">引擎架構、經濟平衡與 AI 協同</div>
          <div class="team-duty">
            • 規劃「3D 俯瞰街道 + 2D 像素小人」移動手感、手機觸控操作與鍵盤支援。<br>
            • 設計實體到店購買機制、大眾交通費率演算法（公車段次緩衝區、捷運票價矩陣、YouBike 補助）。<br>
            • 設計伺服器端「唯一首解原子鎖定」、全服同步結束機制與未來 AI 自動生成案件資料格式（JSON Schema）。
          </div>
        </div>
      </div>
    </div>

    <!-- 02 & 02A｜雙北連續世界、1:1 地理、建築進出圖案標記與大眾交通費率 -->
    <div class="card">
      <h2>🏙️ 02 & 02A｜雙北連續世界、1:1 地理、建築進出圖案標記與真實大眾交通費率建模</h2>

      <h3>1. 1:1 現實地理與無縫連續城市</h3>
      <p>
        雙北地圖以台北市與新北市的真實道路、橋梁、河川、行政區、公車站點、捷運站與相對距離為基礎。<strong>這是一座連續的城市，絕不把區域濃縮成幾個互不相連的關卡傳送門！</strong>
      </p>
      <ul>
        <li><strong>沿道路跨區步行</strong>：即使穿越行政區界（例如台北市中正區跨越中正橋進入新北市永和區、或是跨越大漢溪進入板橋），玩家都能沿著現實街道步行前進，完全不設行政區邊界空氣牆。</li>
        <li><strong>圖資來源與開源合規</strong>：地圖底層採用 OpenStreetMap（OSM）道路與建物圖資，搭配政府交通開放資料平台（TDX/PTX）。嚴格遵守 ODbL 開源協議與署名規範。</li>
      </ul>

      <h3>2. ★ 建築進出發光圖案標記系統（Enterable Building Markers）</h3>
      <p>
        在 1:1 龐大的雙北地圖中，建築物數以萬計。為了避免玩家盲目對著每棟房子碰壁撞牆，系統建立了直覺的<strong>視覺標示機制</strong>：
      </p>
      <div class="feature-grid">
        <div class="feature-box">
          <h4>🚪 可進入建築（上方顯示發光專屬 Icon）</h4>
          <p style="font-size:13.5px; color:var(--text-muted); margin-bottom:6px;">
            凡是具備室內場景、可探索學習或互動的場所，建築大門上方會懸浮<strong>發光動態圖案標籤</strong>：
          </p>
          <ul style="font-size:13px; margin-bottom:0;">
            <li><strong>🚪 門形標記</strong>：事務所基地、住宅公寓、地下街長廊入口</li>
            <li><strong>☕ 咖啡杯</strong>：咖啡店（慢活、隨機觸發中毒突發事件）</li>
            <li><strong>🍜 麵碗</strong>：小吃攤、食堂（吃飯補滿偵探精力值）</li>
            <li><strong>🏪 便利商店</strong>：7-11/全家（實體購買電池、竹夾等現場耗材）</li>
            <li><strong>🛠️ 板手螺絲</strong>：在地五金行、電子零件行（購買手電筒、紫外光燈）</li>
            <li><strong>📚 書本</strong>：圖書館、書店（參與 1~3 分鐘微型知識講堂）</li>
            <li><strong>🏛️ 神殿柱</strong>：博物館、古蹟展館（歷史探究、蓋紀念拓印章）</li>
          </ul>
          <p style="font-size:13px; color:var(--primary); font-weight:700; margin-top:8px; margin-bottom:0;">
            👉 靠近時畫面會彈出 [E] 鍵提示（手機版為觸控點擊），即可推門走進室內！
          </p>
        </div>
        <div class="feature-box">
          <h4>🏢 不可進入建築（無任何圖案標示）</h4>
          <p style="font-size:13.5px; color:var(--text-muted);">
            一般的民宅大樓、辦公大樓與純街景建築，<strong>大門上方不會顯示任何圖案</strong>。<br><br>
            這類建築作為寫實的 1:1 雙北街景 3D 外觀立面，玩家經過時不可穿透、不可進入，視覺一目了然，徹底防止迷茫碰壁！
          </p>
        </div>
      </div>

      <h3>3. 公車為主，捷運、YouBike 與步行四軌並行</h3>
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

      <h3>4. 時間、日夜與動態氣象雙軌制</h3>
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

    <!-- 03｜玩家遊玩流程：自由漫遊、動森式慢活與新手前 15 分鐘 -->
    <div class="card">
      <h2>🍃 03｜玩家遊玩流程：自由漫遊、動森式慢活與新手前 15 分鐘</h2>

      <div class="callout tip">
        <div class="callout-title">🍃 像《動物森友會》一樣放鬆——不一定要一直破案！</div>
        傳統推理遊戲常強迫玩家「被命案追著跑」，本遊戲打破限制：
        <ul style="margin-top:6px; margin-bottom:0;">
          <li><strong>隨心漫遊的都會時光</strong>：你可以花一整天在淡水老街河岸散步吹風、坐在咖啡店戶外露天座看路人通勤、在超商喝珍奶看雨景。</li>
          <li><strong>溫馨事務所基地</strong>：玩家<strong>也可以選擇整天待在自己的事務所/家裡放空</strong>！在房間裡泡茶聽收音機、更換衣櫃服裝、整理相片軟木板，享受無壓力的都會慢活生活。</li>
        </ul>
      </div>

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
        自主選擇目標或閒逛 ➔ 步行散步或搭乘公車/捷運 ➔ 抵達街區觀察街景、拍照、進館學習 ➔ 收集物件證詞並破解名著經典機關 ➔ 提交推理獲得原理解析、考據卡與獎金 ➔ 自由選擇去下一區、接下一案、或是回事務所裝飾房間泡茶慢活。
      </div>
    </div>

    <!-- 04｜案件體系重大擴充：50 宗大案全景矩陣、10 大精選深度案例與 AI 案件生成模組 -->
    <div class="card">
      <h2>🔍 04｜案件體系重大擴充：50 宗大案全景矩陣、10 大精選深度案例與 AI 案件生成模組</h2>
      
      <p>
        本遊戲絕非「只有 4 個案件、通關就結束」的封閉小遊戲！我們預設規劃了<strong>完整的 50 宗雙北推理案件庫全景矩陣</strong>，涵蓋名著經典致敬、中小學自然科學課綱原理、與雙北 29 個行政區在地文史：
      </p>

      <h3>📋 50 宗雙北推理案件全景矩陣表（點擊可展開對照）</h3>
      <div style="overflow-x:auto; max-height:480px; overflow-y:auto; border:1px solid var(--border); border-radius:8px; margin:16px 0;">
        <table>
          <thead>
            <tr>
              <th style="width:10%;">編號</th>
              <th style="width:25%;">案件名稱與類型</th>
              <th style="width:20%;">雙北真實舞台</th>
              <th style="width:25%;">致敬作品與科學原理</th>
              <th style="width:20%;">核心案件梗概</th>
            </tr>
          </thead>
          <tbody>
            {cases_table_html}
          </tbody>
        </table>
      </div>

      <h3>🌟 10 大精選深度案例完整檔案（含致敬、科學考據與在地結合）</h3>
      <p style="font-size:14px; color:var(--text-muted);">
        以下 10 宗案件為第一期深度實裝之核心案例，每宗皆具備完整現場搜查、科學/物理/化學原理考據與名著解析卡：
      </p>
      <div class="case-container">
        {detailed_cases_html_rendered}
      </div>

      <h3>🤖 ★ 未來 AI 案件生成模組架構（AI Case Generator Engine）</h3>
      <div class="callout purple">
        <div class="callout-title">🧠 永不結束的城市：串接 AI 自動生成無盡案件！</div>
        為了讓遊戲「隨時能新增案件、永遠玩不膩」，專案建立了標準化的 <strong>AI 案件生成協議（JSON Schema）</strong>。未來只要將大語言模型（如志炫 / Antigravity Agent）串接至後端，AI 便能自動讀取雙北實體街景與中小學自然科概念，源源不絕產出新案件！
      </div>

      <pre><code>// 【AI 案件生成標準 JSON 資料格式規範】
{{
  "case_id": "CASE-AI-0105",
  "title": "大稻埕中藥行消失的藏紅花",
  "type": "dynamic_event", // dynamic_event (突發) | shared_speedrun (全服競速) | personal_quest (個人晉升)
  "location": {{
    "name": "迪化街百年中藥行",
    "district": "大同區",
    "coordinates": [25.0565, 121.5098],
    "enterable_marker": "store" // 必須對應實體可進入標記
  }},
  "trigger_condition": {{
    "event_type": "enter_building", // 走進店內用餐或購買時觸發
    "cooldown_minutes": 45
  }},
  "npcs": [
    {{"id": "npc_01", "name": "老掌櫃", "dialogue": "剛剛隔壁桌客人撞了一下櫃檯，展示罐就不見了！"}},
    {{"id": "npc_02", "name": "外送員", "dialogue": "我剛才看見有人把黃色粉末倒進了水溝..."}}
  ],
  "clues": [
    {{"id": "clue_01", "name": "黃色水溶痕跡", "science_note": "水溶性藏紅花素光學吸收光譜"}},
    {{"id": "clue_02", "name": "天平砝碼刮痕", "science_note": "假砝碼重心偏置槓桿原理"}}
  ],
  "reasoning_graph": {{
    "motive": "調包昂貴中藥材謀利",
    "method": "利用染色薑黃粉冒充真品",
    "contradiction": "薑黃不溶於水而藏紅花快速溶解呈金黃色"
  }},
  "verification_hash": "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
}}</code></pre>
    </div>

    <!-- 04A｜共享世界體系：突發事件、全服搶案同步結束 vs 個人晉升任務 -->
    <div class="card">
      <h2>🌐 04A｜共享世界體系：突發事件、全服搶案同步結束 vs 個人晉升任務</h2>

      <h3>1. ⚡ 不定時突發事件（Dynamic Events）—— 柯南式用餐遭遇！</h3>
      <div class="callout accent">
        <div class="callout-title">☕ 誰說破案一定要事先接單？</div>
        如同《名偵探柯南》中柯南去咖啡店吃三明治必遇命案，本遊戲設計了逼真的<strong>「街頭突發事件」</strong>：
        <ul style="margin-top:6px; margin-bottom:0;">
          <li><strong>不定時隨機觸發</strong>：玩家在咖啡店用餐、搭乘 307 公車、或在便利超商買飲料時，可能無預警遭遇鄰桌客人中毒、錢包調包等緊急事件。</li>
          <li><strong>現場立即封鎖</strong>：突發瞬間鐵捲門拉下或公車靠邊停駛，現場進入 20~25 分鐘限時排查，代入感極強！</li>
        </ul>
      </div>

      <h3>2. 🏆 全服共享公開案件（Shared Public Cases）—— 全服同步結束機制！</h3>
      <ul>
        <li><strong>同一個在線雙北</strong>：所有人登入同一個在線城市，所有人看到的共享案件數量、內容與倒數計時<strong>完全同步</strong>。</li>
        <li><strong>合作與競速搶案</strong>：同學們可以組隊分工調查，也可以競速爭奪全服唯一首解榮譽與高額破案賞金。</li>
        <li><strong>【全服同步結束】</strong>：<strong>一旦任何一名玩家率先向伺服器提交了正確且完整的推理驗證，或者案件時限倒數結束，伺服器會立即發布全服號外廣播，全服所有玩家的該案件畫面「同步結束」</strong>！已結案案件自動轉入「歷史檔案室」，其他玩家仍可不計分回顧劇情，維護世界的時間流動感。</li>
      </ul>

      <h3>3. 🎖️ 個人專屬晉升任務（Personal Milestone Quests）—— 無搶任務機制！</h3>
      <div class="callout tip">
        <div class="callout-title">🛡️ 專屬於你自己的成長線——絕對沒有搶任務！</div>
        除了全服競爭的公開案件外，遊戲擁有平行的<strong>「個人偵探晉升與主線委託」</strong>體系：
        <ul style="margin-top:6px; margin-bottom:0;">
          <li><strong>任務獨立推進</strong>：例如「新手偵探認證：破獲任意 3 起案件」、「大稻埕里長委託：收集 3 張中藥百科卡」。每個人的任務進度各自累積，<strong>沒有任何人可以搶走你的任務</strong>！</li>
          <li><strong>人脈與彩蛋解鎖</strong>：部分特殊個人任務需要達成「特定 NPC 社區信賴度」（如與早餐店阿姨熟識），或「觸發街道特殊彩蛋」（如遇見黑貓阿巧）才能開啟接取。</li>
        </ul>
      </div>
    </div>

    <!-- 05｜場所互動、短時微型學習手冊與台味隱藏彩蛋 -->
    <div class="card">
      <h2>🏛️ 05｜場所互動、短時微型學習手冊與台味隱藏彩蛋</h2>

      <h3>1. 把學習做成 1~3 分鐘微型互動（拒絕一整頁枯燥講義）</h3>
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

    <!-- 06｜生活慢活、真實實體商店到店購買機制、雙軌貨幣與無障礙防卡關 -->
    <div class="card">
      <h2>🏪 06｜生活慢活、真實實體商店到店購買機制、雙軌貨幣與無障礙防卡關</h2>

      <h3>1. ★ 真實實體商店到店購買機制（拒絕隔空網購直送！）</h3>
      <div class="callout tip">
        <strong>🚶 必須親自用雙腳或搭車走到實體店面！</strong><br>
        就像現實中的偵探一樣，你不能在案發現場按個按鈕就空投道具。玩家必須打開地圖，步行或搭公車走到街角的<strong>真實實體店</strong>，推門進去站在櫃檯前才能購買：
      </div>

      <table>
        <thead>
          <tr>
            <th style="width: 22%;">真實實體商店類型</th>
            <th style="width: 26%;">雙北代表街區地點</th>
            <th style="width: 32%;">現場販售道具清單</th>
            <th style="width: 20%;">貨幣與用途</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>🏪 便利超商<br>(7-11 / 全家)</strong></td>
            <td>西門町、台北車站周邊、淡水老街各分門市</td>
            <td>
              • 防熱加長竹夾 ($35)<br>
              • 3 號鹼性電池組 ($50)<br>
              • 石蕊試紙包 ($30)<br>
              • 純水與運動飲料 ($20~$35)
            </td>
            <td><strong>生活流通金</strong><br>現場解謎必備破關耗材</td>
          </tr>
          <tr>
            <td><strong>🛠️ 在地傳統五金行</strong></td>
            <td>台北後火車站太原路五金街、板橋老街雜貨行</td>
            <td>
              • 高精度鋼捲尺 ($80)<br>
              • 高流明 LED 調焦手電筒 ($120)<br>
              • 防靜電不銹鋼鑷子 ($45)<br>
              • 尼龍棉線與動滑輪組 ($65)
            </td>
            <td><strong>生活流通金</strong><br>現場物理測量與物證夾取</td>
          </tr>
          <tr>
            <td><strong>🌿 百年中藥南北貨行</strong></td>
            <td>大稻埕迪化街一段中藥老店</td>
            <td>
              • 紫甘藍萃取酸鹼指示劑 ($50)<br>
              • 天然白芷顯影粉末 ($40)<br>
              • 精密中藥等臂天平（店內免費借用）
            </td>
            <td><strong>生活流通金</strong><br>化學鑑識與古代暗號解讀</td>
          </tr>
          <tr>
            <td><strong>💻 光華數位新天地<br>& 三創生活園區</strong></td>
            <td>市民大道光華商場、捷運忠孝新生站旁</td>
            <td>
              • 便攜式多波段紫外光鑑識筆 (400 幣)<br>
              • 改裝極速電動滑板 (500 幣)<br>
              • 超微距高倍率電子放大鏡 (350 幣)<br>
              • 定向降噪錄音筆 (300 幣)
            </td>
            <td><strong>破案賞金限定</strong><br>永久加速探查的高階專業神裝</td>
          </tr>
          <tr>
            <td><strong>🚇 台北捷運站服務台<br>& 悠遊卡儲值機</strong></td>
            <td>各捷運站穿堂層剪票閘門口</td>
            <td>
              • 悠遊卡儲值與餘額查詢<br>
              • 捷運一日票 ($150，當日不限次搭乘)
            </td>
            <td><strong>生活流通金</strong><br>長途跨區省錢通行證</td>
          </tr>
        </tbody>
      </table>

      <h3>2. 雙軌貨幣體系與經濟循環</h3>
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
              • 成功破獲主線與全服大案。<br>
              • 解開名著經典物理/密碼機關。<br>
              • 達成全服唯一首解或零提示成就。
            </td>
            <td>
              • <strong>光華商場購買高階裝備</strong>：<br>
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
              • <strong>實體超商/五金行購買耗材</strong>：防熱竹夾、電池組、試紙。<br>
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
        <li><strong>中央主畫面</strong>：3D 俯瞰立體街區，可進入建築上方懸浮清晰的發光 Icon（門形、咖啡杯、超商等）。</li>
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
        <strong>「1 條真實街道（台北車站周邊）+ 2 個公車站 + 1 個可進入學習場館 + 1 家實體超商/小吃店 + 1 個多人可競速首解小案」</strong>，完整跑通核心循環！
      </div>

      <h3>📅 專案推進里程碑</h3>
      <ul>
        <li><strong>第一階段（第 1 ~ 2 週 / 目前進度）</strong>：企劃定案、三人小組分工、1:1 地理圖資規範確立與 50 宗大案架構設計。</li>
        <li><strong>第二階段（第 3 ~ 4 週）</strong>：找 AI（志炫等）製作第一版垂直切片原型（街景移動、吃小吃回體力、實體超商購物、跳舞小人機關與後端首解驗證）。</li>
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
    document.getElementById('copyBuffer').value = {json.dumps(plainMarkdown.strip())};

    function copyFullProposal() {{
      const buffer = document.getElementById('copyBuffer');
      const text = buffer.value.trim();

      if (navigator.clipboard && window.isSecureContext) {{
        navigator.clipboard.writeText(text).then(showToast).catch(fallbackCopy);
      }} else {{
        fallbackCopy();
      }}

      function fallbackCopy() {{
        buffer.select();
        buffer.setSelectionRange(0, 99999);
        try {{
          document.execCommand('copy');
          showToast();
        }} catch (err) {{
          alert('複製失敗，請手動全選複製。');
        }}
      }}
    }}

    function showToast() {{
      const toast = document.getElementById('toast');
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 3500);
    }}
  </script>
</body>
</html>
"""

with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Successfully generated proposal.html! File size: {os.path.getsize(output_html_path)} bytes.")
