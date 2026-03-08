import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run_vortex_google_news_scraper():
    # الرابط القوي الذي اكتشفته يا صديقي
    rss_url = "https://news.google.com/rss/search?q=site:celebritiesarab.com"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    
    try:
        my_link = "https://data527.click/21330bf1d025d41336e6/4ba0cfe12d/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=25)
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        news_html = ""
        for item in items[:15]:
            title = item.title.text
            link = item.link.text
            # ملاحظة: جوجل نيوز أحياناً لا يضع الصورة مباشرة، سنضع صورة افتراضية فخمة إذا لم تتوفر
            img = "https://images.unsplash.com/photo-1514525253344-f814d0746b15?w=800" 

            news_html += f'''
            <div class="v-card">
                <a href="{my_link}" target="_blank">
                    <div class="v-img">
                        <img src="{img}" loading="lazy">
                        <div class="v-badge">تريند الآن</div>
                    </div>
                    <div class="v-info">
                        <h3>{title}</h3>
                        <div class="v-footer">
                            <span>📅 {item.pubDate.text[:16]}</span>
                            <span class="v-btn">اقرأ المزيد</span>
                        </div>
                    </div>
                </a>
            </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VORTEX | CELEBRITIES</title>
    
    <script src="https://data527.click/pfe/current/tag.min.js?z=8345712" data-cfasync="false" async></script>
    <script type='text/javascript' src='//pl25330eef.effectiveratecpm.com/26/33/0e/26330eef1cb397212db567d1385dc0b9.js'></script>

    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --main: #ff0055; --bg: #0a0a0a; --card: #151515; }}
        body {{ background: var(--bg); color: #fff; font-family: 'Cairo', sans-serif; margin: 0; }}
        header {{ background: #000; padding: 20px; border-bottom: 3px solid var(--main); text-align: center; position: sticky; top: 0; z-index: 1000; }}
        .logo {{ font-size: 26px; font-weight: 900; letter-spacing: 1px; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--main); }}
        .container {{ max-width: 1200px; margin: 20px auto; padding: 0 15px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 25px; }}
        .v-card {{ background: var(--card); border-radius: 15px; overflow: hidden; border: 1px solid #222; transition: 0.3s; }}
        .v-card:hover {{ transform: translateY(-10px); border-color: var(--main); box-shadow: 0 10px 30px rgba(255, 0, 85, 0.2); }}
        .v-card a {{ text-decoration: none; color: inherit; }}
        .v-img {{ position: relative; height: 200px; }}
        .v-img img {{ width: 100%; height: 100%; object-fit: cover; }}
        .v-badge {{ position: absolute; top: 15px; right: 15px; background: var(--main); font-size: 11px; font-weight: bold; padding: 4px 12px; border-radius: 5px; }}
        .v-info {{ padding: 20px; }}
        .v-info h3 {{ font-size: 16px; font-weight: 700; line-height: 1.6; height: 52px; overflow: hidden; margin: 0 0 15px 0; }}
        .v-footer {{ display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #888; border-top: 1px solid #222; padding-top: 15px; }}
        .v-btn {{ color: var(--main); font-weight: bold; border: 1px solid var(--main); padding: 3px 12px; border-radius: 20px; }}
    </style>
</head>
<body onclick="void(0)">
    <header><a href="#" class="logo">VORTEX<span>CELEBS</span></a></header>
    <div class="container">
        <h2 style="border-right: 5px solid var(--main); padding-right: 15px; margin-bottom: 30px;">🔥 أخبار المشاهير الحصرية</h2>
        <div class="grid">{news_html}</div>
    </div>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(full_html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    run_vortex_google_news_scraper()
