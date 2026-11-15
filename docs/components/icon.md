# Icon (카카오뱅크 아이콘 시스템)

카카오뱅크 공식 웹(`kakaobank.com`)과 모바일 앱(APK)에서 추출·정제된 **140종의 공식 카카오뱅크 벡터 아이콘** 및 Google Material Symbols 하이브리드 라이브러리입니다. AI 에이전트와 개발자가 목적에 맞게 즉시 검색·선택할 수 있도록 **7대 기능·의미론적(Semantic) 도메인 메타데이터**를 제공합니다.

<div class="kb-visual-container">
  <div class="kb-section-intro">
    <strong>🔍 카카오뱅크 AI 시맨틱 아이콘 라이브러리 (140 Vectors):</strong><br/>
    아이콘명, 한글 용도 또는 추천 의도(Intent)로 검색하세요. 카드를 클릭하면 <strong>WebComponent / React JSX 태그</strong>가 클립보드에 즉시 복사됩니다.
  </div>
  <div class="kb-asset-toolbar" style="margin-block-end: 16px;">
    <div class="kb-asset-tabs" id="kb-icon-tabs" style="display: flex; flex-wrap: wrap; gap: 8px;">
      <button type="button" class="kb-tab-btn active" data-cat="all" onclick="filterIconCat('all', this)">전체 (140)</button>
      <button type="button" class="kb-tab-btn" data-cat="navigation" onclick="filterIconCat('navigation', this)">🧭 네비게이션 (29)</button>
      <button type="button" class="kb-tab-btn" data-cat="action" onclick="filterIconCat('action', this)">⚡ 액션&컨트롤 (54)</button>
      <button type="button" class="kb-tab-btn" data-cat="banking" onclick="filterIconCat('banking', this)">💳 금융&계좌 (9)</button>
      <button type="button" class="kb-tab-btn" data-cat="security" onclick="filterIconCat('security', this)">🔒 보안&인증 (20)</button>
      <button type="button" class="kb-tab-btn" data-cat="support" onclick="filterIconCat('support', this)">📞 고객지원&알림 (10)</button>
      <button type="button" class="kb-tab-btn" data-cat="social" onclick="filterIconCat('social', this)">🌐 공유&외부 (11)</button>
      <button type="button" class="kb-tab-btn" data-cat="emoji" onclick="filterIconCat('emoji', this)">🎨 리액션&배지 (7)</button>
    </div>
    <input 
      id="kb-icon-filter" 
      class="kb-icon-search-input" 
      type="text" 
      placeholder="아이콘명, 한글 설명 또는 의도 검색 (예: call, 송금, 계좌, 화살표, arrow, otp, close...)" 
      oninput="handleIconSearch(this.value)"
      style="margin-top: 12px; width: 100%; box-sizing: border-box;"
    />
  </div>
  <div class="kb-icon-grid" id="kb-icon-grid-container">
    <div style="grid-column: 1 / -1; padding: 40px; text-align: center; color: #8b95a1;">아이콘 데이터를 불러오는 중입니다...</div>
  </div>
</div>

