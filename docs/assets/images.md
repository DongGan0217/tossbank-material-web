<!-- catalog-only-start --><!-- ---
name: Image Library
title: Image Library (카카오뱅크 그래픽 에셋)
order: 1
tags: [asset]
-----><!-- catalog-only-end -->

# 카카오뱅크 이미지 & 그래픽 에셋 라이브러리 (Image Library)

카카오뱅크 공식 상용 앱(APK) 및 웹사이트에서 추출·정제된 **1,000+종의 고해상도 그래픽 에셋(WebP)**과 신규 제작된 **20종 컴포넌트 벡터 SVG 히어로 배너**를 실시간으로 탐색, 검색, 복사할 수 있는 통합 에셋 라이브러리입니다.

<div class="kb-visual-container">
  <!-- Dashboard Stats -->
  <div class="kb-asset-dashboard-stats">
    <div class="kb-stat-card">
      <div class="label">총 보유 그래픽 에셋</div>
      <div class="val" id="kb-stat-total">880+</div>
    </div>
    <div class="kb-stat-card">
      <div class="label">벡터 SVG 히어로 배너</div>
      <div class="val" style="color: #d97706;">20</div>
    </div>
    <div class="kb-stat-card">
      <div class="label">상용 WebP 일러스트·애니메이션</div>
      <div class="val" style="color: #2563eb;">860+</div>
    </div>
    <div class="kb-stat-card">
      <div class="label">페이지당 렌더링 규격</div>
      <div class="val" style="color: #059669;">48 items</div>
    </div>
  </div>

  <!-- Toolbar: Tabs & Search -->
  <div class="kb-asset-toolbar">
    <div class="kb-asset-tabs" id="kb-category-tabs">
      <button type="button" class="kb-tab-btn active" data-cat="all" onclick="filterCategory('all', this)">전체 (880+)</button>
      <button type="button" class="kb-tab-btn" data-cat="hero_banner" onclick="filterCategory('hero_banner', this)">🎨 컴포넌트 배너 (20)</button>
      <button type="button" class="kb-tab-btn" data-cat="banking_card" onclick="filterCategory('banking_card', this)">💳 금융 & 카드 (850+)</button>
      <button type="button" class="kb-tab-btn" data-cat="illust" onclick="filterCategory('illust', this)">✨ 일러스트 & 캐릭터</button>
      <button type="button" class="kb-tab-btn" data-cat="anim" onclick="filterCategory('anim', this)">🎬 모션 & 애니메이션</button>
      <button type="button" class="kb-tab-btn" data-cat="general_ui" onclick="filterCategory('general_ui', this)">🏷️ UI & 에셋</button>
    </div>

    <input 
      type="text" 
      id="kb-asset-search" 
      class="kb-asset-search-input" 
      placeholder="에셋명 또는 키워드 검색 (예: hero, anim, loading, card, loan, character, badge...)"
      oninput="handleSearch(this.value)"
    />
  </div>

  <!-- Asset Grid Container -->
  <div class="kb-asset-grid" id="kb-asset-grid-container">
    <!-- Populated by JavaScript -->
    <div style="grid-column: 1 / -1; padding: 40px; text-align: center; color: #6b7684;">
      에셋 라이브러리 데이터를 로딩 중입니다...
    </div>
  </div>

  <!-- Pagination Bar -->
  <div class="kb-pagination-bar" id="kb-pagination-container">
    <!-- Populated by JavaScript -->
  </div>
</div>

<!-- Lightbox Modal -->
<div class="kb-lightbox-modal" id="kb-lightbox-modal" onclick="closeLightbox(event)">
  <div class="kb-lightbox-content" onclick="event.stopPropagation()">
    <button type="button" class="kb-lightbox-close" onclick="closeLightbox()">&times;</button>
    <div class="kb-lightbox-preview">
      <img id="kb-lightbox-img" src="" alt="Preview" />
    </div>
    <div class="kb-lightbox-details">
      <div class="kb-lightbox-title" id="kb-lightbox-title">Asset Title</div>
      <div class="kb-lightbox-path" id="kb-lightbox-path">/images/kb-assets/...</div>
      <div id="kb-lightbox-ai-info" style="margin-block: 10px; font-size: 13px; color: #4e5968; background: var(--md-sys-color-surface-container, #f2f4f6); padding: 10px 14px; border-radius: 10px; text-align: left; line-height: 1.6;">
        <div><strong>🤖 AI 추천 의도(Intent):</strong> <span id="kb-lightbox-intent" style="color: #2563eb; font-weight: 600;">-</span></div>
        <div><strong>🧩 권장 컴포넌트:</strong> <code id="kb-lightbox-comp" style="background: rgba(0,0,0,0.06); padding: 2px 6px; border-radius: 4px;">-</code></div>
        <div><strong>📝 의미 설명:</strong> <span id="kb-lightbox-desc">-</span></div>
      </div>
      <div class="kb-lightbox-buttons">
        <button type="button" class="kb-lightbox-btn btn-primary-yellow" onclick="copyAssetPath()">경로 복사 (Copy Path)</button>
        <button type="button" class="kb-lightbox-btn btn-secondary-dark" onclick="copyAssetTag()">HTML &lt;img&gt; 복사</button>
      </div>
    </div>
  </div>
