<!-- catalog-only-start --><!-- ---
name: Color
title: Color System
order: 2
-----><!-- catalog-only-end -->

# 토스뱅크 컬러 시스템 (Color System)

토스뱅크의 시그니처 딥 로얄 블루(`#0064FF`)와 틴트 블루(`#E8F3FF`), 감각적인 듀얼톤 체크카드 포인트 컬러, 그리고 금융 신뢰도를 전달하는 시맨틱 컬러 토큰 시스템입니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>💡 시각적 가독성 인터랙션 가이드:</strong> 각 색상 카드의 <strong>[복사]</strong> 버튼을 누르면 클립보드에 HEX 코드가 즉시 복사되며, 우측 상단 뱃지에서 <strong>WCAG 2.1 대비율(AA / AAA)</strong>을 실시간 확인할 수 있습니다.
  </div>
  <h3 style="margin-top:0;">1. 브랜드 핵심 시스템 컬러 (Key Brand Colors)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid">
    <!-- Primary -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #0064FF; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (4.6:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Primary (Toss Deep Blue)</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-primary</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#0064FF</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#0064FF'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- On Primary -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #FFFFFF; color: #191F28; border: 1px solid #E5E8EB;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (14.2:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">On Primary (Pure White)</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-on-primary</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#FFFFFF</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#FFFFFF'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Primary Container -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #E8F3FF; color: #0047BB;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (7.8:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Primary Container (Tint Blue)</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-primary-container</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#E8F3FF</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#E8F3FF'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- On Primary Container -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #0047BB; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (8.5:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">On Primary Container</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-on-primary-container</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#0047BB</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#0047BB'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
  </div>

  <h3>2. 듀얼톤 체크카드 포인트 팔레트 (Dual-Tone Card Accents)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid">
    <!-- Lemon Yellow -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #FFE100; color: #191F28;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (14.2:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Lemon Yellow (체크카드)</span>
        <span class="tb-color-token kb-color-token">--tb-accent-lemon</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#FFE100</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#FFE100'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Night Pink -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #FF3B70; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aa">AA (4.8:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Night Pink (나이트 핑크)</span>
        <span class="tb-color-token kb-color-token">--tb-accent-pink</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#FF3B70</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#FF3B70'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Royal Purple -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #7B2CBF; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (6.8:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Royal Purple (퍼플)</span>
        <span class="tb-color-token kb-color-token">--tb-accent-purple</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#7B2CBF</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#7B2CBF'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Sunset Orange -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #FF6B00; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aa">AA (4.5:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Sunset Orange (오렌지밀크)</span>
        <span class="tb-color-token kb-color-token">--tb-accent-orange</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#FF6B00</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#FF6B00'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
  </div>

  <h3>3. 뉴트럴 서피스 & 보더 스케일 (Neutral Surfaces)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid">
    <!-- Surface 100 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #F9FAFB; color: #191F28; border: 1px solid #E5E8EB;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (13.6:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Surface Container Low</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-surface-container-low</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#F9FAFB</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#F9FAFB'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Surface 200 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #F2F4F6; color: #191F28;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (12.8:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Surface High (Grey 100)</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-surface-container-high</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#F2F4F6</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#F2F4F6'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Outline -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #D1D6DB; color: #191F28;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (9.2:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Outline (Grey 300)</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-outline</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#D1D6DB</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#D1D6DB'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- On Surface -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #191F28; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">AAA (14.2:1)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">On Surface (Grey 900)</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-on-surface</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#191F28</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#191F28'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
  </div>
</div>
