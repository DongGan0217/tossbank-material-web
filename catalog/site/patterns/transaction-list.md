---
name: 5. Transaction List
title: Transaction Timeline Pattern
order: 5
---

# 거래내역 타임라인 패턴 (Transaction Timeline Pattern)

토스 통장 및 카드 거래내역 조회의 핵심 사용자 인터페이스인 **거래내역 타임라인(Transaction Timeline)** 복합 패턴입니다. 일자별 구분 헤더, 가맹점/수취인 카테고리 아이콘, 거래 시간 및 유형, 그리고 입출금 컬러 분기(-빨강, +파랑)와 최종 잔액 표시로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 거래내역 항목을 클릭하면 상세 영수증 정보를 확인할 수 있습니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card" style="max-width:440px; margin:0 auto;">
      <!-- Date Header 1 -->
      <div style="font-size:13px; font-weight:700; color:#8B95A1; padding:8px 4px; border-bottom:1px solid #F2F4F6;">오늘 · 11월 15일</div>

      <!-- Item 1 -->
      <div onclick="alert('스타벅스 강남점 거래상세 영수증을 호출합니다.');" style="display:flex; justify-content:space-between; align-items:center; padding:14px 4px; border-bottom:1px solid #F2F4F6; cursor:pointer;">
        <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:40px; height:40px; border-radius:50%; background:#FFF0F0; color:#EF3341; display:flex; align-items:center; justify-content:center; font-size:18px;">☕</div>
          <div>
            <div style="font-size:15px; font-weight:700; color:#191F28;">스타벅스 강남점</div>
            <div style="font-size:12px; color:#8B95A1; margin-top:2px;">14:32 · 체크카드 승인</div>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:16px; font-weight:800; color:#EF3341;" class="tnum">-6,500원</div>
          <div style="font-size:12px; color:#8B95A1; margin-top:2px;" class="tnum">잔액 3,842,000원</div>
        </div>
      </div>

      <!-- Item 2 -->
      <div onclick="alert('김토스 입금 거래상세 영수증을 호출합니다.');" style="display:flex; justify-content:space-between; align-items:center; padding:14px 4px; border-bottom:1px solid #F2F4F6; cursor:pointer;">
        <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:40px; height:40px; border-radius:50%; background:#E8F3FF; color:#0064FF; display:flex; align-items:center; justify-content:center; font-size:18px;">💸</div>
          <div>
            <div style="font-size:15px; font-weight:700; color:#191F28;">김토스</div>
            <div style="font-size:12px; color:#8B95A1; margin-top:2px;">11:15 · 토스송금 입금</div>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:16px; font-weight:800; color:#0064FF;" class="tnum">+150,000원</div>
          <div style="font-size:12px; color:#8B95A1; margin-top:2px;" class="tnum">잔액 3,848,500원</div>
        </div>
      </div>

      <!-- Date Header 2 -->
      <div style="font-size:13px; font-weight:700; color:#8B95A1; padding:16px 4px 8px 4px; border-bottom:1px solid #F2F4F6;">어제 · 11월 14일</div>

      <!-- Item 3 -->
      <div onclick="alert('GS25 편의점 거래상세 영수증을 호출합니다.');" style="display:flex; justify-content:space-between; align-items:center; padding:14px 4px; cursor:pointer;">
        <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:40px; height:40px; border-radius:50%; background:#F2F4F6; color:#525355; display:flex; align-items:center; justify-content:center; font-size:18px;">🏪</div>
          <div>
            <div style="font-size:15px; font-weight:700; color:#191F28;">GS25 역삼디오빌점</div>
            <div style="font-size:12px; color:#8B95A1; margin-top:2px;">21:40 · 체크카드 승인</div>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:16px; font-weight:800; color:#EF3341;" class="tnum">-4,200원</div>
          <div style="font-size:12px; color:#8B95A1; margin-top:2px;" class="tnum">잔액 3,698,500원</div>
        </div>
      </div>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Category Avatar</strong>: 40px 원형의 파스텔 틴트 배경 카테고리 아이콘</li>
    <li><strong>Tabular Typography</strong>: <code>Toss Product Sans</code>의 <code>tnum</code> 고정폭 숫자로 우측 정렬선 일치 보장</li>
    <li><strong>Semantic Color Coding</strong>: 출금은 <code>red_600</code> (<code>#EF3341</code>), 입금은 <code>blue_600</code> (<code>#3182F6</code>) 실측 토큰 적용</li>
    <li><strong>Divider Header</strong>: 13px 볼드 뉴트럴 그레이 일자 헤딩</li>
  </ul>
</div>
