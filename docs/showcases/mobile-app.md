<!-- catalog-only-start --><!-- ---
name: 2. Mobile App
title: 토스뱅크 모바일 앱 시뮬레이터
order: 3
-----><!-- catalog-only-end -->

# 2. 토스뱅크 모바일 앱 쇼케이스 (Mobile App Simulator)

`@tossbank/material-web` 컴포넌트로 구현된 **iPhone 16 Pro 모바일 뱅킹 앱 시뮬레이터**입니다. 토스뱅크 홈 화면 피드, "지금 이자받기" 실시간 수령 인터랙션, 5대 듀얼톤 체크카드 스위처를 인터랙티브하게 체험할 수 있습니다.

<div class="tb-visual-container kb-visual-container" style="display: flex; justify-content: center; padding: 20px 0;">
  <!-- iPhone 16 Pro Frame -->
  <div style="width: 380px; height: 760px; background: #000000; border-radius: 52px; padding: 12px; box-shadow: 0 25px 60px rgba(0,0,0,0.35); position: relative; border: 4px solid #333D4B;">
    <!-- Dynamic Island -->
    <div style="position: absolute; top: 22px; left: 50%; transform: translateX(-50%); width: 110px; height: 28px; background: #000000; border-radius: 20px; z-index: 100; display: flex; align-items: center; justify-content: flex-end; padding-right: 12px;">
      <div style="width: 10px; height: 10px; border-radius: 50%; background: #0064FF;"></div>
    </div>

    <!-- Screen Content -->
    <div style="width: 100%; height: 100%; background: #F2F4F6; border-radius: 42px; overflow-y: auto; overflow-x: hidden; position: relative; padding: 56px 16px 24px 16px; box-sizing: border-box; font-family: -apple-system, Pretendard, sans-serif;">
      
      <!-- Top App Bar in App -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <span style="font-size: 20px; font-weight: 800; color: #191F28; letter-spacing: -0.02em;">토스뱅크</span>
        <div style="display: flex; gap: 8px;">
          <button style="background: none; border: none; font-size: 18px; cursor: pointer;">🔔</button>
          <button style="background: none; border: none; font-size: 18px; cursor: pointer;">⚙️</button>
        </div>
      </div>

      <!-- Main Account Card -->
      <div style="background: #FFFFFF; border-radius: 20px; padding: 20px; margin-bottom: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <span style="font-size: 13px; color: #4E5968; font-weight: 600;">토스뱅크 통장</span>
          <button onclick="toggleBalance()" style="background: none; border: none; font-size: 12px; color: #8B95A1; cursor: pointer;">숨기기</button>
        </div>
        <div id="app-balance" style="font-size: 26px; font-weight: 800; color: #191F28; letter-spacing: -0.02em; margin-bottom: 16px;">
          4,852,190원
        </div>
        <div style="display: flex; gap: 8px;">
          <button onclick="alert('송금 화면으로 이동합니다.')" style="flex: 1; background: #F2F4F6; color: #191F28; font-size: 14px; font-weight: 700; padding: 10px 0; border-radius: 12px; border: none; cursor: pointer;">송금</button>
          <button onclick="claimInterest()" style="flex: 1.3; background: #0064FF; color: #FFFFFF; font-size: 14px; font-weight: 800; padding: 10px 0; border-radius: 12px; border: none; cursor: pointer; box-shadow: 0 4px 10px rgba(0,100,255,0.25);">
            ⚡ 지금 이자받기 (<span id="unclaimed-interest">1,420</span>원)
          </button>
        </div>
      </div>

      <!-- Dual-Tone Checkcard Preview -->
      <div style="background: #FFFFFF; border-radius: 20px; padding: 20px; margin-bottom: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <span style="font-size: 14px; font-weight: 700; color: #191F28;">토스뱅크 체크카드</span>
          <span style="font-size: 12px; color: #0064FF; font-weight: 700;">혜택 보기</span>
        </div>
        
        <!-- Interactive Card Visual -->
        <div id="checkcard-visual" style="height: 140px; border-radius: 16px; background: linear-gradient(135deg, #0064FF 50%, #FFE100 50%); padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; color: #FFFFFF; box-shadow: 0 8px 18px rgba(0,0,0,0.12); transition: all 0.3s ease;">
          <div style="display: flex; justify-content: space-between; font-weight: 800; font-size: 13px;">
            <span>toss bank</span>
            <span style="font-size: 11px; opacity: 0.85;">체크카드</span>
          </div>
          <div>
            <div style="font-size: 11px; opacity: 0.8; letter-spacing: 0.05em;">IC CHIP</div>
            <div style="font-size: 14px; font-weight: 700; letter-spacing: 0.1em; margin-top: 4px;">•••• 8291</div>
          </div>
        </div>

        <!-- Color Palette Swapper -->
        <div style="display: flex; justify-content: center; gap: 8px; margin-top: 14px;">
          <button onclick="setCardColor('linear-gradient(135deg, #0064FF 50%, #FFE100 50%)')" style="width: 22px; height: 22px; border-radius: 50%; background: #0064FF; border: 2px solid #FFFFFF; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.2);" title="레몬블루"></button>
          <button onclick="setCardColor('linear-gradient(135deg, #FF3B70 50%, #191F28 50%)')" style="width: 22px; height: 22px; border-radius: 50%; background: #FF3B70; border: 2px solid #FFFFFF; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.2);" title="나이트핑크"></button>
          <button onclick="setCardColor('linear-gradient(135deg, #FF6B00 50%, #F9FAFB 50%)')" style="width: 22px; height: 22px; border-radius: 50%; background: #FF6B00; border: 2px solid #FFFFFF; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.2);" title="오렌지밀크"></button>
          <button onclick="setCardColor('linear-gradient(135deg, #7B2CBF 50%, #20BF6B 50%)')" style="width: 22px; height: 22px; border-radius: 50%; background: #7B2CBF; border: 2px solid #FFFFFF; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,0.2);" title="퍼플그린"></button>
        </div>
      </div>

      <!-- Recent Transactions List -->
      <div style="background: #FFFFFF; border-radius: 20px; padding: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
        <div style="font-size: 14px; font-weight: 700; color: #191F28; margin-bottom: 14px;">최근 거래 내역</div>
        
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #F2F4F6;">
          <div>
            <div style="font-size: 14px; font-weight: 700; color: #191F28;">스타벅스 코리아</div>
            <div style="font-size: 11px; color: #8B95A1;">오늘 14:22 · 체크카드</div>
          </div>
          <div style="font-size: 14px; font-weight: 800; color: #191F28;">-4,500원</div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #F2F4F6;">
          <div>
            <div style="font-size: 14px; font-weight: 700; color: #0064FF;">토스뱅크 지금 이자받기</div>
            <div style="font-size: 11px; color: #8B95A1;">오늘 09:00 · 일일이자</div>
          </div>
          <div style="font-size: 14px; font-weight: 800; color: #0064FF;">+1,420원</div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0;">
          <div>
            <div style="font-size: 14px; font-weight: 700; color: #191F28;">쿠팡 결제</div>
            <div style="font-size: 11px; color: #8B95A1;">어제 21:15 · 체크카드</div>
          </div>
          <div style="font-size: 14px; font-weight: 800; color: #191F28;">-28,900원</div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
let balanceVal = 4852190;
let isHidden = false;

function toggleBalance() {
  const el = document.getElementById('app-balance');
  isHidden = !isHidden;
  el.innerText = isHidden ? '•••••••원' : balanceVal.toLocaleString() + '원';
}

function claimInterest() {
  const unclaimed = parseInt(document.getElementById('unclaimed-interest').innerText.replace(/,/g, ''), 10);
  if (unclaimed === 0) {
    alert('오늘 받을 수 있는 이자를 이미 모두 수령하셨습니다!');
    return;
  }
  balanceVal += unclaimed;
  document.getElementById('app-balance').innerText = balanceVal.toLocaleString() + '원';
  document.getElementById('unclaimed-interest').innerText = '0';
  alert('🎉 축하합니다! ' + unclaimed.toLocaleString() + '원의 이자가 통장에 즉시 입금되었습니다.');
}

function setCardColor(gradient) {
  document.getElementById('checkcard-visual').style.background = gradient;
}
</script>