<script>
(function() {
  let allIcons = [];
  let filteredIcons = [];
  let currentIconCat = "all";
  let searchIconQuery = "";

  async function loadIcons() {
    try {
      const res = await fetch("/images/kb-icons/icons.json");
      if (res.ok) {
        allIcons = await res.json();
      } else {
        throw new Error("Failed to load icons.json");
      }
    } catch (e) {
      console.warn("Could not load icons.json, using fallback", e);
      allIcons = [
        { name: "kb_ic-arrow-left", category: "navigation", categoryName: "네비게이션", type: "svg", url: "/images/kb-icons/svg/kb_ic-arrow-left.svg", intent: "navigation_back", description: "뒤로가기" },
        { name: "kb_ic-arrow-right", category: "navigation", categoryName: "네비게이션", type: "svg", url: "/images/kb-icons/svg/kb_ic-arrow-right.svg", intent: "navigation_forward", description: "앞으로가기" },
        { name: "kb_ic-close", category: "navigation", categoryName: "네비게이션", type: "svg", url: "/images/kb-icons/svg/kb_ic-close.svg", intent: "modal_close", description: "닫기" },
        { name: "kb_ic-call", category: "support", categoryName: "고객지원", type: "svg", url: "/images/kb-icons/svg/kb_ic-call.svg", intent: "customer_support", description: "전화상담" }
      ];
    }
    applyIconFilters();
  }

  function applyIconFilters() {
    filteredIcons = allIcons.filter(icon => {
      const matchesCat = (currentIconCat === "all") || (icon.category === currentIconCat);
      const q = searchIconQuery;
      const matchesQuery = !q || 
        icon.name.toLowerCase().includes(q) ||
        (icon.description && icon.description.toLowerCase().includes(q)) ||
        (icon.intent && icon.intent.toLowerCase().includes(q)) ||
        (icon.categoryName && icon.categoryName.toLowerCase().includes(q)) ||
        (icon.tags && icon.tags.some(t => t.toLowerCase().includes(q)));
      return matchesCat && matchesQuery;
    });
    renderIconGrid();
  }

  function renderIconGrid() {
    const container = document.getElementById("kb-icon-grid-container");
    if (!container) return;
    if (filteredIcons.length === 0) {
      container.innerHTML = '<div style="grid-column: 1 / -1; padding: 40px; text-align: center; color: #8b95a1;">일치하는 아이콘이 없습니다.</div>';
      return;
    }
    container.innerHTML = filteredIcons.map(icon => {
      const cleanName = icon.name.replace(/^kb_ic-|^kb_ic_|^kb_icon_|^kb_/, "");
      const isPng = (icon.type === "png" || icon.url.endsWith(".webp") || icon.url.endsWith(".png"));
      return `
        <div class="kb-icon-item" data-icon-name="${icon.name}" onclick="copyIconCode('${icon.url}', '${cleanName}')" title="${icon.description || cleanName} (클릭 시 코드 복사)">
          <div class="kb-icon-preview">
            <img src="${icon.url}" width="24" height="24" alt="${icon.name}" loading="lazy" />
          </div>
          <span class="kb-icon-name">${cleanName}</span>
          <span class="kb-icon-type-tag">${icon.categoryName || icon.type.toUpperCase()}</span>
        </div>
      `;
    }).join("");
  }

  window.filterIconCat = function(cat, btn) {
    currentIconCat = cat;
    document.querySelectorAll("#kb-icon-tabs .kb-tab-btn").forEach(b => b.classList.remove("active"));
    if (btn) btn.classList.add("active");
    applyIconFilters();
  };

  window.handleIconSearch = function(val) {
    searchIconQuery = val.toLowerCase().trim();
    applyIconFilters();
  };

  window.copyIconCode = function(url, name) {
    const tag = `<md-icon><img src="${url}" alt="${name}" /></md-icon>`;
    navigator.clipboard.writeText(tag);
    alert(`복사되었습니다:\n${tag}`);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadIcons);
  } else {
    loadIcons();
  }
})();
</script>

---

## 2. 사용법 (Usage)

카카오뱅크 웹 컴포넌트 환경에서 아이콘은 Material Symbols 텍스트 리가처 또는 카카오뱅크 공식 인라인 SVG / 이미지로 자유롭게 삽입할 수 있습니다.

### 1) 카카오뱅크 공식 SVG 아이콘 사용
```html
<md-icon>
  <img src="/images/kb-icons/svg/kb_ic-arrow-right.svg" alt="arrow-right" />
</md-icon>
```

### 2) Material Symbols 폰트 리가처 사용
```html
<md-icon>settings</md-icon>
<md-icon>notifications</md-icon>
<md-icon>lock</md-icon>
```

### 3) npm 패키지 `@kakaobank/material-web/icons` 임포트
```typescript
import { KakaoBankIcons } from "@kakaobank/material-web/icons";

// AI 자동 매핑 예시:
const callIcon = KakaoBankIcons.find(i => i.intent === "customer_support_call");
console.log(callIcon.url); // "/images/kb-icons/svg/kb_ic-call.svg"
```
