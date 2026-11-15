---
name: 6. Notice Banner
title: Inline Notice & Benefit Banner Pattern
order: 6
---

# 인라인 알림 및 혜택 배너 패턴 (Inline Notice & Benefit Banner Pattern)

토스 홈 화면, 통장 세부 화면, 송금 완료 후 추천 섹션 등에 인라인으로 자연스럽게 삽입되는 **인라인 알림 및 혜택 배너(Notice Banner)** 복합 패턴입니다. 3D 그래픽/아이콘 배지, 2줄 가변 텍스트(강조 타이틀 + 보조 설명), 액션 텍스트 버튼, 그리고 우측 닫기(Dismiss) 컨트롤로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 우측 <strong>[닫기(✕)]</strong> 버튼을 누르면 부드럽게 배너가 숨겨지며, [자세히 보기] 버튼을 누르면 상세 이벤트 모달 인터랙션을 시뮬레이션합니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card" style="max-width:500px; margin:0 auto;">
      <!-- Blue Promo Banner -->
      <div id="demo-banner-1" style="background:#E8F3FF; border:1px solid #D2E7FF; border-radius:18px; padding:18px 20px; display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; position:relative; box-shadow:0 2px 8px rgba(0,100,255,0.06);">
        <div style="display:flex; align-items:center; gap:14px;">
          <div style="font-size:28px;">🎁</div>
          <div>
            <div style="font-size:15px; font-weight:800; color:#0064FF;">지금 토스뱅크 카드 쓰면 캐시백 혜택</div>
            <div style="font-size:13px; color:#4E5968; margin-top:2px;">매달 최대 35,000원 돌려받으세요</div>
          </div>
        </div>
        <div style="display:flex; align-items:center; gap:12px;">
          <button onclick="alert('토스뱅크 체크카드 혜택 페이지로 이동합니다.');" style="background:#0064FF; color:#FFFFFF; border:none; padding:7px 14px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">보기</button>
          <span onclick="document.getElementById('demo-banner-1').style.display='none';" style="font-size:16px; color:#8B95A1; cursor:pointer; font-weight:700; padding:4px;">✕</span>
        </div>
      </div>

      <!-- Teal Investment Banner -->
      <div id="demo-banner-2" style="background:#F0F9F9; border:1px solid #D2F0F0; border-radius:18px; padding:18px 20px; display:flex; align-items:center; justify-content:space-between; position:relative;">
        <div style="display:flex; align-items:center; gap:14px;">
          <div style="font-size:28px;">📈</div>
          <div>
            <div style="font-size:15px; font-weight:800; color:#159999;">미국 국채 24시간 실시간 투자</div>
            <div style="font-size:13px; color:#4E5968; margin-top:2px;">환전 수수료 없이 달러로 바로 시작</div>
          </div>
        </div>
        <div style="display:flex; align-items:center; gap:12px;">
          <button onclick="alert('미국 국채 투자 안내 페이지로 이동합니다.');" style="background:#159999; color:#FFFFFF; border:none; padding:7px 14px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">시작</button>
          <span onclick="document.getElementById('demo-banner-2').style.display='none';" style="font-size:16px; color:#8B95A1; cursor:pointer; font-weight:700; padding:4px;">✕</span>
        </div>
      </div>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Squircle Surface</strong>: 18px <code>Large</code> 스쿼클 코너의 소프트 틴트 배경 카드</li>
    <li><strong>3D Emoji/Graphic</strong>: 직관적 인지성을 제공하는 28px 리치 그래픽 배지</li>
    <li><strong>Typography</strong>: 타이틀(T5 15px Bold) + 설명(B2 13px Regular)</li>
    <li><strong>Dismiss Control</strong>: 간편하게 숨길 수 있는 인라인 닫기 터치 타깃</li>
  </ul>
</div>
