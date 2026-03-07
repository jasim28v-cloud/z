import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celeb_mission():
    # مصدر ET بالعربي - الأكثر استقراراً وشهرة
    rss_url = "https://etbilarabi.com/rss.xml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        # الرابط الإعلاني الجديد الخاص بك
        my_ad_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=30)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"Error: Status {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"🔥 {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:30]):
            title = item.title.text
            
            # استخراج الصورة الحقيقية من ET بالعربي
            img_url = ""
            media_content = item.find('media:content') or item.find('enclosure')
            if media_content:
                img_url = media_content.get('url')
            
            if not img_url:
                # محاولة البحث داخل الوصف
                img_match = re.search(r'src="(.*?)"', str(item.description))
                if img_match:
                    img_url = img_match.group(1)
            
            if not img_url:
                img_url = "https://etbilarabi.com/themes/custom/etbilarabi/logo.png"

            news_html += f'''
            <article class="shadow-card">
                <div class="glow-tag">TRENDING</div>
                <div class="thumb-container">
                    <a href="{my_ad_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="Celebrity News">
                    </a>
                </div>
                <div class="content-box">
                    <h2 class="title-text">{title}</h2>
                    <div class="meta-data">
                        <span>🎬 ET بالعربي</span>
                        <span>⏱️ {datetime.now().strftime("%H:%M")}</span>
                    </div>
                    <a href="{my_ad_link}" target="_blank" class="cyber-btn">التفاصيل الكاملة ⚡</a>
                </div>
            </article>'''

            if (i + 1) % 5 == 0:
                news_html += f'''
                <div class="ad-break">
                    <a href="{my_ad_link}" target="_blank">
                        <div class="ad-inner">
                            <span class="live-blink">LIVE</span>
                            <h3>فضيحة تهز الوسط الفني الآن!</h3>
                            <p>شاهد الصور المسربة قبل الحذف النهائي</p>
                            <div class="btn-glow">دخول الأرشيف السري 🔓</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHΔDØW CELEB | أخبار النجوم</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #050505; --card: #111111; --primary: #ff003c; --gold: #ffcc00; --text: #e0e0e0; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--bg); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        
        header {{ background: rgba(0,0,0,0.9); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 2px solid var(--primary); display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(15px); }}
        .logo {{ font-size: 26px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--primary); text-shadow: 0 0 10px var(--primary); }}

        .ticker-wrap {{ position: fixed; top: 75px; width: 100%; background: #fff; color: #000; height: 35px; display: flex; align-items: center; z-index: 999; font-weight: 900; }}
        .ticker-label {{ background: var(--primary); color: #fff; padding: 0 20px; font-size: 13px; height: 100%; display: flex; align-items: center; }}
        .ticker-content {{ white-space: nowrap; animation: scroll 40s linear infinite; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-350%); }} }}

        .grid {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }}
        
        .shadow-card {{ background: var(--card); border-radius: 12px; overflow: hidden; border: 1px solid #222; position: relative; transition: 0.4s ease; }}
        .shadow-card:hover {{ transform: translateY(-10px); border-color: var(--primary); box-shadow: 0 0 20px rgba(255,0,60,0.2); }}
        
        .glow-tag {{ position: absolute; top: 12px; right: 12px; background: var(--primary); color: #fff; padding: 3px 12px; font-size: 11px; font-weight: 900; border-radius: 4px; z-index: 5; box-shadow: 0 0 10px var(--primary); }}

        .thumb-container {{ height: 230px; overflow: hidden; }}
        .thumb-container img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
        .shadow-card:hover img {{ transform: scale(1.1); }}
        
        .content-box {{ padding: 20px; }}
        .title-text {{ font-size: 18px; font-weight: 700; height: 54px; overflow: hidden; margin-bottom: 15px; line-height: 1.5; }}
        .meta-data {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 20px; }}
        
        .cyber-btn {{ display: block; background: var(--primary); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 6px; font-weight: 900; font-size: 14px; text-transform: uppercase; }}

        .ad-break {{ grid-column: 1 / -1; background: linear-gradient(45deg, #1a1a1a, #000); border: 2px solid var(--gold); padding: 40px; text-align: center; border-radius: 15px; }}
        .btn-glow {{ background: #fff; color: #000; display: inline-block; padding: 12px 40px; border-radius: 50px; font-weight: 900; margin-top: 20px; animation: pulse 1.5s infinite; }}
        @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(255,204,0,0.4); }} 70% {{ box-shadow: 0 0 0 15px rgba(255,204,0,0); }} 100% {{ box-shadow: 0 0 0 0 rgba(255,204,0,0); }} }}

        @media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header><a href="#" class="logo">ET<span>.SHΔDØW</span></a></header>
    <div class="ticker-wrap"><div class="ticker-label">عاجل الآن</div><div class="ticker-content">{ticker_items}</div></div>
    <main class="grid">{news_html}</main>
    <footer style="text-align:center; padding: 60px; color: #222;">CORE ENGINE BY SHΔDØW</footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("Mission Accomplished: ET Content Synced.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_celeb_mission()
