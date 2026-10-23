# -*- coding: utf-8 -*-
"""
build_cases_html.py
將 5 批共 50 宗雙北歷史風情與生活科學案件編譯為獨立靜態 GitHub 網頁 (cases.html) 與 cases.json
具備：
1. 50 案完整起因、經過、最後、人物誌、歷史、生活科學
2. 每案獨立的一鍵複製按鈕與純文字/Markdown 複製文字框
3. 即時搜尋與目錄跳轉導覽
"""
import json
import html

import cases_data_chunk1 as c1
import cases_data_chunk2 as c2
import cases_data_chunk3 as c3
import cases_data_chunk4 as c4
import cases_data_chunk5 as c5

all_cases = c1.chunk1_cases + c2.chunk2_cases + c3.chunk3_cases + c4.chunk4_cases + c5.chunk5_cases

# 1. 儲存完整 JSON 檔案
with open('/Users/home/crew-deck-role/planner/cases.json', 'w', encoding='utf-8') as f:
    json.dump(all_cases, f, ensure_ascii=False, indent=2)

print(f"Exported cases.json with {len(all_cases)} cases.")

# 2. 構建 cases.html
html_parts = []

html_parts.append("""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>《雙北漫遊：都會行蹤》50 宗歷史風情與生活科學案件全集</title>
  <style>
    :root {
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --accent: #0f172a;
      --text: #1e293b;
      --text-muted: #64748b;
      --success: #16a34a;
      --code-bg: #f1f5f9;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", sans-serif;
      line-height: 1.6;
      padding-bottom: 60px;
    }
    header {
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #fff;
      padding: 36px 20px 24px;
      text-align: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    header h1 {
      font-size: 26px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }
    header p {
      font-size: 14px;
      color: #94a3b8;
      max-width: 800px;
      margin: 0 auto 16px;
    }
    .search-bar-wrap {
      max-width: 600px;
      margin: 0 auto;
      display: flex;
      gap: 8px;
    }
    .search-input {
      flex: 1;
      padding: 10px 16px;
      border-radius: 8px;
      border: 1px solid #475569;
      background: #0f172a;
      color: #fff;
      font-size: 14px;
      outline: none;
    }
    .search-input:focus {
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }
    .quick-stats {
      margin-top: 10px;
      font-size: 13px;
      color: #cbd5e1;
    }
    .container {
      max-width: 1080px;
      margin: 24px auto;
      padding: 0 16px;
    }
    .toc-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
    }
    .toc-card summary {
      font-weight: 700;
      color: var(--primary-dark);
      cursor: pointer;
      font-size: 16px;
      user-select: none;
    }
    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 8px;
      margin-top: 14px;
      max-height: 280px;
      overflow-y: auto;
      padding-right: 6px;
    }
    .toc-link {
      font-size: 12px;
      color: #334155;
      text-decoration: none;
      padding: 6px 10px;
      border-radius: 6px;
      background: var(--code-bg);
      display: block;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      transition: background 0.15s, color 0.15s;
    }
    .toc-link:hover {
      background: #e0f2fe;
      color: var(--primary-dark);
    }
    .case-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 32px;
      box-shadow: var(--shadow);
      scroll-margin-top: 140px;
      transition: transform 0.2s;
    }
    .case-card:hover {
      border-color: #cbd5e1;
    }
    .case-header {
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 12px;
      margin-bottom: 16px;
    }
    .case-id-badge {
      display: inline-block;
      background: #0284c7;
      color: #fff;
      font-size: 12px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      margin-right: 8px;
    }
    .case-title {
      font-size: 20px;
      font-weight: 800;
      color: var(--accent);
      display: inline-block;
      vertical-align: middle;
    }
    .case-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }
    .tag {
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      background: #f1f5f9;
      color: #475569;
    }
    .tag-district { background: #e0f2fe; color: #0369a1; }
    .tag-type { background: #fef3c7; color: #92400e; }
    .tag-difficulty { background: #dcfce7; color: #166534; }
    .section-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--primary-dark);
      margin: 16px 0 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .box-info {
      background: #f8fafc;
      border-left: 4px solid var(--primary);
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      font-size: 14px;
      margin-bottom: 12px;
      color: #334155;
    }
    .story-triad {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
      margin: 12px 0;
    }
    @media (min-width: 768px) {
      .story-triad { grid-template-columns: 1fr 1fr 1fr; }
    }
    .story-col {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px 14px;
    }
    .story-col h4 {
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 6px;
      padding-bottom: 4px;
      border-bottom: 1px dashed #cbd5e1;
    }
    .story-col p {
      font-size: 13px;
      color: #475569;
      text-align: justify;
    }
    .char-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      margin: 12px 0;
    }
    @media (min-width: 640px) {
      .char-grid { grid-template-columns: 1fr 1fr; }
    }
    .char-card {
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 10px 12px;
      background: #fafafa;
      font-size: 12px;
    }
    .char-card.culprit {
      border-color: #fca5a5;
      background: #fff5f5;
    }
    .char-name {
      font-weight: 700;
      font-size: 13px;
      color: var(--accent);
      margin-bottom: 4px;
    }
    .char-card.culprit .char-name {
      color: #b91c1c;
    }
    .char-detail {
      margin-top: 3px;
      color: #475569;
    }
    .copy-box-wrap {
      margin-top: 20px;
      padding: 14px;
      background: #f1f5f9;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
    }
    .copy-box-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .copy-box-title {
      font-size: 13px;
      font-weight: 700;
      color: #334155;
    }
    .btn-copy {
      background: var(--primary);
      color: #fff;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: background 0.15s;
    }
    .btn-copy:hover {
      background: var(--primary-dark);
    }
    .copy-textarea {
      width: 100%;
      height: 90px;
      font-family: monospace;
      font-size: 11px;
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      color: #334155;
      resize: vertical;
    }
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0f172a;
      color: #fff;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease-in-out;
      z-index: 1000;
    }
    .toast.show {
      opacity: 1;
    }
  </style>
</head>
<body>

  <header>
    <h1>🔍 《雙北漫遊：都會行蹤》50 宗歷史風情與生活科學案件全集</h1>
    <p>六年級獨立研究專題成果・結合雙北百年歷史風俗 ✕ 108 課綱自然科學原理 ✕ 柯南/福爾摩斯人物誌人物關係譜</p>
    <div class="search-bar-wrap">
      <input type="text" id="searchInput" class="search-input" placeholder="🔍 搜尋案件編號、標題、行政區、歷史事件或科學原理..." oninput="filterCases()">
    </div>
    <div class="quick-stats">
      收錄雙北 17 個行政特區・共 50 宗完整偵探案件（每案均附帶「起因、經過、最後」與「一鍵複製文本框」）
    </div>
  </header>

  <div class="container">

    <details class="toc-card" open>
      <summary>📑 50 大案件快速目錄檢索（點擊快速跳轉到案件）</summary>
      <div class="toc-grid" id="tocGrid">
""")

