<!-- catalog-only-start --><!-- ---
name: 1. Official Web
title: 토스뱅크 공식 웹 랜딩
order: 2
-----><!-- catalog-only-end -->

# 1. 토스뱅크 공식 웹 랜딩 쇼케이스 (Official Web)

`@tossbank/material-web` 컴포넌트로 구축된 **토스뱅크 대표 웹 서비스** 랜딩 페이지입니다. 시그니처 "지금 이자받기", "평생 무료 환전 외화통장", 그리고 실시간 이자 계산기 슬라이더와 계좌 개설 모달을 직접 체험해보세요.

<div class="tb-visual-container kb-visual-container">
  <!-- Hero Section -->
  <div style="background: linear-gradient(145deg, #0064FF 0%, #0047BB 100%); border-radius: 24px; padding: 48px 36px; color: #FFFFFF; box-shadow: 0 12px 32px rgba(0, 100, 255, 0.28); margin-bottom: 32px;">
    <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 9999px; font-size: 13px; font-weight: 700; margin-bottom: 16px; letter-spacing: -0.01em;">
      조건 없이 매일 받는 이자
    </div>
    <h2 style="font-size: 34px; font-weight: 800; line-height: 1.3; margin: 0 0 12px 0; letter-spacing: -0.03em;">
      토스뱅크 통장 하나로<br/>매일 바로 이자받기
    </h2>
    <p style="font-size: 16px; opacity: 0.9; margin: 0 0 28px 0; max-width: 520px; line-height: 1.5;">
      하루만 넣어도 연 2.0% (세전). 클릭 한 번으로 기다릴 필요 없이 오늘 쌓인 이자를 바로 통장에 입금받으세요.
    </p>
    <div style="display: flex; gap: 12px; flex-wrap: wrap;">
      <button onclick="document.getElementById('open-account-dialog').show()" style="background: #FFFFFF; color: #0064FF; font-weight: 800; font-size: 16px; padding: 14px 28px; border-radius: 16px; border: none; cursor: pointer; box-shadow: 0 4px 14px rgba(0,0,0,0.15); transition: transform 0.15s ease;">
        통장 개설하기 (1분 완료)
      </button>
      <button onclick="document.getElementById('interest-calc-section').scrollIntoView({behavior: 'smooth'})" style="background: rgba(255,255,255,0.15); color: #FFFFFF; font-weight: 700; font-size: 16px; padding: 14px 24px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.3); cursor: pointer;">
        이자 계산해보기 ▾
      </button>
    </div>
  </div>

  <!-- Interactive Interest Calculator -->
  <div id="interest-calc-section" style="background: var(--md-sys-color-surface, #FFFFFF); border: 1px solid var(--md-sys-color-outline-variant, #E5E8EB); border-radius: 20px; padding: 28px; margin-bottom: 32px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
      <div>
        <h3 style="margin: 0; font-size: 20px; font-weight: 800; color: #191F28;">💰 실시간 이자 계산기</h3>
        <p style="margin: 4px 0 0 0; font-size: 14px; color: #4E5968;">슬라이더를 움직여 예치 금액별 매일/매월 받는 이자를 확인하세요 (연 2.0% 기준).</p>
      </div>
      <div style="text-align: right;">
        <span style="font-size: 12px; color: #4E5968; font-weight: 600;">예치 금액</span>
        <div id="deposit-amount-display" style="font-size: 24px; font-weight: 800; color: #0064FF;">3,000만원</div>
      </div>
    </div>

    <input type="range" id="deposit-slider" min="100" max="10000" step="100" value="3000" style="width: 100%; accent-color: #0064FF; cursor: pointer; height: 8px; border-radius: 4px;" oninput="updateInterest(this.value)" />

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-top: 24px;">
      <div style="background: #F2F4F6; padding: 18px; border-radius: 16px;">
        <span style="font-size: 13px; color: #4E5968; font-weight: 600;">매일 받는 이자 (세전)</span>
        <div id="daily-interest" style="font-size: 22px; font-weight: 800; color: #191F28; margin-top: 4px;">약 1,643원</div>
      </div>
      <div style="background: #E8F3FF; padding: 18px; border-radius: 16px; border: 1px solid #BBDCFF;">
        <span style="font-size: 13px; color: #0047BB; font-weight: 700;">매월 모이는 이자 (세전)</span>
        <div id="monthly-interest" style="font-size: 22px; font-weight: 800; color: #0064FF; margin-top: 4px;">약 50,000원</div>
      </div>
      <div style="background: #FFF8CC; padding: 18px; border-radius: 16px;">
        <span style="font-size: 13px; color: #5C4900; font-weight: 700;">1년 복리 누적 (세전)</span>
        <div id="yearly-interest" style="font-size: 22px; font-weight: 800; color: #191F28; margin-top: 4px;">약 600,000원</div>
      </div>
    </div>
  </div>

  <!-- Key Products 4-Grid -->
  <h3 style="font-size: 22px; font-weight: 800; color: #191F28; margin-bottom: 16px;">토스뱅크 4대 핵심 프로덕트</h3>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
    <!-- 1. 통장 -->
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 20px; padding: 24px; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
      <div style="width: 44px; height: 44px; border-radius: 14px; background: #E8F3FF; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 16px;">🏦</div>
      <h4 style="margin: 0 0 6px 0; font-size: 17px; font-weight: 700; color: #191F28;">토스뱅크 통장</h4>
      <p style="margin: 0 0 16px 0; font-size: 13px; color: #4E5968; line-height: 1.4;">수시입출금 통장 하나로 아무 조건 없이 매일 이자받기 가능</p>
      <span style="color: #0064FF; font-weight: 800; font-size: 14px;">연 2.0% (세전)</span>
    </div>

    <!-- 2. 외화통장 -->
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 20px; padding: 24px; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
      <div style="width: 44px; height: 44px; border-radius: 14px; background: #E8F3FF; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 16px;">✈️</div>
      <h4 style="margin: 0 0 6px 0; font-size: 17px; font-weight: 700; color: #191F28;">외화통장</h4>
      <p style="margin: 0 0 16px 0; font-size: 13px; color: #4E5968; line-height: 1.4;">살 때도 팔 때도 평생 100% 무료 환전, 해외 결제 수수료 무료</p>
      <span style="color: #0064FF; font-weight: 800; font-size: 14px;">환전 수수료 0원</span>
    </div>

    <!-- 3. 굴비적금 -->
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 20px; padding: 24px; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
      <div style="width: 44px; height: 44px; border-radius: 14px; background: #FFF8CC; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 16px;">🐟</div>
      <h4 style="margin: 0 0 6px 0; font-size: 17px; font-weight: 700; color: #191F28;">굴비적금</h4>
      <p style="margin: 0 0 16px 0; font-size: 13px; color: #4E5968; line-height: 1.4;">저금할 때마다 밥상 위 굴비가 내려오는 재미있는 저축 습관</p>
      <span style="color: #0064FF; font-weight: 800; font-size: 14px;">최고 연 5.0% (세전)</span>
    </div>

    <!-- 4. 비상금대출 -->
    <div style="background: #FFFFFF; border: 1px solid #E5E8EB; border-radius: 20px; padding: 24px; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
      <div style="width: 44px; height: 44px; border-radius: 14px; background: #F2F4F6; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 16px;">⚡</div>
      <h4 style="margin: 0 0 6px 0; font-size: 17px; font-weight: 700; color: #191F28;">토스뱅크 비상금대출</h4>
      <p style="margin: 0 0 16px 0; font-size: 13px; color: #4E5968; line-height: 1.4;">직장·소득 상관없이 모바일로 1분 만에 최대 300만원 즉시 조회</p>
      <span style="color: #0064FF; font-weight: 800; font-size: 14px;">최저 연 4.8%</span>
    </div>
  </div>

  <!-- Account Open Dialog Modal (HTML Dialog) -->
  <dialog id="open-account-dialog" style="border: none; border-radius: 24px; padding: 28px; width: 90%; max-width: 420px; box-shadow: 0 20px 48px rgba(0,0,0,0.2); font-family: inherit;">
    <h3 style="margin: 0 0 8px 0; font-size: 20px; font-weight: 800; color: #191F28;">토스뱅크 통장 만들기</h3>
    <p style="margin: 0 0 20px 0; font-size: 14px; color: #4E5968; line-height: 1.4;">
      본인 명의 스마트폰과 신분증만 있으면 1분 안에 비대면 계좌 개설이 완료됩니다.
    </p>
    <div style="background: #F9FAFB; padding: 16px; border-radius: 16px; margin-bottom: 24px; font-size: 13px; color: #191F28; line-height: 1.6;">
      ✓ 금리: 연 2.0% (세전, 수시입출금)<br/>
      ✓ 이자 지급: 매일 "지금 이자받기" 클릭 시 즉시 지급<br/>
      ✓ 이체 수수료: 당행 및 타행 무제한 전액 면제
    </div>
    <div style="display: flex; gap: 10px; justify-content: flex-end;">
      <button onclick="document.getElementById('open-account-dialog').close()" style="background: #F2F4F6; color: #4E5968; font-weight: 700; font-size: 14px; padding: 10px 18px; border-radius: 12px; border: none; cursor: pointer;">취소</button>
      <button onclick="alert('신분증 비대면 인증 프로세스로 연결됩니다.'); document.getElementById('open-account-dialog').close();" style="background: #0064FF; color: #FFFFFF; font-weight: 800; font-size: 14px; padding: 10px 22px; border-radius: 12px; border: none; cursor: pointer;">개설 시작</button>
    </div>
  </dialog>
</div>

<script>
function updateInterest(val) {
  const amount = parseInt(val, 10);
  document.getElementById('deposit-amount-display').innerText = amount.toLocaleString() + '만원';
  const totalWon = amount * 10000;
  const rate = 0.02;
  const daily = Math.floor((totalWon * rate) / 365);
  const monthly = Math.floor(totalWon * rate / 12);
  const yearly = Math.floor(totalWon * rate);
  document.getElementById('daily-interest').innerText = '약 ' + daily.toLocaleString() + '원';
  document.getElementById('monthly-interest').innerText = '약 ' + monthly.toLocaleString() + '원';
  document.getElementById('yearly-interest').innerText = '약 ' + yearly.toLocaleString() + '원';
}
</script>
