<!-- catalog-only-start --><!-- ---
name: Switch
dirname: switch
-----><!-- catalog-only-end -->

<catalog-component-header>
<catalog-component-header-title slot="title">

# Switch

<!--*
# Document freshness: For more information, see go/fresh-source.
freshness: { owner: 'lizmitchell' reviewed: '2026-07-31' }
tag: 'docType:reference'
*-->

<!-- no-catalog-start -->

<!-- go/md-switch -->

<!-- [TOC] -->

<!-- external-only-start -->
**This documentation is fully rendered on the
[KakaoBank Material Web catalog](https://material-web.dev/components/switch/).**
<!-- external-only-end -->

<!-- no-catalog-end -->

[Switches](https://m3.material.io/components/switch)<!-- {.external} --> toggle the state
of an item on or off.

</catalog-component-header-title>

<img
    class="hero"
    src="images/switch/hero.svg"
    alt="Two switches on a settings page for Wi-Fi and Bluetooth. The first is on and the second is off."
    title="Switches on a settings page.">

</catalog-component-header>

<!-- KakaoBank Interactive Options Playground & Live Sandbox -->
<div class="kb-playground-container">
  <div class="kb-playground-header">
    <div class="kb-playground-title">
      <span>🛠️ Switch 옵션 실시간 미리보기 샌드박스</span>
      <span class="kb-playground-badge">Live Interactive</span>
    </div>
    <span style="font-size: 12px; color: #4E5968;">옵션을 변경하거나 직접 스위치를 클릭해보세요.</span>
  </div>
  <div class="kb-playground-body">
    <div class="kb-playground-controls">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <label class="kb-control-checkbox">
          <input id="kb-switch-selected" type="checkbox" checked onchange="updateSwitchDemo()" />
          <span>선택됨 (Selected / On)</span>
        </label>
        <label class="kb-control-checkbox">
          <input id="kb-switch-icons" type="checkbox" checked onchange="updateSwitchDemo()" />
          <span>아이콘 표시 (Icons on thumb)</span>
        </label>
        <label class="kb-control-checkbox">
          <input id="kb-switch-disabled" type="checkbox" onchange="updateSwitchDemo()" />
          <span>비활성화 (Disabled)</span>
        </label>
      </div>
    </div>
    <div class="kb-playground-canvas" id="kb-switch-canvas">
      <!-- Live Render Target -->
      <div id="kb-switch-render" style="display: flex; align-items: center; gap: 14px; cursor: pointer;" onclick="document.getElementById('kb-switch-selected').click()">
        <div id="kb-switch-track" style="width: 56px; height: 32px; background: #FFE100; border-radius: 9999px; position: relative; transition: all 0.2s ease;">
          <div id="kb-switch-thumb" style="width: 24px; height: 24px; background: #191F28; border-radius: 50%; position: absolute; top: 4px; left: 28px; transition: all 0.2s ease; display: flex; align-items: center; justify-content: center; color: #FFE100; font-size: 12px; font-weight: 700;">
            ✓
          </div>
        </div>
        <span id="kb-switch-state-text" style="font-weight: 700; font-size: 15px; color: #191F28;">활성화됨 (On)</span>
      </div>
    </div>
  </div>
  <div class="kb-playground-footer">
    <pre class="kb-code-preview" id="kb-switch-code">&lt;md-switch selected icons aria-label="카카오뱅크 서비스 설정"&gt;&lt;/md-switch&gt;</pre>
    <button class="kb-copy-code-btn" type="button" onclick="navigator.clipboard.writeText(document.getElementById('kb-switch-code').innerText); this.innerText='복사 완료!'; setTimeout(()=>this.innerText='코드 복사', 1500)">코드 복사</button>
  </div>
</div>

<script>
  function updateSwitchDemo() {
    const selected = document.getElementById('kb-switch-selected').checked;
    const hasIcons = document.getElementById('kb-switch-icons').checked;
    const disabled = document.getElementById('kb-switch-disabled').checked;

    const track = document.getElementById('kb-switch-track');
    const thumb = document.getElementById('kb-switch-thumb');
    const text = document.getElementById('kb-switch-state-text');
    const wrap = document.getElementById('kb-switch-render');
    const code = document.getElementById('kb-switch-code');

    if (disabled) {
      wrap.style.opacity = '0.38';
      wrap.style.cursor = 'not-allowed';
    } else {
      wrap.style.opacity = '1';
      wrap.style.cursor = 'pointer';
    }

    if (selected) {
      track.style.background = '#FFE100';
      thumb.style.left = '28px';
      thumb.style.background = '#191F28';
      thumb.innerText = hasIcons ? '✓' : '';
      thumb.style.color = '#FFE100';
      text.innerText = '활성화됨 (On)';
    } else {
      track.style.background = '#E5E8EB';
      thumb.style.left = '4px';
      thumb.style.background = '#76808E';
      thumb.innerText = hasIcons ? '✕' : '';
      thumb.style.color = '#FFFFFF';
      text.innerText = '꺼짐 (Off)';
    }

    const selSnippet = selected ? ' selected' : '';
    const iconSnippet = hasIcons ? ' icons' : '';
    const disSnippet = disabled ? ' disabled' : '';
    code.innerText = `<md-switch${selSnippet}${iconSnippet}${disSnippet} aria-label="카카오뱅크 설정">\n</md-switch>`;
  }
</script>

*   [Design article](https://m3.material.io/components/switch) <!-- {.external} -->
*   [API Documentation](#api)
*   [Source code](https://github.com/material-components/material-web/tree/main/switch)
    <!-- {.external} -->

<!-- catalog-only-start -->

<!--

## Interactive Demo

{% playgroundexample dirname=dirname %}

-->

<!-- catalog-only-end -->

## Usage

Switches are similar to checkboxes, and can be unselected or selected.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-switch></md-switch>
<md-switch selected></md-switch>
```

### Icons

Icons can be used to visually emphasize the switch's selected state. Switches
can choose to display both icons or only selected icons.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<md-switch icons></md-switch>
<md-switch icons selected></md-switch>

<md-switch icons show-only-selected-icon></md-switch>
<md-switch icons show-only-selected-icon selected></md-switch>
```

### Label

Associate a label with a switch using the `<label>` element.

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<label>
  Wi-Fi
  <md-switch selected></md-switch>
</label>

<label for="switch">Bluetooth</label>
<md-switch id="switch"></md-switch>
```

## Accessibility

Add an
[`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)<!-- {.external} -->
attribute to switches without labels or switches whose labels need to be more
descriptive.

```html
<md-switch aria-label="Lights"></md-switch>

<label>
  All
  <md-switch aria-label="All notifications"></md-switch>
</label>
```

> Note: switches are not automatically labelled by `<label>` elements and always
> need an `aria-label`. See b/294081528.

## Theming

Switches supports [Material theming](../theming/README.md) and can be customized
in terms of color and shape.

### Tokens

Token                               | Default value
----------------------------------- | ------------------------------------------
`--md-switch-handle-color`          | `--md-sys-color-outline`
`--md-switch-handle-shape`          | `--md-sys-shape-corner-full`
`--md-switch-track-color`           | `--md-sys-color-surface-container-highest`
`--md-switch-track-shape`           | `--md-sys-shape-corner-full`
`--md-switch-selected-handle-color` | `--md-sys-color-on-primary`
`--md-switch-selected-track-color`  | `--md-sys-color-primary`

*   [All tokens](https://github.com/material-components/material-web/blob/main/tokens/_md-comp-switch.scss)
    <!-- {.external} -->

### Example

<!-- no-catalog-start -->
<!-- Need to add image -->
<!-- no-catalog-end -->
<!-- Need to add catalog-include "figures/<component>/usage.html" -->

```html
<style>
  :root {
    /* System tokens */
    --md-sys-color-primary: #006a6a;
    --md-sys-color-on-primary: #ffffff;
    --md-sys-color-outline: #6f7979;
    --md-sys-color-surface-container-highest: #dde4e3;

    /* Component tokens */
    --md-switch-handle-shape: 0px;
    --md-switch-track-shape: 0px;
  }
</style>

<md-switch></md-switch>
<md-switch selected></md-switch>
```

<!-- auto-generated API docs start -->

## API


### MdSwitch <code>&lt;md-switch&gt;</code>

#### Properties

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Property | Attribute | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `selected` | `selected` | `boolean` | `false` | Puts the switch in the selected state and sets the form submission value to the `value` property. |
| `icons` | `icons` | `boolean` | `false` | Shows both the selected and deselected icons. |
| `showOnlySelectedIcon` | `show-only-selected-icon` | `boolean` | `false` | Shows only the selected icon, and not the deselected icon. If `true`, overrides the behavior of the `icons` property. |
| `required` | `required` | `boolean` | `false` | When true, require the switch to be selected when participating in form submission.<br>https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox#validation |
| `value` | `value` | `string` | `'on'` | The value associated with this switch on form submission. `null` is submitted when `selected` is `false`. |
| `name` | `name` | `string` | `undefined` | The HTML name to use in form submission. |
| `disabled` | `disabled` | `boolean` | `undefined` | Whether or not the element is disabled. |
| `form` |  | `HTMLFormElement` | `undefined` | The associated form element with which this element's value will submit. |
| `labels` |  | `NodeList` | `undefined` | The labels this element is associated with. |
| `validity` |  | `ValidityState` | `undefined` | Returns a ValidityState object that represents the validity states of the element.<br>https://developer.mozilla.org/en-US/docs/Web/API/ValidityState |
| `validationMessage` |  | `string` | `undefined` | Returns a validation error message or an empty string if the element is valid.<br>https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/validationMessage |
| `willValidate` |  | `boolean` | `undefined` | Returns whether an element will successfully validate based on forms validation rules and constraints.<br>Disabled and readonly elements will not validate.<br>https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/willValidate |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

#### Methods

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `formResetCallback` | _None_ | `void` |  |
| `formStateRestoreCallback` | `state` | `void` |  |
| `checkValidity` | _None_ | `boolean` | Checks the element's constraint validation and returns true if the element is valid or false if not.<br>If invalid, this method will dispatch an `invalid` event.<br>https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/checkValidity |
| `reportValidity` | _None_ | `boolean` | Checks the element's constraint validation and returns true if the element is valid or false if not.<br>If invalid, this method will dispatch a cancelable `invalid` event. If not canceled, a the current `validationMessage` will be reported to the user.<br>https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/reportValidity |
| `setCustomValidity` | `error` | `void` | Sets the element's constraint validation error message. When set to a non-empty string, `validity.customError` will be true and `validationMessage` will display the provided error.<br>Use this method to customize error messages reported.<br>https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/setCustomValidity |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

#### Events

<!-- mdformat off(autogenerated might break rendering in catalog) -->

| Event | Type | [Bubbles](https://developer.mozilla.org/en-US/docs/Web/API/Event/bubbles) | [Composed](https://developer.mozilla.org/en-US/docs/Web/API/Event/composed) | Description |
| --- | --- | --- | --- | --- |
| `input` | `InputEvent` | No | No | Fired whenever `selected` changes due to user interaction (bubbles and composed). |
| `change` | `Event` | No | No | Fired whenever `selected` changes due to user interaction (bubbles). |

<!-- mdformat on(autogenerated might break rendering in catalog) -->

<!-- auto-generated API docs end -->
