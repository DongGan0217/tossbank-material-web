---
name: 4. Agreement Terms
title: Agreement & Terms Pattern
order: 4
---

# 약관 및 전체 동의 아코디언 패턴 (Agreement & Terms Pattern)

금융 상품 가입, 대출 심사, 카드 발급 등 법적 고지 및 서약 절차에서 사용되는 **약관 및 전체 동의(Agreement Terms)** 복합 패턴입니다. 마스터 전체 동의 체크박스 카드, 필수/선택 하위 체크리스트, 그리고 약관 전문 보기 링크 트리거로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 상단의 <strong>[약관에 전체 동의합니다]</strong>를 체크하면 하위 항목들이 일괄 선택/해제되며 하단 가입 버튼이 활성화됩니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card" style="max-width:440px; margin:0 auto;">
      <!-- Master Agreement Box -->
      <div onclick="toggleAllTerms()" style="background:#F2F8FF; border:1px solid #BFDBFD; border-radius:14px; padding:16px 18px; display:flex; align-items:center; gap:12px; cursor:pointer; margin-bottom:16px; transition:all 0.15s ease;">
        <input type="checkbox" id="master-terms-cb" style="width:20px; height:20px; accent-color:#0064FF; cursor:pointer;" onclick="event.stopPropagation(); toggleAllTerms();" />
        <label for="master-terms-cb" style="font-size:16px; font-weight:800; color:#0064FF; cursor:pointer;">약관에 전체 동의합니다</label>
      </div>

      <!-- Child Terms List -->
      <div style="display:flex; flex-direction:column; gap:12px; padding:0 6px; margin-bottom:24px;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <label style="display:flex; align-items:center; gap:10px; cursor:pointer;">
            <input type="checkbox" class="child-term-cb" data-required="true" onchange="checkTermsState()" style="width:18px; height:18px; accent-color:#0064FF;" />
            <span style="font-size:14px; color:#191F28;"><span style="color:#0064FF; font-weight:700;">[필수]</span> 토스뱅크 금융거래 기본약관</span>
          </label>
          <span onclick="alert('금융거래 기본약관 전문 모달을 호출합니다.');" style="font-size:12px; color:#8B95A1; cursor:pointer;">보기 &gt;</span>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center;">
          <label style="display:flex; align-items:center; gap:10px; cursor:pointer;">
            <input type="checkbox" class="child-term-cb" data-required="true" onchange="checkTermsState()" style="width:18px; height:18px; accent-color:#0064FF;" />
            <span style="font-size:14px; color:#191F28;"><span style="color:#0064FF; font-weight:700;">[필수]</span> 개인정보 수집 및 이용 동의</span>
          </label>
          <span onclick="alert('개인정보 수집 및 이용 동의 전문 모달을 호출합니다.');" style="font-size:12px; color:#8B95A1; cursor:pointer;">보기 &gt;</span>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center;">
          <label style="display:flex; align-items:center; gap:10px; cursor:pointer;">
            <input type="checkbox" class="child-term-cb" data-required="false" onchange="checkTermsState()" style="width:18px; height:18px; accent-color:#0064FF;" />
            <span style="font-size:14px; color:#191F28;"><span style="color:#8B95A1; font-weight:600;">[선택]</span> 혜택 정보 및 이벤트 알림 수신</span>
          </label>
          <span onclick="alert('혜택 정보 수신 동의 전문 모달을 호출합니다.');" style="font-size:12px; color:#8B95A1; cursor:pointer;">보기 &gt;</span>
        </div>
      </div>

      <!-- Action Button -->
      <button id="terms-submit-btn" disabled style="width:100%; background:#D1D6DB; color:#FFFFFF; border:none; padding:15px; border-radius:14px; font-size:16px; font-weight:800; cursor:not-allowed; transition:all 0.2s ease;">동의하고 계속하기</button>

      <script>
        function toggleAllTerms() {
          const master = document.getElementById('master-terms-cb');
          master.checked = !master.checked;
          document.querySelectorAll('.child-term-cb').forEach(cb => cb.checked = master.checked);
          checkTermsState();
        }
        function checkTermsState() {
          const cbs = Array.from(document.querySelectorAll('.child-term-cb'));
          const reqCbs = cbs.filter(cb => cb.dataset.required === 'true');
          const allRequired = reqCbs.every(cb => cb.checked);
          const allChecked = cbs.every(cb => cb.checked);
          document.getElementById('master-terms-cb').checked = allChecked;
          
          const submitBtn = document.getElementById('terms-submit-btn');
          if (allRequired) {
            submitBtn.disabled = false;
            submitBtn.style.background = '#0064FF';
            submitBtn.style.cursor = 'pointer';
            submitBtn.style.boxShadow = '0 4px 14px rgba(0,100,255,0.25)';
          } else {
            submitBtn.disabled = true;
            submitBtn.style.background = '#D1D6DB';
            submitBtn.style.cursor = 'not-allowed';
            submitBtn.style.boxShadow = 'none';
          }
        }
      </script>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Master Selection Card</strong>: 14px <code>Medium</code> 스쿼클 코너의 프라이머리 틴트 박스</li>
    <li><strong>Checkbox Atoms</strong>: 브랜드 블루(<code>#0064FF</code>) 액센트 컬러가 적용된 20px 터치 체크박스</li>
    <li><strong>Typography</strong>: 필수/선택 뱃지 라벨링 및 14px 서브 텍스트</li>
    <li><strong>State-Bound Button</strong>: 필수 약관 충족 조건에 따라 연동되는 비활성/활성 상태 전환 버튼</li>
  </ul>
</div>
