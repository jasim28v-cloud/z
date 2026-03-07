import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def run_celebs_pro():
    # تغيير المصدر إلى بوابة متخصصة في المشاهير والتريندات (VetoGate - فن)
    rss_url = "https://www.vetogate.com/rss.aspx?id=31" 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        my_direct_link = "Https://data527.click/21330bf1d025d41336e6/57154ac610/?placementName=default"
        
        response = requests.get(rss_url, headers=headers, timeout=25)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_items = " • ".join([f"✨ {item.title.text.strip()}" for item in items[:15]])
        news_html = ""
        
        for i, item in enumerate(items[:24]):
            title = item.title.text.strip()
            news_url = item.link.text.strip()
            
            # محاولة استخراج الصورة من ميديا الوصف أو enclosure
            img_url = "https://images.pexels.com/photos/2747449/pexels-photo-2747449.jpeg"
            enclosure = item.find('enclosure')
            if enclosure:
                img_url = enclosure.get('url')
            else:
                description = item.find('description').text
                img_match = re.search(r'<img src="(.*?)"', description)
                if img_match:
                    img_url = img_match.group(1)
            
            news_html += f'''
            <article class="celeb-card">
                <div class="trend-tag">🔥 تريند الآن</div>
                <div class="card-thumb">
                    <a href="{my_direct_link}" target="_blank">
                        <img src="{img_url}" loading="lazy" alt="celeb news">
                    </a>
                </div>
                <div class="card-body">
                    <h2 class="card-title">{title}</h2>
                    <div class="meta-info">
                        <span>🎬 كواليس النجوم</span>
                        <span>⏱️ {datetime.now().strftime("%H:%M")}</span>
                    </div>
                    <div class="button-group">
                        <a href="{my_direct_link}" target="_blank" class="btn-exclusive">شاهد الفضيحة كاملة ⚡</a>
                        <a href="{news_url}" target="_blank" class="btn-source">التفاصيل</a>
                    </div>
                </div>
            </article>'''

            if (i + 1) % 5 == 0:
                news_html += f'''
                <div class="premium-ad-block">
                    <a href="{my_direct_link}" target="_blank" style="text-decoration:none;">
                        <div class="ad-content">
                            <span class="ad-label">حصري لزوارنا</span>
                            <h3>تسريبات وصور تظهر لأول مرة</h3>
                            <p>اضغط هنا للدخول إلى الألبوم السري للمشاهير</p>
                            <div class="ad-button">دخول الآن 🔓</div>
                        </div>
                    </a>
                </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مشاهير لايف | فضائح وتريندات</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --dark: #080808; --pink: #ff2e63; --gold: #f9d423; --white: #ffffff;
            --card-bg: #121212;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Cairo', sans-serif; }}
        body {{ background: var(--dark); color: var(--white); padding-top: 150px; }}
        
        header {{ background: rgba(0, 0, 0, 0.9); padding: 20px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; border-bottom: 2px solid var(--pink); display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 28px; font-weight: 900; color: #fff; text-decoration: none; }}
        .logo span {{ color: var(--pink); }}

        .live-ticker {{ position: fixed; top: 85px; width: 100%; background: var(--pink); color: #fff; overflow: hidden; height: 35px; display: flex; align-items: center; z-index: 999; font-size: 13px; }}
        .ticker-label {{ background: #000; padding: 0 20px; font-weight: 900; }}
        .ticker-text {{ white-space: nowrap; animation: scroll-rtl 50s linear infinite; }}
        @keyframes scroll-rtl {{ 0% {{ transform: translateX(-100%); }} 100% {{ transform: translateX(100%); }} }}

        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 25px; }}
        
        .celeb-card {{ background: var(--card-bg); border-radius: 12px; overflow: hidden; transition: 0.3s; border: 1px solid #222; position: relative; }}
        .celeb-card:hover {{ transform: scale(1.02); border-color: var(--pink); }}
        
        .trend-tag {{ position: absolute; top: 10px; right: 10px; background: rgba(255, 46, 99, 0.9); color: #fff; padding: 4px 10px; font-size: 11px; font-weight: 900; border-radius: 4px; z-index: 5; }}

        .card-thumb {{ height: 200px; }}
        .card-thumb img {{ width: 100%; height: 100%; object-fit: cover; }}
        
        .card-body {{ padding: 20px; }}
        .card-title {{ font-size: 17px; font-weight: 700; line-height: 1.5; margin-bottom: 15px; height: 50px; overflow: hidden; }}
        .meta-info {{ display: flex; justify-content: space-between; font-size: 11px; color: var(--gold); margin-bottom: 20px; }}
        
        .button-group {{ display: flex; gap: 8px; }}
        .btn-exclusive {{ flex: 2; background: var(--pink); color: #fff; text-decoration: none; text-align: center; padding: 12px; border-radius: 6px; font-weight: 900; }}
        .btn-source {{ flex: 1; background: #222; color: #888; text-decoration: none; text-align: center; padding: 12px; border-radius: 6px; font-size: 11px; border: 1px solid #333; }}

        .premium-ad-block {{ grid-column: 1 / -1; background: linear-gradient(45deg, #121212, #250a10); border: 2px dashed var(--pink); border-radius: 15px; padding: 40px; text-align: center; }}
        .ad-button {{ background: var(--gold); color: #000; display: inline-block; padding: 12px 40px; border-radius: 50px; font-weight: 900; margin-top: 15px; }}

        @media (max-width: 600px) {{ .container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">CELEB<span>24</span></a>
        <div style="font-size: 12px; font-weight: bold; color: var(--pink);">📸 نبض النجوم</div>
    </header>
    <div class="live-ticker">
        <div class="ticker-label">عاجل</div>
        <div class="ticker-text">{ticker_items}</div>
    </div>
    <main class="container">{news_html}</main>
    <footer style="text-align:center; padding: 40px; color: #444; font-size: 12px;">
        <p>CELEB 24 &copy; 2026 | Exclusive Celebrity News</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("Success: Professional Celeb Portal is LIVE.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_celebs_pro()
