# -*- coding: utf-8 -*-
"""
build_cases_site.py
六年級獨立研究專題：50 大歷史風情與生活科學案件 ✕ 靜態 GitHub 網站建置
生成獨立、優雅、易讀且支援一鍵複製各案 Markdown 的靜態網頁 cases.html
恪守憲法級三大禁忌：一律使用「都會調查員」或「市民」，實體步行與大眾運輸，全域 0 違規。
"""

import json
import html
import os
import sys

import cases_data_chunk1 as c1
import cases_data_chunk2 as c2
import cases_data_chunk3 as c3
import cases_data_chunk4 as c4
import cases_data_chunk5 as c5

all_cases = (
    c1.chunk1_cases +
    c2.chunk2_cases +
    c3.chunk3_cases +
    c4.chunk4_cases +
    c5.chunk5_cases
)

print(f"Loaded {len(all_cases)} cases successfully.")

# Validate taboo words
taboos = ["少年" + "偵探", "藝" + "碩", "益" + "碩"]
for c in all_cases:
    dump = json.dumps(c, ensure_ascii=False)
    for t in taboos:
        if t in dump:
            raise ValueError(f"CRITICAL TABOO DETECTED: {t} in {c['id']}")

print("All 50 cases validated: Zero taboo words detected!")

def generate_case_markdown(c):
    chars_md = []
    for char in c['characters']:
        chars_md.append(f"""### 👤 {char['name']}（{char['identity']}）
- **職業身分與生活作息**：{char['job_daily']}
- **與他人關係**：{char['relation_others']}
- **與被害人關係**：{char['relation_victim']}
- **犯罪動機分析**：{char['motive']}
- **口供陳述**：{char['statement']}
- **破綻與打臉關鍵**：{char['flaw']}""")

    depo = c['deposition']
    testimony = depo.get('testimony', depo.get('testimacy', ''))
    props = c['props_and_easter_egg']

    md = f"""# 【{c['id']}】{c['title']}
- **案件類型**：{c['type']}
- **難度星級**：{c['difficulty']}
- **驚悚指數**：{c['spookiness']}
- **案發地點**：{c['location']}（{c['district']}）

## 🏛️ 當地歷史事件與地方風情
{c['history_culture']}
- **交通常識與生活動線**：{c['traffic_trivia']}

## 🔬 生活科學原理與鑑識依據（108 課綱）
{c['science_principle']}

## 👥 嚴謹細節人物誌
{chr(10).join(chars_md)}

## 📖 案情推導三部曲
### 【起因】
{c['story_cause']}

### 【經過】
{c['story_process']}

### 【最後】
{c['story_climax']}

## ⚖️ 官方警訊偵查筆錄
- **筆錄編號**：{depo.get('record_id', '')}
- **承辦人員**：{depo.get('officer', '')}
- **受訊人**：{depo.get('interrogee', '')}
- **受訊供述**：{testimony}
- **矛盾破綻**：{depo.get('contradiction', '')}
- **關鍵鐵證**：{depo.get('critical_evidence', '')}

## 🎒 破案輔助道具三軌與鄰近彩蛋
- **💰 金錢購買途徑**：{props.get('prop_money', '')}
- **🏛️ 親身探索途徑**：{props.get('prop_explore', '')}
- **🤝 社交打聽途徑**：{props.get('prop_social', '')}
- **🥚 鄰近文化彩蛋**：{props.get('easter_egg', '')}
"""
    return md.strip()

