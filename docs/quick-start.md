<!-- catalog-only-start --><!-- ---
name: Quick Start
title: Quick Start
order: 2
-----><!-- catalog-only-end -->

# 빠른 시작 가이드 (Quick Start)

`@kakaobank/material-web`을 프로젝트에 설치하고 사용하는 방법을 안내합니다.

---

## 1. 패키지 설치

npm 또는 yarn, pnpm을 통해 패키지를 설치합니다:

```bash
# npm
npm install @kakaobank/material-web

# pnpm
pnpm add @kakaobank/material-web
```

---

## 2. 기본 사용법 (HTML & JavaScript)

필요한 컴포넌트를 JavaScript에서 import하면 커스텀 엘리먼트(`md-*`)로 등록되어 브라우저에서 바로 렌더링됩니다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>카카오뱅크 서비스</title>
  <!-- Pretendard Variable 웹폰트 링크 -->
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.css" />
  
  <!-- 카카오뱅크 컴포넌트 임포트 -->
  <script type="module">
    import '@kakaobank/material-web/button/filled-button.js';
    import '@kakaobank/material-web/textfield/outlined-text-field.js';
  </script>
</head>
<body>
  <div style="padding: 24px; max-width: 480px;">
    <h2>간편 이체</h2>
    <md-outlined-text-field label="보낼 금액" supporting-text="원 단위로 입력하세요" style="width: 100%; margin-bottom: 16px;"></md-outlined-text-field>
    <md-filled-button style="width: 100%;">이체하기 (52px Touch)</md-filled-button>
  </div>
</body>
</html>
```

---

## 3. React / Next.js 프로젝트 연동

React 19 이상에서는 Web Components를 기본 JSX 엘리먼트로 직접 지원합니다.

```tsx
'use client';

import { useEffect } from 'react';

export default function TransferPage() {
  useEffect(() => {
    import('@kakaobank/material-web/button/filled-button.js');
  }, []);

  return (
    <div className="p-6">
      <md-filled-button onClick={() => alert('이체 완료!')}>
        확인
      </md-filled-button>
    </div>
  );
}
```
