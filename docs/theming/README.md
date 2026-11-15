<!-- catalog-only-start --><!-- ---
name: Overview
title: Theming Overview
order: 1
-----><!-- catalog-only-end -->

# 토스뱅크 디자인 시스템 테마 개요 (Theming Overview)

토스뱅크 디자인 시스템(`@tossbank/material-web`)은 W3C DTCG(Design Tokens Community Group) 표준과 CSS Custom Properties를 완벽하게 준수하여 설계된 엔터프라이즈 테마 시스템입니다.

---

## 1. 3-Tier 토큰 아키텍처

1. **참조 토큰 (Reference Tokens)**:
   - 토스뱅크 브랜드 기본값 정의 (예: 토스 딥 로얄 블루 `#0064FF`, 틴트 블루 `#E8F3FF`, 듀얼톤 체크카드 포인트, `Pretendard Variable` 웹폰트)
2. **시스템 토큰 (System Tokens)**:
   - 역할 기반 시맨틱 토큰 (예: `--md-sys-color-primary`, `--md-sys-shape-corner-medium: 16px`, `--md-sys-typescale-body-large`)
3. **컴포넌트 토큰 (Component Tokens)**:
   - 각 컴포넌트별 전용 토큰 (예: `--md-filled-button-container-color`, `--md-filled-button-container-shape`)

---

## 2. 3대 동적 테마 (Clean White / Cool Slate / Dark)

토스뱅크 카탈로그는 3대 공식 동적 테마를 기본 제공합니다:

- **Clean White (기본)**: 금융의 명확함과 신뢰를 대변하는 화이트 서피스와 토스 딥블루 포인트
- **Cool Slate**: 슬레이트 네이비 배경과 시아닌 블루 포인트의 개발자/전문가 친화적 테마
- **Modern Dark**: 고대비 다크 서피스(`--grey900`)와 시인성 강화 블루 포인트

```html
<!-- 특정 섹션을 토스뱅크 블루 테마로 스타일링 -->
<div class="tossbank-theme-container">
  <md-filled-button>지금 이자받기</md-filled-button>
  <md-outlined-button>상세 내역</md-outlined-button>
</div>

<style>
  .tossbank-theme-container {
    --md-sys-color-primary: #0064FF;
    --md-sys-color-on-primary: #FFFFFF;
    --md-filled-button-container-shape: 16px;
    letter-spacing: -0.02em;
  }
</style>
```
