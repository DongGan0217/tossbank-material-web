---
name: Typography
title: Typography System
order: 3
---

# 토스 디자인 시스템 타이포그래피 (TDS Typography System)

토스 상용 앱(`viva.republica.toss.apk`)에서 추출한 정품 `Toss Product Sans`(8대 가중치), 헤드라인 전용 `Toss Design Sans Bold`, 한글 본문 최적화 `Pretendard Variable`, 그리고 금융 송금/잔액 필수 오픈타입 피처인 **`tnum` (Tabular Numbers)** 시스템입니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>✍️ 실시간 타이핑 샌드박스 & 타뷸라 넘버:</strong> 아래 입력창에 금액이나 텍스트를 입력하면 15단계 TDS 타입 스케일에 즉시 반영됩니다. 특히 <strong>[타뷸라 넘버 On/Off]</strong> 스위치를 통해 금융 숫자가 수직선상에서 완벽히 고정되는 효과를 확인하세요.
  </div>

  <div class="tb-type-tester-box kb-type-tester-box" style="background:#FFFFFF; border:1px solid #E5E8EB; border-radius:14px; padding:18px; margin-bottom:24px;">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
      <div style="flex:1; min-width:260px;">
        <label for="tb-type-input" style="font-size: 13px; font-weight: 700; color: #4E5968;">테스트 문구 / 금융 금액:</label>
        <input id="tb-type-input" class="tb-type-input kb-type-input" type="text" value="3,842,000원 (연 2.0% 복리)" oninput="document.querySelectorAll('.tb-sample-target').forEach(el=>el.innerText=this.value)" style="margin-top: 6px; width:100%; padding:10px 14px; font-size:15px; border-radius:10px; border:1px solid #D1D6DB;" />
      </div>
      <div>
        <label style="font-size:13px; font-weight:700; color:#4E5968; display:block; margin-bottom:6px;">타뷸라 넘버 (tnum):</label>
        <button id="tnum-toggle-btn" class="tb-copy-btn" onclick="const targets=document.querySelectorAll('.tb-sample-target'); const active=this.dataset.active==='true'; targets.forEach(t=>t.style.fontFeatureSettings=active?'normal':'\'tnum\' 1'); this.dataset.active=!active; this.innerText=active?'tnum OFF':'tnum ON (고정폭)'; this.style.background=active?'#F2F4F6':'#0064FF'; this.style.color=active?'#191F28':'#FFFFFF';" style="padding:9px 16px; border-radius:8px; font-weight:700; background:#0064FF; color:#FFFFFF; border:none; cursor:pointer;" data-active="true">tnum ON (고정폭)</button>
      </div>
    </div>
  </div>

  <h3 style="margin-top:0;">1. 서체 패밀리 아키텍처 (Font Family Architecture)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));">
    <div class="tb-color-card kb-color-card" style="padding:18px;">
      <span class="tb-shape-token" style="color:#0064FF; font-weight:700;">Display & Numeric Standard</span>
      <h4 style="margin:8px 0; font-family:'Toss Product Sans'; font-size:20px;">Toss Product Sans</h4>
      <p style="font-size:13px; color:#6B7684; margin:0;">Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black, Heavy 8종 가중치. 숫자/영문 및 대형 디스플레이 특화.</p>
    </div>
    <div class="tb-color-card kb-color-card" style="padding:18px;">
      <span class="tb-shape-token" style="color:#0064FF; font-weight:700;">Display Headline Bold</span>
      <h4 style="margin:8px 0; font-family:'Toss Design Sans', sans-serif; font-size:20px;">Toss Design Sans Bold</h4>
      <p style="font-size:13px; color:#6B7684; margin:0;">상용 앱 타이틀 및 모달 핵심 헤드라인 강조에 채택되는 묵직하고 신뢰도 높은 볼드 전용 서체.</p>
    </div>
    <div class="tb-color-card kb-color-card" style="padding:18px;">
      <span class="tb-shape-token" style="color:#0064FF; font-weight:700;">Korean Interface Body</span>
      <h4 style="margin:8px 0; font-family:Pretendard, sans-serif; font-size:20px;">Pretendard Variable</h4>
      <p style="font-size:13px; color:#6B7684; margin:0;">한글 자간 -0.02em 밀착 보정 및 시스템 디바이스 전반에 무손실 렌더링되는 모바일 웹 표준 한글 본문 본체.</p>
    </div>
  </div>

  <h3>2. TDS 텍스트 위계 스케일 (Typography Hierarchy)</h3>
  <div class="tb-type-scale-grid kb-type-scale-grid">
    <!-- D1 -->
    <div class="tb-type-scale-card kb-type-scale-card">
      <div class="tb-type-meta kb-type-meta">
        <span class="tb-type-role kb-type-role">Display 1 (D1)</span>
        <span class="tb-type-specs kb-type-specs">56px / 68px / Heavy 950 / Toss Product Sans</span>
      </div>
      <div class="tb-type-sample kb-type-sample tb-sample-target" style="font-family:'Toss Product Sans', Pretendard; font-size: 44px; line-height: 1.2; font-weight: 900; font-feature-settings:'tnum' 1;">3,842,000원 (연 2.0% 복리)</div>
    </div>
    <!-- T1 -->
    <div class="tb-type-scale-card kb-type-scale-card">
      <div class="tb-type-meta kb-type-meta">
        <span class="tb-type-role kb-type-role">Title 1 (T1)</span>
        <span class="tb-type-specs kb-type-specs">30px / 38px / Bold 700 / Toss Design Sans</span>
      </div>
      <div class="tb-type-sample kb-type-sample tb-sample-target" style="font-family:'Toss Design Sans', Pretendard; font-size: 28px; line-height: 1.3; font-weight: 700; font-feature-settings:'tnum' 1;">3,842,000원 (연 2.0% 복리)</div>
    </div>
    <!-- T3 -->
    <div class="tb-type-scale-card kb-type-scale-card">
      <div class="tb-type-meta kb-type-meta">
        <span class="tb-type-role kb-type-role">Title 3 (T3 - 모달/섹션 헤더)</span>
        <span class="tb-type-specs kb-type-specs">22px / 30px / Bold 700</span>
      </div>
      <div class="tb-type-sample kb-type-sample tb-sample-target" style="font-size: 20px; line-height: 1.35; font-weight: 700; font-feature-settings:'tnum' 1;">3,842,000원 (연 2.0% 복리)</div>
    </div>
    <!-- T5 -->
    <div class="tb-type-scale-card kb-type-scale-card">
      <div class="tb-type-meta kb-type-meta">
        <span class="tb-type-role kb-type-role">Title 5 (T5 - 리스트 헤딩)</span>
        <span class="tb-type-specs kb-type-specs">17px / 24px / SemiBold 600</span>
      </div>
      <div class="tb-type-sample kb-type-sample tb-sample-target" style="font-size: 17px; line-height: 1.4; font-weight: 600; font-feature-settings:'tnum' 1;">3,842,000원 (연 2.0% 복리)</div>
    </div>
    <!-- B1 -->
    <div class="tb-type-scale-card kb-type-scale-card">
      <div class="tb-type-meta kb-type-meta">
        <span class="tb-type-role kb-type-role">Body 1 (B1 - 표준 본문)</span>
        <span class="tb-type-specs kb-type-specs">16px / 24px / Regular 400</span>
      </div>
      <div class="tb-type-sample kb-type-sample tb-sample-target" style="font-size: 15px; line-height: 1.5; font-weight: 400; font-feature-settings:'tnum' 1;">3,842,000원 (연 2.0% 복리)</div>
    </div>
    <!-- B2 -->
    <div class="tb-type-scale-card kb-type-scale-card">
      <div class="tb-type-meta kb-type-meta">
        <span class="tb-type-role kb-type-role">Body 2 (B2 - 서브 설명)</span>
        <span class="tb-type-specs kb-type-specs">14px / 20px / Regular 400</span>
      </div>
      <div class="tb-type-sample kb-type-sample tb-sample-target" style="font-size: 14px; line-height: 1.4; font-weight: 400; color: #6B7684; font-feature-settings:'tnum' 1;">3,842,000원 (연 2.0% 복리)</div>
    </div>
    <!-- C1 -->
    <div class="tb-type-scale-card kb-type-scale-card">
      <div class="tb-type-meta kb-type-meta">
        <span class="tb-type-role kb-type-role">Caption 1 (C1 - 배지 및 각주)</span>
        <span class="tb-type-specs kb-type-specs">12px / 16px / SemiBold 600</span>
      </div>
      <div class="tb-type-sample kb-type-sample tb-sample-target" style="font-size: 12px; line-height: 1.3; font-weight: 600; color: #0064FF; font-feature-settings:'tnum' 1;">3,842,000원 (연 2.0% 복리)</div>
    </div>
  </div>
</div>
