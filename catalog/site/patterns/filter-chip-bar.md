---
name: 7. Filter Chip Bar
title: Selection Filter Chip Bar Pattern
order: 7
---

# 수평 스크롤 필터 칩 바 패턴 (Selection Filter Chip Bar Pattern)

거래내역, 자산 목록, 금융 상품 검색 등 다양한 필터링 옵션을 모바일 터치 스크린 상에서 효율적으로 제공하는 **수평 스크롤 필터 칩 바(Filter Chip Bar)** 복합 패턴입니다. 가로 스크롤 컨테이너, 선택 상태 토글(Selected / Unselected), 건수 카운트 배지, 그리고 정렬 드롭다운 트리거로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 각 필터 칩을 클릭하면 선택 상태가 즉시 토글되며 하단 결과 목록의 필터링 카운트가 실시간 변경됩니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card" style="max-width:480px; margin:0 auto;">
      <!-- Filter Chips Bar -->
      <div style="display:flex; gap:8px; overflow-x:auto; padding-bottom:8px; scrollbar-width:none; -webkit-overflow-scrolling:touch;">
        <button id="chip-all" class="filter-chip-btn active" onclick="selectFilter('all', 28)">전체 28</button>
        <button id="chip-in" class="filter-chip-btn" onclick="selectFilter('in', 8)">입금 8</button>
        <button id="chip-out" class="filter-chip-btn" onclick="selectFilter('out', 20)">출금 20</button>
        <button id="chip-card" class="filter-chip-btn" onclick="selectFilter('card', 14)">체크카드 14</button>
        <button id="chip-trans" class="filter-chip-btn" onclick="selectFilter('trans', 6)">계좌이체 6</button>
      </div>

      <!-- Result Filter Status Banner -->
      <div style="margin-top:16px; background:#F6F7F9; border-radius:14px; padding:16px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <span style="font-size:12px; color:#8B95A1;">선택된 필터 조건</span>
          <div id="filter-status-text" style="font-size:15px; font-weight:700; color:#191F28; margin-top:2px;">전체 거래내역 (28건)</div>
        </div>
        <button onclick="alert('기간 설정 드로어를 호출합니다.');" style="background:#FFFFFF; border:1px solid #D1D6DB; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:600; color:#4E5968; cursor:pointer;">최신순 ▼</button>
      </div>

      <script>
        function selectFilter(type, count) {
          document.querySelectorAll('.filter-chip-btn').forEach(btn => btn.classList.remove('active'));
          const target = document.getElementById('chip-' + type);
          if (target) target.classList.add('active');
          
          const names = { all: '전체 거래내역', in: '입금 내역', out: '출금 내역', card: '체크카드 승인', trans: '계좌이체' };
          document.getElementById('filter-status-text').innerText = names[type] + ' (' + count + '건)';
        }
      </script>
      <style>
        .filter-chip-btn {
          white-space: nowrap;
          padding: 8px 16px;
          border-radius: 9999px;
          border: 1px solid #E5E8EB;
          background: #FFFFFF;
          color: #525355;
          font-size: 13px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.15s ease;
        }
        .filter-chip-btn:hover { background: #F8F9FA; }
        .filter-chip-btn.active {
          background: #0064FF;
          border-color: #0064FF;
          color: #FFFFFF;
          font-weight: 700;
          box-shadow: 0 2px 8px rgba(0, 100, 255, 0.25);
        }
      </style>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Full Rounded Pills</strong>: 36px 높이의 <code>Full</code> (9999px) 코너 래디우스 필터 버튼</li>
    <li><strong>State Binding</strong>: 활성 상태 시 <code>Primary Blue</code> 및 그림자 강조, 비활성 시 <code>Surface Low</code> 및 보더</li>
    <li><strong>Horizontal Scroll Surface</strong>: 모바일 가로 플릭 터치 스크롤 컨테이너</li>
    <li><strong>Dropdown Sort Trigger</strong>: 우측 고정 정렬 변경 트리거 버튼</li>
  </ul>
</div>
