# 《雙北漫遊偵探：都會行蹤》
### Urban Wanderer: Taipei Mystery

> 🌐 **【跨電腦 AI 開發必讀】如果你是在其他電腦接手本專案的 AI**：  
> 請立即閱讀 [REMOTE_AI_INSTRUCTIONS.md](REMOTE_AI_INSTRUCTIONS.md)，內含 3 大模組（1. 地圖、2. 故事、3. 偵探代碼）之核心檔案速查表、四大憲法紅線與一鍵調度規範！


> **六年級獨立研究專題成果 —— 結合真實雙北地理圖資、古典偵探名著機關與大眾運輸系統的開放式網頁推理 RPG**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20via%20main%20branch-brightgreen)](https://hsiaoyujui114-code.github.io/city-pulse-detective/cyber-realmap.html)
[![Architecture](https://img.shields.io/badge/Current%20Stack-Canvas%20%2B%20Leaflet%20%2B%20ws-blue)](https://hsiaoyujui114-code.github.io/taipei-detective-rpg/proposal.html)

🌐 **線上立即遊玩（全倉庫統一官方試玩網址）**：  
[https://hsiaoyujui114-code.github.io/city-pulse-detective/cyber-realmap.html](https://hsiaoyujui114-code.github.io/city-pulse-detective/cyber-realmap.html)

---

## 📦 四倉庫分工定位與 SSOT 權威來源對照表

| GitHub 倉庫 | 定位與職責 | 權威維護內容 (SSOT) |
| :--- | :--- | :--- |
| **`city-pulse-detective`** | **線上試玩與地圖主站** | `cyber-realmap.*`、`index.html`、`game.js`、`shared-data.js`、`server.js`（GitHub Pages 主入口） |
| **`taipei-metro-detective-rpg`** | **地圖／多人在線鏡像倉** | 鏡像同步主站雙軌地圖、`shared-data.js`、`cases.json`、`PROPOSAL.md` 與 `server.js` |
| **`taipei-detective-rpg`** | **故事劇本與 50 案件展示倉** | 50 案件資料、`cases.html`、`PROPOSAL.md`、`proposal.html` 靜態展示與雙軌地圖同步 |
| **`taipei-detective-core`** | **獨立偵探系統核心引擎** | JSON 驅動案件／NPC／對話樹、`EcoWallet` 真實運價、`MapBridge`、`/detective` 工作台（Port 3001） |

> ⚙️ **現行實作技術棧 vs 未來規劃 (`ISSUE-09`)**：現行實作採用 **HTML5 Canvas 2D ＋ Leaflet 1.9.4（Canvas 繪圖模式）＋ Node.js ＋ `ws` WebSocket**（靜態頁面可於 GitHub Pages 免後端單機展示）；`PixiJS` 與 `Socket.io` 屬於 Phase 2+ 未來擴充規劃（請勿重寫切換引擎）。  
> 📋 **共用檔案同步鐵則 (`ISSUE-11`)**：本倉為 **`cases.json`、`cases.html`、`CASES_50_FULL_SPEC.md`、`PROPOSAL.md`、`PROJECT_PROPOSAL.md`、`proposal.html` 之主倉庫**；本倉內之 `cyber-realmap.*`、`shared-data.js`、`game.js`、`index.html` 為 **`city-pulse-detective` 之鏡像（勿直接單邊修改）**；`AI_HANDOFF_PROJECT_SPEC.md`、`COMPLETE_CONVERSATION_CHRONICLE.md`、`MAP_ISSUE_BOARD_PROTOCOL.md` 四倉同步維持一致。  
> 🔧 **本機雙服務協作前提 (`ISSUE-08`)**：若要在本機啟用完整偵探核心工作台（`localhost:3000/detective` + `localhost:3001`），須於同一父目錄並排 `git clone` `city-pulse-detective` 與 `taipei-detective-core` 並分別啟動 `localhost:3000` 與 `localhost:3001`。

📄 **完整專題企劃書 (含一鍵複製與列印功能)**：  
[https://hsiaoyujui114-code.github.io/taipei-detective-rpg/proposal.html](https://hsiaoyujui114-code.github.io/taipei-detective-rpg/proposal.html)

🔍 **50 宗歷史風情與生活科學案件全集 (含一鍵複製按鈕與檢索)**：  
[https://hsiaoyujui114-code.github.io/taipei-detective-rpg/cases.html](https://hsiaoyujui114-code.github.io/taipei-detective-rpg/cases.html)

---

## 👥 獨立研究三人小組全員協同研發

> 對齊 `PROPOSAL.md` §01（不設僵化固定分工，採全員全能協作模式）：

- 全員共同參與案件劇本發想、名著致敬與 108 課綱自然科學無毒替代實驗考據。
- 全員共同進行雙北 GIS 真實地理測繪、公車路線踩點與連鎖門市座標核對。
- 全員共同參與介面規劃、筆錄對質邏輯設計、自動化驗證與獨立研究發表會演練。

---

## 🎮 遊戲核心特色與亮點

### 1. 🚇 真實雙北捷運與生活圈探索
- **四大經典景點自由穿梭**：台北車站中心樞紐、淡水紅毛城、北投地熱溫泉、板橋林本源園邸（林家花園）。
- **非線性自由調查**：不限制先解哪一關，只要在捷運地圖上選擇站點，刷悠遊卡扣款即可搭乘捷運到達現場。
- **生活化交通**：平時以捷運、步行與 YouBike 移動，特殊緊急重大案件才會解鎖呼叫計程車或專車。

### 2. 🧩 四大柯南與福爾摩斯經典機關實裝（可互動 Mini-games）
1. **淡水紅毛城 ✕ 福爾摩斯〈跳舞的人〉**：地牢石壁刻著 26 塊跳舞小人磚，利用英文單字頻率分析（E 出現率最高）拼出密碼單字解開暗門。
2. **北投地熱谷 ✕ 名偵探柯南化學熱敏密室**：用防熱竹夾將空白信紙置於 85°C 地熱硫磺蒸氣上方烘烤加熱，化學墨水遇熱脫水顯影浮現水閥暗號。
3. **台北車站地下迷宮 ✕ 柯南〈霧天狗傳說〉與建築聲學**：利用虹吸定時蓄水傾倒裝置與 300 公尺長廊聲波多次反射，比對監視器時間戳與聲速延遲，破解偽不在場證明。
4. **板橋林家花園 ✕ 福爾摩斯〈馬斯格雷夫禮儀〉**：調整日晷時鐘至午後三刻（15:00），太陽光線穿透八角漏窗折射在水面上，光斑精準投射至假山石縫找出古銅鑰匙。

### 3. 📜 名著名案考據圖鑑庫（Detective Codex）
- 每破解一樁案件，即可收入一張精美的【破案解密考據卡】。
- 詳細解析原著小說/動畫篇章、背後的物理/化學/密碼學原理，以及雙北在地歷史文化背景，達到「邊玩邊學」的素養教育目標！

### 4. 🛒 經濟循環與偵探補給行
- 破案可賺取 **$500 委託金** 與 **100 都會調查員聲望**。
- 可在商店購買：
  - 🧥 **福爾摩斯經典獵鹿風衣**：更換 2D 像素造型，古蹟 NPC 好感度提升。
  - 🛹 **柯南極速電動滑板**：人行道移動速度提升 60%。
  - 🔍 **高倍率微距放大鏡**：現場隱密線索自動發光提示。

### 5. 🔊 靜態展示與雙軌地圖互通
- 本倉庫提供 50 宗案件展示頁（`cases.html`）、研究企劃書（`proposal.html`）與同步之 2.5D 主沙盤（`index.html`）／1:1 真實地圖（`cyber-realmap.html`）。
- 現行地圖技術棧採用 **HTML5 Canvas 2D ＋ Leaflet 1.9.4（Canvas 模式）**，可直接在瀏覽器與 GitHub Pages 免後端開啟運行。

---

## 🕹️ 遊戲操作指南

- **電腦鍵盤**：
  - 移動：`[W] [A] [S] [D]` 或 `[方向鍵]`
  - 對話與調查：靠近 NPC 或金色光圈按 `[空白鍵 Space]` 或 `[Enter]`
- **手機 / 平板**：
  - 點擊畫面右下角虛擬十字方向鍵移動，點擊畫面即可互動。

---

## 🚀 本地執行與 GitHub Pages 部署說明

### 1. 本地開啟
直接在電腦上連按兩下 `index.html` 即可在瀏覽器中開始遊玩！

### 2. GitHub Pages Branch 發布說明
本專案為純靜態 HTML/CSS/JS 前端，直接透過 GitHub Pages Branch 部署（未使用額外 GitHub Actions workflow 腳本）：
1. 進入本 GitHub Repo 的 **Settings ➔ Pages**
2. 在 **Build and deployment** 下方的 **Source** 選擇 **Deploy from a branch**（Branch：`main` / Folder：`/ (root)`）
3. 稍等 1~2 分鐘，靜態網站便會發布至：  
   `https://hsiaoyujui114-code.github.io/taipei-detective-rpg/`（統一遊戲試玩入口：[https://hsiaoyujui114-code.github.io/city-pulse-detective/cyber-realmap.html](https://hsiaoyujui114-code.github.io/city-pulse-detective/cyber-realmap.html)）

### 3. 本地資料與地圖一致性驗證測試
```bash
npm test
```