</div>

<script>
(function() {
  let allAssets = [];
  let filteredAssets = [];
  let currentCategory = 'all';
  let searchQuery = '';
  let currentPage = 1;
  const itemsPerPage = 48;
  let currentActiveAsset = null;

  async function loadCatalog() {
    try {
      const res = await fetch('/assets/image-catalog.json');
      if (res.ok) {
        allAssets = await res.json();
      } else {
        throw new Error('Failed to load JSON');
      }
    } catch (e) {
      console.warn('Could not fetch JSON catalog, using fallback heroes', e);
      allAssets = [
        { id: 'hero-button', name: 'Button Hero Banner', filename: 'hero_button.svg', category: 'hero', categoryName: '히어로 배너', format: 'SVG', url: '/images/kb-assets/heroes/hero_button.svg', tags: ['hero', 'button'] },
        { id: 'hero-dialog', name: 'Dialog Hero Banner', filename: 'hero_dialog.svg', category: 'hero', categoryName: '히어로 배너', format: 'SVG', url: '/images/kb-assets/heroes/hero_dialog.svg', tags: ['hero', 'dialog'] },
        { id: 'hero-fab', name: 'FAB Hero Banner', filename: 'hero_fab.svg', category: 'hero', categoryName: '히어로 배너', format: 'SVG', url: '/images/kb-assets/heroes/hero_fab.svg', tags: ['hero', 'fab'] },
        { id: 'hero-slider', name: 'Slider Hero Banner', filename: 'hero_slider.svg', category: 'hero', categoryName: '히어로 배너', format: 'SVG', url: '/images/kb-assets/heroes/hero_slider.svg', tags: ['hero', 'slider'] },
        { id: 'hero-tabs', name: 'Tabs Hero Banner', filename: 'hero_tabs.svg', category: 'hero', categoryName: '히어로 배너', format: 'SVG', url: '/images/kb-assets/heroes/hero_tabs.svg', tags: ['hero', 'tabs'] },
      ];
    }
    
    // Update total count
    const totalEl = document.getElementById('kb-stat-total');
    if (totalEl) totalEl.innerText = allAssets.length + '+';

    applyFilters();
  }

  function applyFilters() {
    filteredAssets = allAssets.filter(item => {
      const matchesCat = (currentCategory === 'all') || 
        (item.category === currentCategory) || 
        (item.domain === currentCategory);
      const matchesQuery = !searchQuery || 
        item.name.toLowerCase().includes(searchQuery) || 
        item.filename.toLowerCase().includes(searchQuery) ||
        (item.description && item.description.toLowerCase().includes(searchQuery)) ||
        (item.intent && item.intent.toLowerCase().includes(searchQuery)) ||
        (item.domainName && item.domainName.toLowerCase().includes(searchQuery)) ||
        (item.tags && item.tags.some(t => t.toLowerCase().includes(searchQuery)));
      return matchesCat && matchesQuery;
    });

    currentPage = 1;
    renderGrid();
    renderPagination();
  }

  function renderGrid() {
    const container = document.getElementById('kb-asset-grid-container');
    if (!container) return;

    if (filteredAssets.length === 0) {
      container.innerHTML = '<div style="grid-column: 1 / -1; padding: 60px 20px; text-align: center; color: #8b95a1; font-size: 15px;">검색 결과와 일치하는 에셋이 없습니다.</div>';
      return;
    }

    const startIndex = (currentPage - 1) * itemsPerPage;
    const pageItems = filteredAssets.slice(startIndex, startIndex + itemsPerPage);

    container.innerHTML = pageItems.map(item => `
      <div class="kb-asset-card" onclick="openLightbox('${item.id}')">
        <div class="kb-asset-thumb">
          <img src="${item.url}" alt="${item.name}" loading="lazy" decoding="async" />
        </div>
        <div class="kb-asset-info">
          <div class="kb-asset-title" title="${item.name}">${item.name}</div>
          <div class="kb-asset-meta">
            <span class="kb-asset-cat-tag">${item.categoryName}</span>
            <span class="kb-asset-format-badge format-${item.format.toLowerCase()}">${item.format}</span>
          </div>
          <div class="kb-asset-actions" onclick="event.stopPropagation()">
            <button type="button" class="kb-asset-action-btn" onclick="copyPathDirect('${item.url}', this)">경로</button>
            <button type="button" class="kb-asset-action-btn" onclick="copyTagDirect('${item.url}', '${item.name}', this)">태그</button>
          </div>
        </div>
      </div>
    `).join('');
  }

  function renderPagination() {
    const container = document.getElementById('kb-pagination-container');
    if (!container) return;

    const totalPages = Math.ceil(filteredAssets.length / itemsPerPage);
    if (totalPages <= 1) {
      container.innerHTML = '';
      return;
    }

    let html = '';
    html += `<button type="button" class="kb-page-btn" ${currentPage === 1 ? 'disabled' : ''} onclick="changePage(${currentPage - 1})">이전</button>`;

    // Show limited page numbers
    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, currentPage + 2);

    if (startPage > 1) {
      html += `<button type="button" class="kb-page-btn" onclick="changePage(1)">1</button>`;
      if (startPage > 2) html += `<span style="padding: 0 4px; color: #8b95a1;">...</span>`;
    }

    for (let p = startPage; p <= endPage; p++) {
      html += `<button type="button" class="kb-page-btn ${p === currentPage ? 'active' : ''}" onclick="changePage(${p})">${p}</button>`;
    }

    if (endPage < totalPages) {
      if (endPage < totalPages - 1) html += `<span style="padding: 0 4px; color: #8b95a1;">...</span>`;
      html += `<button type="button" class="kb-page-btn" onclick="changePage(${totalPages})">${totalPages}</button>`;
    }

    html += `<button type="button" class="kb-page-btn" ${currentPage === totalPages ? 'disabled' : ''} onclick="changePage(${currentPage + 1})">다음</button>`;
    container.innerHTML = html;
  }

  window.changePage = function(page) {
    currentPage = page;
    renderGrid();
    renderPagination();
    const anchor = document.getElementById('kb-asset-grid-container');
    if (anchor) anchor.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  window.filterCategory = function(cat, btn) {
    currentCategory = cat;
    document.querySelectorAll('#kb-category-tabs .kb-tab-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    applyFilters();
  };

  window.handleSearch = function(val) {
    searchQuery = val.toLowerCase().trim();
    applyFilters();
  };

  window.openLightbox = function(assetId) {
    const item = allAssets.find(a => a.id === assetId);
    if (!item) return;
    currentActiveAsset = item;

    document.getElementById('kb-lightbox-img').src = item.url;
    document.getElementById('kb-lightbox-title').innerText = item.name;
    document.getElementById('kb-lightbox-path').innerText = item.url;
    document.getElementById('kb-lightbox-intent').innerText = item.intent || item.category || '-';
    document.getElementById('kb-lightbox-comp').innerText = item.suggestedComponent || '<md-card>, <img>';
    document.getElementById('kb-lightbox-desc').innerText = item.description || item.name;
    document.getElementById('kb-lightbox-modal').classList.add('open');
  };

  window.closeLightbox = function(e) {
    if (e && e.target !== document.getElementById('kb-lightbox-modal') && !e.target.classList.contains('kb-lightbox-close')) return;
    document.getElementById('kb-lightbox-modal').classList.remove('open');
  };

  window.copyAssetPath = function() {
    if (!currentActiveAsset) return;
    navigator.clipboard.writeText(currentActiveAsset.url);
    alert('에셋 경로가 복사되었습니다:\n' + currentActiveAsset.url);
  };

  window.copyAssetTag = function() {
    if (!currentActiveAsset) return;
    const tag = `<img src="${currentActiveAsset.url}" alt="${currentActiveAsset.name}" />`;
    navigator.clipboard.writeText(tag);
    alert('HTML <img> 태그가 복사되었습니다:\n' + tag);
  };

  window.copyPathDirect = function(url, btn) {
    navigator.clipboard.writeText(url);
    const originText = btn.innerText;
    btn.innerText = '복사됨!';
    setTimeout(() => btn.innerText = originText, 1200);
  };

  window.copyTagDirect = function(url, name, btn) {
    const tag = `<img src="${url}" alt="${name}" />`;
    navigator.clipboard.writeText(tag);
    const originText = btn.innerText;
    btn.innerText = '복사됨!';
    setTimeout(() => btn.innerText = originText, 1200);
  };

  // Keyboard escape
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      const modal = document.getElementById('kb-lightbox-modal');
      if (modal && modal.classList.contains('open')) {
        modal.classList.remove('open');
      }
    }
  });

  document.addEventListener('DOMContentLoaded', loadCatalog);
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    loadCatalog();
  }
})();
</script>
