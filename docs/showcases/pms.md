<!-- catalog-only-start --><!-- ---
name: 4. PMS
title: 금융상품 출시 프로젝트 관리 시스템 (PMS)
order: 5
-----><!-- catalog-only-end -->

# 4. 토스뱅크 금융상품 출시 PMS 쇼케이스 (Product Management System)

`@tossbank/material-web` 컴포넌트로 구축된 **토스뱅크 금융상품 출시 프로젝트 관리 시스템(PMS)**입니다. 금융당국 규제 검토, 보안성 심의, 개발 스프린트 및 대고객 런칭까지의 전체 파이프라인을 칸반 보드와 인터랙티브 체크리스트로 관리할 수 있습니다.

<div class="tb-visual-container kb-visual-container">
  <!-- PMS Top Action Bar -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; flex-wrap: wrap; gap: 12px;">
    <div>
      <h3 style="margin: 0; font-size: 20px; font-weight: 800; color: #191F28;">📊 2026 Q4 신규 금융상품 출시 파이프라인</h3>
      <p style="margin: 4px 0 0 0; font-size: 13px; color: #4E5968;">금융위 혁신금융서비스 및 자체 개발 스프린트 진행 현황</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <button onclick="document.getElementById('new-task-dialog').show()" style="background: #0064FF; color: #FFFFFF; border: none; padding: 10px 18px; border-radius: 12px; font-size: 13px; font-weight: 800; cursor: pointer; box-shadow: 0 4px 12px rgba(0,100,255,0.25);">
        + 신규 상품 태스크 추가
      </button>
    </div>
  </div>

  <!-- Kanban Board 3-Columns -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 32px;">
    
    <!-- Column 1: 기획 & 규제 심의 -->
    <div style="background: #F9FAFB; border: 1px solid #E5E8EB; border-radius: 18px; padding: 18px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <span style="font-weight: 800; font-size: 14px; color: #191F28;">1. 기획 & 규제 심의</span>
        <span style="background: #E5E8EB; color: #4E5968; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 9999px;">2건</span>
      </div>

      <!-- Card 1 -->
      <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 14px; padding: 16px; margin-bottom: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
          <span style="font-size: 11px; font-weight: 800; color: #0064FF; background: #E8F3FF; padding: 2px 6px; border-radius: 4px;">수신상품</span>
          <span style="font-size: 11px; color: #8B95A1;">D-15</span>
        </div>
        <h5 style="margin: 0 0 6px 0; font-size: 15px; font-weight: 700; color: #191F28;">외화 자동투자 통장 v2</h5>
        <p style="margin: 0 0 12px 0; font-size: 12px; color: #4E5968; line-height: 1.4;">환율 지정가 자동 환전 및 달러 RP 자동 매수 연계</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 11px; color: #FF3B70; font-weight: 700;">● 금감원 약관 심의 중</span>
          <button onclick="moveCard(this)" style="background: #F2F4F6; border: none; font-size: 11px; font-weight: 700; color: #191F28; padding: 4px 8px; border-radius: 6px; cursor: pointer;">다음 단계 ▷</button>
        </div>
      </div>

      <!-- Card 2 -->
      <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 14px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
          <span style="font-size: 11px; font-weight: 800; color: #7B2CBF; background: #F3E8FF; padding: 2px 6px; border-radius: 4px;">여신상품</span>
          <span style="font-size: 11px; color: #8B95A1;">D-28</span>
        </div>
        <h5 style="margin: 0 0 6px 0; font-size: 15px; font-weight: 700; color: #191F28;">개인사업자 비대면 한도대출</h5>
        <p style="margin: 0 0 12px 0; font-size: 12px; color: #4E5968; line-height: 1.4;">부가세 신고 데이터 기반 실시간 한도 산출 모델</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 11px; color: #5C4900; font-weight: 700;">● 리스크 모델 검증</span>
          <button onclick="moveCard(this)" style="background: #F2F4F6; border: none; font-size: 11px; font-weight: 700; color: #191F28; padding: 4px 8px; border-radius: 6px; cursor: pointer;">다음 단계 ▷</button>
        </div>
      </div>
    </div>

    <!-- Column 2: 개발 & 보안성 심의 -->
    <div id="col-dev" style="background: #F9FAFB; border: 1px solid #E5E8EB; border-radius: 18px; padding: 18px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <span style="font-weight: 800; font-size: 14px; color: #191F28;">2. 개발 & 보안성 심의</span>
        <span style="background: #E8F3FF; color: #0064FF; font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 9999px;">1건</span>
      </div>

      <!-- Card 3 -->
      <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 14px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
          <span style="font-size: 11px; font-weight: 800; color: #20BF6B; background: #E8F8F0; padding: 2px 6px; border-radius: 4px;">체크카드</span>
          <span style="font-size: 11px; color: #8B95A1;">Sprint 42</span>
        </div>
        <h5 style="margin: 0 0 6px 0; font-size: 15px; font-weight: 700; color: #191F28;">체크카드 듀얼톤 신규 에디션</h5>
        <p style="margin: 0 0 12px 0; font-size: 12px; color: #4E5968; line-height: 1.4;">나이트핑크 & 오렌지밀크 플레이트 결제망 연동</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 11px; color: #0064FF; font-weight: 700;">● 보안성 심의 승인</span>
          <button onclick="moveCard(this)" style="background: #F2F4F6; border: none; font-size: 11px; font-weight: 700; color: #191F28; padding: 4px 8px; border-radius: 6px; cursor: pointer;">다음 단계 ▷</button>
        </div>
      </div>
    </div>

    <!-- Column 3: QA & 출시 완료 -->
    <div id="col-done" style="background: #F9FAFB; border: 1px solid #E5E8EB; border-radius: 18px; padding: 18px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <span style="font-weight: 800; font-size: 14px; color: #191F28;">3. QA & 출시 준비</span>
        <span style="background: #FFF8CC; color: #5C4900; font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 9999px;">1건</span>
      </div>

      <!-- Card 4 -->
      <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 14px; padding: 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
          <span style="font-size: 11px; font-weight: 800; color: #FF6B00; background: #FFF0E6; padding: 2px 6px; border-radius: 4px;">적금</span>
          <span style="font-size: 11px; color: #8B95A1;">Release 1.8</span>
        </div>
        <h5 style="margin: 0 0 6px 0; font-size: 15px; font-weight: 700; color: #191F28;">굴비적금 시즌 2 (골든굴비)</h5>
        <p style="margin: 0 0 12px 0; font-size: 12px; color: #4E5968; line-height: 1.4;">최종 E2E 통합 테스트 및 앱스토어 심사 완료</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 11px; color: #20BF6B; font-weight: 700;">✓ 출시 대기 (100%)</span>
          <span style="font-size: 11px; color: #8B95A1;">내일 오픈</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Compliance Checklist -->
  <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 20px; padding: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
    <h4 style="margin: 0 0 14px 0; font-size: 16px; font-weight: 800; color: #191F28;">🛡️ 금융상품 출시 전 컴플라이언스 체크리스트</h4>
    <div style="display: flex; flex-direction: column; gap: 10px; font-size: 14px; color: #191F28;">
      <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
        <input type="checkbox" checked style="accent-color: #0064FF; width: 18px; height: 18px;" />
        금융소비자보호법(금소법) 설명의무 및 중요사항 고지 화면 검증 완료
      </label>
      <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
        <input type="checkbox" checked style="accent-color: #0064FF; width: 18px; height: 18px;" />
        금융보안원 비대면 실명확인 및 생체인증 보안성 심의 적합 판정
      </label>
      <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
        <input type="checkbox" checked style="accent-color: #0064FF; width: 18px; height: 18px;" />
        예금자보호법 적용 대상 여부 및 5천만원 보호 한도 표기 규격 준수
      </label>
      <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
        <input type="checkbox" style="accent-color: #0064FF; width: 18px; height: 18px;" />
        금융감독원 약관 제정 및 보고 최종 확인
      </label>
    </div>
  </div>

  <!-- New Task Dialog Modal -->
  <dialog id="new-task-dialog" style="border: none; border-radius: 24px; padding: 28px; width: 90%; max-width: 440px; box-shadow: 0 20px 48px rgba(0,0,0,0.2); font-family: inherit;">
    <h3 style="margin: 0 0 8px 0; font-size: 20px; font-weight: 800; color: #191F28;">신규 금융상품 태스크 등록</h3>
    <p style="margin: 0 0 20px 0; font-size: 13px; color: #4E5968;">새로운 예적금/대출/외환 프로젝트를 파이프라인에 등록합니다.</p>
    
    <div style="margin-bottom: 14px;">
      <label style="font-size: 12px; font-weight: 700; color: #4E5968;">상품명:</label>
      <input type="text" id="new-task-name" placeholder="예: 평생무료 외화적금" style="width: 100%; box-sizing: border-box; padding: 10px 14px; border-radius: 12px; border: 1px solid #D1D6DB; margin-top: 4px; font-size: 14px; outline: none;" />
    </div>

    <div style="margin-bottom: 24px;">
      <label style="font-size: 12px; font-weight: 700; color: #4E5968;">카테고리:</label>
      <select id="new-task-cat" style="width: 100%; box-sizing: border-box; padding: 10px 14px; border-radius: 12px; border: 1px solid #D1D6DB; margin-top: 4px; font-size: 14px; outline: none; background: #FFFFFF;">
        <option>수신상품 (통장/적금)</option>
        <option>여신상품 (신용/주담대)</option>
        <option>외환 (FX/송금)</option>
        <option>체크카드</option>
      </select>
    </div>

    <div style="display: flex; gap: 10px; justify-content: flex-end;">
      <button onclick="document.getElementById('new-task-dialog').close()" style="background: #F2F4F6; color: #4E5968; font-weight: 700; font-size: 14px; padding: 10px 18px; border-radius: 12px; border: none; cursor: pointer;">취소</button>
      <button onclick="addTask()" style="background: #0064FF; color: #FFFFFF; font-weight: 800; font-size: 14px; padding: 10px 22px; border-radius: 12px; border: none; cursor: pointer;">등록하기</button>
    </div>
  </dialog>
</div>

<script>
function moveCard(btn) {
  const card = btn.closest('div[style*="background: #FFFFFF"]');
  const targetCol = document.getElementById('col-done');
  btn.innerText = '✓ 완료됨';
  btn.disabled = true;
  targetCol.appendChild(card);
}

function addTask() {
  const name = document.getElementById('new-task-name').value;
  if (!name) {
    alert('상품명을 입력해주세요.');
    return;
  }
  alert('"' + name + '" 상품이 1단계 기획 & 규제 심의 대기열에 성공적으로 등록되었습니다!');
  document.getElementById('new-task-dialog').close();
}
</script>