# Generate HTML
html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>《雙北漫遊：都會行蹤》50 大歷史風情與生活科學案件全集 ✕ 六年級獨立研究專題</title>
  <style>
    :root {
      --primary: #1e40af;
      --primary-light: #3b82f6;
      --primary-subtle: #eff6ff;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #475569;
      --accent-conan: #dc2626;
      --accent-holmes: #b45309;
      --accent-science: #059669;
      --accent-history: #7c3aed;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.06), 0 2px 4px -2px rgba(0, 0, 0, 0.04);
      --shadow-hover: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.68;
    }

    /* Header Bar */
    header.site-header {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      color: #ffffff;
      padding: 2.5rem 1.5rem;
      border-bottom: 4px solid var(--primary-light);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .header-container {
      max-width: 1240px;
      margin: 0 auto;
    }

    .header-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(59, 130, 246, 0.2);
      border: 1px solid rgba(59, 130, 246, 0.4);
      color: #93c5fd;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 700;
      margin-bottom: 0.8rem;
      letter-spacing: 0.5px;
    }

    .site-title {
      font-size: 2.1rem;
      font-weight: 900;
      letter-spacing: 0.5px;
      margin-bottom: 0.6rem;
      color: #ffffff;
    }

    .site-subtitle {
      font-size: 1.05rem;
      color: #cbd5e1;
      max-width: 900px;
      margin-bottom: 1.4rem;
    }

    .header-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 1rem;
    }

    .btn-nav {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 8px;
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s ease;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .btn-nav:hover {
      background: var(--primary-light);
      border-color: var(--primary-light);
      transform: translateY(-1px);
    }

    /* Stats Ribbon */
    .stats-ribbon {
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 1.5rem;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .stats-container {
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: space-between;
      align-items: center;
    }

    .stat-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    .stat-pill strong {
      color: var(--primary);
      font-size: 1.15rem;
      font-weight: 800;
    }

    /* Main Container & Layout */
    .main-layout {
      max-width: 1240px;
      margin: 2rem auto;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      align-items: start;
    }

    /* Sticky Sidebar Directory */
    .sidebar-panel {
      position: sticky;
      top: 1.5rem;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      box-shadow: var(--shadow);
      max-height: calc(100vh - 3rem);
      display: flex;
      flex-direction: column;
    }

    .sidebar-header {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary-subtle);
      margin-bottom: 0.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .search-input {
      width: 100%;
      padding: 8px 12px;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 0.88rem;
      margin-bottom: 0.75rem;
      outline: none;
      transition: border-color 0.2s;
    }

    .search-input:focus {
      border-color: var(--primary-light);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }

    .sidebar-nav-list {
      list-style: none;
      overflow-y: auto;
      padding-right: 4px;
      flex: 1;
    }

    .sidebar-nav-list::-webkit-scrollbar {
      width: 4px;
    }

    .sidebar-nav-list::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }

    .sidebar-nav-item {
      margin-bottom: 4px;
    }

    .sidebar-nav-link {
      display: block;
      padding: 6px 10px;
      border-radius: 6px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.84rem;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      transition: all 0.15s ease;
    }

    .sidebar-nav-link:hover {
      background: var(--primary-subtle);
      color: var(--primary);
      font-weight: 600;
    }

    /* Content Area */
    .content-area {
      min-width: 0;
    }

    /* Filter Toolbar */
    .filter-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow);
    }

    .filter-group {
      margin-bottom: 0.8rem;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
    }

    .filter-group:last-child {
      margin-bottom: 0;
    }

    .filter-label {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
      min-width: 68px;
    }

    .filter-chip {
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      color: var(--text-muted);
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }

    .filter-chip:hover {
      background: #e2e8f0;
      color: var(--text-main);
    }

    .filter-chip.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }

    /* Case Card */
    .case-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 2rem;
      box-shadow: var(--shadow);
      overflow: hidden;
      transition: box-shadow 0.2s ease;
    }

    .case-card:hover {
      box-shadow: var(--shadow-hover);
    }

    .case-header {
      background: linear-gradient(to right, #f8fafc, #ffffff);
      padding: 1.25rem 1.5rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    .case-header-left {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .case-id-badge {
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.88rem;
      letter-spacing: 0.5px;
    }

    .case-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--text-main);
    }

    .case-badges {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.78rem;
      font-weight: 700;
    }

    .badge-type {
      background: #ede9fe;
      color: #6d28d9;
      border: 1px solid #ddd6fe;
    }

    .badge-diff {
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fde68a;
    }

    .badge-spook {
      background: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fecaca;
    }

    .badge-location {
      background: #dcfce7;
      color: #15803d;
      border: 1px solid #bbf7d0;
    }

    .case-body {
      padding: 1.5rem;
    }

    /* Section Blocks */
    .section-block {
      margin-bottom: 1.5rem;
    }

    .section-block:last-child {
      margin-bottom: 0;
    }

    .section-title {
      font-size: 1.02rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 0.6rem;
      display: flex;
      align-items: center;
      gap: 6px;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 4px;
    }

    .section-content {
      font-size: 0.94rem;
      color: var(--text-main);
      background: #f8fafc;
      padding: 1rem 1.15rem;
      border-radius: 8px;
      border: 1px solid #f1f5f9;
    }

    .section-content p {
      margin-bottom: 0.6rem;
    }

    .section-content p:last-child {
      margin-bottom: 0;
    }

    /* Characters Grid */
    .characters-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 0.6rem;
    }

    .character-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      border-left: 4px solid var(--primary-light);
    }

    .character-card.killer {
      border-left-color: var(--accent-conan);
      background: #fffafa;
    }

    .character-card.victim {
      border-left-color: var(--accent-holmes);
      background: #fffdfa;
    }

    .char-name {
      font-weight: 800;
      font-size: 1rem;
      color: var(--text-main);
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .char-identity {
      font-size: 0.78rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      background: #f1f5f9;
      color: var(--text-muted);
    }

    .char-field {
      font-size: 0.85rem;
      margin-top: 6px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    .char-field strong {
      color: var(--text-main);
    }

    .char-flaw {
      color: #991b1b;
      background: #fef2f2;
      padding: 4px 8px;
      border-radius: 4px;
      margin-top: 6px;
      border: 1px solid #fee2e2;
    }

    /* Deposition Table */
    .deposition-box {
      background: #fffbeb;
      border: 1px solid #fef3c7;
      border-radius: 8px;
      padding: 1rem 1.15rem;
      font-size: 0.88rem;
    }

    .deposition-row {
      margin-bottom: 6px;
    }

    .deposition-row:last-child {
      margin-bottom: 0;
    }

    .deposition-row strong {
      color: #92400e;
    }

    /* Copy Box Area - SPECIAL USER REQUIREMENT */
    .copy-box-container {
      margin-top: 1.5rem;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
    }

    .copy-box-header {
      background: #e2e8f0;
      padding: 8px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .btn-copy {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.84rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    .btn-copy:hover {
      background: var(--primary-light);
      transform: translateY(-1px);
    }

    .btn-toggle-md {
      background: transparent;
      border: 1px solid #94a3b8;
      color: var(--text-muted);
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      margin-right: 8px;
    }

    .btn-toggle-md:hover {
      background: #cbd5e1;
      color: var(--text-main);
    }

    .copy-textarea {
      width: 100%;
      height: 160px;
      padding: 10px 14px;
      font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size: 0.8rem;
      line-height: 1.5;
      color: #334155;
      background: #ffffff;
      border: none;
      resize: vertical;
      outline: none;
      display: none; /* Collapsed by default for clean view, can toggle */
    }

    .copy-textarea.show {
      display: block;
    }

    /* Toast Notification */
    #toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #1e293b;
      color: #ffffff;
      padding: 12px 20px;
      border-radius: 8px;
      font-size: 0.92rem;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
      border-left: 4px solid #10b981;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease, transform 0.25s ease;
      transform: translateY(10px);
      z-index: 9999;
    }

    #toast.active {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }

    /* Responsive */
    @media (max-width: 900px) {
      .main-layout {
        grid-template-columns: 1fr;
      }
      .sidebar-panel {
        display: none; /* Hide on small screens, can use filter */
      }
      .site-title {
        font-size: 1.6rem;
      }
    }
  </style>
</head>
<body>

  <!-- Site Header -->
  <header class="site-header">
    <div class="header-container">
      <div class="header-badge">🏛️ 六年級獨立研究專題 ✕ 108 課綱生活科學探究</div>
      <h1 class="site-title">《雙北漫遊：都會行蹤》50 大歷史風情與生活科學案件全集</h1>
      <p class="site-subtitle">
        收錄雙北 50 宗深度原創推理案件：將淡水稅關、艋舺龍山寺剝皮寮、大稻埕百年茶行、北投日治溫泉與青磺泉、平溪鐵道等在地風情，與 pH 酸鹼指示、365nm 螢光防偽、阿基米德浮力比重、熱敏水蒸氣顯影等生活科學緊密結合。
      </p>
      <div class="header-nav">
        <a href="index.html" class="btn-nav">🗺️ 返回雙北 2.5D 都會地圖沙盒</a>
        <a href="proposal.html" class="btn-nav">📋 查閱 16 週遊戲企劃全書</a>
        <button class="btn-nav" onclick="expandAllMarkdown()" style="cursor:pointer; background:rgba(16, 185, 129, 0.2); border-color:#34d399;">📂 全部展開 Markdown</button>
        <button class="btn-nav" onclick="collapseAllMarkdown()" style="cursor:pointer; background:rgba(239, 68, 68, 0.2); border-color:#f87171;">📁 全部收合 Markdown</button>
      </div>
    </div>
  </header>

  <!-- Stats Ribbon -->
  <div class="stats-ribbon">
    <div class="stats-container">
      <div class="stat-pill">📚 總收錄案件：<strong>50 宗完整大案</strong></div>
      <div class="stat-pill">🔬 跨學科素養：<strong>108 課綱自然與生活科技</strong></div>
      <div class="stat-pill">👥 人物誌標準：<strong>柯南 ✕ 福爾摩斯嚴謹名冊</strong></div>
      <div class="stat-pill">🚶 移動原則：<strong>實體大眾運輸與街區步行</strong></div>
      <div class="stat-pill">📋 一鍵複製：<strong>每案支援獨立 Markdown 複製</strong></div>
    </div>
  </div>

  <!-- Main Layout -->
  <div class="main-layout">
    <!-- Sticky Sidebar Directory -->
    <aside class="sidebar-panel">
      <div class="sidebar-header">
        <span>📑 50 宗案件目錄索引</span>
        <span style="font-size: 0.8rem; color: var(--text-muted);" id="navCaseCount">50 案</span>
      </div>
      <input type="text" class="search-input" id="sidebarSearch" placeholder="🔍 快速搜尋案件或編號..." oninput="filterCases()">
      <ul class="sidebar-nav-list" id="sidebarList">
""")

for c in all_cases:
    html_parts.append(f"""        <li class="sidebar-nav-item">
          <a href="#{c['id']}" class="sidebar-nav-link" title="{c['title']}">
            <strong>{c['id']}</strong> {c['title']}
          </a>
        </li>""")

html_parts.append("""      </ul>
    </aside>

    <!-- Content Area -->
    <main class="content-area">
      <!-- Filter Toolbar -->
      <div class="filter-card">
        <div class="filter-group">
          <span class="filter-label">🏙️ 區域篩選:</span>
          <span class="filter-chip active" onclick="setDistrictFilter('all', this)">全部地區</span>
          <span class="filter-chip" onclick="setDistrictFilter('萬華', this)">萬華/西門</span>
          <span class="filter-chip" onclick="setDistrictFilter('中正', this)">中正/北車</span>
          <span class="filter-chip" onclick="setDistrictFilter('淡水', this)">淡水</span>
          <span class="filter-chip" onclick="setDistrictFilter('北投', this)">北投</span>
          <span class="filter-chip" onclick="setDistrictFilter('板橋', this)">板橋</span>
          <span class="filter-chip" onclick="setDistrictFilter('新莊', this)">新莊</span>
          <span class="filter-chip" onclick="setDistrictFilter('大同', this)">大稻埕/大同</span>
          <span class="filter-chip" onclick="setDistrictFilter('士林', this)">士林</span>
          <span class="filter-chip" onclick="setDistrictFilter('三重', this)">三重</span>
          <span class="filter-chip" onclick="setDistrictFilter('其他', this)">其他行政區</span>
        </div>
        <div class="filter-group">
          <span class="filter-label">🏷️ 案件類型:</span>
          <span class="filter-chip active" onclick="setTypeFilter('all', this)">全部類型</span>
          <span class="filter-chip" onclick="setTypeFilter('突發案件', this)">突發案件</span>
          <span class="filter-chip" onclick="setTypeFilter('主線案件', this)">主線案件</span>
          <span class="filter-chip" onclick="setTypeFilter('個人任務', this)">個人任務</span>
          <span class="filter-chip" onclick="setTypeFilter('共享競速', this)">共享競速</span>
          <span class="filter-chip" onclick="setTypeFilter('歷史懸案', this)">歷史懸案</span>
        </div>
      </div>

      <!-- Cases Stream -->
      <div id="casesStream">
""")

for c in all_cases:
    md_text = generate_case_markdown(c)
    escaped_md = html.escape(md_text)

    # Characters HTML
    chars_html = []
    for char in c['characters']:
        card_class = "character-card"
        if "真兇" in char['identity']:
            card_class += " killer"
        elif "被害" in char['identity'] or "受害" in char['identity']:
            card_class += " victim"

        chars_html.append(f"""          <div class="{card_class}">
            <div class="char-name">
              <span>{html.escape(char['name'])}</span>
              <span class="char-identity">{html.escape(char['identity'])}</span>
            </div>
            <div class="char-field"><strong>身分與作息：</strong>{html.escape(char['job_daily'])}</div>
            <div class="char-field"><strong>與他人關係：</strong>{html.escape(char['relation_others'])}</div>
            <div class="char-field"><strong>與被害人關係：</strong>{html.escape(char['relation_victim'])}</div>
            <div class="char-field"><strong>犯罪動機：</strong>{html.escape(char['motive'])}</div>
            <div class="char-field"><strong>口供陳述：</strong><em>{html.escape(char['statement'])}</em></div>
            <div class="char-field char-flaw"><strong>⚠️ 破綻關鍵：</strong>{html.escape(char['flaw'])}</div>
          </div>""")

    depo = c['deposition']
    testimony = depo.get('testimony', depo.get('testimacy', ''))
    props = c['props_and_easter_egg']

    html_parts.append(f"""
        <!-- Case Card: {c['id']} -->
        <article class="case-card" id="{c['id']}" data-district="{html.escape(c['district'])}" data-type="{html.escape(c['type'])}" data-title="{html.escape(c['title'])}">
          <div class="case-header">
            <div class="case-header-left">
              <span class="case-id-badge">{c['id']}</span>
              <h2 class="case-title">{html.escape(c['title'])}</h2>
            </div>
            <div class="case-badges">
              <span class="badge badge-type">🏷️ {html.escape(c['type'])}</span>
              <span class="badge badge-diff">難度：{html.escape(c['difficulty'])}</span>
              <span class="badge badge-spook">{html.escape(c['spookiness'])}</span>
              <span class="badge badge-location">📍 {html.escape(c['district'])}</span>
            </div>
          </div>

          <div class="case-body">
            <!-- 1. Location & History -->
            <div class="section-block">
              <div class="section-title">🏛️ 當地歷史事件與地方風情</div>
              <div class="section-content">
                <p><strong>【精確地點】</strong>{html.escape(c['location'])}</p>
                <p>{html.escape(c['history_culture'])}</p>
                <p><strong>【交通常識與生活動線】</strong>{html.escape(c['traffic_trivia'])}</p>
              </div>
            </div>

            <!-- 2. Science Principle -->
            <div class="section-block">
              <div class="section-title">🔬 生活科學原理與鑑識依據（108 課綱）</div>
              <div class="section-content" style="background:#f0fdf4; border-color:#dcfce7;">
                <p>{html.escape(c['science_principle'])}</p>
              </div>
            </div>

            <!-- 3. Characters Directory -->
            <div class="section-block">
              <div class="section-title">👥 嚴謹細節人物誌（柯南 ✕ 福爾摩斯標準名冊）</div>
              <div class="characters-grid">
{chr(10).join(chars_html)}
              </div>
            </div>

            <!-- 4. Story Trilogy -->
            <div class="section-block">
              <div class="section-title">📖 案情推導三部曲（起因 ✕ 經過 ✕ 最後）</div>
              <div class="section-content">
                <p><strong>【起因・案發前情】</strong>{html.escape(c['story_cause'])}</p>
                <p><strong>【經過・調查動線】</strong>{html.escape(c['story_process'])}</p>
                <p><strong>【最後・破案邏輯】</strong>{html.escape(c['story_climax'])}</p>
              </div>
            </div>

            <!-- 5. Deposition -->
            <div class="section-block">
              <div class="section-title">⚖️ 官方警訊偵查筆錄檔案</div>
              <div class="deposition-box">
                <div class="deposition-row"><strong>筆錄編號：</strong>{html.escape(depo.get('record_id', ''))} ｜ <strong>承辦人員：</strong>{html.escape(depo.get('officer', ''))}</div>
                <div class="deposition-row"><strong>受訊對象：</strong>{html.escape(depo.get('interrogee', ''))}</div>
                <div class="deposition-row"><strong>受訊供述：</strong><em>{html.escape(testimony)}</em></div>
                <div class="deposition-row"><strong>矛盾破綻：</strong>{html.escape(depo.get('contradiction', ''))}</div>
                <div class="deposition-row" style="color:#b91c1c; font-weight:700;"><strong>關鍵鐵證：</strong>{html.escape(depo.get('critical_evidence', ''))}</div>
              </div>
            </div>

            <!-- 6. Props & Easter Egg -->
            <div class="section-block">
              <div class="section-title">🎒 破案輔助道具三軌與鄰近文化彩蛋</div>
              <div class="section-content" style="background:#faf5ff; border-color:#f3e8ff;">
                <p><strong>💰 金錢購買途徑：</strong>{html.escape(props.get('prop_money', ''))}</p>
                <p><strong>🏛️ 親身探索途徑：</strong>{html.escape(props.get('prop_explore', ''))}</p>
                <p><strong>🤝 社交打聽途徑：</strong>{html.escape(props.get('prop_social', ''))}</p>
                <p><strong>🥚 鄰近文化彩蛋：</strong>{html.escape(props.get('easter_egg', ''))}</p>
              </div>
            </div>

            <!-- 7. Copy Area (Special Client Requirement) -->
            <div class="copy-box-container">
              <div class="copy-box-header">
                <span>📋 本案完整企劃設定（Markdown 規格文本）</span>
                <div>
                  <button class="btn-toggle-md" onclick="toggleMarkdown('{c['id']}')">👁️ 展開 / 收合 Markdown</button>
                  <button class="btn-copy" onclick="copyCaseMarkdown('{c['id']}')">📋 複製本案完整設定</button>
                </div>
              </div>
              <textarea class="copy-textarea" id="md_{c['id']}" readonly>{escaped_md}</textarea>
            </div>
          </div>
        </article>
""")

html_parts.append("""
      </div>
    </main>
  </div>

  <!-- Toast Notification Popup -->
  <div id="toast">✅ 已成功複製本案完整設定！</div>

  <script>
    // Copy Markdown to Clipboard
    function copyCaseMarkdown(caseId) {
      const textarea = document.getElementById('md_' + caseId);
      if (!textarea) return;

      navigator.clipboard.writeText(textarea.value).then(() => {
        showToast('✅ 已複製 ' + caseId + ' 完整設定至剪貼簿！');
      }).catch(err => {
        // Fallback
        textarea.classList.add('show');
        textarea.select();
        document.execCommand('copy');
        showToast('✅ 已複製 ' + caseId + ' 完整設定！');
      });
    }

    function toggleMarkdown(caseId) {
      const textarea = document.getElementById('md_' + caseId);
      if (!textarea) return;
      textarea.classList.toggle('show');
    }

    function expandAllMarkdown() {
      document.querySelectorAll('.copy-textarea').forEach(el => el.classList.add('show'));
      showToast('📂 已全部展開所有案件 Markdown 框！');
    }

    function collapseAllMarkdown() {
      document.querySelectorAll('.copy-textarea').forEach(el => el.classList.remove('show'));
      showToast('📁 已全部收合所有案件 Markdown 框！');
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.textContent = msg;
      toast.classList.add('active');
      setTimeout(() => {
        toast.classList.remove('active');
      }, 2500);
    }

    // Filter Logic
    let currentDistrict = 'all';
    let currentType = 'all';

    function setDistrictFilter(district, chip) {
      currentDistrict = district;
      document.querySelectorAll('.filter-group:nth-child(1) .filter-chip').forEach(el => el.classList.remove('active'));
      chip.classList.add('active');
      applyFilters();
    }

    function setTypeFilter(type, chip) {
      currentType = type;
      document.querySelectorAll('.filter-group:nth-child(2) .filter-chip').forEach(el => el.classList.remove('active'));
      chip.classList.add('active');
      applyFilters();
    }

    function filterCases() {
      applyFilters();
    }

    function applyFilters() {
      const query = (document.getElementById('sidebarSearch')?.value || '').toLowerCase().trim();
      const cards = document.querySelectorAll('.case-card');
      const sidebarLinks = document.querySelectorAll('.sidebar-nav-item');
      let visibleCount = 0;

      cards.forEach((card, index) => {
        const cDistrict = card.getAttribute('data-district') || '';
        const cType = card.getAttribute('data-type') || '';
        const cTitle = card.getAttribute('data-title') || '';
        const cId = card.id || '';
        const cardText = card.textContent.toLowerCase();

        let districtMatch = (currentDistrict === 'all') || cDistrict.includes(currentDistrict);
        let typeMatch = (currentType === 'all') || (cType === currentType);
        let searchMatch = true;

        if (query) {
          searchMatch = cId.toLowerCase().includes(query) ||
                        cTitle.toLowerCase().includes(query) ||
                        cDistrict.toLowerCase().includes(query) ||
                        cardText.includes(query);
        }

        const isVisible = districtMatch && typeMatch && searchMatch;
        card.style.display = isVisible ? 'block' : 'none';

        if (sidebarLinks[index]) {
          sidebarLinks[index].style.display = isVisible ? 'block' : 'none';
        }

        if (isVisible) visibleCount++;
      });

      const countEl = document.getElementById('navCaseCount');
      if (countEl) countEl.textContent = visibleCount + ' 案';
    }
  </script>
</body>
</html>
""")

output_file = os.path.join(os.path.dirname(__file__), "cases.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print(f"Successfully generated cases.html! Size: {os.path.getsize(output_file)} bytes.")
