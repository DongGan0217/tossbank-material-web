---
name: 3. Keypad Transfer
title: Keypad & Transfer Input Pattern
order: 3
---

# 금액 송금 및 가상 키패드 패턴 (Keypad & Transfer Input Pattern)

토스 서비스의 정체성을 가장 직관적으로 보여주는 **금액 송금 및 가상 키패드(Keypad Transfer)** 복합 패턴입니다. 한글 단위 실시간 치환이 포함된 대형 금액 디스플레이, 빠른 단위 증액 칩(+1만, +5만, 전액), 그리고 3x4 가상 햅틱 숫자 키패드로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 아래 가상 키패드의 숫자 버튼이나 퀵 칩을 누르면 실제 토스 앱처럼 금액이 실시간 누적 계산되어 디스플레이에 반영됩니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card" style="max-width:380px; margin:0 auto;">
      <!-- Amount Display Area -->
      <div style="text-align:center; padding:24px 16px 16px 16px;">
        <span style="font-size:13px; color:#8B95A1;">송금할 금액을 입력해주세요</span>
        <div id="transfer-display-val" style="font-size:36px; font-weight:900; color:#191F28; margin:12px 0 6px 0;" class="tnum">0원</div>
        <div id="transfer-korean-val" style="font-size:13px; font-weight:700; color:#0064FF; min-height:18px;">영원</div>
      </div>

      <!-- Quick Chips Bar -->
      <div style="display:flex; justify-content:center; gap:8px; margin-bottom:20px;">
        <button onclick="addAmount(10000)" style="background:#F2F4F6; color:#191F28; border:none; padding:6px 14px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">+1만</button>
        <button onclick="addAmount(50000)" style="background:#F2F4F6; color:#191F28; border:none; padding:6px 14px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">+5만</button>
        <button onclick="addAmount(100000)" style="background:#F2F4F6; color:#191F28; border:none; padding:6px 14px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">+10만</button>
        <button onclick="setAmount(3842000)" style="background:#E8F3FF; color:#0064FF; border:none; padding:6px 14px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">전액</button>
      </div>

      <!-- 3x4 Virtual Keypad -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; margin-bottom:16px;">
        <button onclick="pressKey('1')" class="keypad-btn">1</button>
        <button onclick="pressKey('2')" class="keypad-btn">2</button>
        <button onclick="pressKey('3')" class="keypad-btn">3</button>
        <button onclick="pressKey('4')" class="keypad-btn">4</button>
        <button onclick="pressKey('5')" class="keypad-btn">5</button>
        <button onclick="pressKey('6')" class="keypad-btn">6</button>
        <button onclick="pressKey('7')" class="keypad-btn">7</button>
        <button onclick="pressKey('8')" class="keypad-btn">8</button>
        <button onclick="pressKey('9')" class="keypad-btn">9</button>
        <button onclick="pressKey('00')" class="keypad-btn">00</button>
        <button onclick="pressKey('0')" class="keypad-btn">0</button>
        <button onclick="pressKey('del')" class="keypad-btn">←</button>
      </div>

      <!-- Send Action Button -->
      <button id="send-cta-btn" onclick="if(currentAmount>0) alert(currentAmount.toLocaleString() + '원 송금을 시작합니다.');" style="width:100%; background:#0064FF; color:#FFFFFF; border:none; padding:15px; border-radius:14px; font-size:16px; font-weight:800; cursor:pointer; box-shadow:0 4px 14px rgba(0,100,255,0.25);">다음</button>

      <script>
        let currentAmount = 0;
        function updateDisplay() {
          const display = document.getElementById('transfer-display-val');
          const korDisplay = document.getElementById('transfer-korean-val');
          display.innerText = currentAmount.toLocaleString() + '원';
          display.style.color = currentAmount > 0 ? '#0064FF' : '#191F28';
          if (currentAmount === 0) {
            korDisplay.innerText = '영원';
          } else if (currentAmount >= 10000) {
            const man = Math.floor(currentAmount / 10000);
            const remainder = currentAmount % 10000;
            korDisplay.innerText = man + '만 ' + (remainder > 0 ? remainder.toLocaleString() + '원' : '원');
          } else {
            korDisplay.innerText = currentAmount.toLocaleString() + '원';
          }
        }
        function addAmount(val) { currentAmount += val; updateDisplay(); }
        function setAmount(val) { currentAmount = val; updateDisplay(); }
        function pressKey(k) {
          if (k === 'del') {
            currentAmount = Math.floor(currentAmount / 10);
          } else {
            let str = (currentAmount === 0 ? '' : currentAmount.toString()) + k;
            if (str.length > 10) return;
            currentAmount = parseInt(str, 10) || 0;
          }
          updateDisplay();
        }
      </script>
      <style>
        .keypad-btn {
          background: #FFFFFF;
          border: 1px solid #E5E8EB;
          border-radius: 12px;
          height: 52px;
          font-size: 20px;
          font-weight: 700;
          color: #191F28;
          cursor: pointer;
          transition: background 0.1s ease;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .keypad-btn:active { background: #E9EBED; }
      </style>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Hero Typography</strong>: 36px/46px의 초대형 금액 표시 및 <code>tnum</code>(타뷸라 넘버) 강제 적용</li>
    <li><strong>Quick Chips</strong>: 8px 코너의 수평 증액 컨트롤러 칩 세트</li>
    <li><strong>Numeric Keypad</strong>: 52px 터치 타깃 규격을 준수하는 3x4 햅틱 터치 버튼 그리드</li>
    <li><strong>Primary Wide CTA</strong>: 하단 고정형 14px 스쿼클 코너 54px 높이 버튼</li>
  </ul>
</div>
