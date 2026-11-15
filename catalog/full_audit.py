import asyncio
import json
import re
from playwright.async_api import async_playwright

BASE_URL = "http://localhost:8086"

ROUTES = [
    # Main
    "/",
    # About (5)
    "/about/intro/",
    "/about/quick-start/",
    "/about/roadmap/",
    "/about/size/",
    "/about/support/",
    # Theming (4)
    "/theming/material-theming/",
    "/theming/color/",
    "/theming/shape/",
    "/theming/typography/",
    # Components (20)
    "/components/overview/",
    "/components/button/",
    "/components/checkbox/",
    "/components/chips/",
    "/components/dialog/",
    "/components/divider/",
    "/components/elevation/",
    "/components/fab/",
    "/components/focus-ring/",
    "/components/icon/",
    "/components/icon-button/",
    "/components/list/",
    "/components/menu/",
    "/components/progress/",
    "/components/radio/",
    "/components/ripple/",
    "/components/select/",
    "/components/slider/",
    "/components/switch/",
    "/components/tabs/",
    "/components/text-field/",
    # Assets (1)
    "/assets/images/",
    # Showcases (5)
    "/showcases/",
    "/showcases/official-web/",
    "/showcases/mobile-app/",
    "/showcases/backoffice/",
    "/showcases/pms/",
    # Backward-compatible Redirect Routes (2)
    "/showcase/remittance.html",
    "/assets/icon-library.html",
]

async def audit():
    results = []
    total_routes = len(ROUTES)
    passed_routes = 0
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        
        for route in ROUTES:
            url = f"{BASE_URL}{route}"
            page = await context.new_page()
            
            failed_requests = []
            console_errors = []
            
            page.on("requestfailed", lambda req: failed_requests.append({
                "url": req.url,
                "failure": req.failure
            }))
            
            def handle_response(res):
                if res.status >= 400:
                    failed_requests.append({
                        "url": res.url,
                        "status": res.status,
                        "status_text": res.status_text
                    })
            page.on("response", handle_response)
            
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            http_status = None
            try:
                resp = await page.goto(url, wait_until="networkidle", timeout=12000)
                http_status = resp.status if resp else None
            except Exception as e:
                http_status = f"Error: {e}"
            
            # Wait for content to stabilize and scroll to bottom to test lazy loading
            try:
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(0.5)
                await page.evaluate("window.scrollTo(0, 0)")
            except Exception:
                pass
            
            # 1. Broken images check (exclude empty mask SVGs or data URIs)
            broken_images = await page.evaluate('''() => {
                const imgs = Array.from(document.querySelectorAll('img'));
                return imgs.filter(img => {
                    if (img.src.startsWith('data:image/svg+xml')) return false;
                    if (img.src.includes('web_inline_')) return false;
                    return img.naturalWidth === 0 && img.complete;
                }).map(img => img.src);
            }''')
            
            # 2. Residual text check: check main content and headers, excluding the Multi-DS dropdown option
            main_text = await page.evaluate('''() => {
                const clone = document.body.cloneNode(true);
                const switcher = clone.querySelector('#global-ds-switcher');
                if (switcher) switcher.remove();
                return clone.innerText || '';
            }''')
            
            # Match residual kakao keywords
            kakao_matches = re.findall(r'(?:카카오뱅크|kakaobank|카카오(?!톡)|kakao(?!talk))', main_text, re.IGNORECASE)
            
            # Filter failed_requests for actual errors
            significant_failures = [
                f for f in failed_requests 
                if not any(ign in f["url"] for ign in ["favicon.ico", "google-analytics"])
            ]
            
            # Filter console errors
            significant_console = [
                c for c in console_errors 
                if not any(ign in c.lower() for ign in ["favicon", "analytics"])
            ]
            
            is_pass = (
                (http_status == 200 or http_status is None) and
                len(significant_failures) == 0 and
                len(significant_console) == 0 and
                len(broken_images) == 0 and
                len(kakao_matches) == 0
            )
            
            if is_pass:
                passed_routes += 1
                status_label = "PASS"
            else:
                status_label = "FAIL"
                
            result = {
                "route": route,
                "status": http_status,
                "passed": is_pass,
                "failed_requests_count": len(significant_failures),
                "failed_requests": significant_failures,
                "console_errors_count": len(significant_console),
                "console_errors": significant_console,
                "broken_images_count": len(broken_images),
                "broken_images": broken_images,
                "residual_kakao_count": len(kakao_matches),
                "residual_kakao_samples": kakao_matches[:5]
            }
            results.append(result)
            print(f"[{status_label}] {route:30} -> Status: {http_status}, NetErrors: {len(significant_failures)}, Console: {len(significant_console)}, BrokenImgs: {len(broken_images)}, ResidualKakao: {len(kakao_matches)}")
            
            await page.close()
            
        await browser.close()
        
    print(f"\n==========================================")
    print(f"Final Audit Summary: {passed_routes}/{total_routes} Routes Passed ({(passed_routes/total_routes)*100:.1f}%)")
    print(f"==========================================")
    
    with open("final_audit_results.json", "w", encoding="utf-8") as f:
        json.dump({
            "total_routes": total_routes,
            "passed_routes": passed_routes,
            "pass_rate": f"{(passed_routes/total_routes)*100:.1f}%",
            "results": results
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    asyncio.run(audit())
