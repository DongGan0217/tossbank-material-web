---
name: 2. Bottom Sheet
title: Bottom Sheet Action Pattern
order: 2
---

# 바텀시트 확인 모달 패턴 (Bottom Sheet Action Pattern)

모바일 금융 서비스에서 송금 최종 확인, 자동이체 등록 확인, 한도 증액 승인 등 사용자의 명시적인 결정이 필요한 맥락에서 채택되는 **바텀시트 확인 모달(Bottom Sheet)** 복합 패턴입니다. 상단 드래그 핸들 인디케이터, 요약 카드, 그리고 2단 액션 버튼(취소 / 확인)으로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 아래 <strong>[바텀시트 열기]</strong> 버튼을 누르면 실제 토스 상용 앱 스타일의 바텀시트가 열리며 송금 확인 인터랙션을 체험할 수 있습니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card" style="text-align:center;">
      <button onclick="document.getElementById('demo-sheet-overlay').style.display='flex';" style="background:#0064FF; color:#FFFFFF; border:none; padding:12px 28px; border-radius:14px; font-size:15px; font-weight:700; cursor:pointer; box-shadow:0 4px 14px rgba(0,100,255,0.25);">바텀시트 확인 모달 열기</button>

      <!-- Simulated Bottom Sheet Modal Overlay -->
      <div id="demo-sheet-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; justify-content:center; align-items:flex-end;">
        <div style="background:#FFFFFF; width:100%; max-width:440px; border-top-left-radius:24px; border-top-right-radius:24px; padding:20px 24px 32px 24px; box-shadow:0 -8px 30px rgba(0,0,0,0.15); text-align:left; animation:slideUp 0.25s ease-out;">
          <div style="width:40px; height:4px; background:#D1D6DB; border-radius:2px; margin:0 auto 18px auto;"></div>
          <h3 style="font-size:20px; font-weight:800; color:#191F28; margin:0 0 8px 0;">송금 내용을 확인해주세요</h3>
          <p style="font-size:14px; color:#6B7684; margin:0 0 20px 0;">받는 분과 계좌번호가 맞는지 다시 한 번 확인해주세요.</p>
          
          <div style="background:#F6F7F9; border-radius:14px; padding:16px; margin-bottom:24px;">
            <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
              <span style="font-size:13px; color:#8B95A1;">받는 사람</span>
              <span style="font-size:14px; font-weight:700; color:#191F28;">홍길동 (토스뱅크)</span>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
              <span style="font-size:13px; color:#8B95A1;">받는 계좌</span>
              <span style="font-size:14px; font-weight:600; color:#191F28;">1000-01-234567</span>
            </div>
            <div style="display:flex; justify-content:space-between; border-top:1px solid #E5E8EB; padding-top:10px;">
              <span style="font-size:13px; color:#8B95A1;">출금 금액</span>
              <span style="font-size:17px; font-weight:800; color:#0064FF;" class="tnum">50,000원</span>
            </div>
          </div>

          <div style="display:flex; gap:10px;">
            <button onclick="document.getElementById('demo-sheet-overlay').style.display='none';" style="flex:1; background:#F2F4F6; color:#525355; border:none; padding:14px; border-radius:12px; font-size:15px; font-weight:700; cursor:pointer;">취소</button>
            <button onclick="alert('송금이 성공적으로 완료되었습니다!'); document.getElementById('demo-sheet-overlay').style.display='none';" style="flex:2; background:#0064FF; color:#FFFFFF; border:none; padding:14px; border-radius:12px; font-size:15px; font-weight:700; cursor:pointer;">50,000원 보내기</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Surface Container</strong>: 상단 24px <code>X-Large</code> 스쿼클 코너가 적용된 드로어 시트</li>
    <li><strong>Drag Handle Indicator</strong>: 40px x 4px의 <code>Full</code> 코너 뉴트럴 인디케이터</li>
    <li><strong>Summary Card</strong>: 14px 코너의 <code>grey_050</code> 배경 및 Key-Value 정보 행</li>
    <li><strong>Action Buttons</strong>: 48px 터치 높이의 2단 액션 버튼 그룹 (Secondary 1 : Primary 2 비율)</li>
  </ul>
</div>
