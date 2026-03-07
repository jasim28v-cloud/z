import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_sports():
    # المصدر الأساسي للأخبار
    rss_url = "https://arabic.rt.com/rss/sport/"
    # إعدادات الرأس لضمان عدم الحظر
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # الرابط الربحي (USDT / Direct Link)
        my_direct_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        # تنفيذ طلب جلب البيانات
        response = requests.get(rss_url, headers=headers, timeout=25)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        # تحسين شريط الأخبار المتحرك (Ticker)
        ticker_items = " • ".join([f"🔥 {item.title.text.strip()}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:24]):
            title = item.title.text.strip()
            news_url = item.link.text.strip()
            
            # استخراج الصورة الأصلية بجودة عالية
            img_element = item.find('enclosure')
            img_url = img_element.get('url') if img_element else "https://images.pexels.com/photos/46798/the-ball-stadion-football-the-pitch-46798.jpeg"
            
            # هيكلة كروت الأخبار بتصميم عصري
            news_html += f'''
            <article class="sport-card">
                <div class="live-tag">LIVE | مباشر</div>
                <div class="card-thumb">
                    <a href="{my_direct_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="{title[:20]}">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="match-info">
                        <span>🏆 البطولة العالمية</span>
                        <span>🕒 {datetime.now().strftime("%H:%M")} GMT</span>
                    </div>
                    <div class="button-group">
                        <a href="{my_direct_link}" target="_blank" class="btn-live">دخول البث ⚡</a>
                        <a href="{news_url}" target="_blank" class="btn-source">التفاصيل</a>
                    </div>
                </div>
            </article>'''

            # إدراج إعلانات بينية احترافية كل 6 كروت
            if (i + 1) % 6 == 0:
                news_html += f'''
                <div class="premium-ad-block">
                    <a href="{my_direct_link}" target="_blank" style="text-decoration:none;">
                        <div class="ad-content">
                            <span class="ad-label">AD | إعلان</span>
                            <h3>ترتيب الهدافين وجدول ترتيب الدوريات</h3>
                            <p>اضغط هنا لمتابعة الإحصائيات الحية لحظة بلحظة</p>
                            <div class="ad-button">النتائج المباشرة 📊</div>
                        </div>
                    </a>
                </div>'''

        # توليد صفحة الـ HTML الكاملة مع تحسينات CSS
        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="ستاديوم 24 - تغطية مباشرة وحصرية لأهم المباريات والأخبار الرياضية">
    <title>ستاديوم 24 | نبض الرياضة العالمية</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-dark: #0f0f0f; --gold: #cfa84e; --white: #ffffff;
            --danger: #e74c3c; --card-bg: #1a1a1a; --hover-bg: #222222;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Cairo', sans-serif; }}
        body {{ background: var(--bg-dark); color: var(--white); padding-top: 150px; scroll-behavior: smooth; }}
        
        header {{ background: rgba(15, 15, 15, 0.98); padding: 20px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 2px solid var(--gold); display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(10px); }}
        .logo {{ font-size: 30px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--gold); }}

        .live-ticker {{ position: fixed; top: 85px; width: 100%; background: var(--danger); color: #fff; overflow: hidden; height: 40px; display: flex; align-items: center; z-index: 999; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }}
        .ticker-label {{ background: #000; padding: 0 20px; font-weight: 900; font-size: 14px; height: 100%; display: flex; align-items: center; z-index: 2; }}
        .ticker-text {{ white-space: nowrap; animation: scroll-rtl 50s linear infinite; font-weight: 600; padding-right: 100%; }}
        @keyframes scroll-rtl {{ 0% {{ transform: translateX(-100%); }} 100% {{ transform: translateX(100%); }} }}

        .container {{ max-width: 1300px; margin: 0 auto; padding: 20px; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 30px; }}
        
        .sport-card {{ background: var(--card-bg); border-radius: 20px; overflow: hidden; transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94); border: 1px solid #2a2a2a; position: relative; }}
        .sport-card:hover {{ transform: translateY(-10px); border-color: var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.8); }}
        
        .live-tag {{ position: absolute; top: 15px; right: 15px; background: var(--danger); color: #fff; padding: 5px 15px; font-size: 11px; font-weight: 900; border-radius: 5px; z-index: 10; animation: flash 1s infinite; }}
        @keyframes flash {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.6; }} }}

        .card-thumb {{ height: 210px; overflow: hidden; border-bottom: 4px solid var(--gold); }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s; }}
        .sport-card:hover .card-thumb img {{ transform: scale(1.1); }}
        
        .card-body {{ padding: 25px; }}
        .card-title {{ font-size: 18px; font-weight: 700; line-height: 1.6; margin-bottom: 20px; height: 58px; overflow: hidden; color: #eee; }}
        .match-info {{ display: flex; justify-content: space-between; font-size: 13px; color: var(--gold); margin-bottom: 25px; font-weight: bold; border-top: 1px solid #333; padding-top: 15px; }}
        
        .button-group {{ display: flex; gap: 12px; }}
        .btn-live {{ flex: 2; background: linear-gradient(90deg, #cfa84e, #f2cc60); color: #000; text-decoration: none; text-align: center; padding: 14px; border-radius: 12px; font-weight: 900; transition: 0.3s; }}
        .btn-live:hover {{ filter: brightness(1.2); letter-spacing: 1px; }}
        .btn-source {{ flex: 1; background: #333; color: #fff; text-decoration: none; text-align: center; padding: 14px; border-radius: 12px; border: none; font-size: 13px; transition: 0.3s; }}
        .btn-source:hover {{ background: #444; }}

        .premium-ad-block {{ grid-column: 1 / -1; background: linear-gradient(135deg, #1a1a1a 0%, #000 100%); border: 2px dashed var(--gold); border-radius: 25px; padding: 50px; text-align: center; margin: 30px 0; transition: 0.4s; cursor: pointer; }}
        .premium-ad-block:hover {{ background: #000; border-style: solid; }}
        .ad-label {{ background: var(--gold); color: #000; padding: 5px 15px; font-weight: 900; border-radius: 5px; font-size: 12px; }}
        .ad-content h3 {{ font-size: 28px; color: #fff; margin: 20px 0; }}
        .ad-button {{ background: var(--white); color: #000; display: inline-block; padding: 15px 50px; border-radius: 12px; font-weight: 900; margin-top: 25px; text-transform: uppercase; }}

        @media (max-width: 768px) {{ body {{ padding-top: 140px; }} .container {{ grid-template-columns: 1fr; }} .logo {{ font-size: 24px; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">ستاديوم <span>24</span></a>
        <div style="font-size: 14px; font-weight: bold; color: var(--gold); display: flex; align-items:center; gap:8px;">
            <span style="width:10px; height:10px; background:var(--danger); border-radius:50%; display:inline-block; animation: flash 1s infinite;"></span>
            تغطية حصرية 2026
        </div>
    </header>
    <div class="live-ticker">
        <div class="ticker-label">عاجل</div>
        <div class="ticker-text">{ticker_items}</div>
    </div>
    <main class="container">{news_html}</main>
    <footer style="text-align:center; padding: 60px 20px; color: #555; font-size: 14px; background: #050505; margin-top: 50px;">
        <p>حقوق النشر &copy; 2026 ستاديوم 24 | جميع الحقوق محفوظة لرواد الرياضة</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("Done: Mission Accomplished. index.html is ready.")
            
    except Exception as e:
        print(f"Extraction Error: {e}")

if __name__ == "__main__":
    run_sports()
