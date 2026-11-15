<!-- catalog-only-start --><!-- ---
name: 3. Backoffice / Admin
title: 여수신 대출 심사 어드민
order: 4
-----><!-- catalog-only-end -->

# 3. 토스뱅크 여수신 대출 심사 어드민 쇼케이스 (Backoffice)

`@tossbank/material-web` 컴포넌트로 구축된 **토스뱅크 여수신 비대면 대출 심사 백오피스 대시보드**입니다. 고대비 다크/라이트 테마를 지원하며, 실시간 대출 심사 큐, 신용평가(CSS) 스코어 모니터링, 그리고 1-Click 승인/반려 워크플로우를 직접 조작할 수 있습니다.

<div class="tb-visual-container kb-visual-container">
  <!-- KPI Metrics Cards -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px;">
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
      <span style="font-size: 13px; color: #4E5968; font-weight: 600;">총 여신 잔액</span>
      <div style="font-size: 24px; font-weight: 800; color: #191F28; margin-top: 4px;">14조 8,200억</div>
      <span style="font-size: 12px; color: #0064FF; font-weight: 700;">▲ 전월 대비 +3.4%</span>
    </div>
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
      <span style="font-size: 13px; color: #4E5968; font-weight: 600;">금일 비대면 신청</span>
      <div style="font-size: 24px; font-weight: 800; color: #0064FF; margin-top: 4px;">1,428건</div>
      <span style="font-size: 12px; color: #20BF6B; font-weight: 700;">실시간 자동승인률 86.2%</span>
    </div>
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
      <span style="font-size: 13px; color: #4E5968; font-weight: 600;">수동 심사 대기열</span>
      <div id="pending-count" style="font-size: 24px; font-weight: 800; color: #FF3B70; margin-top: 4px;">4건</div>
      <span style="font-size: 12px; color: #FF3B70; font-weight: 700;">● 처리 필요</span>
    </div>
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
      <span style="font-size: 13px; color: #4E5968; font-weight: 600;">평균 대출 실행 금리</span>
      <div style="font-size: 24px; font-weight: 800; color: #191F28; margin-top: 4px;">연 5.12%</div>
      <span style="font-size: 12px; color: #4E5968; font-weight: 600;">기준금리 대비 안정</span>
    </div>
  </div>

  <!-- Review Queue Table -->
  <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 20px; padding: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px;">
      <div>
        <h3 style="margin: 0; font-size: 18px; font-weight: 800; color: #191F28;">비대면 여신 수동 심사 대기열</h3>
        <p style="margin: 4px 0 0 0; font-size: 13px; color: #4E5968;">DSR 및 자체 머신러닝 신용평가(Toss-CSS) 기반 심사</p>
      </div>
      <input type="text" id="admin-search" placeholder="고객명 또는 신청 상품 검색..." oninput="filterAdminTable(this.value)" style="padding: 10px 16px; border-radius: 12px; border: 1px solid #D1D6DB; font-size: 13px; outline: none; width: 240px; font-family: inherit;" />
    </div>

    <div style="overflow-x: auto;">
      <table id="admin-table" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;">
        <thead>
          <tr style="border-bottom: 2px solid #F2F4F6; color: #4E5968; font-weight: 700;">
            <th style="padding: 12px 10px;">신청번호</th>
            <th style="padding: 12px 10px;">고객명</th>
            <th style="padding: 12px 10px;">신청 상품</th>
            <th style="padding: 12px 10px;">신청 한도</th>
            <th style="padding: 12px 10px;">DSR</th>
            <th style="padding: 12px 10px;">CSS 등급</th>
            <th style="padding: 12px 10px;">심사 상태</th>
            <th style="padding: 12px 10px; text-align: right;">의사결정</th>
          </tr>
        </thead>
        <tbody>
          <!-- Row 1 -->
          <tr style="border-bottom: 1px solid #F2F4F6;">
            <td style="padding: 14px 10px; font-weight: 600;">LN-202611-01</td>
            <td style="padding: 14px 10px; font-weight: 700; color: #191F28;">김토스</td>
            <td style="padding: 14px 10px;">비상금대출</td>
            <td style="padding: 14px 10px; font-weight: 700;">300만원</td>
            <td style="padding: 14px 10px; color: #20BF6B; font-weight: 700;">22.4%</td>
            <td style="padding: 14px 10px;"><span style="background: #E8F3FF; color: #0064FF; padding: 2px 8px; border-radius: 6px; font-weight: 800;">1등급 (942점)</span></td>
            <td style="padding: 14px 10px;" id="status-1"><span style="background: #FFF8CC; color: #5C4900; padding: 3px 8px; border-radius: 6px; font-weight: 700;">심사 대기</span></td>
            <td style="padding: 14px 10px; text-align: right;">
              <button onclick="approveRow(1)" style="background: #0064FF; color: #FFFFFF; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">승인</button>
              <button onclick="rejectRow(1)" style="background: #F2F4F6; color: #4E5968; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer;">반려</button>
            </td>
          </tr>
          <!-- Row 2 -->
          <tr style="border-bottom: 1px solid #F2F4F6;">
            <td style="padding: 14px 10px; font-weight: 600;">LN-202611-02</td>
            <td style="padding: 14px 10px; font-weight: 700; color: #191F28;">이뱅크</td>
            <td style="padding: 14px 10px;">직장인 신용대출</td>
            <td style="padding: 14px 10px; font-weight: 700;">5,000만원</td>
            <td style="padding: 14px 10px; color: #0064FF; font-weight: 700;">34.8%</td>
            <td style="padding: 14px 10px;"><span style="background: #E8F3FF; color: #0064FF; padding: 2px 8px; border-radius: 6px; font-weight: 800;">2등급 (885점)</span></td>
            <td style="padding: 14px 10px;" id="status-2"><span style="background: #FFF8CC; color: #5C4900; padding: 3px 8px; border-radius: 6px; font-weight: 700;">심사 대기</span></td>
            <td style="padding: 14px 10px; text-align: right;">
              <button onclick="approveRow(2)" style="background: #0064FF; color: #FFFFFF; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">승인</button>
              <button onclick="rejectRow(2)" style="background: #F2F4F6; color: #4E5968; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer;">반려</button>
            </td>
          </tr>
          <!-- Row 3 -->
          <tr style="border-bottom: 1px solid #F2F4F6;">
            <td style="padding: 14px 10px; font-weight: 600;">LN-202611-03</td>
            <td style="padding: 14px 10px; font-weight: 700; color: #191F28;">박사장</td>
            <td style="padding: 14px 10px;">사장님 대출</td>
            <td style="padding: 14px 10px; font-weight: 700;">8,000만원</td>
            <td style="padding: 14px 10px; color: #FF3B70; font-weight: 700;">39.2%</td>
            <td style="padding: 14px 10px;"><span style="background: #F2F4F6; color: #4E5968; padding: 2px 8px; border-radius: 6px; font-weight: 800;">3등급 (810점)</span></td>
            <td style="padding: 14px 10px;" id="status-3"><span style="background: #FFF8CC; color: #5C4900; padding: 3px 8px; border-radius: 6px; font-weight: 700;">심사 대기</span></td>
            <td style="padding: 14px 10px; text-align: right;">
              <button onclick="approveRow(3)" style="background: #0064FF; color: #FFFFFF; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">승인</button>
              <button onclick="rejectRow(3)" style="background: #F2F4F6; color: #4E5968; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer;">반려</button>
            </td>
          </tr>
          <!-- Row 4 -->
          <tr>
            <td style="padding: 14px 10px; font-weight: 600;">LN-202611-04</td>
            <td style="padding: 14px 10px; font-weight: 700; color: #191F28;">최청년</td>
            <td style="padding: 14px 10px;">전월세보증금대출</td>
            <td style="padding: 14px 10px; font-weight: 700;">1억 2,000만원</td>
            <td style="padding: 14px 10px; color: #20BF6B; font-weight: 700;">18.5%</td>
            <td style="padding: 14px 10px;"><span style="background: #E8F3FF; color: #0064FF; padding: 2px 8px; border-radius: 6px; font-weight: 800;">1등급 (960점)</span></td>
            <td style="padding: 14px 10px;" id="status-4"><span style="background: #FFF8CC; color: #5C4900; padding: 3px 8px; border-radius: 6px; font-weight: 700;">심사 대기</span></td>
            <td style="padding: 14px 10px; text-align: right;">
              <button onclick="approveRow(4)" style="background: #0064FF; color: #FFFFFF; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer; margin-right: 4px;">승인</button>
              <button onclick="rejectRow(4)" style="background: #F2F4F6; color: #4E5968; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; cursor: pointer;">반려</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<script>
let remainingPending = 4;

function approveRow(id) {
  const el = document.getElementById('status-' + id);
  el.innerHTML = '<span style="background: #E8F3FF; color: #0064FF; padding: 3px 8px; border-radius: 6px; font-weight: 800;">✓ 승인 완료</span>';
  updatePending();
}

function rejectRow(id) {
  const el = document.getElementById('status-' + id);
  el.innerHTML = '<span style="background: #FEECEE; color: #F04452; padding: 3px 8px; border-radius: 6px; font-weight: 800;">✕ 심사 반려</span>';
  updatePending();
}

function updatePending() {
  remainingPending = Math.max(0, remainingPending - 1);
  document.getElementById('pending-count').innerText = remainingPending + '건';
}

function filterAdminTable(query) {
  const q = query.toLowerCase();
  const rows = document.querySelectorAll('#admin-table tbody tr');
  rows.forEach(r => {
    const text = r.innerText.toLowerCase();
    r.style.display = text.includes(q) ? '' : 'none';
  });
}
</script>
