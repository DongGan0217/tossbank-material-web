<!-- catalog-only-start --><!-- ---
name: Bundle Size
title: Bundle Size & Performance
order: 4
-----><!-- catalog-only-end -->

# 토스뱅크 번들 사이즈 및 성능 최적화 (Bundle Size & Performance)

`@tossbank/material-web`은 개별 컴포넌트 단위의 트리 셰이킹(Tree-Shaking)과 브라우저 네이티브 Custom Elements 기술을 통해 극대화된 런타임 성능을 제공합니다.

---

## 1. 개별 모듈 임포트를 통한 초경량화

전체 번들을 일괄 로드할 필요 없이, 실제 화면에서 필요한 컴포넌트만 독립적으로 임포트하여 초기 로딩 속도(FCP)를 0.3초 미만으로 단축합니다.

| 컴포넌트 | Gzip 번들 크기 | 설명 |
| :--- | :--- | :--- |
| `button/filled-button.js` | ~3.8 KB | 토스 딥블루 16px 표준 액션 버튼 |
| `textfield/outlined-text-field.js` | ~6.2 KB | 송금액/계좌번호 아웃라인 입력 필드 |
| `dialog/dialog.js` | ~4.5 KB | 24px 곡률 서피스 모달 다이얼로그 |
| `checkbox/checkbox.js` | ~2.9 KB | 비대면 약관 동의 체크박스 |
| `slider/slider.js` | ~5.1 KB | 대출 한도/이자 계산 실시간 슬라이더 |
| `chips/chip-set.js` | ~4.2 KB | 상품 카테고리 필터 칩 셋 |

---

## 2. 렌더링 최적화

- **Shadow DOM 캡슐화**: 글로벌 CSS 오염 없이 격리된 스타일 보장.
- **Lit 반응형 렌더링**: 변경된 프로퍼티만 부분 갱신하여 60fps 부드러운 인터랙션 유지.
- **모바일 배터리 절약**: 하드웨어 가속 트랜지션 및 경량 애니메이션 채택.
