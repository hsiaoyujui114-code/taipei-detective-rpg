# -*- coding: utf-8 -*-
"""
build_cases_site.py
六年級獨立研究專題：50 大歷史風情與生活科學案件 ✕ 靜態 GitHub 網站建置
支援功能：
1. 50 宗大案極其詳盡企劃（起因、經過、最後、人物誌、歷史、生活科學）
2. 每案下方獨立 Markdown 框與「📋 複製本案完整設定」按鈕
3. ★ 委託人特別需求：【免安裝任何軟體，任何知道網址的人皆可在網頁上直接打字修改（所見即所得線上編輯模式）】
4. 自動同步更新 Markdown、保存至瀏覽器 LocalStorage、支援寫入伺服器 API、支援匯出 HTML
5. 提供直通 GitHub 線上編輯器（Web IDE）之快捷通道
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
  <title>《雙北漫遊：都會行蹤》50 大歷史風情與生活科學案件全集 ✕ 六年級獨立研究專題（支援線上直接編輯）</title>
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
      --edit-glow: #f59e0b;
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

    /* Top Sticky Collaboration & Edit Toolbar */
    .edit-sticky-toolbar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: #1e293b;
      color: #ffffff;
      padding: 10px 1.5rem;
      border-bottom: 2px solid var(--primary-light);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    .toolbar-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .edit-status-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.84rem;
      padding: 4px 10px;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.1);
      font-weight: 700;
    }

    .edit-status-badge.active {
      background: #f59e0b;
      color: #0f172a;
    }

    .toolbar-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .btn-tool {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid transparent;
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .btn-tool-edit {
      background: #f59e0b;
      color: #0f172a;
      border-color: #d97706;
    }

    .btn-tool-edit:hover {
      background: #fbbf24;
      transform: translateY(-1px);
    }

    .btn-tool-save {
      background: #10b981;
      color: #ffffff;
      border-color: #059669;
    }

    .btn-tool-save:hover {
      background: #059669;
      transform: translateY(-1px);
    }

    .btn-tool-ghost {
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.25);
    }

    .btn-tool-ghost:hover {
      background: rgba(255, 255, 255, 0.22);
    }

    .btn-tool-github {
      background: #24292f;
      color: #ffffff;
      border-color: #444c56;
    }

    .btn-tool-github:hover {
      background: #32383f;
    }

    /* Edit Mode Styling */
    body.edit-mode-active [data-editable="true"] {
      outline: 1.5px dashed #3b82f6;
      border-radius: 4px;
      padding: 2px 4px;
      cursor: text;
      transition: all 0.2s ease;
      background: rgba(59, 130, 246, 0.03);
    }

    body.edit-mode-active [data-editable="true"]:hover {
      outline-color: #f59e0b;
      background: rgba(245, 158, 11, 0.08);
    }

    body.edit-mode-active [data-editable="true"]:focus {
      outline: 2px solid #2563eb;
      background: #ffffff;
      box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15);
    }

    .edit-hint-banner {
      display: none;
      background: #fef3c7;
      border-bottom: 1px solid #fde68a;
      color: #92400e;
      padding: 8px 1.5rem;
      font-size: 0.88rem;
      font-weight: 700;
      text-align: center;
    }

    body.edit-mode-active .edit-hint-banner {
      display: block;
    }

    .card-edited-tag {
      display: none;
      background: #f59e0b;
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      margin-left: 6px;
    }

    .case-card.is-edited .card-edited-tag {
      display: inline-block;
    }

    /* Site Header */
    header.site-header {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      color: #ffffff;
      padding: 2.2rem 1.5rem;
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
      font-size: 1.02rem;
      color: #cbd5e1;
      max-width: 950px;
      margin-bottom: 1.2rem;
    }

    .header-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 0.8rem;
    }

    .btn-nav {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      padding: 7px 14px;
      border-radius: 8px;
      text-decoration: none;
      font-size: 0.88rem;
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
      padding: 0.9rem 1.5rem;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .stats-container {
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      justify-content: space-between;
      align-items: center;
    }

    .stat-pill {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.88rem;
      color: var(--text-muted);
    }

    .stat-pill strong {
      color: var(--primary);
      font-size: 1.1rem;
      font-weight: 800;
    }

    /* Main Container & Layout */
    .main-layout {
      max-width: 1240px;
      margin: 1.8rem auto;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 1.8rem;
      align-items: start;
    }

    /* Sticky Sidebar Directory */
    .sidebar-panel {
      position: sticky;
      top: 4.5rem;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      box-shadow: var(--shadow);
      max-height: calc(100vh - 6rem);
      display: flex;
      flex-direction: column;
    }

    .sidebar-header {
      font-size: 1.02rem;
      font-weight: 800;
      color: var(--text-main);
      padding-bottom: 0.6rem;
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
      padding: 1.15rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow);
    }

    .filter-group {
      margin-bottom: 0.75rem;
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
      transition: box-shadow 0.2s ease, border-color 0.2s ease;
    }

    .case-card:hover {
      box-shadow: var(--shadow-hover);
    }

    .case-card.is-edited {
      border-color: #f59e0b;
    }

    .case-header {
      background: linear-gradient(to right, #f8fafc, #ffffff);
      padding: 1.15rem 1.4rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
    }

    .case-header-left {
      display: flex;
      align-items: center;
      gap: 10px;
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
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--text-main);
    }

    .case-badges {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      align-items: center;
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

    .btn-github-mini {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.15s ease;
    }

    .btn-github-mini:hover {
      background: #24292f;
      color: #ffffff;
      border-color: #24292f;
    }

    .case-body {
      padding: 1.4rem;
    }

    /* Section Blocks */
    .section-block {
      margin-bottom: 1.4rem;
    }

    .section-block:last-child {
      margin-bottom: 0;
    }

    .section-title {
      font-size: 0.98rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 6px;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 4px;
    }

    .section-content {
      font-size: 0.92rem;
      color: var(--text-main);
      background: #f8fafc;
      padding: 0.9rem 1.1rem;
      border-radius: 8px;
      border: 1px solid #f1f5f9;
    }

    .section-content p {
      margin-bottom: 0.5rem;
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
      font-size: 0.98rem;
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
      padding: 0.9rem 1.1rem;
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
      margin-top: 1.4rem;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
    }

    .copy-box-header {
      background: #e2e8f0;
      padding: 8px 14px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      font-size: 0.84rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .copy-actions {
      display: flex;
      align-items: center;
      gap: 6px;
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
      background: #ffffff;
      border: 1px solid #94a3b8;
      color: var(--text-main);
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-toggle-md:hover {
      background: #e2e8f0;
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
      display: none;
    }

    .copy-textarea.show {
      display: block;
    }

    /* Modal dialog for GitHub Edit instructions */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.6);
      z-index: 99999;
      justify-content: center;
      align-items: center;
      padding: 1rem;
    }

    .modal-backdrop.active {
      display: flex;
    }

    .modal-box {
      background: #ffffff;
      border-radius: 12px;
      max-width: 600px;
      width: 100%;
      padding: 1.8rem;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
    }

    .modal-title {
      font-size: 1.25rem;
      font-weight: 800;
      margin-bottom: 0.8rem;
      color: var(--text-main);
    }

    .modal-content {
      font-size: 0.92rem;
      line-height: 1.6;
      color: var(--text-muted);
      margin-bottom: 1.2rem;
    }

    .modal-content ol {
      padding-left: 1.2rem;
      margin-top: 0.6rem;
    }

    .modal-content li {
      margin-bottom: 0.5rem;
    }

    .modal-btn-close {
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      cursor: pointer;
      float: right;
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
        display: none;
      }
      .site-title {
        font-size: 1.6rem;
      }
    }
  </style>
</head>
<body>

  <!-- Top Sticky Collaboration & Edit Toolbar -->
  <div class="edit-sticky-toolbar">
    <div class="toolbar-left">
      <span class="edit-status-badge" id="editStatusBadge">🟢 瀏覽模式</span>
      <span style="font-size: 0.82rem; color: #cbd5e1;" id="saveIndicator">隨時可點擊「✏️ 開啟直接編輯模式」直接在網頁修改文字！</span>
    </div>
    <div class="toolbar-actions">
      <button class="btn-tool btn-tool-edit" id="btnToggleEdit" onclick="toggleEditMode()">✏️ 開啟直接編輯模式 (點擊文字直接改)</button>
      <button class="btn-tool btn-tool-save" onclick="saveAllEdits()">💾 儲存修改內容</button>
      <button class="btn-tool" style="background: #2563eb; color: #ffffff; border-color: #3b82f6;" onclick="copyAllCasesMarkdown()" title="一鍵複製全部 50 個案件的完整規格文本">📋 複製全文</button>
      <button class="btn-tool btn-tool-ghost" onclick="resetToDefault()">🔄 還原官方原始設定</button>
      <button class="btn-tool btn-tool-ghost" onclick="downloadEditedHtml()">📥 下載修改後網頁</button>
      <a href="https://github.com/hsiaoyujui114-code/taipei-detective-rpg/edit/main/cases.html" target="_blank" class="btn-tool btn-tool-github">🐙 在 GitHub 編輯原始碼</a>
      <button class="btn-tool btn-tool-ghost" onclick="openGitHubHelp()">❓ 如何在 GitHub 更改？</button>
    </div>
  </div>

  <!-- Edit Mode Active Notification Banner -->
  <div class="edit-hint-banner" id="editHintBanner">
    ✏️ 【您已進入線上直接修改模式】現在您可以直接用滑鼠點擊下方任何案件標題、歷史風情、科學原理、人物設定或破綻文字進行打字修改！修改完成後點擊上方「💾 儲存修改內容」即可永久保存！
  </div>

  <!-- Site Header -->
  <header class="site-header">
    <div class="header-container">
      <div class="header-badge">🏛️ 六年級獨立研究專題 ✕ 108 課綱生活科學探究 ✕ 全員直接編輯系統</div>
      <h1 class="site-title">《雙北漫遊：都會行蹤》50 大歷史風情與生活科學案件全集</h1>
      <p class="site-subtitle">
        收錄雙北 50 宗深度原創推理案件：將淡水稅關、艋舺龍山寺剝皮寮、大稻埕百年茶行、北投日治溫泉與青磺泉、平溪鐵道等在地風情，與 pH 酸鹼指示、365nm 螢光防偽、阿基米德浮力比重、熱敏水蒸氣顯影等生活科學緊密結合。
        <strong style="color: #fbbf24;">★ 只要知道本網址，任何人均可直接在網頁上點擊文字修改錯字，亦可一鍵同步至 Markdown 或 GitHub！</strong>
      </p>
      <div class="header-nav">
        <a href="index.html" class="btn-nav">🗺️ 返回雙北 2.5D 都會地圖沙盒</a>
        <a href="proposal.html" class="btn-nav">📋 查閱 16 週遊戲企劃全書</a>
        <button class="btn-nav" onclick="copyAllCasesMarkdown()" style="cursor:pointer; background:rgba(37, 99, 235, 0.45); border-color:#60a5fa; font-weight:700;">📋 一鍵複製 50 案全文</button>
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
      <div class="stat-pill">✍️ 線上直接改：<strong>點擊網頁文字即可打字修正</strong></div>
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
      <button class="btn-tool" onclick="copyAllCasesMarkdown()" style="width: 100%; margin-bottom: 0.75rem; justify-content: center; background: #2563eb; color: #ffffff; border-color: #3b82f6; padding: 7px; font-weight: 700;">📋 一鍵複製 50 案全文</button>
      <input type="text" class="search-input" id="sidebarSearch" placeholder="🔍 快速搜尋案件或編號..." oninput="filterCases()">
      <ul class="sidebar-nav-list" id="sidebarList">
""")

