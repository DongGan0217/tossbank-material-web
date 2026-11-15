---
name: Color
title: Color System
order: 2
---

# 토스 디자인 시스템 컬러 (TDS Color System)

토스 상용 앱(`viva.republica.toss.apk`)의 `resources.arsc`에서 100% 실측 추출한 TDS 원시 10단계 컬러 팔레트(Light/Dark), 183개 시맨틱 기능 토큰, 그리고 토스뱅크 고유의 딥 로얄 블루(`#0064FF`) 및 틴트 블루(`#E8F3FF`) 체계입니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>💡 TDS 실측 토큰 가이드:</strong> 토스의 컬러 체계는 Light 모드와 Dark 모드가 완전히 1:1로 정밀하게 튜닝된 10단계(`050`~`900`) 원시 팔레트와 목적 지향 시맨틱 토큰으로 구성됩니다. 각 카드의 <strong>[복사]</strong> 버튼을 누르면 실측 HEX 코드가 즉시 복사됩니다.
  </div>

  <h3 style="margin-top:0;">1. TDS 핵심 브랜드 블루 스케일 (TDS Blue Palette 10단계)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid">
    <!-- blue_050 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #F2F8FF; color: #1E1F21; border: 1px solid #E5E8EB;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Light 050</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">blue_050 (틴트 배경)</span>
        <span class="tb-color-token kb-color-token">--toss-color-blue-050</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#F2F8FF</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#F2F8FF'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- blue_100 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #EBF4FF; color: #1E1F21; border: 1px solid #E5E8EB;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Light 100</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">blue_100 (연한 하이라이트)</span>
        <span class="tb-color-token kb-color-token">--toss-color-blue-100</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#EBF4FF</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#EBF4FF'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- blue_300 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #BFDBFD; color: #1E1F21;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Light 300</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">blue_300 (소프트 인포)</span>
        <span class="tb-color-token kb-color-token">--toss-color-blue-300</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#BFDBFD</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#BFDBFD'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- blue_500 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #4396FB; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aa">Light 500</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">blue_500 (액티브 인터랙션)</span>
        <span class="tb-color-token kb-color-token">--toss-color-blue-500</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#4396FB</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#4396FB'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- blue_600 (Signature) -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #3182F6; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Toss Blue (600)</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">blue_600 (토스 시그니처)</span>
        <span class="tb-color-token kb-color-token">--toss-color-blue-600</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#3182F6</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#3182F6'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- blue_700 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #2272EB; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Light 700</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">blue_700 (호버/프레스 블루)</span>
        <span class="tb-color-token kb-color-token">--toss-color-blue-700</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#2272EB</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#2272EB'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Toss Bank Deep Blue -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #0064FF; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">TossBank Deep</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">Toss Bank Royal Deep Blue</span>
        <span class="tb-color-token kb-color-token">--md-sys-color-primary</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#0064FF</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#0064FF'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- blue_900 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #1C4989; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Light 900</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">blue_900 (다크 블루 텍스트)</span>
        <span class="tb-color-token kb-color-token">--toss-color-blue-900</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#1C4989</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#1C4989'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
  </div>

  <h3>2. TDS 뉴트럴 그레이 스케일 (TDS Grey Palette 10단계)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid">
    <!-- grey_050 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #F6F7F9; color: #1E1F21; border: 1px solid #E5E8EB;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">grey_050</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_050 (화면 배경 바탕)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-050</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#F6F7F9</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#F6F7F9'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- grey_100 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #F2F4F6; color: #1E1F21; border: 1px solid #E5E8EB;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">grey_100</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_100 (카드/박스 채우기)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-100</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#F2F4F6</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#F2F4F6'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- grey_200 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #E9EBED; color: #1E1F21;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">grey_200</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_200 (구분선 디바이더)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-200</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#E9EBED</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#E9EBED'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- grey_300 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #D7D9DB; color: #1E1F21;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">grey_300</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_300 (강조 보더)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-300</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#D7D9DB</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#D7D9DB'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- grey_500 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #939597; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aa">grey_500</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_500 (보조 캡션)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-500</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#939597</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#939597'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- grey_600 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #757779; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">grey_600</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_600 (서브 타이틀)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-600</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#757779</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#757779'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- grey_700 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #525355; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">grey_700</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_700 (본문 텍스트)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-700</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#525355</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#525355'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- grey_900 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #1E1F21; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">grey_900</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">grey_900 (메인 볼드 헤딩)</span>
        <span class="tb-color-token kb-color-token">--toss-color-grey-900</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#1E1F21</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#1E1F21'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
  </div>

  <h3>3. TDS 시맨틱 기능 토큰 (Semantic Function Tokens)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid">
    <!-- Green 600 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #1F9D6F; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Success</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">green_600 (입금/완료/상승)</span>
        <span class="tb-color-token kb-color-token">--toss-color-green-600</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#1F9D6F</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#1F9D6F'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Red 600 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #EF3341; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Danger</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">red_600 (출금/오류/감소)</span>
        <span class="tb-color-token kb-color-token">--toss-color-red-600</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#EF3341</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#EF3341'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Teal 600 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #159999; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Teal</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">teal_600 (투자/자산/혜택)</span>
        <span class="tb-color-token kb-color-token">--toss-color-teal-600</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#159999</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#159999'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
    <!-- Yellow 600 -->
    <div class="tb-color-card kb-color-card">
      <div class="tb-swatch-chip kb-swatch-chip" style="background-color: #E26D00; color: #FFFFFF;">
        <span class="tb-contrast-badge kb-contrast-badge pass-aaa">Warning</span>
      </div>
      <div class="tb-color-info kb-color-info">
        <span class="tb-color-role kb-color-role">yellow_600 (경고/유의사항)</span>
        <span class="tb-color-token kb-color-token">--toss-color-yellow-600</span>
        <div class="tb-color-actions kb-color-actions">
          <span class="tb-hex-code kb-hex-code">#E26D00</span>
          <button class="tb-copy-btn kb-copy-btn" onclick="navigator.clipboard.writeText('#E26D00'); this.innerText='복사됨!'; setTimeout(()=>this.innerText='복사', 1500)">복사</button>
        </div>
      </div>
    </div>
  </div>
</div>
