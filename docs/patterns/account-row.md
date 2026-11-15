---
name: 1. Account Row
title: Account & Asset Row Pattern
order: 1
---

# 계좌 및 자산 목록 행 패턴 (Account & Asset Row Pattern)

토스뱅크 홈 화면 및 자산 탭의 핵심 기본 단위인 **계좌 및 자산 목록 행(Account Row)** 복합 패턴입니다. 은행 심볼 로고, 계좌명, 마스킹된 계좌번호, 그리고 `Toss Product Sans`의 `tnum` 속성이 적용된 잔액과 우측 송금 Pill 버튼으로 구성됩니다.

<div class="tb-visual-container kb-visual-container">
  <div class="tb-section-intro kb-section-intro">
    <strong>인터랙티브 라이브 데모:</strong> 우측 <strong>[송금]</strong> 버튼을 누르면 송금 금액 모달 시뮬레이션 인터랙션을 확인할 수 있습니다.
  </div>

  <div class="tb-pattern-container">
    <div class="tb-pattern-demo-card">
      <div style="font-size:12px; font-weight:700; color:#8B95A1; margin-bottom:12px; text-transform:uppercase;">토스뱅크 입출금 통장 행</div>
      <div style="background:#FFFFFF; border:1px solid #E5E8EB; border-radius:18px; padding:16px 20px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
        <div style="display:flex; align-items:center; gap:14px;">
          <div style="width:44px; height:44px; border-radius:50%; background:#0064FF; color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:16px; box-shadow:0 2px 8px rgba(0,100,255,0.25);">T</div>
          <div>
            <div style="font-size:15px; font-weight:700; color:#191F28;">토스뱅크 통장</div>
            <div style="font-size:12px; color:#8B95A1; margin-top:2px;">토스 1000-01-234567</div>
          </div>
        </div>
        <div style="display:flex; align-items:center; gap:16px;">
          <div style="text-align:right;">
            <div style="font-size:17px; font-weight:800; color:#191F28;" class="tnum">3,842,000원</div>
          </div>
          <button onclick="alert('토스뱅크 통장 송금 화면으로 이동합니다.')" style="background:#E8F3FF; color:#0064FF; border:none; padding:8px 16px; border-radius:9999px; font-size:13px; font-weight:700; cursor:pointer; transition:all 0.15s ease;">송금</button>
        </div>
      </div>

      <div style="margin-top:12px; background:#FFFFFF; border:1px solid #E5E8EB; border-radius:18px; padding:16px 20px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
        <div style="display:flex; align-items:center; gap:14px;">
          <div style="width:44px; height:44px; border-radius:50%; background:#1F9D6F; color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:16px; box-shadow:0 2px 8px rgba(31,157,111,0.25);">K</div>
          <div>
            <div style="font-size:15px; font-weight:700; color:#191F28;">KB국민 마이핏통장</div>
            <div style="font-size:12px; color:#8B95A1; margin-top:2px;">국민 827102-01-382910</div>
          </div>
        </div>
        <div style="display:flex; align-items:center; gap:16px;">
          <div style="text-align:right;">
            <div style="font-size:17px; font-weight:800; color:#191F28;" class="tnum">1,250,400원</div>
          </div>
          <button onclick="alert('KB국민 마이핏통장 송금 화면으로 이동합니다.')" style="background:#E8F3FF; color:#0064FF; border:none; padding:8px 16px; border-radius:9999px; font-size:13px; font-weight:700; cursor:pointer; transition:all 0.15s ease;">송금</button>
        </div>
      </div>
    </div>
  </div>

  <h3>사용된 컴포넌트 조합 명세</h3>
  <ul>
    <li><strong>Avatar/Symbol Icon</strong>: 44px 원형 브랜드 서피스</li>
    <li><strong>Typography</strong>: 계좌명(T5 17px SemiBold), 계좌번호(C1 12px Regular), 잔액(T4 17px Bold, <code>tnum</code> 활성화)</li>
    <li><strong>Button</strong>: 32px Pill 높이의 <code>Full</code> 코너 래디우스 틴트 액션 버튼</li>
  </ul>
</div>
