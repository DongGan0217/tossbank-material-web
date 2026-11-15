---
name: Shape
title: Shape System
order: 4
---

# 토스 디자인 시스템 형태 (TDS Squircle Shape System)

토스 상용 앱(`viva.republica.toss.apk`)의 독보적인 비주얼 아이덴티티를 형성하는 **초타원 스쿼클(Squircle / G2 연속 곡률)** 모델과 8단계 코너 래디우스 시스템입니다. 일반적인 원호(Circular Arc) `border-radius`와 달리 모서리 시작점과 끝점의 곡률이 매끄럽게 연결되어 친근하고 유기적인 조약돌 감성을 완성합니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>📐 스쿼클(Squircle) vs 원호(Circular Arc) 비교:</strong> 토스의 모든 모듈/카드/버튼은 모서리 접합부가 꺾여 보이지 않는 연속 곡률(Squircle) 원리를 기반으로 설계되었습니다. 아래 인터랙티브 비교 뷰어에서 두 형태의 시각적 곡률 차이를 직접 체감할 수 있습니다.
  </div>

  <h3 style="margin-top:0;">1. 원호 vs 스쿼클 1:1 비교 렌더러 (Visual Curvature Comparison)</h3>
  <div class="tb-color-swatch-grid kb-color-swatch-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));">
    <!-- Standard Circular Arc -->
    <div class="tb-shape-card kb-shape-card" style="padding:20px; text-align:center;">
      <span class="tb-shape-token" style="color:#6B7684; font-weight:700;">일반 원호 (Circular Arc)</span>
      <div style="margin:20px auto; width:160px; height:110px; background:#D1D6DB; border-radius:24px; display:flex; align-items:center; justify-content:center; color:#1E1F21; font-weight:700; font-size:13px;">
        border-radius: 24px
      </div>
      <p style="font-size:12px; color:#6B7684; margin:0;">직선과 곡선 접점에서 곡률이 0에서 1/r로 급변하여 모서리 경계가 꺾여 보임.</p>
    </div>
    <!-- TDS Squircle Continuous Curvature -->
    <div class="tb-shape-card kb-shape-card" style="padding:20px; text-align:center; border:2px solid #0064FF;">
      <span class="tb-shape-token" style="color:#0064FF; font-weight:700;">TDS 스쿼클 (Squircle G2 연속성)</span>
      <div class="tb-squircle-preview" style="margin:20px auto; width:160px; height:110px; background:#0064FF; border-radius:24px; display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:700; font-size:13px; box-shadow:0 8px 24px rgba(0, 100, 255, 0.25);">
        TDS Squircle 24px
      </div>
      <p style="font-size:12px; color:#0064FF; font-weight:600; margin:0;">모서리 곡률이 서서히 증가하여 자연스럽고 부드러운 유기적 라운딩 완성.</p>
    </div>
  </div>

  <h3>2. 실시간 코너 래디우스 Knob 컨트롤러</h3>
  <div class="tb-type-tester-box kb-type-tester-box" style="background:#FFFFFF; border:1px solid #E5E8EB; border-radius:14px; padding:20px; margin-bottom:24px;">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
      <div style="flex:1; min-width:240px;">
        <label for="tb-radius-knob" style="font-size: 13px; font-weight: 700; color: #4E5968;">곡률 슬라이더: <span id="knob-val-display" style="color:#0064FF;">16px (TDS 표준 버튼)</span></label>
        <input id="tb-radius-knob" type="range" min="0" max="40" value="16" step="2" oninput="document.getElementById('knob-demo-box').style.borderRadius=this.value+'px'; document.getElementById('knob-val-display').innerText=this.value+'px';" style="width:100%; margin-top:8px; accent-color:#0064FF;" />
      </div>
      <div style="display:flex; align-items:center; justify-content:center; width:220px;">
        <div id="knob-demo-box" style="width:180px; height:70px; background:#0064FF; color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:14px; border-radius:16px; box-shadow:0 4px 14px rgba(0,100,255,0.25); transition:border-radius 0.1s ease;">
          토스뱅크 인터랙티브 버튼
        </div>
      </div>
    </div>
  </div>

  <h3>3. TDS 8단계 코너 래디우스 스케일 (Corner Radius Scale)</h3>
  <div class="tb-shape-scale-grid kb-shape-scale-grid">
    <!-- Micro (4px) -->
    <div class="tb-shape-card kb-shape-card">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 4px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name">Micro</span>
        <span class="tb-shape-value kb-shape-value">4px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-micro</span>
        <p class="tb-shape-desc kb-shape-desc">배지, 카운터 점, 최소 인디케이터</p>
      </div>
    </div>
    <!-- Small (8px) -->
    <div class="tb-shape-card kb-shape-card">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 8px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name">Small</span>
        <span class="tb-shape-value kb-shape-value">8px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-small</span>
        <p class="tb-shape-desc kb-shape-desc">필터 칩, 인라인 태그, 툴팁</p>
      </div>
    </div>
    <!-- Medium-Small (12px) -->
    <div class="tb-shape-card kb-shape-card">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 12px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name">Medium-Small</span>
        <span class="tb-shape-value kb-shape-value">12px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-ms</span>
        <p class="tb-shape-desc kb-shape-desc">소형 서브 카드, 인풋 내부 박스</p>
      </div>
    </div>
    <!-- Medium (16px - Standard) -->
    <div class="tb-shape-card kb-shape-card" style="border:2px solid #0064FF;">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 16px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name" style="color:#0064FF;">Medium (TDS 표준)</span>
        <span class="tb-shape-value kb-shape-value">16px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-medium</span>
        <p class="tb-shape-desc kb-shape-desc">표준 버튼, 텍스트필드 컨테이너, 리스트 로우</p>
      </div>
    </div>
    <!-- Large (20px) -->
    <div class="tb-shape-card kb-shape-card">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 20px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name">Large</span>
        <span class="tb-shape-value kb-shape-value">20px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-large</span>
        <p class="tb-shape-desc kb-shape-desc">토스뱅크 통장 카드, 모듈 컨테이너</p>
      </div>
    </div>
    <!-- X-Large (24px) -->
    <div class="tb-shape-card kb-shape-card">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 24px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name">X-Large</span>
        <span class="tb-shape-value kb-shape-value">24px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-xl</span>
        <p class="tb-shape-desc kb-shape-desc">바텀시트 상단 모서리, 다이얼로그 모달</p>
      </div>
    </div>
    <!-- XX-Large (28px) -->
    <div class="tb-shape-card kb-shape-card">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 28px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name">XX-Large</span>
        <span class="tb-shape-value kb-shape-value">28px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-xxl</span>
        <p class="tb-shape-desc kb-shape-desc">대형 프로모션 배너, 하이라이트 시트</p>
      </div>
    </div>
    <!-- Full (Pill 9999px) -->
    <div class="tb-shape-card kb-shape-card">
      <div class="tb-shape-preview-box kb-shape-preview-box">
        <div class="tb-shape-object kb-shape-object" style="border-radius: 9999px; background: #0064FF;"></div>
      </div>
      <div class="tb-shape-info kb-shape-info">
        <span class="tb-shape-name kb-shape-name">Full (Pill)</span>
        <span class="tb-shape-value kb-shape-value">9999px</span>
        <span class="tb-shape-token kb-shape-token">--toss-radius-full</span>
        <p class="tb-shape-desc kb-shape-desc">송금 Pill 버튼, 플로팅 FAB, 원형 아바타</p>
      </div>
    </div>
  </div>
</div>
