# 《雙北漫遊偵探：都會行蹤》
### Urban Wanderer: Taipei Mystery

> **六年級獨立研究專題成果 —— 結合真實雙北地理圖資、古典偵探名著機關與大眾運輸系統的開放式網頁推理 RPG**

[![Deploy to GitHub Pages](https://github.com/hsiaoyujui114-code/taipei-detective-rpg/actions/workflows/deploy.yml/badge.svg)](https://github.com/hsiaoyujui114-code/taipei-detective-rpg/actions/workflows/deploy.yml)

🌐 **線上立即遊玩 (GitHub Pages)**：  
[https://hsiaoyujui114-code.github.io/taipei-detective-rpg/](https://hsiaoyujui114-code.github.io/taipei-detective-rpg/)

📄 **完整專題企劃書 (含一鍵複製與列印功能)**：  
[https://hsiaoyujui114-code.github.io/taipei-detective-rpg/proposal.html](https://hsiaoyujui114-code.github.io/taipei-detective-rpg/proposal.html)

---

## 👥 獨立研究三人小組分工

| 成員角色 | 專責領域 | 具體任務 |
| :--- | :--- | :--- |
| **組員 1（組長 / 企劃總監）** | 世界觀與劇本編撰 | 統籌專案時程、研讀《名偵探柯南》與《福爾摩斯》挑選經典機關改編、撰寫 NPC 對話與破案考據卡文案 |
| **組員 2（美術與圖資）** | 視覺設計與圖資調研 | 收集雙北地標與捷運路線資料、設計 2D 復古像素主角外觀、運用 AI 生成現場證物與地圖素材 |
| **組員 3（技術與測試）** | 程式協同與平台發布 | 與 AI（Anti-gravity）協作編寫網頁程式碼、實作捷運搭乘與機關 Mini-games、負責 GitHub Pages 部署發布 |

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
- 破案可賺取 **$500 委託金** 與 **100 名偵探聲望**。
- 可在商店購買：
  - 🧥 **福爾摩斯經典獵鹿風衣**：更換 2D 像素造型，古蹟 NPC 好感度提升。
  - 🛹 **柯南極速電動滑板**：人行道移動速度提升 60%。
  - 🔍 **高倍率微距放大鏡**：現場隱密線索自動發光提示。

### 5. 🔊 純前端免伺服器與 8-bit 音效
- 使用 Web Audio API 即時合成復古 8-bit 晶片音效與台北捷運動態進站四音階（G4, B4, D5, G5）。
- 100% 純靜態網頁（HTML5 + Canvas + Vanilla JS + CSS），零伺服器依賴，任何裝置瀏覽器隨點隨玩！

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

### 2. GitHub Pages 自動發布
本專案已包含 `.github/workflows/deploy.yml` 自動部署腳本：
1. 進入本 GitHub Repo 的 **Settings ➔ Pages**
2. 在 **Build and deployment** 下方的 **Source** 選擇 **GitHub Actions**
3. 稍等 1~2 分鐘，網站便會發布至：  
   `https://hsiaoyujui114-code.github.io/taipei-detective-rpg/`
