---
name: Overview
title: Pattern Library Overview
order: 0
---

# 토스 디자인 시스템 복합 패턴 라이브러리 (TDS Pattern Library)

토스 상용 앱(`viva.republica.toss.apk`)의 실제 서비스 화면에서 가장 빈번하게 사용되는 원자 단위 컴포넌트(Button, TextField, Checkbox, Dialog 등)의 결합체인 **8대 실전 금융 복합 패턴(Molecules & Organisms)** 라이브러리입니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>🧩 복합 패턴 아키텍처:</strong> 토스의 UI는 개별 컴포넌트 단위가 아니라 일관된 사용자 경험과 터치 플로우를 보장하는 '패턴' 단위로 조립됩니다. 각 패턴 카드를 클릭하면 상세 명세와 실시간 동작 샌드박스로 이동합니다.
  </div>

  <div class="tb-pattern-grid">
    <!-- 1. Account Row -->
    <a href="/patterns/account-row/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Molecule · 금융 자산</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">1. 계좌 및 자산 목록 행 (Account Row)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">은행 로고 + 계좌명/번호 + 잔액(tnum 볼드) + 송금 Pill 버튼 결합 패턴.</p>
      <div style="background:#F6F7F9; border-radius:12px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
        <div style="display:flex; align-items:center; gap:10px;">
          <div style="width:36px; height:36px; border-radius:50%; background:#0064FF; color:#FFF; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:13px;">T</div>
          <div><div style="font-size:13px; font-weight:700; color:#191F28;">토스뱅크 통장</div><div style="font-size:11px; color:#8B95A1;">1000-01-234567</div></div>
        </div>
        <div style="text-align:right;"><span style="font-size:14px; font-weight:700; color:#191F28;" class="tnum">3,842,000원</span></div>
      </div>
    </a>
    <!-- 2. Bottom Sheet -->
    <a href="/patterns/bottom-sheet/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Organism · 모달 액션</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">2. 바텀시트 확인 모달 (Bottom Sheet)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">상단 드래그 핸들 + 핵심 요약 카드 + 2단 확인 액션 버튼 결합 패턴.</p>
      <div style="background:#F6F7F9; border-radius:12px; padding:12px; text-align:center;">
        <div style="width:36px; height:4px; background:#D1D6DB; border-radius:2px; margin:0 auto 10px auto;"></div>
        <div style="font-size:13px; font-weight:700; color:#191F28; margin-bottom:8px;">정말 송금하시겠습니까?</div>
        <div style="background:#0064FF; color:#FFF; border-radius:8px; padding:6px; font-size:12px; font-weight:700;">확인</div>
      </div>
    </a>
    <!-- 3. Keypad Transfer -->
    <a href="/patterns/keypad-transfer/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Organism · 송금 플로우</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">3. 금액 송금 & 키패드 (Keypad Transfer)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">초대형 금액 인풋 + 단위 치환 퀵 칩(+1만, +5만) + 3x4 가상 키패드.</p>
      <div style="background:#F6F7F9; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:18px; font-weight:800; color:#0064FF;" class="tnum">50,000원</div>
        <div style="display:flex; justify-content:center; gap:6px; margin-top:8px;"><span style="font-size:10px; background:#FFF; border:1px solid #D1D6DB; padding:2px 6px; border-radius:4px;">+1만</span><span style="font-size:10px; background:#FFF; border:1px solid #D1D6DB; padding:2px 6px; border-radius:4px;">+5만</span><span style="font-size:10px; background:#FFF; border:1px solid #D1D6DB; padding:2px 6px; border-radius:4px;">전액</span></div>
      </div>
    </a>
    <!-- 4. Agreement Terms -->
    <a href="/patterns/agreement-terms/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Molecule · 필수 서약</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">4. 약관 및 전체 동의 (Agreement Terms)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">전체 동의 마스터 체크박스 + 필수/선택 하위 체크리스트 + 상세 드로어.</p>
      <div style="background:#F6F7F9; border-radius:12px; padding:12px;">
        <div style="font-size:12px; font-weight:700; color:#0064FF; margin-bottom:4px;">✓ 약관에 전체 동의합니다</div>
        <div style="font-size:11px; color:#6B7684;">[필수] 금융거래 기본약관 ></div>
      </div>
    </a>
    <!-- 5. Transaction Timeline -->
    <a href="/patterns/transaction-list/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Organism · 거래 내역</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">5. 거래내역 타임라인 (Transaction Timeline)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">날짜 헤더 + 가맹점 아이콘 + 거래 내역명 + 입출금 컬러 분기(-빨강, +파랑).</p>
      <div style="background:#F6F7F9; border-radius:12px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
        <div><div style="font-size:12px; font-weight:700; color:#191F28;">스타벅스 강남점</div><div style="font-size:10px; color:#8B95A1;">11.15 14:20</div></div>
        <div style="font-size:13px; font-weight:700; color:#EF3341;" class="tnum">-6,500원</div>
      </div>
    </a>
    <!-- 6. Notice Banner -->
    <a href="/patterns/notice-banner/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Molecule · 인라인 배너</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">6. 인라인 알림 및 혜택 배너 (Notice Banner)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">그래픽/아이콘 + 2줄 가변 텍스트 + 액션 버튼 + 닫기(X) 컨트롤.</p>
      <div style="background:#E8F3FF; border-radius:12px; padding:12px; display:flex; align-items:center; gap:8px;">
        <span style="font-size:16px;">🎁</span>
        <div style="font-size:11px; font-weight:700; color:#0064FF;">지금 토스뱅크 카드 쓰면 캐시백 혜택</div>
      </div>
    </a>
    <!-- 7. Filter Chip Bar -->
    <a href="/patterns/filter-chip-bar/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Molecule · 탐색 필터</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">7. 수평 스크롤 필터 칩 바 (Filter Chip Bar)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">수평 스크롤 칩 그룹 + 정렬 필터 드롭다운 + 카운트 배지 결합.</p>
      <div style="background:#F6F7F9; border-radius:12px; padding:12px; display:flex; gap:6px; overflow:hidden;">
        <span style="font-size:11px; background:#0064FF; color:#FFF; padding:4px 8px; border-radius:12px; font-weight:700;">전체 12</span>
        <span style="font-size:11px; background:#FFF; border:1px solid #D1D6DB; padding:4px 8px; border-radius:12px;">입금</span>
        <span style="font-size:11px; background:#FFF; border:1px solid #D1D6DB; padding:4px 8px; border-radius:12px;">출금</span>
      </div>
    </a>
    <!-- 8. Result Feedback -->
    <a href="/patterns/result-feedback/" class="tb-pattern-card">
      <span class="tb-pattern-badge">Organism · 피드백 결과</span>
      <h3 style="margin:4px 0 8px 0; font-size:18px; font-weight:700; color:#191F28;">8. 송금 완료 결과 피드백 (Result Feedback)</h3>
      <p style="font-size:13px; color:#6B7684; margin:0 0 16px 0; line-height:1.4;">3D 축하 일러스트 + 상태 타이틀 + 영수증 Key-Value 테이블 + 와이드 CTA.</p>
      <div style="background:#F6F7F9; border-radius:12px; padding:12px; text-align:center;">
        <span style="font-size:20px;">🎉</span>
        <div style="font-size:12px; font-weight:800; color:#191F28; margin:4px 0;">송금을 완료했어요</div>
        <div style="font-size:11px; color:#8B95A1;" class="tnum">홍길동님께 50,000원</div>
      </div>
    </a>
  </div>
</div>
