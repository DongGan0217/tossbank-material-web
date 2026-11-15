<!-- catalog-only-start --><!-- ---
name: Bundle Size
title: Bundle Size & Performance
order: 4
-----><!-- catalog-only-end -->

# 번들 사이즈 및 성능 최적화 (Bundle Size & Performance)

`@kakaobank/material-web`은 개별 컴포넌트 단위의 트리 셰이킹(Tree-Shaking)을 완벽하게 지원합니다.

---

## 1. 개별 모듈 임포트를 통한 초경량화

전체 라이브러리를 통째로 불러오지 않고, 실제 페이지에서 필요한 컴포넌트만 독립적으로 임포트하여 로딩 속도를 극대화합니다.

| 컴포넌트 | Gzip 번들 크기 | 설명 |
| :--- | :--- | :--- |
| `button/filled-button.js` | ~3.8 KB | 카카오 옐로우 52px 액션 버튼 |
| `textfield/outlined-text-field.js` | ~6.2 KB | 금융 금액/계좌 입력 필드 |
| `dialog/dialog.js` | ~4.5 KB | 확인/취소 알림 다이얼로그 |
| `checkbox/checkbox.js` | ~2.9 KB | 약관 동의 체크박스 |
