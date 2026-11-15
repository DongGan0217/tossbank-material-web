<!-- catalog-only-start --><!-- ---
name: Quick Start
title: Quick Start
order: 2
-----><!-- catalog-only-end -->

# 토스뱅크 빠른 시작 가이드 (Quick Start)

`@tossbank/material-web`을 웹 및 앱 프로젝트에 설치하고 사용하는 방법을 안내합니다.

---

## 1. 패키지 설치

npm, yarn, pnpm을 통해 토스뱅크 공식 Material Web 패키지를 설치합니다:

```bash
# npm
npm install @tossbank/material-web

# pnpm
pnpm add @tossbank/material-web

# yarn
yarn add @tossbank/material-web
```

---

## 2. 기본 사용법 (HTML & JavaScript)

필요한 컴포넌트를 JavaScript 모듈에서 import하면 W3C 표준 커스텀 엘리먼트(`md-*`)로 자동 등록되어 브라우저에서 즉시 렌더링됩니다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>토스뱅크 웹 서비스</title>
  <!-- Pretendard Variable 웹폰트 -->
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.css" />
  
  <!-- 토스뱅크 Web Components 임포트 -->
  <script type="module">
    import '@tossbank/material-web/button/filled-button.js';
    import '@tossbank/material-web/button/outlined-button.js';
    import '@tossbank/material-web/textfield/outlined-text-field.js';
    import '@tossbank/material-web/dialog/dialog.js';
  </script>
</head>
<body>
  <div style="padding: 24px; max-width: 480px; font-family: 'Pretendard Variable', sans-serif;">
    <h2 style="color: #191F28;">토스뱅크 통장</h2>
    <p style="color: #4E5968;">지금 쌓인 이자를 바로 확인하고 통장으로 입금받으세요.</p>
    
    <md-outlined-text-field label="보낼 금액" supporting-text="수수료 전액 무료" style="width: 100%; margin-bottom: 16px;"></md-outlined-text-field>
    
    <div style="display: flex; gap: 8px;">
      <md-filled-button style="flex: 1;">지금 이자받기 (연 2.0%)</md-filled-button>
      <md-outlined-button style="flex: 1;">송금하기</md-outlined-button>
    </div>
  </div>
</body>
</html>
```

---

## 3. React / Next.js 프로젝트 연동

React 19 이상에서는 Web Components를 네이티브 JSX 태그로 직접 지원합니다:

```tsx
import React, { useEffect } from 'react';

export default function TossBankWidget() {
  useEffect(() => {
    import('@tossbank/material-web/button/filled-button.js');
    import('@tossbank/material-web/chips/chip-set.js');
  }, []);

  return (
    <div className="tossbank-card">
      <h3>토스뱅크 4대 프로덕트</h3>
      {/* @ts-ignore */}
      <md-filled-button onClick={() => alert('이자 지급 완료!')}>
        지금 이자받기
      {/* @ts-ignore */}
      </md-filled-button>
    </div>
  );
}
```

---

## 4. 토스뱅크 동적 테마 전환

카탈로그에서 제공하는 3대 테마(Clean White, Cool Slate, Dark)를 애플리케이션 루트에 적용하려면 `data-theme` 속성을 지정합니다:

```html
<!-- 클린 화이트 테마 (기본) -->
<html data-theme="white">

<!-- 쿨 슬레이트 테마 -->
<html data-theme="slate">

<!-- 모던 다크 테마 -->
<html data-theme="dark">
```
