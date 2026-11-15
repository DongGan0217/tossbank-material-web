<!-- catalog-only-start --><!-- ---
name: Tabs
dirname: tabs
-----><!-- catalog-only-end -->

<catalog-component-header image-align="start">
<catalog-component-header-title slot="title">

# Tabs

<!-- no-catalog-start -->

<!--*
# Document freshness: For more information, see go/fresh-source.
freshness: { owner: 'lizmitchell' reviewed: '2026-07-31' }
tag: 'docType:reference'
*-->

<!-- go/md-tabs -->

<!-- [TOC] -->

<!-- external-only-start -->
**This documentation is fully rendered on the
[KakaoBank Material Web catalog](https://material-web.dev/components/tabs/)**
<!-- external-only-end -->

<!-- no-catalog-end -->

[Tabs](https://m3.material.io/components/tabs)<!-- {.external} --> organize groups of
related content that are at the same level of hierarchy.

</catalog-component-header-title>

<img
  class="hero"
  src="images/tabs/hero.svg"
  alt="Media gallery screen with tabs labeled 'Video', 'Photos', and 'Audio'.">

</catalog-component-header>

<!-- KakaoBank Interactive Options Playground & Live Sandbox -->
<div class="kb-playground-container">
  <div class="kb-playground-header">
    <div class="kb-playground-title">
      <span>🛠️ Tabs (탭 바) 실시간 옵션 샌드박스</span>
      <span class="kb-playground-badge">Live Interactive</span>
    </div>
    <span style="font-size: 12px; color: #4E5968;">금융 거래 내역 뷰 전환 탭을 실시간으로 조작해보세요.</span>
  </div>
  <div class="kb-playground-body">
    <div class="kb-playground-controls">
      <div class="kb-control-group">
        <label class="kb-control-label" for="kb-tabs-variant">탭 형태 (Variant):</label>
        <select id="kb-tabs-variant" class="kb-control-select" onchange="updateTabsDemo()">
          <option value="primary" selected>Primary (밑줄 인디케이터 바)</option>
          <option value="secondary">Secondary (서피스 캡슐형)</option>
        </select>
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 4px;">
        <label class="kb-control-checkbox">
          <input id="kb-tabs-icon" type="checkbox" onchange="updateTabsDemo()" />
          <span>아이콘 포함 (with Icon)</span>
        </label>
      </div>
    </div>
    <div class="kb-playground-canvas" id="kb-tabs-canvas" style="min-height: 160px; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 24px;">
      <div id="kb-tabs-container" style="width: 100%; max-width: 420px; display: flex; border-bottom: 2px solid #E5E8EB;">
        <div id="kb-tab-0" onclick="selectTab(0)" style="flex: 1; text-align: center; padding: 12px 0; font-size: 15px; font-weight: 700; color: #191F28; border-bottom: 3px solid #191F28; margin-bottom: -2px; cursor: pointer;">
          <span id="kb-tab-icon-0" style="display: none; margin-right: 4px;">📋</span>전체 내역
        </div>
        <div id="kb-tab-1" onclick="selectTab(1)" style="flex: 1; text-align: center; padding: 12px 0; font-size: 15px; font-weight: 500; color: #8B95A1; border-bottom: 3px solid transparent; margin-bottom: -2px; cursor: pointer;">
          <span id="kb-tab-icon-1" style="display: none; margin-right: 4px;">💰</span>입금만
        </div>
        <div id="kb-tab-2" onclick="selectTab(2)" style="flex: 1; text-align: center; padding: 12px 0; font-size: 15px; font-weight: 500; color: #8B95A1; border-bottom: 3px solid transparent; margin-bottom: -2px; cursor: pointer;">
          <span id="kb-tab-icon-2" style="display: none; margin-right: 4px;">💳</span>출금만
        </div>
      </div>
      <div id="kb-tab-panel" style="margin-top: 16px; font-size: 13px; color: #4E5968;">
        현재 선택된 뷰: <strong>전체 내역 (모든 입출금 내역 표시)</strong>
      </div>
    </div>
  </div>
  <div class="kb-playground-footer">
    <pre class="kb-code-preview" id="kb-tabs-code">&lt;md-tabs active-tab-index="0"&gt;
  &lt;md-primary-tab&gt;전체 내역&lt;/md-primary-tab&gt;
  &lt;md-primary-tab&gt;입금만&lt;/md-primary-tab&gt;
  &lt;md-primary-tab&gt;출금만&lt;/md-primary-tab&gt;
&lt;/md-tabs&gt;</pre>
    <button class="kb-copy-code-btn" type="button" onclick="navigator.clipboard.writeText(document.getElementById('kb-tabs-code').innerText); this.innerText='복사 완료!'; setTimeout(()=>this.innerText='코드 복사', 1500)">코드 복사</button>
  </div>
</div>
<script>
  let currentActiveTab = 0;
  function selectTab(idx) {
    currentActiveTab = idx;
    updateTabsDemo();
  }

  function updateTabsDemo() {
    const variant = document.getElementById('kb-tabs-variant').value;
    const hasIcon = document.getElementById('kb-tabs-icon').checked;
    const panel = document.getElementById('kb-tab-panel');
    const code = document.getElementById('kb-tabs-code');

    const tabNames = ['전체 내역 (모든 입출금 내역 표시)', '입금만 (타행 입금 및 월급 입금 내역)', '출금만 (카드 결제 및 자동이체 출금)'];
    panel.innerHTML = `현재 선택된 뷰: <strong>${tabNames[currentActiveTab]}</strong>`;

    for (let i = 0; i < 3; i++) {
      const tabEl = document.getElementById('kb-tab-' + i);
      const iconEl = document.getElementById('kb-tab-icon-' + i);
      iconEl.style.display = hasIcon ? 'inline' : 'none';

      if (i === currentActiveTab) {
        tabEl.style.fontWeight = '700';
        tabEl.style.color = '#191F28';
        tabEl.style.borderBottom = variant === 'primary' ? '3px solid #191F28' : '3px solid #FFE100';
      } else {
        tabEl.style.fontWeight = '500';
        tabEl.style.color = '#8B95A1';
        tabEl.style.borderBottom = '3px solid transparent';
      }
    }

    const tag = variant === 'secondary' ? 'md-secondary-tab' : 'md-primary-tab';
    code.innerText = `<md-tabs active-tab-index="${currentActiveTab}">\n  <${tag}>전체 내역</${tag}>\n  <${tag}>입금만</${tag}>\n  <${tag}>출금만</${tag}>\n</md-tabs>`;
  }
</script>

*   [Design article](https://m3.material.io/components/tabs) <!-- {.external} -->
*   [API Documentation](#api)
*   [Source code](https://github.com/material-components/material-web/tree/main/tabs)
    <!-- {.external} -->

## Types

1.  [Primary tabs](#primary-tabs)
1.  [Secondary tabs](#secondary-tabs)

<!-- catalog-only-start -->

<!--

## Interactive Demo

{% playgroundexample dirname=dirname %}

-->

<!-- catalog-only-end -->

## Usage

Tabs contain multiple primary or secondary tab children. Use the same type of
tab in a tab bar.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-tabs>
  <md-primary-tab>Video</md-primary-tab>
  <md-primary-tab>Photos</md-primary-tab>
  <md-primary-tab>Audio</md-primary-tab>
</md-tabs>

<md-tabs>
  <md-secondary-tab>Birds</md-secondary-tab>
  <md-secondary-tab>Cats</md-secondary-tab>
  <md-secondary-tab>Dogs</md-secondary-tab>
</md-tabs>
```

### Selection

Add an `active` attribute to change which tab is selected.

```html
<md-tabs>
  <md-primary-tab>Video</md-primary-tab>
  <md-primary-tab active>Photos</md-primary-tab>
  <md-primary-tab>Audio</md-primary-tab>
</md-tabs>
```

To observe changes to tab selections, add an event listener to `<md-tabs>`,
listening for the `change` event.

```ts
tabs.addEventListener('change', (event: Event) => {
  if (event.target.activeTabIndex === 2) {
    // ... perform logic only if index of selected item is 2.
  }
});
```

### Icons

Tabs may optionally show an icon.

Icons communicate the type of content within a tab. Icons should be simple and
recognizable.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-tabs>
  <md-primary-tab>
    <md-icon slot="icon">piano</md-icon>
    Keyboard
  </md-primary-tab>
  <md-primary-tab>
    <md-icon slot="icon">tune</md-icon>
    Guitar
  </md-primary-tab>
</md-tabs>
```

Tabs may optionally show icons without a label.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-tabs>
  <md-primary-tab>
    <md-icon slot="icon">piano</md-icon>
  </md-primary-tab>
  <md-primary-tab>
    <md-icon slot="icon">tune</md-icon>
  </md-primary-tab>
</md-tabs>
```

## Primary tabs

<!-- go/md-primary-tab -->

Primary tabs are placed at the top of the content pane under a top app bar. They
display the main content destinations.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-tabs>
  <md-primary-tab>
    <md-icon slot="icon">piano</md-icon>
    Keyboard
  </md-primary-tab>
  <md-primary-tab>
    <md-icon slot="icon">tune</md-icon>
    Guitar
  </md-primary-tab>
</md-tabs>
```

### Inline icons

Primary tabs can show their icons inline, like secondary tabs.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-tabs>
  <md-primary-tab inline-icon>
    <md-icon slot="icon">piano</md-icon>
    Keyboard
  </md-primary-tab>
  <md-primary-tab inline-icon>
    <md-icon slot="icon">tune</md-icon>
    Guitar
  </md-primary-tab>
</md-tabs>
```

## Secondary tabs

<!-- go/md-secondary-tab -->

Secondary tabs are used within a content area to further separate related
content and establish hierarchy.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-tabs>
  <md-secondary-tab>
    <md-icon slot="icon">flight</md-icon>
    Travel
  </md-secondary-tab>
  <md-secondary-tab>
    <md-icon slot="icon">hotel</md-icon>
    Hotel
  </md-secondary-tab>
  <md-secondary-tab>
    <md-icon slot="icon">hiking</md-icon>
    Activities
  </md-secondary-tab>
</md-tabs>
```

## Accessibility

Add an
[`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)<!-- {.external} -->
attribute to `<md-tabs>` and any individual tab whose label needs to be more
descriptive, such as icon-only tabs.

```html
<md-tabs aria-label="Content to view">
  <md-primary-tab aria-label="Photos">
    <md-icon slot="icon">photo</md-icon>
  </md-primary-tab>
  <md-primary-tab aria-label="Videos">
    <md-icon slot="icon">videocam</md-icon>
  </md-primary-tab>
  <md-primary-tab aria-label="Music">
    <md-icon slot="icon">audiotrack</md-icon>
  </md-primary-tab>
</md-tabs>
```

### Tab panels

Every tab must reference a
[`role="tabpanel"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/tabpanel_role)<!-- {.external} -->
element with `aria-controls`. Tab panels must be labelled with `aria-label` or
`aria-labelledby`.

It's common to reference the panel's tab with `aria-labelledby`.

```html
<md-tabs aria-label="Content to view">
  <md-primary-tab id="photos-tab" aria-controls="photos-panel">
    Photos
  </md-primary-tab>
  <md-primary-tab id="videos-tab" aria-controls="videos-panel">
    Videos
  </md-primary-tab>
  <md-primary-tab id="music-tab" aria-controls="music-panel">
    Music
  </md-primary-tab>
</md-tabs>

<div id="photos-panel" role="tabpanel" aria-labelledby="photos-tab">
  ...
</div>
<div id="videos-panel" role="tabpanel" aria-labelledby="videos-tab" hidden>
  ...
</div>
<div id="music-panel" role="tabpanel" aria-labelledby="music-tab" hidden>
  ...
</div>
```

## Theming

Tabs supports [Material theming](../theming/README.md) and can be customized in
terms of color, typography, and shape.

### Primary tab tokens

Token                                     | Default value
----------------------------------------- | -------------
`--md-primary-tab-container-color`        | `--md-sys-color-surface`
`--md-primary-tab-label-text-font`        | `--md-sys-typescale-title-small-font`
`--md-primary-tab-active-indicator-color` | `--md-sys-color-primary`
`--md-primary-tab-icon-color`             | `--md-sys-color-on-surface-variant`
`--md-primary-tab-container-shape`        | `--md-sys-shape-corner-none`

*   [All tokens](https://github.com/material-components/material-web/blob/main/tokens/_md-comp-primary-tab.scss)
    <!-- {.external} -->

### Primary tab example

<!-- no-catalog-start -->

![Image of tabs with a different theme applied](images/tabs/theming.webp "Tab theming example.")

<!-- no-catalog-end -->

```html
<style>
:root {
  /* System tokens */
  --md-sys-color-surface: #f7faf9;
  --md-sys-color-primary: #005353;

  /* Component tokens */
  --md-primary-tab-label-text-font: cursive, system-ui;
  --md-primary-tab-label-text-size: 0.8em;
}
</style>

<md-tabs>
  <md-primary-tab>Tab 1</md-primary-tab>
  <md-primary-tab>Tab 2</md-primary-tab>
  <md-primary-tab>Tab 3</md-primary-tab>
</md-tabs>
```

### Secondary tab tokens

Token                                       | Default value
------------------------------------------- | -------------
`--md-secondary-tab-container-color`        | `--md-sys-color-surface`
`--md-secondary-tab-label-text-font`        | `--md-sys-typescale-title-small-font`
`--md-secondary-tab-active-indicator-color` | `--md-sys-color-primary`
`--md-secondary-tab-icon-color`             | `--md-sys-color-on-surface-variant`
`--md-secondary-tab-container-shape`        | `--md-sys-shape-corner-none`

*   [All tokens](https://github.com/material-components/material-web/blob/main/tokens/_md-comp-secondary-tab.scss)
    <!-- {.external} -->

### Secondary tab example

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->

```html
<style>
:root {
  /* System tokens */
  --md-sys-color-surface: #f7faf9;
  --md-sys-color-primary: #005353;

  /* Component tokens */
  --md-secondary-tab-label-text-font: cursive, system-ui;
  --md-secondary-tab-label-text-size: 0.8em;
}
</style>

<md-tabs>
  <md-secondary-tab>Tab 1</md-secondary-tab>
  <md-secondary-tab>Tab 2</md-secondary-tab>
  <md-secondary-tab>Tab 3</md-secondary-tab>
</md-tabs>
```

<!-- auto-generated API docs start -->

## API


### MdTabs <code>&lt;md-tabs&gt;</code>

#### Properties

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Property | Attribute | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `autoActivate` | `auto-activate` | `boolean` | `false` | Whether or not to automatically select a tab when it is focused. |
| `activeTabIndex` | `active-tab-index` | `number` | `undefined` |  |
| `tabs` |  | `Tab[]` | `undefined` | The tabs of this tab bar. |
| `activeTab` |  | `Tab` | `undefined` |  |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

#### Methods

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `scrollToTab` | `tabToScrollTo` | `Promise<void>` | Scrolls the toolbar, if overflowing, to the active tab, or the provided tab. |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

#### Events

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Event | Type | [Bubbles](https://developer.mozilla.org/en-US/docs/Web/API/Event/bubbles) | [Composed](https://developer.mozilla.org/en-US/docs/Web/API/Event/composed) | Description |
| --- | --- | --- | --- | --- |
| `change` | `Event` | Yes | No | Fired when the selected tab changes. The target's `activeTabIndex` or `activeTab` provide information about the selection change. The change event is fired when a user interaction like a space/enter key or click cause a selection change. The tab selection based on these actions can be cancelled by calling preventDefault on the triggering `keydown` or `click` event. |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

### MdPrimaryTab <code>&lt;md-primary-tab&gt;</code>

#### Properties

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Property | Attribute | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `inlineIcon` | `inline-icon` | `boolean` | `false` | Whether or not the icon renders inline with label or stacked vertically. |
| `isTab` | `md-tab` | `boolean` | `true` | The attribute `md-tab` indicates that the element is a tab for the parent element, `<md-tabs>`. Make sure if you're implementing your own `md-tab` component that you have an `md-tab` attribute set. |
| `active` | `active` | `boolean` | `false` | Whether or not the tab is selected. |
| `hasIcon` | `has-icon` | `boolean` | `false` | In SSR, set this to true when an icon is present. |
| `iconOnly` | `icon-only` | `boolean` | `false` | In SSR, set this to true when there is no label and only an icon. |
| `selected` | `selected` | `boolean` | `undefined` |  |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

### MdSecondaryTab <code>&lt;md-secondary-tab&gt;</code>

#### Properties

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Property | Attribute | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `isTab` | `md-tab` | `boolean` | `true` | The attribute `md-tab` indicates that the element is a tab for the parent element, `<md-tabs>`. Make sure if you're implementing your own `md-tab` component that you have an `md-tab` attribute set. |
| `active` | `active` | `boolean` | `false` | Whether or not the tab is selected. |
| `hasIcon` | `has-icon` | `boolean` | `false` | In SSR, set this to true when an icon is present. |
| `iconOnly` | `icon-only` | `boolean` | `false` | In SSR, set this to true when there is no label and only an icon. |
| `selected` | `selected` | `boolean` | `undefined` |  |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

<!-- auto-generated API docs end -->
