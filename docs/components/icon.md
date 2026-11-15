<!-- catalog-only-start --><!-- ---
name: Icon
dirname: icon
title: Icon Library
order: 10
-----><!-- catalog-only-end -->

# 토스뱅크 공식 아이콘 라이브러리 (Icon Library)

토스뱅크의 직관적이고 친근한 사용자 경험을 완성하는 140+종 공식 금융 벡터 아이콘입니다. AI 시맨틱 분류 체계(7대 도메인)를 탑재하여 기능적 의도(Intent)와 권장 컴포넌트 메타데이터를 제공하며, 클릭 한 번으로 사용 코드를 복사할 수 있습니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>💡 AI 시맨틱 아이콘 탐색:</strong> 7개 도메인 탭 또는 검색창을 통해 원하는 금융 아이콘을 빠르게 찾고, 카드를 클릭하여 <code>&lt;md-icon&gt;</code> 코드를 즉시 복사하세요.
  </div>

  <!-- Search & Tab Filter Bar -->
  <div class="tb-icon-search-bar kb-icon-search-bar" style="margin-bottom: 20px;">
    <input type="text" id="icon-search-input" class="tb-icon-search-input kb-icon-search-input" placeholder="아이콘 이름 또는 키워드 검색 (예: arrow, bank, card, check)..." oninput="filterIcons()" style="width: 100%; box-sizing: border-box; padding: 12px 18px; border-radius: 12px; border: 1px solid #D1D6DB; font-size: 14px; outline: none; font-family: inherit;" />
  </div>

  <!-- 7 Semantic Category Tabs -->
  <div class="tb-category-tabs kb-category-tabs" style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px;">
    <button type="button" class="tb-tab-btn kb-tab-btn active" data-cat="all" onclick="selectCategory('all', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #0064FF; color: #FFFFFF; cursor: pointer;">전체 (140+)</button>
    <button type="button" class="tb-tab-btn kb-tab-btn" data-cat="banking" onclick="selectCategory('banking', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #FFFFFF; color: #4E5968; cursor: pointer;">뱅킹 & 자산</button>
    <button type="button" class="tb-tab-btn kb-tab-btn" data-cat="navigation" onclick="selectCategory('navigation', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #FFFFFF; color: #4E5968; cursor: pointer;">네비게이션 & 제어</button>
    <button type="button" class="tb-tab-btn kb-tab-btn" data-cat="action" onclick="selectCategory('action', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #FFFFFF; color: #4E5968; cursor: pointer;">사용자 액션</button>
    <button type="button" class="tb-tab-btn kb-tab-btn" data-cat="security" onclick="selectCategory('security', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #FFFFFF; color: #4E5968; cursor: pointer;">인증 & 보안</button>
    <button type="button" class="tb-tab-btn kb-tab-btn" data-cat="support" onclick="selectCategory('support', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #FFFFFF; color: #4E5968; cursor: pointer;">고객지원 & 알림</button>
    <button type="button" class="tb-tab-btn kb-tab-btn" data-cat="social" onclick="selectCategory('social', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #FFFFFF; color: #4E5968; cursor: pointer;">소셜 & 브랜드</button>
    <button type="button" class="tb-tab-btn kb-tab-btn" data-cat="emoji" onclick="selectCategory('emoji', this)" style="padding: 8px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700; border: 1px solid #D1D6DB; background: #FFFFFF; color: #4E5968; cursor: pointer;">금융 이모지 & 상태</button>
  </div>

  <!-- Icon Grid Container -->
  <div id="icon-gallery-grid" class="tb-icon-grid kb-icon-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 14px;">
    <!-- Rendered via JavaScript -->
  </div>
</div>

<script>
(function() {
  let allIcons = [];
  let currentCategory = 'all';

  fetch('/images/tb-icons/icons.json')
    .then(res => res.json())
    .then(data => {
      allIcons = data;
      renderIcons(allIcons);
    })
    .catch(err => {
      console.warn('Fallback to kb-icons:', err);
      fetch('/images/tb-icons/icons.json')
        .then(res => res.json())
        .then(data => {
          allIcons = data;
          renderIcons(allIcons);
        });
    });

  function renderIcons(icons) {
    const grid = document.getElementById('icon-gallery-grid');
    if (!grid) return;
    if (icons.length === 0) {
      grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: #8B95A1;">검색 결과가 없습니다.</div>';
      return;
    }
    grid.innerHTML = icons.map(icon => {
      const cleanName = icon.name.replace(/^(tb_|kb_)(ic_)?/, '');
      return `
        <div class="tb-icon-item kb-icon-item" onclick="copyIconCode('${icon.url}', '${cleanName}')" title="${icon.description || cleanName} (클릭 시 코드 복사)" style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 14px; padding: 14px; display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; transition: all 0.15s ease;">
          <div style="width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; margin-bottom: 8px;">
            <img src="${icon.url}" width="24" height="24" alt="${icon.name}" loading="lazy" style="max-width: 100%; max-height: 100%; object-fit: contain;" />
          </div>
          <span style="font-size: 12px; font-weight: 700; color: #191F28; text-align: center; word-break: break-all; max-width: 100%;">${cleanName}</span>
          <span style="font-size: 10px; color: #0064FF; background: #E8F3FF; padding: 2px 6px; border-radius: 4px; margin-top: 4px; font-weight: 700;">${icon.categoryName || icon.type.toUpperCase()}</span>
        </div>
      `;
    }).join('');
  }

  window.selectCategory = function(cat, btn) {
    currentCategory = cat;
    document.querySelectorAll('.tb-tab-btn, .kb-tab-btn').forEach(b => {
      b.style.background = '#FFFFFF';
      b.style.color = '#4E5968';
    });
    btn.style.background = '#0064FF';
    btn.style.color = '#FFFFFF';
    filterIcons();
  };

  window.filterIcons = function() {
    const q = (document.getElementById('icon-search-input').value || '').toLowerCase().trim();
    const filtered = allIcons.filter(icon => {
      const matchesCat = (currentCategory === 'all') || (icon.category === currentCategory);
      const matchesQuery = !q || icon.name.toLowerCase().includes(q) || (icon.description && icon.description.toLowerCase().includes(q));
      return matchesCat && matchesQuery;
    });
    renderIcons(filtered);
  };

  window.copyIconCode = function(url, name) {
    const tag = `<md-icon><img src="${url}" alt="${name}" /></md-icon>`;
    navigator.clipboard.writeText(tag);
    alert(`복사되었습니다:\n${tag}`);
  };
})();
</script>

---

## 3. 컴포넌트별 아이콘 활용 예시

### 1) 토스뱅크 공식 SVG 아이콘 사용
```html
<md-icon>
  <img src="/images/tb-icons/svg/tb_ic-arrow-right.svg" alt="arrow-right" />
</md-icon>
```

### 2) 버튼 내 선행(Leading) 아이콘 적용
```html
<md-filled-button>
  <md-icon slot="icon">
    <img src="/images/tb-icons/svg/tb_ic-check.svg" alt="check" />
  </md-icon>
  계좌 인증 완료
</md-filled-button>
```
