import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_shadow_entertainment():
    rss_url = "https://www.sayidaty.net/rss.xml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        my_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=30)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"✨ {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:35]):
            title = item.title.text
            link = item.link.text
            
            # --- محرك استخراج الصور الذكي ---
            img_url = ""
            # 1. البحث في وسوم ميديا
            media_content = item.find('media:content') or item.find('enclosure')
            if media_content:
                img_url = media_content.get('url')
            
            # 2. إذا لم يجد، يبحث داخل الوصف (Description) باستخدام Regex
            if not img_url:
                desc = item.description.text if item.description else ""
                img_match = re.search(r'<img src="(.*?)"', desc)
                if img_match:
                    img_url = img_match.group(1)
            
            # 3. صورة افتراضية احترافية في حال الفشل التام
            if not img_url:
                img_url = "https://www.sayidaty.net/themes/custom/sayidaty/logo.png"

            news_html += f'''
            <article class="celeb-card">
                <div class="trend-tag">تريند المشاهير</div>
                <div class="card-thumb">
                    <a href="{my_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="Sayidaty News">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="meta-info">
                        <span>👤 مشاهير العرب</span>
                        <span>📅 {datetime.now().strftime("%d %B %Y")}</span>
                    </div>
                    <div class="action-buttons">
                        <a href="{my_link}" target="_blank" class="btn-main">اقرأ الخبر كاملاً ⚡</a>
                    </div>
                </div>
            </article>'''

            if (i + 1) % 5 == 0:
                news_html += f'''
                <div class="premium-ad-block">
                    <a href="{my_link}" target="_blank">
                        <div class="ad-wrap">
                            <span class="exclusive">حصري</span>
                            <h3>شاهد الفيديوهات المسربة التي حذفتها الفنانة!</h3>
                            <p>اضغط هنا للمشاهدة قبل الحذف</p>
                            <div class="ad-button">مشاهدة الآن 📽️</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سيدتي VIP | بوابة النجوم</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --main: #d4207e; --gold: #fbc02d; --dark: #0f0f0f; --card: #1a1a1a; --text: #ffffff; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--dark); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        header {{ background: rgba(0,0,0,0.95); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 3px solid var(--main); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 26px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--main); }}
        .ticker-bar {{ position: fixed; top: 76px; width: 100%; background: #fff; color: #000; overflow: hidden; height: 38px; display: flex; align-items: center; z-index: 999; border-bottom: 2px solid var(--gold); }}
        .ticker-label {{ background: var(--main); color: #fff; padding: 0 15px; font-weight: 800; font-size: 13px; height: 100%; display: flex; align-items: center; }}
        .ticker-text {{ white-space: nowrap; animation: scroll 40s linear infinite; font-weight: 700; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-300%); }} }}
        .grid-container {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 20px; }}
        .celeb-card {{ background: var(--card); border-radius: 15px; overflow: hidden; border: 1px solid #222; position: relative; transition: 0.3s; }}
        .celeb-card:hover {{ transform: scale(1.02); border-color: var(--main); }}
        .trend-tag {{ position: absolute; top: 10px; right: 10px; background: rgba(212, 32, 126, 0.9); color: #fff; padding: 2px 12px; font-size: 10px; font-weight: 900; border-radius: 4px; z-index: 5; }}
        .card-thumb {{ height: 240px; overflow: hidden; border-bottom: 2px solid var(--main); }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
        .card-body {{ padding: 15px; }}
        .card-title {{ font-size: 17px; font-weight: 700; height: 50px; overflow: hidden; margin-bottom: 12px; line-height: 1.5; }}
        .meta-info {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 15px; }}
        .btn-main {{ display: block; background: var(--main); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 8px; font-weight: 900; font-size: 14px; }}
        .premium-ad-block {{ grid-column: 1 / -1; background: linear-gradient(90deg, #d4207e 0%, #6a1b9a 100%); border-radius: 15px; padding: 30px; text-align: center; color: white; }}
        .ad-button {{ background: #fff; color: #d4207e; display: inline-block; padding: 10px 30px; border-radius: 50px; font-weight: 900; margin-top: 15px; text-decoration: none; }}
        @media (max-width: 600px) {{ .grid-container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">SAYIDATY <span>VIP</span></a>
        <div style="font-size: 12px; color: var(--gold);">EXCLUSIVES ✨</div>
    </header>
    <div class="ticker-bar">
        <div class="ticker-label">عاجل والآن</div>
        <div class="ticker-text">{ticker_items}</div>
    </div>
    <main class="grid-container">{news_html}</main>
    <footer style="text-align:center; padding: 40px; color: #444;">
        <p>SAYIDATY VIP PORTAL &copy; 2026</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_shadow_entertainment()
