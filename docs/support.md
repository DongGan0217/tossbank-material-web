<!-- catalog-only-start --><!-- ---
name: Browser Support
title: Browser Support & Accessibility
order: 5
-----><!-- catalog-only-end -->

# 토스뱅크 브라우저 지원 및 웹 접근성 (Browser Support & A11y)

토스뱅크 금융 서비스를 이용하는 모든 사용자가 디바이스와 신체적 제약 없이 편리하게 금융을 누릴 수 있도록 광범위한 브라우저 지원과 웹 접근성(WCAG 2.1) 표준을 엄격히 준수합니다.

---

## 1. 브라우저 지원 범위

- **모바일 브라우저 & 인앱 웹뷰**:
  - iOS Safari 14+ / iOS WKWebView
  - Android Chrome 88+ / Android WebView
  - Samsung Internet 14+
- **데스크톱 브라우저**:
  - Google Chrome 88+
  - Apple Safari 14+
  - Microsoft Edge 88+
  - Mozilla Firefox 85+

---

## 2. 웹 접근성(A11y) 가이드라인

- **고대비 명도비 준수 (WCAG 2.1 AA/AAA)**:
  - 토스뱅크 딥블루(`#0064FF`) 위의 흰색 텍스트(`#FFFFFF`)는 최소 4.6:1 이상의 명도 대비를 유지하여 텍스트 판독성을 보장합니다.
  - 틴트 블루(`#E8F3FF`) 배경 위의 On-Primary Container 텍스트(`#0047BB`)는 7.8:1 이상의 대비율을 만족합니다.
- **키보드 접근성 및 포커스 링**:
  - 마우스 없이도 Tab 키만으로 모든 폼, 버튼, 다이얼로그 모달을 자유롭게 탐색할 수 있으며, 3px 고대비 포커스 링(`md-focus-ring`)이 시각적 포커스 위치를 명확히 안내합니다.
- **스크린 리더(VoiceOver / TalkBack) 완벽 지원**:
  - W3C WAI-ARIA 표준 롤(Role), 레이블(Aria-label), 상태 속성(Aria-expanded, Aria-selected)을 전 컴포넌트에 내장하여 시각장애인 고객의 안전한 금융 거래를 돕습니다.
