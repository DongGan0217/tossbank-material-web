# Elevation

<!--*
# Document freshness: For more information, see go/fresh-source.
freshness: { owner: 'lizmitchell' reviewed: '2026-07-31' }
tag: 'docType:reference'
*-->

<!-- go/md-elevation -->

<!-- [TOC] -->

[Elevation](https://m3.material.io/styles/elevation)<!-- {.external} --> is the relative
distance between two surfaces along the z-axis.

Material's elevation system is deliberately limited to just a handful of levels.
This creative constraint means you need to make thoughtful decisions about your
UI’s elevation story.

![Diagram showing the five elevation levels and their respective dp values](images/elevation/hero.svg "Material uses six levels of elevation, each with a corresponding dp value. These values are named for their relative distance above the UI’s surface: 0, +1, +2, +3, +4, and +5. An element’s resting state can be on levels 0 to +3, while levels +4 and +5 are reserved for user-interacted states such as hover and dragged.")

<!-- KakaoBank Interactive Options Playground & Live Sandbox -->
<div class="kb-playground-container">
  <div class="kb-playground-header">
    <div class="kb-playground-title">
      <span>🛠️ Elevation (입체감 & 그림자) 실시간 옵션 샌드박스</span>
      <span class="kb-playground-badge">Live Interactive</span>
    </div>
    <span style="font-size: 12px; color: #4E5968;">카카오뱅크 카드의 0~5단계 그림자 레벨을 실시간으로 조작해보세요.</span>
  </div>
  <div class="kb-playground-body">
    <div class="kb-playground-controls">
      <div class="kb-control-group">
        <label class="kb-control-label" for="kb-elev-level">그림자 레벨 (Level: <span id="kb-elev-num">2</span>):</label>
        <input id="kb-elev-level" type="range" min="0" max="5" value="2" oninput="updateElevDemo()" style="width: 100%; accent-color: #FFE100; cursor: pointer;" />
      </div>
      <div class="kb-control-group">
        <label class="kb-control-label" for="kb-elev-radius">코너 곡률 (Border Radius):</label>
        <select id="kb-elev-radius" class="kb-control-select" onchange="updateElevDemo()">
          <option value="16" selected>16px (카카오뱅크 표준 카드)</option>
          <option value="24">24px (다이얼로그 및 시트)</option>
          <option value="8">8px (콤팩트 박스)</option>
        </select>
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 4px;">
        <label class="kb-control-checkbox">
          <input id="kb-elev-border" type="checkbox" checked onchange="updateElevDemo()" />
          <span>카카오 옐로우 액센트 보더 (Signature Yellow Border)</span>
        </label>
      </div>
    </div>
    <div class="kb-playground-canvas" id="kb-elev-canvas" style="min-height: 200px; display: flex; justify-content: center; align-items: center; padding: 24px;">
      <div id="kb-elev-render" style="width: 260px; height: 140px; background: #FFFFFF; border-radius: 16px; border: 1.5px solid #FFE100; box-shadow: 0 4px 14px rgba(0,0,0,0.08); display: flex; flex-direction: column; align-items: center; justify-content: center; transition: all 0.25s ease;">
        <span style="font-size: 18px; font-weight: 800; color: #191F28;" id="kb-elev-label">Elevation Level 2</span>
        <span style="font-size: 12px; color: #76808E; margin-top: 4px;" id="kb-elev-sub">기본 카드 및 컴포넌트 부유 상태</span>
      </div>
    </div>
  </div>
  <div class="kb-playground-footer">
    <pre class="kb-code-preview" id="kb-elev-code">&lt;div style="position: relative;"&gt;
  &lt;md-elevation style="--md-elevation-level: 2;"&gt;&lt;/md-elevation&gt;
  카카오뱅크 카드
&lt;/div&gt;</pre>
    <button class="kb-copy-code-btn" type="button" onclick="navigator.clipboard.writeText(document.getElementById('kb-elev-code').innerText); this.innerText='복사 완료!'; setTimeout(()=>this.innerText='코드 복사', 1500)">코드 복사</button>
  </div>
</div>
<script>
  function updateElevDemo() {
    const level = Number(document.getElementById('kb-elev-level').value);
    const radius = document.getElementById('kb-elev-radius').value;
    const hasBorder = document.getElementById('kb-elev-border').checked;

    document.getElementById('kb-elev-num').innerText = level;
    const card = document.getElementById('kb-elev-render');
    const label = document.getElementById('kb-elev-label');
    const sub = document.getElementById('kb-elev-sub');
    const code = document.getElementById('kb-elev-code');

    label.innerText = 'Elevation Level ' + level;
    card.style.borderRadius = radius + 'px';
    card.style.border = hasBorder ? '1.5px solid #FFE100' : '1px solid #E5E8EB';

    const shadows = [
      'none',
      '0 1px 3px rgba(0,0,0,0.06)',
      '0 4px 14px rgba(0,0,0,0.08)',
      '0 8px 24px rgba(0,0,0,0.12)',
      '0 12px 36px rgba(0,0,0,0.16)',
      '0 20px 48px rgba(0,0,0,0.22)'
    ];
    const subs = [
      'Flat (바닥 서피스에 밀착된 상태)',
      'Level 1 (미세한 분리형 카드)',
      'Level 2 (카카오뱅크 시그니처 카드)',
      'Level 3 (호버 및 활성 카드 부유 상태)',
      'Level 4 (모달 다이얼로그 및 바텀시트)',
      'Level 5 (최상위 알림 및 팝업)'
    ];

    card.style.boxShadow = shadows[level];
    sub.innerText = subs[level];

    code.innerText = `<div style="position: relative; border-radius: ${radius}px; ${hasBorder ? 'border: 1.5px solid #FFE100;' : ''}">\n  <md-elevation style="--md-elevation-level: ${level};"></md-elevation>\n  카카오뱅크 카드 (Level ${level})\n</div>`;
  }
</script>

*   [Design article](https://m3.material.io/styles/elevation) <!-- {.external} -->
*   [API Documentation](#api)
*   [Source code](https://github.com/material-components/material-web/tree/main/elevation)
    <!-- {.external} -->

## Usage

Elevation can be set from 0 to 5 using the `--md-elevation-level` CSS custom
property. The elevation will automatically fill the nearest `position: relative`
element's size and shape.

![A rounded square with a drop shadow beneath it.](images/elevation/usage.webp "A surface with an elevation shadow.")

```html
<style>
  .surface {
    position: relative;
    border-radius: 16px;
    height: 64px;
    width: 64px;

    --md-elevation-level: 3;
  }
</style>
<div class="surface">
  <md-elevation></md-elevation>
  <!-- Content -->
</div>
```

### Animation

Shadows may be animated between levels by adding `transition-duration` and
`transition-easing-function` CSS properties.

![A rounded square with a drop shadow beneath it. After a moment, the square
lowers into the background and the shadow disappears, then
repeats.](images/elevation/usage-animation.gif "Animating between elevations.")

```html
<style>
  .surface {
    /* ... */
    transition-duration: 250ms;
    transition-timing-function: ease-in-out;

    --md-elevation-level: 3;
  }

  .surface:active {
    --md-elevation-level: 0;
  }
</style>
<div class="surface">
  <md-elevation></md-elevation>
  <!-- Content -->
</div>
```

## Accessibility

Elevation is a visual component and does not have accessibility concerns.

## Theming

Elevation supports [Material theming](../theming/README.md) and can be
customized in terms of color.

### Tokens

Token                         | Default value
----------------------------- | -----------------------
`--md-elevation-level`        | `0`
`--md-elevation-shadow-color` | `--md-sys-color-shadow`

*   [All tokens](https://github.com/material-components/material-web/blob/main/tokens/_md-comp-elevation.scss)
    <!-- {.external} -->

### Example

![Image of an elevation surface with a different theme applied](images/elevation/theming.webp "Elevation theming example.")

```html
<style>
  .surface {
    position: relative;
    border-radius: 16px;
    height: 64px;
    width: 64px;
  }

  :root {
    --md-elevation-level: 5;
    --md-sys-color-shadow: #006A6A;
  }
</style>
<div class="surface">
  <md-elevation></md-elevation>
  <!-- Content -->
</div>
```

<!-- auto-generated API docs start -->
<!-- auto-generated API docs end -->
