---
name: 8. Result Feedback
title: Transaction Result & Feedback Pattern
order: 8
---

# 송금 완료 및 피드백 결과 패턴 (Transaction Result Feedback Pattern)

송금, 대출 신청, 계좌 개설, 카드 신청 등 금융 트랜잭션이 성공적으로 처리되었을 때 사용자에게 안도감과 명확한 처리 결과를 전달하는 **송금 완료 결과 피드백(Result Feedback)** 복합 패턴입니다. 3D 축하 그래픽 일러스트, 성공 타이틀 및 요약, 영수증 형태의 상세 Key-Value 테이블, 그리고 하단 와이드 CTA 버튼으로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 하단의 <strong>[확인]</strong> 버튼을 누르면 송금 완료 축하 피드백 애니메이션과 함께 초기 상태로 복귀합니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card" style="max-width:440px; margin:0 auto; text-align:center;">
      <!-- Hero Celebration Icon -->
      <div style="font-size:54px; margin:16px 0 12px 0;">🎉</div>
      <h2 style="font-size:24px; font-weight:800; color:#191F28; margin:0 0 8px 0;">50,000원을 보냈어요</h2>
      <p style="font-size:15px; color:#6B7684; margin:0 0 28px 0;">홍길동님께 성공적으로 전달되었습니다.</p>

      <!-- Receipt Key-Value Box -->
      <div style="background:#F6F7F9; border-radius:18px; padding:20px; text-align:left; margin-bottom:28px;">
        <div style="font-size:12px; font-weight:700; color:#8B95A1; margin-bottom:14px; text-transform:uppercase;">거래 상세 정보</div>
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
          <span style="font-size:14px; color:#6B7684;">받는 계좌</span>
          <span style="font-size:14px; font-weight:700; color:#191F28;">토스뱅크 1000-01-234567</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
          <span style="font-size:14px; color:#6B7684;">보낸 계좌</span>
          <span style="font-size:14px; font-weight:600; color:#191F28;">토스뱅크 통장</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
          <span style="font-size:14px; color:#6B7684;">거래 일시</span>
          <span style="font-size:14px; color:#191F28;">2026.11.15 22:05</span>
        </div>
        <div style="display:flex; justify-content:space-between; border-top:1px solid #E5E8EB; padding-top:12px;">
          <span style="font-size:14px; font-weight:700; color:#191F28;">송금 후 잔액</span>
          <span style="font-size:16px; font-weight:800; color:#0064FF;" class="tnum">3,792,000원</span>
        </div>
      </div>

      <!-- Action Button Group -->
      <div style="display:flex; flex-direction:column; gap:10px;">
        <button onclick="alert('송금 확인증 발급 화면으로 이동합니다.');" style="background:#F2F4F6; color:#191F28; border:none; padding:14px; border-radius:14px; font-size:15px; font-weight:700; cursor:pointer;">확인증 공유하기</button>
        <button onclick="alert('홈 화면으로 복귀합니다.');" style="background:#0064FF; color:#FFFFFF; border:none; padding:15px; border-radius:14px; font-size:16px; font-weight:800; cursor:pointer; box-shadow:0 4px 14px rgba(0,100,255,0.25);">확인</button>
      </div>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Celebration Hero Graphic</strong>: 54px 크기의 성공 상태 시각화</li>
    <li><strong>Receipt Box</strong>: 18px <code>Large</code> 스쿼클 코너의 뉴트럴 서피스 컨테이너</li>
    <li><strong>Key-Value Ledger</strong>: 명확한 정렬선과 <code>tnum</code> 잔액 표기</li>
    <li><strong>Dual Action CTA</strong>: 14px 코너 52px 높이의 확인 및 공유 버튼 스택</li>
  </ul>
</div>
