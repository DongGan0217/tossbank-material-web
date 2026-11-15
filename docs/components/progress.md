<!-- catalog-only-start --><!-- ---
name: Progress indicators
dirname: progress
ssrOnly: true
-----><!-- catalog-only-end -->

<catalog-component-header image-align="end">
<catalog-component-header-title slot="title">

# Progress indicators

<!-- no-catalog-start -->

<!--*
# Document freshness: For more information, see go/fresh-source.
freshness: { owner: 'lizmitchell' reviewed: '2026-07-31' }
tag: 'docType:reference'
*-->

<!-- go/md-progress -->

<!-- [TOC] -->

<!-- external-only-start -->
**This documentation is fully rendered on the
[KakaoBank Material Web catalog](https://material-web.dev/components/progress/).**
<!-- external-only-end -->

<!-- no-catalog-end -->

[Progress indicators](https://m3.material.io/components/progress-indicators)<!-- {.external} -->
inform users about the status of ongoing processes, such as loading an app or
submitting a form.

There are two types of progress indicators: linear and circular.

</catalog-component-header-title>

<img
    src="images/progress/hero.svg"
    alt="Circular and linear progress indicators showing indetermine and determinate examples"
    title="Progress indicators can be used to show indeterminate or determinate progress.">

</catalog-component-header>

<!-- KakaoBank Interactive Options Playground & Live Sandbox -->
<div class="kb-playground-container">
  <div class="kb-playground-header">
    <div class="kb-playground-title">
      <span>🛠️ Progress (진행 상태 바) 실시간 옵션 샌드박스</span>
      <span class="kb-playground-badge">Live Interactive</span>
    </div>
    <span style="font-size: 12px; color: #4E5968;">적금 달성률 및 비대면 심사 로딩 상태를 실시간 제어해보세요.</span>
  </div>
  <div class="kb-playground-body">
    <div class="kb-playground-controls">
      <div class="kb-control-group">
        <label class="kb-control-label" for="kb-prog-type">인디케이터 유형 (Type):</label>
        <select id="kb-prog-type" class="kb-control-select" onchange="updateProgressDemo()">
          <option value="linear" selected>Linear (선형 프로그레스 바)</option>
          <option value="circular">Circular (원형 인디케이터)</option>
        </select>
      </div>
      <div class="kb-control-group">
        <label class="kb-control-label" for="kb-prog-val">진행률 (Value: <span id="kb-prog-num">70%</span>):</label>
        <input id="kb-prog-val" type="range" min="0" max="100" value="70" oninput="updateProgressDemo()" style="width: 100%; accent-color: #FFE100; cursor: pointer;" />
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 4px;">
        <label class="kb-control-checkbox">
          <input id="kb-prog-indet" type="checkbox" onchange="updateProgressDemo()" />
          <span>무한 로딩 상태 (Indeterminate)</span>
        </label>
      </div>
    </div>
    <div class="kb-playground-canvas" id="kb-prog-canvas" style="min-height: 160px; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 24px;">
      <div id="kb-linear-box" style="width: 90%; max-width: 400px;">
        <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; margin-bottom: 8px;">
          <span>26주 적금 달성률</span>
          <span id="kb-linear-pct" style="color: #3182F6;">70%</span>
        </div>
        <div style="height: 10px; background: #E5E8EB; border-radius: 9999px; overflow: hidden;">
          <div id="kb-linear-bar" style="width: 70%; height: 100%; background: #FFE100; border-radius: 9999px; transition: width 0.2s ease;"></div>
        </div>
      </div>
      <div id="kb-circular-box" style="display: none; flex-direction: column; align-items: center; gap: 12px;">
        <svg width="64" height="64" viewBox="0 0 64 64" id="kb-circ-svg">
          <circle cx="32" cy="32" r="26" fill="none" stroke="#E5E8EB" stroke-width="6"/>
          <circle id="kb-circ-bar" cx="32" cy="32" r="26" fill="none" stroke="#FFE100" stroke-width="6" stroke-dasharray="163.36" stroke-dashoffset="49" stroke-linecap="round" transform="rotate(-90 32 32)" style="transition: stroke-dashoffset 0.2s ease;"/>
        </svg>
        <span id="kb-circ-pct" style="font-size: 14px; font-weight: 700; color: #191F28;">70%</span>
      </div>
    </div>
  </div>
  <div class="kb-playground-footer">
    <pre class="kb-code-preview" id="kb-prog-code">&lt;md-linear-progress value="0.7" style="--md-linear-progress-active-indicator-color: #FFE100;"&gt;&lt;/md-linear-progress&gt;</pre>
    <button class="kb-copy-code-btn" type="button" onclick="navigator.clipboard.writeText(document.getElementById('kb-prog-code').innerText); this.innerText='복사 완료!'; setTimeout(()=>this.innerText='코드 복사', 1500)">코드 복사</button>
  </div>
</div>
<script>
  function updateProgressDemo() {
    const type = document.getElementById('kb-prog-type').value;
    const val = Number(document.getElementById('kb-prog-val').value);
    const indet = document.getElementById('kb-prog-indet').checked;

    document.getElementById('kb-prog-num').innerText = val + '%';
    const linearBox = document.getElementById('kb-linear-box');
    const circularBox = document.getElementById('kb-circular-box');
    const code = document.getElementById('kb-prog-code');

    if (type === 'linear') {
      linearBox.style.display = 'block';
      circularBox.style.display = 'none';
      const bar = document.getElementById('kb-linear-bar');
      const pct = document.getElementById('kb-linear-pct');
      pct.innerText = indet ? '로딩 중...' : val + '%';
      bar.style.width = indet ? '100%' : val + '%';
      code.innerText = indet
        ? `<md-linear-progress indeterminate style="--md-linear-progress-active-indicator-color: #FFE100;"></md-linear-progress>`
        : `<md-linear-progress value="${val / 100}" style="--md-linear-progress-active-indicator-color: #FFE100;"></md-linear-progress>`;
    } else {
      linearBox.style.display = 'none';
      circularBox.style.display = 'flex';
      const bar = document.getElementById('kb-circ-bar');
      const pct = document.getElementById('kb-circ-pct');
      pct.innerText = indet ? '심사 중...' : val + '%';
      const circumference = 2 * Math.PI * 26;
      const offset = circumference * (1 - (indet ? 0.3 : val / 100));
      bar.style.strokeDashoffset = offset;
      code.innerText = indet
        ? `<md-circular-progress indeterminate style="--md-circular-progress-active-indicator-color: #FFE100;"></md-circular-progress>`
        : `<md-circular-progress value="${val / 100}" style="--md-circular-progress-active-indicator-color: #FFE100;"></md-circular-progress>`;
    }
  }
</script>

*   [Design article](https://m3.material.io/components/progress-indicators)
    <!-- {.external} -->
*   [API Documentation](#api)
*   [Source code](https://github.com/material-components/material-web/tree/main/progress)
    <!-- {.external} -->

## Types

1.  [Circular progress](#circular-progress)
1.  [Linear progress](#linear-progress)

<!-- catalog-only-start -->

<!--

## Interactive Demo

{% playgroundexample dirname=dirname %}

-->

<!-- catalog-only-end -->

## Usage

Progress indicators may be determinate to show progress, or indeterminate for an
unspecified amount of progress.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- catalog-only-start -->

<!--

<div class="figure-wrapper">
  <figure
      style="justify-content:center; gap: 16px"
      title="Determinate and indeterminate progress indicators."
      aria-label="Two circular and linear progress indicator examples, one with three quarters of the track full
and the other
indeterminate.">
    <md-circular-progress value="0.75"></md-circular-progress>
    <md-circular-progress indeterminate></md-circular-progress>
    <div style="display: flex; flex-direction: column; align-self: stretch; justify-content: space-evenly;">
      <md-linear-progress value="0.75"></md-linear-progress>
      <md-linear-progress indeterminate></md-linear-progress>
    </div>
  </figure>
</div>

-->

<!-- catalog-only-end -->

```html
<md-circular-progress value="0.75"></md-circular-progress>
<md-circular-progress indeterminate></md-circular-progress>

<md-linear-progress indeterminate></md-linear-progress>
<md-linear-progress value="0.5"></md-linear-progress>
```

### Four colors

Indeterminate progress indicators may cycle between four colors (primary,
primary container, tertiary, and tertiary container by default).

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- catalog-only-start -->

<!--

<div class="figure-wrapper">
  <figure
      style="justify-content:center; gap: 16px;"
      title="A four-color indeterminate circular and linear progress indicator"
      aria-label="Indeterminate progress indicators that cycles between four colors.">
    <md-circular-progress four-color indeterminate></md-circular-progress>
    <md-linear-progress four-color indeterminate></md-linear-progress>
  </figure>
</div>

-->

<!-- catalog-only-end -->

```html
<md-circular-progress four-color indeterminate></md-circular-progress>
<md-linear-progress four-color indeterminate></md-linear-progress>
```

## Accessibility

Add an
[`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)<!-- {.external} -->
attribute to progress indicators to give them a descriptive name.

```html
<md-circular-progress value="0.5" aria-label="Page refresh progress"></md-circular-progress>

<md-linear-progress value="0.5" aria-label="Download progress"></md-linear-progress>
```

## Circular progress

<!-- go/md-circular-progress -->

Circular progress indicators display progress by animating along an invisible
circular track in a clockwise direction.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- catalog-only-start -->

<!--

<div class="figure-wrapper">
  <figure
      style="justify-content:center; gap: 16px;"
      title="Circular progress indicators"
      aria-label="An indeterminate and determinate circular progress indicator.">
    <md-circular-progress indeterminate></md-circular-progress>
    <md-circular-progress value="0.6"></md-circular-progress>
  </figure>
</div>

-->

<!-- catalog-only-end -->

```html
<md-circular-progress indeterminate></md-circular-progress>
<md-circular-progress value="0.6"></md-circular-progress>
```

## Linear progress

<!-- go/md-linear-progress -->

Linear progress indicators display progress by animating along the length of a
fixed, visible track.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- catalog-only-start -->

<!--

<div class="figure-wrapper">
  <figure
      style="justify-content:center; gap: 16px;"
      title="Linear progress indicators"
      aria-label="An indeterminate and determinate linear progress indicator.">
    <md-linear-progress indeterminate></md-linear-progress>
    <md-linear-progress value="0.6"></md-linear-progress>
  </figure>
</div>

-->

<!-- catalog-only-end -->

```html
<md-linear-progress indeterminate></md-linear-progress>
<md-linear-progress value="0.6"></md-linear-progress>
```

### Buffer

Linear progress indicators may show a buffer to communicate both determinate and
indeterminate progress. The progress bar and track represent known progress
while the buffer dots represent unknown progress.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- catalog-only-start -->

<!--

<div class="figure-wrapper">
  <figure
      style="justify-content:center;"
      title="Progress and buffer"
      aria-label="A linear progress indicator with partial progress and an indeterminate buffer.">
    <md-linear-progress value="0.5" buffer="0.8"></md-linear-progress>
  </figure>
</div>

-->

<!-- catalog-only-end -->

```html
<md-linear-progress value="0.5" buffer="0.8"></md-linear-progress>
```

## Theming

Progress indicators supports [Material theming](../theming/README.md) and can be
customized in terms of color.

### Circular progress tokens

Token                                           | Default value
----------------------------------------------- | ------------------------
`--md-circular-progress-active-indicator-color` | `--md-sys-color-primary`
`--md-circular-progress-size`                   | `48px`
`--md-circular-progress-active-indicator-width` | `8.3333` (%)

> Note: the active indicator width must be specified as a unit-less percentage
> of the size.

*   [All tokens](https://github.com/material-components/material-web/blob/main/tokens/_md-comp-circular-progress.scss)
    <!-- {.external} -->

### Circular progress example

<!-- no-catalog-start -->

![Image of a circular progress indicator with a different theme applied](images/progress/theming-circular.webp "Circular progress indicator theming example.")

<!-- no-catalog-end -->
<!-- catalog-only-start -->

<!--

<div class="figure-wrapper">
  <figure
      style="justify-content:center;align-items:center;"
      class="styled-example"
      title="Circular progress indicator theming example."
      aria-label="Image of a circular progress indicator with a different theme applied">
    <style>
      .styled-example {
        background-color: white;
        --md-circular-progress-size: 32px;
        --md-circular-progress-active-indicator-width: 20;
        --md-sys-color-primary: #006A6A;
      }
    </style>

    <md-circular-progress value="0.5"></md-circular-progress>
  </figure>
</div>

-->

<!-- catalog-only-end -->

```html
<style>
:root {
  --md-circular-progress-size: 32px;
  --md-circular-progress-active-indicator-width: 20;
  --md-sys-color-primary: #006A6A;
}
</style>

<md-circular-progress value="0.5"></md-circular-progress>
```

### Linear progress tokens

Token                                          | Default value
---------------------------------------------- | -------------
`--md-linear-progress-track-color`             | `--md-sys-color-surface-container-highest`
`--md-linear-progress-track-height`            | `4px`
`--md-linear-progress-track-shape`             | `--md-sys-shape-corner-none`
`--md-linear-progress-active-indicator-color`  | `--md-sys-color-primary`
`--md-linear-progress-active-indicator-height` | `4px`

*   [All tokens](https://github.com/material-components/material-web/blob/main/tokens/_md-comp-linear-progress.scss)
    <!-- {.external} -->

### Linear progress example

<!-- no-catalog-start -->

![Image of a linear progress indicator with a different theme applied](images/progress/theming-linear.webp "Linear progress theming example.")

<!-- no-catalog-end -->
<!-- catalog-only-start -->

<!--

<div class="figure-wrapper">
  <figure
      style="min-width:300px;"
      class="styled-example"
      aria-label="Image of a linear progress indicator with a different theme applied"
      title="Linear progress theming example.">
  <style>
    .styled-example {
      background-color: white;
      --md-linear-progress-track-height: 8px;
      --md-linear-progress-track-shape: 8px;
      --md-linear-progress-active-indicator-height: 8px;
      --md-sys-color-primary: #006A6A;
      --md-sys-color-surface-container-highest: #DDE4E3;
    }
    .styled-example md-linear-progress {
      flex-grow: 1;
    }
  </style>
  <md-linear-progress value="0.5"></md-linear-progress>
  </figure>
</div>

-->

<!-- catalog-only-end -->

```html
<style>
:root {
  --md-linear-progress-track-height: 8px;
  --md-linear-progress-track-shape: 8px;
  --md-linear-progress-active-indicator-height: 8px;
  --md-sys-color-primary: #006A6A;
  --md-sys-color-surface-container-highest: #DDE4E3;
}
</style>

<md-linear-progress value="0.5"></md-linear-progress>
```

<!-- auto-generated API docs start -->

## API


### MdLinearProgress <code>&lt;md-linear-progress&gt;</code>

#### Properties

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Property | Attribute | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `buffer` | `buffer` | `number` | `0` | Buffer amount to display, a fraction between 0 and `max`. If the value is 0 or negative, the buffer is not displayed. |
| `value` | `value` | `number` | `0` | Progress to display, a fraction between 0 and `max`. |
| `max` | `max` | `number` | `1` | Maximum progress to display, defaults to 1. |
| `indeterminate` | `indeterminate` | `boolean` | `false` | Whether or not to display indeterminate progress, which gives no indication to how long an activity will take. |
| `fourColor` | `four-color` | `boolean` | `false` | Whether or not to render indeterminate mode using 4 colors instead of one. |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

### MdCircularProgress <code>&lt;md-circular-progress&gt;</code>

#### Properties

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Property | Attribute | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | `value` | `number` | `0` | Progress to display, a fraction between 0 and `max`. |
| `max` | `max` | `number` | `1` | Maximum progress to display, defaults to 1. |
| `indeterminate` | `indeterminate` | `boolean` | `false` | Whether or not to display indeterminate progress, which gives no indication to how long an activity will take. |
| `fourColor` | `four-color` | `boolean` | `false` | Whether or not to render indeterminate mode using 4 colors instead of one. |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

<!-- auto-generated API docs end -->
