import streamlit as st
import streamlit.components.v1 as components

# Sayfa Yapılandırması (Geniş ekran modu yapıldı)
st.set_page_config(
    page_title="iyi ki doğdun ablam",
    page_icon="🎉",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iyi ki doğdun ablam</title>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --primary: #d946ef;
            --secondary: #8b5cf6;
            --accent: #f43f5e;
            --bg-dark: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.7);
            --text-light: #f8fafc;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: radial-gradient(circle at center, #1e1b4b 0%, #0f172a 100%);
            color: var(--text-light);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
            padding-bottom: 2rem;
        }

        /* kilit ekranı stilleri ve geçiş efekti */
        #lock-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: #0f172a;
            z-index: 999;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 1.5rem;
            text-align: center;
            transition: opacity 0.8s ease, transform 0.8s ease;
        }

        #lock-screen.fade-out {
            opacity: 0;
            transform: scale(1.1);
            pointer-events: none;
        }

        .lock-box {
            background: rgba(30, 41, 59, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 20px;
            max-width: 400px;
            width: 100%;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .lock-box input {
            width: 100%;
            padding: 0.8rem 1rem;
            margin: 1.2rem 0;
            border-radius: 10px;
            border: 1px solid var(--primary);
            background: rgba(15, 23, 42, 0.8);
            color: white;
            font-size: 1.1rem;
            text-align: center;
            outline: none;
        }

        .lock-box button {
            background: linear-gradient(135deg, #ec4899, #8b5cf6);
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s ease;
        }

        .lock-box button:hover {
            transform: scale(1.05);
        }

        #error-msg {
            color: #f43f5e;
            margin-top: 1rem;
            display: none;
            font-size: 0.95rem;
        }

        /* ana içerik */
        #main-content {
            display: none;
            animation: fadeIn 1s ease forwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .heart-particle {
            position: fixed;
            color: var(--accent);
            opacity: 0.6;
            animation: floatUp 8s linear infinite;
            z-index: 0;
            pointer-events: none;
        }

        @keyframes floatUp {
            0% { transform: translateY(100vh) scale(0.5) rotate(0deg); opacity: 0; }
            20% { opacity: 0.7; }
            100% { transform: translateY(-10vh) scale(1.2) rotate(360deg); opacity: 0; }
        }

        .container {
            max-width: 900px;
            width: 100%;
            margin: 0 auto;
            padding: 1.5rem 1rem;
            position: relative;
            z-index: 1;
        }

        header {
            text-align: center;
            padding: 1rem 0;
        }

        h1 {
            font-size: 2.3rem;
            background: linear-gradient(135deg, #f472b6, #a855f7, #38bdf8);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 30px rgba(217, 70, 239, 0.3);
        }

        p.subtitle {
            font-size: 1.1rem;
            color: #cbd5e1;
        }

        .cake-section {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 1.5rem;
            text-align: center;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            position: relative;
        }

        .cake-container {
            position: relative;
            width: 200px;
            height: 180px;
            margin: 1.5rem auto 1rem;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .cake-container:hover {
            transform: scale(1.05);
        }

        .cake-base {
            position: absolute;
            bottom: 0;
            width: 200px;
            height: 90px;
            background: linear-gradient(to right, #ec4899, #8b5cf6);
            border-radius: 15px 15px 5px 5px;
            box-shadow: inset 0 -10px 0 rgba(0,0,0,0.2);
        }

        .cake-top {
            position: absolute;
            bottom: 85px;
            left: 15px;
            width: 170px;
            height: 60px;
            background: linear-gradient(to right, #f472b6, #c084fc);
            border-radius: 15px 15px 5px 5px;
        }

        .candles {
            position: absolute;
            bottom: 145px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
        }

        .candle {
            width: 12px;
            height: 35px;
            background: repeating-linear-gradient(45deg, #fbbf24, #fbbf24 5px, #f59e0b 5px, #f59e0b 10px);
            border-radius: 3px;
            position: relative;
        }

        .flame {
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 12px;
            height: 18px;
            background: #f97316;
            border-radius: 50% 50% 20% 20%;
            box-shadow: 0 0 15px #f97316, 0 0 25px #fef08a;
            animation: flicker 0.6s infinite alternate;
        }

        .flame.off {
            display: none;
        }

        @keyframes flicker {
            0% { transform: translateX(-50%) scale(1); }
            100% { transform: translateX(-50%) scale(1.15); }
        }

        .messages-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
            margin: 1.5rem 0;
        }

        @media (min-width: 600px) {
            .messages-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .card {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 1.2rem;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
        }

        .card-icon {
            font-size: 1.8rem;
            margin-bottom: 0.4rem;
        }

        .card-title {
            font-size: 1.1rem;
            color: #f472b6;
            margin-bottom: 0.4rem;
            font-weight: bold;
        }

        .card-text {
            color: #cbd5e1;
            font-size: 0.9rem;
            line-height: 1.5;
        }

        .letter-section {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            text-align: center;
        }

        .envelope-btn {
            background: linear-gradient(135deg, #ec4899, #8b5cf6);
            color: white;
            border: none;
            padding: 0.9rem 1.8rem;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4);
            width: 100%;
        }

        @media (min-width: 600px) {
            .envelope-btn {
                width: auto;
            }
        }

        .envelope-btn:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 6px 20px rgba(236, 72, 153, 0.6);
        }

        .letter-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.8s ease-in-out, opacity 0.5s ease;
            opacity: 0;
            text-align: left;
            margin-top: 1.5rem;
            background: rgba(15, 23, 42, 0.8);
            padding: 0 1rem;
            border-radius: 12px;
            border-left: 4px solid var(--primary);
            line-height: 1.8;
            font-size: 0.95rem;
            color: #e2e8f0;
        }

        .letter-content.open {
            max-height: 2500px;
            opacity: 1;
            padding: 1.2rem;
        }

        footer {
            text-align: center;
            padding: 1rem 0;
            color: #94a3b8;
            font-size: 0.85rem;
        }
    </style>
</head>
<body>

    <!-- Kilit Ekranı -->
    <div id="lock-screen">
        <div class="lock-box">
            <h2 style="color: #f472b6; margin-bottom: 0.5rem;">🔒 Giriş Kontrolü</h2>
            <p style="color: #cbd5e1; font-size: 0.95rem;">siteye girmek için soruyu bilmen lazım</p>
            <p style="margin-top: 1rem; font-weight: bold; color: #38bdf8;">ablamdan en çok istediğim şey nedir</p>
            <input type="text" id="answer-input" placeholder="cevabını yaz..." onkeydown="if(event.key==='Enter') checkAnswer()">
            <button onclick="checkAnswer()">Giriş Yap 🚀</button>
            <p id="error-msg">yanlış cevap tekrar dene</p>
        </div>
    </div>

    <!-- Ana İçerik -->
    <div id="main-content">
        <div class="container">
            <header>
                <h1>iyi ki doğdun ablam</h1>
                <p class="subtitle">dünyanın en harika ablası için özel olarak hazırlandı</p>
            </header>

            <!-- Pasta Bölümü -->
            <div class="cake-section">
                <h2>mumları söndürmek için tıkla</h2>
                <div class="cake-container" id="cake" onclick="blowCandles()">
                    <div class="candles">
                        <div class="candle"><div class="flame" id="flame1"></div></div>
                        <div class="candle"><div class="flame" id="flame2"></div></div>
                        <div class="candle"><div class="flame" id="flame3"></div></div>
                    </div>
                    <div class="cake-top"></div>
                    <div class="cake-base"></div>
                </div>
                <p id="cake-msg" style="color: #94a3b8; font-size: 0.95rem;">mumları söndür ve dileğini tut</p>
            </div>

            <!-- Özellik Kutuları -->
            <div class="messages-grid">
                <div class="card">
                    <div class="card-icon">👑</div>
                    <div class="card-title">evin kraliçesi</div>
                    <div class="card-text">her zaman arkamda duran en zor anlarımda bile bana yol gösteren fikirleriyle yön veren ve evdeki tüm dengeleri ustalıkla koruyan tek kişisin</div>
                </div>
                <div class="card">
                    <div class="card-icon">💫</div>
                    <div class="card-title">sırdaşım ve dostum</div>
                    <div class="card-text">aramızdaki o güzel bağ kahkahalar ve eğlenceli anlar bile seninle bambaşka güzel iyi ki benim ablamsın sırrımı paylaştığım en güvenli limanımsın</div>
                </div>
                <div class="card">
                    <div class="card-icon">🎮</div>
                    <div class="card-title">gizli sponsor ve oyun dostu</div>
                    <div class="card-text">bizimkiler oyuna para yatırmama izin vermediğinde hemen araya girip halleden benim yerime yatıran kral ablamsın hakkın ödenmez</div>
                </div>
                <div class="card">
                    <div class="card-icon">🧽</div>
                    <div class="card-title">temizlik ve düzen yardımcısı</div>
                    <div class="card-text">evde yanlışlıkla bir şeyler döküldüğünde veya ortalık kirlendiğinde hiç ikiletmeden hemen koşup temizlemeye yardım eden gizli kahramanımızsın</div>
                </div>
                <div class="card" style="grid-column: 1 / -1;">
                    <div class="card-icon">🌟</div>
                    <div class="card-title">ilham kaynağı</div>
                    <div class="card-text">gücün sabrın ve neşenle her zaman hayatıma ışık tutuyorsun yeni yaşın sana katbekat mutluluk ve huzur getirsin</div>
                </div>
            </div>

            <!-- Ablaya Karşı Saf Sevgi Notu (Uzun) -->
            <div class="letter-section">
                <button class="envelope-btn" onclick="toggleLetter()">ablama duyduğum sevgiyi aç</button>
                <div class="letter-content" id="letter">
                    <h3 style="margin-bottom: 1rem; color: #f472b6;">canım ablam</h3>
                    <p>
                        seni gerçekten çok seviyorum ve bunu sana her zaman söze dökemesem de kalbimde yerin bambaşka evde yaşanan tüm o güzel anların ve huzurun arkasındaki en büyük güç sensin
                        <br><br>
                        evdekiler oyuna para yatırmama izin vermediğinde beni kırmayıp hemen halletmen aradaki o kral desteğin benim için çok kıymetli üstüne bir de evde ne zaman bir şey dökülse veya ortalık karışsa hemen yardıma koşup temizlemene yardım etmen senin ne kadar düşünceli bir abla olduğunu gösteriyor
                        <br><br>
                        bazen her şey üst üste gelse bile senin yanımda olduğunu bilmek bana güç veriyor seninle konuşmak aynı evde vakit geçirmek hayatın stresini unutturuyor aramızdaki bu kardeşlik bağı dünyadaki her şeyden daha değerli ve ben senin gibi bir ablaya sahip olduğum için gerçekten çok şanslıyım
                        <br><br>
                        hayat koşturmacası içinde belki her gün süslü laflar etmiyoruz ama içten içe ne kadar değer verdiğimizi ikimiz de biliyoruz senin mutluluğun senin yüzünün gülmesi benim için çok önemli umarım yeni yaşında dilediğin her şey sırayla gerçekleşir hayallerine bir adım daha yaklaşırsın
                        <br><br>
                        iyi ki benim ablamsın iyi ki varsın seninle her şey çok daha kolay ve eğlenceli yeni yaşında dilediğin tüm güzellikler seni bulsun yüzün her zaman gülsün doğum günün kutlu olsun seni çok seviyorum
                    </p>
                </div>
            </div>

            <footer>
                <p>sevgilerle hazırlanmıştır 2026</p>
            </footer>
        </div>
    </div>

    <script>
        function checkAnswer() {
            const input = document.getElementById('answer-input').value.toLowerCase().trim();
            if (input.includes('para')) {
                const lockScreen = document.getElementById('lock-screen');
                lockScreen.classList.add('fade-out');
                
                setTimeout(() => {
                    lockScreen.style.display = 'none';
                    document.getElementById('main-content').style.display = 'block';
                    createHearts();
                    confetti({ particleCount: 150, spread: 90, origin: { y: 0.5 } });
                }, 700);
            } else {
                document.getElementById('error-msg').style.display = 'block';
            }
        }

        function createHearts() {
            for(let i = 0; i < 15; i++) {
                let heart = document.createElement('div');
                heart.className = 'heart-particle';
                heart.innerHTML = '❤️';
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.animationDuration = (Math.random() * 4 + 4) + 's';
                heart.style.fontSize = (Math.random() * 15 + 10) + 'px';
                document.body.appendChild(heart);
            }
        }

        let candlesBlown = false;
        function blowCandles() {
            if(candlesBlown) return;
            document.getElementById('flame1').classList.add('off');
            document.getElementById('flame2').classList.add('off');
            document.getElementById('flame3').classList.add('off');
            
            document.getElementById('cake-msg').innerHTML = "✨ dileğin kabul oldu benden istediğin bir şey olsun söyle halledelim iyi ki doğdun ✨";
            document.getElementById('cake-msg').style.color = "#f472b6";
            document.getElementById('cake-msg').style.fontWeight = "bold";
            
            confetti({ particleCount: 200, spread: 100, origin: { y: 0.6 } });
            setTimeout(() => {
                confetti({ particleCount: 100, angle: 60, spread: 55, origin: { x: 0 } });
                confetti({ particleCount: 100, angle: 120, spread: 55, origin: { x: 1 } });
            }, 300);

            candlesBlown = true;
        }

        function toggleLetter() {
            document.getElementById('letter').classList.toggle('open');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=1400, scrolling=True)
