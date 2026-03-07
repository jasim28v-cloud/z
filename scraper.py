import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celeb_scraper():
    rss_url = "https://www.elfann.com/rss/all"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        # الرابط الإعلاني الجديد الخاص بك
        my_ad_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=30)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"📢 {item.title.text}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:35]):
            title = item.title.text
            
            # محرك استخراج الصور لموقع الفن
            img_url = ""
            media_content = item.find('media:content') or item.find('enclosure')
            if media_content:
                img_url = media_content.get('url')
            
            if not img_url and item.description:
                img_match = re.search(r'<img src="(.*?)"', item.description.text)
                if img_match:
                    img_url = img_match.group(1)
            
            if not img_url:
                img_url = "https://www.elfann.com/images/logo.png"

            news_html += f'''
            <article class="elfann-card">
                <div class="status-tag">حصري الآن</div>
                <div class="card-thumb">
                    <a href="{my_ad_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="Elfann News">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="info-bar">
                        <span>⭐ نجوم الفن</span>
                        <span>🗓️ {datetime.now().strftime("%d/%m/%Y")}</span>
                    </div>
                    <a href="{my_ad_link}" target="_blank" class="action-btn">مشاهدة التفاصيل والصور ⚡</a>
                </div>
            </article>'''

            if (i + 1) % 6 == 0:
                news_html += f'''
                <div class="shadow-ad-box">
                    <a href="{my_ad_link}" target="_blank">
                        <div class="ad-content">
                            <span class="warning-label">تنبيه هام</span>
                            <h3>تسريب فيديو يثير ضجة واسعة في الوسط الفني!</h3>
                            <p>اضغط هنا لمشاهدة المقطع قبل أن يتم حذفه من المنصات</p>
                            <div class="pulsing-btn">شاهد الفيديو المسرب 🎞️</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الفن نيوز | أخبار المشاهير والنجوم</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #000000; --accent: #ff0055; --gold: #ffd700; --text: #ffffff; --card: #151515; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: var(--primary); font-family: 'Cairo', sans-serif; color: var(--text); padding-top: 140px; }}
        
        header {{ background: rgba(0,0,0,0.95); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 3px solid var(--accent); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 28px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--accent); }}

        .news-ticker {{ position: fixed; top: 78px; width: 100%; background: var(--accent); color: #fff; height: 35px; display: flex; align-items: center; z-index: 999; overflow: hidden; }}
        .ticker-label {{ background: #000; padding: 0 20px; font-weight: 900; height: 100%; display: flex; align-items: center; font-size: 13px; }}
        .ticker-text {{ white-space: nowrap; animation: scroll 40s linear infinite; font-weight: 700; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-300%); }} }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
        
        .elfann-card {{ background: var(--card); border-radius: 12px; overflow: hidden; border: 1px solid #333; transition: 0.3s; position: relative; }}
        .elfann-card:hover {{ transform: translateY(-8px); border-color: var(--accent); box-shadow: 0 0 20px rgba(255, 0, 85, 0.3); }}
        
        .status-tag {{ position: absolute; top: 12px; right: 12px; background: var(--accent); color: #fff; padding: 4px 12px; font-size: 11px; font-weight: 900; border-radius: 4px; z-index: 5; }}

        .card-thumb {{ height: 230px; overflow: hidden; }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
        
        .card-body {{ padding: 18px; }}
        .card-title {{ font-size: 18px; font-weight: 700; height: 52px; overflow: hidden; margin-bottom: 15px; line-height: 1.5; }}
        .info-bar {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 20px; }}
        
        .action-btn {{ display: block; background: var(--accent); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 8px; font-weight: 900; }}

        .shadow-ad-box {{ grid-column: 1 / -1; background: linear-gradient(135deg, #111 0%, #000 100%); border: 2px solid var(--accent); border-radius: 15px; padding: 40px; text-align: center; }}
        .pulsing-btn {{ background: #fff; color: #000; display: inline-block; padding: 12px 40px; border-radius: 50px; font-weight: 900; margin-top: 20px; animation: pulse 1.5s infinite; }}
        @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(255,255,255,0.4); }} 70% {{ box-shadow: 0 0 0 15px rgba(255,255,255,0); }} 100% {{ box-shadow: 0 0 0 0 rgba(255,255,255,0); }} }}

        @media (max-width: 600px) {{ .container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header><a href="#" class="logo">ELFANN<span>.PRO</span></a></header>
    <div class="news-ticker"><div class="ticker-label">تغطية مباشرة</div><div class="ticker-text">{ticker_items}</div></div>
    <main class="container">{news_html}</main>
    <footer style="text-align:center; padding: 50px; color: #444; font-size: 11px;">ELFANN PRO ENGINE &copy; 2026</footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_celeb_scraper()