# 生成目錄連結
for c in all_cases:
    cid = c['id']
    title = html.escape(c['title'])
    district = html.escape(c.get('district', '').split('（')[0])
    html_parts.append(f'<a href="#{cid}" class="toc-link"><strong>{cid}</strong> {title} ({district})</a>\n')

html_parts.append("""      </div>
    </details>

    <div id="casesContainer">
""")

# 生成每個案件的卡片
for c in all_cases:
    cid = c['id']
    title = html.escape(c['title'])
    ctype = html.escape(c.get('type', '核心主線案'))
    diff = html.escape(c.get('difficulty', '★★☆☆☆'))
    spook = html.escape(c.get('spookiness', '👻☆☆☆☆'))
    loc = html.escape(c.get('location', ''))
    dist = html.escape(c.get('district', ''))
    hist = html.escape(c.get('history_culture', ''))
    sci = html.escape(c.get('science_principle', ''))
    traf = html.escape(c.get('traffic_trivia', ''))
    cause = html.escape(c.get('story_cause', ''))
    proc = html.escape(c.get('story_process', ''))
    climax = html.escape(c.get('story_climax', ''))

    # 生成純文字 Markdown 複製文本
    lines = []
    lines.append(f"【{cid}】{c['title']}")
    lines.append(f"地點：{c.get('location', '')}（{c.get('district', '')}）")
    lines.append(f"難度：{c.get('difficulty', '')} | 驚悚度：{c.get('spookiness', '')}")
    lines.append(f"---")
    lines.append(f"🏛️【在地歷史與風情】：\n{c.get('history_culture', '')}\n")
    lines.append(f"🔬【解題生活科學原理】：\n{c.get('science_principle', '')}\n")
    lines.append(f"📖【案情推導三部曲】：")
    lines.append(f"【起因】：{c.get('story_cause', '')}")
    lines.append(f"【經過】：{c.get('story_process', '')}")
    lines.append(f"【最後】：{c.get('story_climax', '')}\n")
    lines.append(f"👥【涉案群像人物誌】：")
    for ch in c.get('characters', []):
        lines.append(f"- {ch.get('name', '')}（{ch.get('identity', '')}）")
        lines.append(f"  日常身分：{ch.get('job_daily', '')}")
        lines.append(f"  與他人關係：{ch.get('relation_others', '')} | 與被害人：{ch.get('relation_victim', '')}")
        lines.append(f"  動機：{ch.get('motive', '')}")
        lines.append(f"  供詞：{ch.get('statement', '')}")
        lines.append(f"  破綻：{ch.get('flaw', '')}")
    if 'deposition' in c:
        dp = c['deposition']
        lines.append(f"\n📜【警方筆錄與關鍵物證】：")
        lines.append(f"- 筆錄案號：{dp.get('record_id', '')} (承辦員警: {dp.get('officer', '')})")
        lines.append(f"- 受訊人：{dp.get('interrogee', '')}")
        lines.append(f"- 供述：{dp.get('testimony', '')}")
        lines.append(f"- 矛盾反駁：{dp.get('contradiction', '')}")
        lines.append(f"- 核心定罪物證：{dp.get('critical_evidence', '')}")
    if 'props_and_easter_egg' in c:
        pe = c['props_and_easter_egg']
        lines.append(f"\n🎒【三軌道具與彩蛋】：")
        lines.append(f"- 貨幣購買道具：{pe.get('prop_money', '')}")
        lines.append(f"- 探索學習道具：{pe.get('prop_explore', '')}")
        lines.append(f"- 社交信賴道具：{pe.get('prop_social', '')}")
        lines.append(f"- 50~100m 生活圈彩蛋：{pe.get('easter_egg', '')}")

    raw_text = "\n".join(lines)
    escaped_raw = html.escape(raw_text)

    # 輸出 HTML 卡片
    html_parts.append(f"""
      <article class="case-card" id="{cid}">
        <div class="case-header">
          <span class="case-id-badge">{cid}</span>
          <h2 class="case-title">{title}</h2>
          <div class="case-tags">
            <span class="tag tag-district">📍 {dist}</span>
            <span class="tag tag-type">🏷️ {ctype}</span>
            <span class="tag tag-difficulty">⭐ 難度: {diff}</span>
            <span class="tag">👻 {spook}</span>
            <span class="tag">🚇 現場: {loc}</span>
          </div>
        </div>

        <div class="section-title">🏛️ 在地歷史風情與人文背景</div>
        <div class="box-info">{hist}</div>

        <div class="section-title">🔬 解題生活科學原理（108 課綱）</div>
        <div class="box-info" style="border-left-color: #10b981;">{sci}</div>

        <div class="section-title">📖 案情推導三部曲（起因 ➔ 經過 ➔ 最後推導）</div>
        <div class="story-triad">
          <div class="story-col">
            <h4 style="color:#0284c7;">【起因】案發引線</h4>
            <p>{cause}</p>
          </div>
          <div class="story-col">
            <h4 style="color:#f59e0b;">【經過】調查排查</h4>
            <p>{proc}</p>
          </div>
          <div class="story-col">
            <h4 style="color:#10b981;">【最後】科學推導</h4>
            <p>{climax}</p>
          </div>
        </div>

        <div class="section-title">👥 涉案關係人群像人物誌（柯南 / 福爾摩斯式精密設定）</div>
        <div class="char-grid">
""")

    for ch in c.get('characters', []):
        is_culprit = '真兇' in ch.get('name', '') or '真兇' in ch.get('identity', '')
        culprit_cls = "culprit" if is_culprit else ""
        cname = html.escape(ch.get('name', ''))
        cident = html.escape(ch.get('identity', ''))
        cjob = html.escape(ch.get('job_daily', ''))
        crel_others = html.escape(ch.get('relation_others', ''))
        crel_vic = html.escape(ch.get('relation_victim', ''))
        cmotive = html.escape(ch.get('motive', ''))
        cstmt = html.escape(ch.get('statement', ''))
        cflaw = html.escape(ch.get('flaw', ''))

        html_parts.append(f"""
          <div class="char-card {culprit_cls}">
            <div class="char-name">👤 {cname} <span style="font-weight:normal; font-size:11px; color:#64748b;">({cident})</span></div>
            <div class="char-detail"><strong>日常身分：</strong>{cjob}</div>
            <div class="char-detail"><strong>他人關係：</strong>{crel_others}</div>
            <div class="char-detail"><strong>被害人關係：</strong>{crel_vic}</div>
            <div class="char-detail"><strong>作案動機：</strong>{cmotive}</div>
            <div class="char-detail"><strong>證詞：</strong>{cstmt}</div>
            <div class="char-detail" style="color:#b91c1c;"><strong>破綻：</strong>{cflaw}</div>
          </div>
""")

    html_parts.append(f"""
        </div>

        <div class="copy-box-wrap">
          <div class="copy-box-header">
            <span class="copy-box-title">📋 本案完整文字檔（可直接複製貼上使用）</span>
            <button class="btn-copy" onclick="copyCaseText('{cid}')">📋 點擊一鍵複製本案文本</button>
          </div>
          <textarea id="text-{cid}" class="copy-textarea" readonly>{escaped_raw}</textarea>
        </div>
      </article>
""")

html_parts.append("""
    </div>
  </div>

  <div id="toast" class="toast">✅ 已成功複製案件文本至剪貼簿！</div>

  <script>
    function copyCaseText(caseId) {
      const textarea = document.getElementById('text-' + caseId);
      if (!textarea) return;
      textarea.select();
      textarea.setSelectionRange(0, 99999);
      navigator.clipboard.writeText(textarea.value).then(() => {
        showToast('✅ 已成功複製 ' + caseId + ' 案件文本至剪貼簿！');
      }).catch(err => {
        document.execCommand('copy');
        showToast('✅ 已成功複製 ' + caseId + ' 案件文本至剪貼簿！');
      });
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2500);
    }

    function filterCases() {
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      const articles = document.querySelectorAll('.case-card');
      articles.forEach(art => {
        const text = art.innerText.toLowerCase();
        if (!q || text.includes(q)) {
          art.style.display = 'block';
        } else {
          art.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
""")

with open('/Users/home/crew-deck-role/planner/cases.html', 'w', encoding='utf-8') as f:
    f.write("".join(html_parts))

print("Successfully generated cases.html!")
