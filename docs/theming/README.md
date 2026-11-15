<!-- catalog-only-start --><!-- ---
name: Overview
title: Theming Overview
order: 1
-----><!-- catalog-only-end -->

# 카카오뱅크 디자인 시스템 테마 개요 (Theming Overview)

카카오뱅크 디자인 시스템(`@kakaobank/material-web`)은 W3C DTCG(Design Tokens Community Group) 표준과 CSS Custom Properties를 완벽하게 준수하여 구성되어 있습니다.

---

## 1. 3-Tier 토큰 아키텍처

1. **참조 토큰 (Reference Tokens)**:
   - 카카오뱅크 브랜드의 기본값 정의 (예: 카카오 옐로우 `#FFE100`, Pretendard Variable 웹폰트)
2. **시스템 토큰 (System Tokens)**:
   - 역할 기반 시맨틱 토큰 (예: `--md-sys-color-primary`, `--md-sys-typescale-body-large`)
3. **컴포넌트 토큰 (Component Tokens)**:
   - 각 컴포넌트별 전용 토큰 (예: `--md-filled-button-container-color`, `--md-filled-button-container-height`)

---

## 2. 간편한 테마 커스터마이징 예시

```html
<!-- 특정 컨테이너를 카카오뱅크 옐로우 테마로 래핑 -->
<div class="kb-theme-container">
  <md-filled-button>계좌 개설하기</md-filled-button>
  <md-outlined-button>자세히 보기</md-outlined-button>
</div>

<style>
  .kb-theme-container {
    --md-sys-color-primary: #FFE100;
    --md-sys-color-on-primary: #000000;
    --md-filled-button-container-height: 52px;
    --md-filled-button-container-shape: 16px;
  }
</style>
```