for c in all_cases:
    html_parts.append(f"""        <li class="sidebar-nav-item">
          <a href="#{c['id']}" class="sidebar-nav-link" title="{c['title']}">
            <strong>{c['id']}</strong> <span class="nav-title-{c['id']}">{html.escape(c['title'])}</span>
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

      <!-- Cases Stream Header with Quick Copy -->
      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 1.2rem; padding: 12px 18px; background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow);">
        <div>
          <span style="font-size: 1rem; font-weight: 800; color: var(--primary);">📚 雙北 50 大深度推理案件全書規格庫</span>
          <div style="font-size: 0.82rem; color: var(--text-muted);">含起因、經過、最後、人物誌、歷史考證、108 課綱自然科學與司法筆錄</div>
        </div>
        <button class="btn-copy" onclick="copyAllCasesMarkdown()" style="background: #2563eb; font-size: 0.88rem; padding: 8px 18px; cursor: pointer;">📋 一鍵複製 50 案完整全文 (Markdown)</button>
      </div>

      <!-- Cases Stream -->
      <div id="casesStream">
""")

for c in all_cases:
    md_text = generate_case_markdown(c)
    escaped_md = html.escape(md_text)

    # Characters HTML
    chars_html = []
    for idx_char, char in enumerate(c['characters']):
        card_class = "character-card"
        if "真兇" in char['identity']:
            card_class += " killer"
        elif "被害" in char['identity'] or "受害" in char['identity']:
            card_class += " victim"

        chars_html.append(f"""          <div class="{card_class}" data-char-idx="{idx_char}">
            <div class="char-name">
              <span data-editable="true" data-field="char_name" oninput="handleFieldChange('{c['id']}')">{html.escape(char['name'])}</span>
              <span class="char-identity" data-editable="true" data-field="char_identity" oninput="handleFieldChange('{c['id']}')">{html.escape(char['identity'])}</span>
            </div>
            <div class="char-field"><strong>身分與作息：</strong><span data-editable="true" data-field="char_job" oninput="handleFieldChange('{c['id']}')">{html.escape(char['job_daily'])}</span></div>
            <div class="char-field"><strong>與他人關係：</strong><span data-editable="true" data-field="char_rel_others" oninput="handleFieldChange('{c['id']}')">{html.escape(char['relation_others'])}</span></div>
            <div class="char-field"><strong>與被害人關係：</strong><span data-editable="true" data-field="char_rel_victim" oninput="handleFieldChange('{c['id']}')">{html.escape(char['relation_victim'])}</span></div>
            <div class="char-field"><strong>犯罪動機：</strong><span data-editable="true" data-field="char_motive" oninput="handleFieldChange('{c['id']}')">{html.escape(char['motive'])}</span></div>
            <div class="char-field"><strong>口供陳述：</strong><em data-editable="true" data-field="char_statement" oninput="handleFieldChange('{c['id']}')">{html.escape(char['statement'])}</em></div>
            <div class="char-field char-flaw"><strong>⚠️ 破綻關鍵：</strong><span data-editable="true" data-field="char_flaw" oninput="handleFieldChange('{c['id']}')">{html.escape(char['flaw'])}</span></div>
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
              <h2 class="case-title" data-editable="true" data-field="title" oninput="handleFieldChange('{c['id']}')">{html.escape(c['title'])}</h2>
              <span class="card-edited-tag">✏️ 已修改</span>
            </div>
            <div class="case-badges">
              <span class="badge badge-type">🏷️ <span data-editable="true" data-field="type" oninput="handleFieldChange('{c['id']}')">{html.escape(c['type'])}</span></span>
              <span class="badge badge-diff">難度：<span data-editable="true" data-field="difficulty" oninput="handleFieldChange('{c['id']}')">{html.escape(c['difficulty'])}</span></span>
              <span class="badge badge-spook"><span data-editable="true" data-field="spookiness" oninput="handleFieldChange('{c['id']}')">{html.escape(c['spookiness'])}</span></span>
              <span class="badge badge-location">📍 <span data-editable="true" data-field="district" oninput="handleFieldChange('{c['id']}')">{html.escape(c['district'])}</span></span>
              <a href="https://github.com/hsiaoyujui114-code/taipei-detective-rpg/edit/main/cases.html" target="_blank" class="btn-github-mini" title="在 GitHub 線上編輯原始碼">🐙 GitHub 編輯</a>
            </div>
          </div>

          <div class="case-body">
            <!-- 1. Location & History -->
            <div class="section-block">
              <div class="section-title">🏛️ 當地歷史事件與地方風情</div>
              <div class="section-content">
                <p><strong>【精確地點】</strong><span data-editable="true" data-field="location" oninput="handleFieldChange('{c['id']}')">{html.escape(c['location'])}</span></p>
                <p data-editable="true" data-field="history_culture" oninput="handleFieldChange('{c['id']}')">{html.escape(c['history_culture'])}</p>
                <p><strong>【交通常識與生活動線】</strong><span data-editable="true" data-field="traffic_trivia" oninput="handleFieldChange('{c['id']}')">{html.escape(c['traffic_trivia'])}</span></p>
              </div>
            </div>

            <!-- 2. Science Principle -->
            <div class="section-block">
              <div class="section-title">🔬 生活科學原理與鑑識依據（108 課綱）</div>
              <div class="section-content" style="background:#f0fdf4; border-color:#dcfce7;">
                <p data-editable="true" data-field="science_principle" oninput="handleFieldChange('{c['id']}')">{html.escape(c['science_principle'])}</p>
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
                <p><strong>【起因・案發前情】</strong><span data-editable="true" data-field="story_cause" oninput="handleFieldChange('{c['id']}')">{html.escape(c['story_cause'])}</span></p>
                <p><strong>【經過・調查動線】</strong><span data-editable="true" data-field="story_process" oninput="handleFieldChange('{c['id']}')">{html.escape(c['story_process'])}</span></p>
                <p><strong>【最後・破案邏輯】</strong><span data-editable="true" data-field="story_climax" oninput="handleFieldChange('{c['id']}')">{html.escape(c['story_climax'])}</span></p>
              </div>
            </div>

            <!-- 5. Deposition -->
            <div class="section-block">
              <div class="section-title">⚖️ 官方警訊偵查筆錄檔案</div>
              <div class="deposition-box">
                <div class="deposition-row"><strong>筆錄編號：</strong><span data-editable="true" data-field="depo_record_id" oninput="handleFieldChange('{c['id']}')">{html.escape(depo.get('record_id', ''))}</span> ｜ <strong>承辦人員：</strong><span data-editable="true" data-field="depo_officer" oninput="handleFieldChange('{c['id']}')">{html.escape(depo.get('officer', ''))}</span></div>
                <div class="deposition-row"><strong>受訊對象：</strong><span data-editable="true" data-field="depo_interrogee" oninput="handleFieldChange('{c['id']}')">{html.escape(depo.get('interrogee', ''))}</span></div>
                <div class="deposition-row"><strong>受訊供述：</strong><em data-editable="true" data-field="depo_testimony" oninput="handleFieldChange('{c['id']}')">{html.escape(testimony)}</em></div>
                <div class="deposition-row"><strong>矛盾破綻：</strong><span data-editable="true" data-field="depo_contradiction" oninput="handleFieldChange('{c['id']}')">{html.escape(depo.get('contradiction', ''))}</span></div>
                <div class="deposition-row" style="color:#b91c1c; font-weight:700;"><strong>關鍵鐵證：</strong><span data-editable="true" data-field="depo_evidence" oninput="handleFieldChange('{c['id']}')">{html.escape(depo.get('critical_evidence', ''))}</span></div>
              </div>
            </div>

            <!-- 6. Props & Easter Egg -->
            <div class="section-block">
              <div class="section-title">🎒 破案輔助道具三軌與鄰近文化彩蛋</div>
              <div class="section-content" style="background:#faf5ff; border-color:#f3e8ff;">
                <p><strong>💰 金錢購買途徑：</strong><span data-editable="true" data-field="prop_money" oninput="handleFieldChange('{c['id']}')">{html.escape(props.get('prop_money', ''))}</span></p>
                <p><strong>🏛️ 親身探索途徑：</strong><span data-editable="true" data-field="prop_explore" oninput="handleFieldChange('{c['id']}')">{html.escape(props.get('prop_explore', ''))}</span></p>
                <p><strong>🤝 社交打聽途徑：</strong><span data-editable="true" data-field="prop_social" oninput="handleFieldChange('{c['id']}')">{html.escape(props.get('prop_social', ''))}</span></p>
                <p><strong>🥚 鄰近文化彩蛋：</strong><span data-editable="true" data-field="prop_egg" oninput="handleFieldChange('{c['id']}')">{html.escape(props.get('easter_egg', ''))}</span></p>
              </div>
            </div>

            <!-- 7. Copy Area (Special Client Requirement) -->
            <div class="copy-box-container">
              <div class="copy-box-header">
                <span>📋 本案完整企劃設定（Markdown 規格文本・隨修改即時自動同步）</span>
                <div class="copy-actions">
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

  <!-- Help Modal Dialog -->
  <div class="modal-backdrop" id="gitHelpModal">
    <div class="modal-box">
      <h3 class="modal-title">🐙 任何人如何直接在 GitHub 上更改本網頁？</h3>
      <div class="modal-content">
        <p>委託人特別指示：只要知道本專案網址的人，都能隨時參與修改與更正錯字！您有以下兩種最簡單的方法：</p>
        <ol>
          <li><strong>方法一：在當前網頁直接改（最直覺推薦）</strong><br>
            點擊頂部黃色按鈕「<strong>✏️ 開啟直接編輯模式</strong>」，整張網頁的文字會立刻變成可以打字的狀態。修改完後點擊「<strong>💾 儲存修改內容</strong>」，修改會自動保存在您的瀏覽器中，亦可一鍵下載修改後 HTML！
          </li>
          <li><strong>方法二：在 GitHub 網站線上編輯（永久貢獻）</strong><br>
            前往 GitHub 倉庫頁面，按下鍵盤上的 <code>.</code> (英文點號) 鍵，或點擊任何案件右上角的「<strong>🐙 GitHub 編輯</strong>」按鈕，GitHub 就會在瀏覽器中開啟免安裝的 <strong>Web VS Code 編輯器</strong>！修改好字句後點擊左側「Commit」，即可送出您的更新！
          </li>
        </ol>
      </div>
      <button class="modal-btn-close" onclick="closeGitHubHelp()">我知道了，關閉說明</button>
    </div>
  </div>

  <!-- Toast Notification Popup -->
  <div id="toast">✅ 已成功複製本案完整設定！</div>

  <script>
    // Edit Mode State
    let isEditMode = false;
    const STORAGE_KEY = 'shuangbei_cases_custom_edits_v1';

    function toggleEditMode() {
      isEditMode = !isEditMode;
      document.body.classList.toggle('edit-mode-active', isEditMode);
      
      const btn = document.getElementById('btnToggleEdit');
      const badge = document.getElementById('editStatusBadge');
      const indicator = document.getElementById('saveIndicator');

      document.querySelectorAll('[data-editable="true"]').forEach(el => {
        el.contentEditable = isEditMode ? 'true' : 'false';
      });

      if (isEditMode) {
        btn.textContent = '🔒 退出編輯模式 (儲存變更)';
        btn.style.background = '#10b981';
        btn.style.color = '#ffffff';
        badge.textContent = '🟡 編輯模式進行中';
        badge.classList.add('active');
        indicator.textContent = '直接點選下方任何文字即可打字改錯！修改完成請點儲存。';
        showToast('✏️ 已開啟直接編輯模式！點擊任何文字即可打字修改！');
      } else {
        btn.textContent = '✏️ 開啟直接編輯模式 (點擊文字直接改)';
        btn.style.background = '#f59e0b';
        btn.style.color = '#0f172a';
        badge.textContent = '🟢 瀏覽模式';
        badge.classList.remove('active');
        indicator.textContent = '隨時可點擊「✏️ 開啟直接編輯模式」直接在網頁修改文字！';
        saveAllEdits();
      }
    }

    // Auto-update Card Markdown on Field Change
    function handleFieldChange(caseId) {
      const card = document.getElementById(caseId);
      if (!card) return;

      card.classList.add('is-edited');
      reconstructCardMarkdown(card, caseId);
    }

    function reconstructCardMarkdown(card, caseId) {
      const getVal = (field) => {
        const el = card.querySelector(`[data-field="${field}"]`);
        return el ? el.innerText.trim() : '';
      };

      const title = getVal('title');
      const type = getVal('type');
      const difficulty = getVal('difficulty');
      const spookiness = getVal('spookiness');
      const district = getVal('district');
      const location = getVal('location');
      const history_culture = getVal('history_culture');
      const traffic_trivia = getVal('traffic_trivia');
      const science_principle = getVal('science_principle');
      const story_cause = getVal('story_cause');
      const story_process = getVal('story_process');
      const story_climax = getVal('story_climax');
      const depo_record_id = getVal('depo_record_id');
      const depo_officer = getVal('depo_officer');
      const depo_interrogee = getVal('depo_interrogee');
      const depo_testimony = getVal('depo_testimony');
      const depo_contradiction = getVal('depo_contradiction');
      const depo_evidence = getVal('depo_evidence');
      const prop_money = getVal('prop_money');
      const prop_explore = getVal('prop_explore');
      const prop_social = getVal('prop_social');
      const prop_egg = getVal('prop_egg');

      // Update Nav title if changed
      const navTitleEl = document.querySelector(`.nav-title-${caseId}`);
      if (navTitleEl && title) navTitleEl.textContent = title;

      // Characters Markdown
      const charCards = card.querySelectorAll('.character-card');
      const charsMd = [];
      charCards.forEach(cCard => {
        const cName = cCard.querySelector('[data-field="char_name"]')?.innerText.trim() || '';
        const cIden = cCard.querySelector('[data-field="char_identity"]')?.innerText.trim() || '';
        const cJob = cCard.querySelector('[data-field="char_job"]')?.innerText.trim() || '';
        const cRelO = cCard.querySelector('[data-field="char_rel_others"]')?.innerText.trim() || '';
        const cRelV = cCard.querySelector('[data-field="char_rel_victim"]')?.innerText.trim() || '';
        const cMot = cCard.querySelector('[data-field="char_motive"]')?.innerText.trim() || '';
        const cStat = cCard.querySelector('[data-field="char_statement"]')?.innerText.trim() || '';
        const cFlaw = cCard.querySelector('[data-field="char_flaw"]')?.innerText.trim() || '';

        charsMd.push(`### 👤 ${cName}（${cIden}）
- **職業身分與生活作息**：${cJob}
- **與他人關係**：${cRelO}
- **與被害人關係**：${cRelV}
- **犯罪動機分析**：${cMot}
- **口供陳述**：${cStat}
- **破綻與打臉關鍵**：${cFlaw}`);
      });

      const updatedMd = `# 【${caseId}】${title}
- **案件類型**：${type}
- **難度星級**：${difficulty}
- **驚悚指數**：${spookiness}
- **案發地點**：${location}（${district}）

## 🏛️ 當地歷史事件與地方風情
${history_culture}
- **交通常識與生活動線**：${traffic_trivia}

## 🔬 生活科學原理與鑑識依據（108 課綱）
${science_principle}

## 👥 嚴謹細節人物誌
${charsMd.join('\\n')}

## 📖 案情推導三部曲
### 【起因】
${story_cause}

### 【經過】
${story_process}

### 【最後】
${story_climax}

## ⚖️ 官方警訊偵查筆錄
- **筆錄編號**：${depo_record_id}
- **承辦人員**：${depo_officer}
- **受訊人**：${depo_interrogee}
- **受訊供述**：${depo_testimony}
- **矛盾破綻**：${depo_contradiction}
- **關鍵鐵證**：${depo_evidence}

## 🎒 破案輔助道具三軌與鄰近彩蛋
- **💰 金錢購買途徑**：${prop_money}
- **🏛️ 親身探索途徑**：${prop_explore}
- **🤝 社交打聽途徑**：${prop_social}
- **🥚 鄰近文化彩蛋**：${prop_egg}`;

      const textarea = document.getElementById('md_' + caseId);
      if (textarea) textarea.value = updatedMd;
    }

    // Save All Edits to LocalStorage & Server API
    function saveAllEdits() {
      const edits = {};
      let editedCount = 0;

      document.querySelectorAll('.case-card.is-edited').forEach(card => {
        const caseId = card.id;
        const fields = {};
        card.querySelectorAll('[data-field]').forEach(el => {
          const key = el.getAttribute('data-field');
          fields[key] = el.innerHTML;
        });
        edits[caseId] = fields;
        editedCount++;
      });

      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(edits));
      } catch (e) {
        console.warn('LocalStorage save failed:', e);
      }

      // Try server-side persistence if server.js is running
      const fullHtml = '<!DOCTYPE html>\\n' + document.documentElement.outerHTML;
      fetch('/api/save-cases', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ html: fullHtml })
      }).then(r => r.json()).then(res => {
        if (res.success) {
          showToast(`💾 儲存成功！已同步寫入伺服器與瀏覽器！`);
        } else {
          showToast(`💾 已儲存！修改已保存在您的本機瀏覽器中！`);
        }
      }).catch(() => {
        showToast(`💾 已儲存！修改已保存在您的本機瀏覽器中（重新整理不消失）！`);
      });
    }

    // Restore Edits on Load
    function restoreSavedEdits() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (!saved) return;
        const edits = JSON.parse(saved);
        let count = 0;

        for (const [caseId, fields] of Object.entries(edits)) {
          const card = document.getElementById(caseId);
          if (!card) continue;
          card.classList.add('is-edited');
          count++;

          for (const [key, val] of Object.entries(fields)) {
            const el = card.querySelector(`[data-field="${key}"]`);
            if (el) el.innerHTML = val;
          }
          reconstructCardMarkdown(card, caseId);
        }

        if (count > 0) {
          showToast(`📝 已自動還原您先前的 ${count} 項自訂修改！`);
        }
      } catch (e) {
        console.warn('Restore edits error:', e);
      }
    }

    // Reset to Default
    function resetToDefault() {
      if (!confirm('確定要清除所有自訂修改，還原為官方預設版本嗎？')) return;
      localStorage.removeItem(STORAGE_KEY);
      location.reload();
    }

    // Download Edited HTML
    function downloadEditedHtml() {
      saveAllEdits();
      const content = '<!DOCTYPE html>\\n' + document.documentElement.outerHTML;
      const blob = new Blob([content], { type: 'text/html;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'cases_edited.html';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast('📥 成功下載修改後的完整 HTML 檔案！');
    }

    // GitHub Help Modal
    function openGitHubHelp() {
      document.getElementById('gitHelpModal').classList.add('active');
    }

    function closeGitHubHelp() {
      document.getElementById('gitHelpModal').classList.remove('active');
    }

    // Copy Markdown to Clipboard (Single Case)
    function copyCaseMarkdown(caseId) {
      const textarea = document.getElementById('md_' + caseId);
      if (!textarea) return;

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(textarea.value).then(() => {
          showToast('✅ 已複製 ' + caseId + ' 完整設定至剪貼簿！');
        }).catch(() => {
          fallbackCopyText(textarea.value, '✅ 已複製 ' + caseId + ' 完整設定！');
        });
      } else {
        fallbackCopyText(textarea.value, '✅ 已複製 ' + caseId + ' 完整設定！');
      }
    }

    // Copy All 50 Cases Markdown to Clipboard (Full Text - Special Client Requirement)
    function copyAllCasesMarkdown() {
      const textareas = document.querySelectorAll('.copy-textarea');
      if (!textareas || textareas.length === 0) {
        showToast('⚠️ 未找到可複製的案件內容！');
        return;
      }

      const parts = [
        '# 《雙北漫遊：都會行蹤》50 大歷史風情與生活科學案件全集',
        '六年級獨立研究專題 ✕ 108 課綱生活科學探究 ✕ 柯南/福爾摩斯嚴謹人物誌\\n',
        '---\\n'
      ];

      textareas.forEach(ta => {
        if (ta && ta.value && ta.value.trim()) {
          parts.push(ta.value.trim());
          parts.push('\\n\\n---\\n');
        }
      });

      const fullText = parts.join('\\n');

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(fullText).then(() => {
          showToast('📋✅ 已成功複製全站 50 案完整全文（含即時修改）至剪貼簿！');
        }).catch(() => {
          fallbackCopyText(fullText, '📋✅ 已成功複製全站 50 案完整全文！');
        });
      } else {
        fallbackCopyText(fullText, '📋✅ 已成功複製全站 50 案完整全文！');
      }
    }

    function fallbackCopyText(text, successMsg) {
      const dummy = document.createElement('textarea');
      dummy.value = text;
      dummy.style.position = 'fixed';
      dummy.style.top = '0';
      dummy.style.left = '-9999px';
      dummy.style.opacity = '0';
      document.body.appendChild(dummy);
      dummy.focus();
      dummy.select();
      try {
        const ok = document.execCommand('copy');
        if (ok) {
          showToast(successMsg || '📋✅ 複製成功！');
        } else {
          showToast('❌ 瀏覽器限制，請點擊各案展開手動複製！');
        }
      } catch (e) {
        showToast('❌ 複製失敗，請手動複製！');
      }
      document.body.removeChild(dummy);
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
      }, 3000);
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

    // Auto run on load
    window.addEventListener('DOMContentLoaded', () => {
      restoreSavedEdits();
    });
  </script>
</body>
</html>
""")

output_file = os.path.join(os.path.dirname(__file__), "cases.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print(f"Successfully generated cases.html with interactive in-place editor! Size: {os.path.getsize(output_file)} bytes.")
