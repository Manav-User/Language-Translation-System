from flask import Flask, request, render_template_string
from translator import translate

app = Flask(__name__)

LANGUAGES = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Gujarati": "guj_Gujr",
    "Marathi": "mar_Deva",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Bengali": "ben_Beng",
    "Punjabi": "pan_Guru",
    "Urdu": "urd_Arab",
    "Nepali": "npi_Deva",
    "Sinhala": "sin_Sinh",
    "Odia": "ory_Orya",
    "Assamese": "asm_Beng",
    "Maithili": "mai_Deva",
    "Sanskrit": "san_Deva",
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Italian": "ita_Latn",
    "Portuguese": "por_Latn",
    "Dutch": "nld_Latn",
    "Swedish": "swe_Latn",
    "Norwegian": "nob_Latn",
    "Danish": "dan_Latn",
    "Finnish": "fin_Latn",
    "Polish": "pol_Latn",
    "Czech": "ces_Latn",
    "Slovak": "slk_Latn",
    "Hungarian": "hun_Latn",
    "Romanian": "ron_Latn",
    "Greek": "ell_Grek",
    "Bulgarian": "bul_Cyrl",
    "Russian": "rus_Cyrl",
    "Ukrainian": "ukr_Cyrl",
    "Serbian": "srp_Cyrl",
    "Croatian": "hrv_Latn",
    "Slovenian": "slv_Latn",
    "Lithuanian": "lit_Latn",
    "Latvian": "lav_Latn",
    "Estonian": "est_Latn",
    "Arabic": "arb_Arab",
    "Hebrew": "heb_Hebr",
    "Persian": "pes_Arab",
    "Turkish": "tur_Latn",
    "Azerbaijani": "aze_Latn",
    "Kazakh": "kaz_Cyrl",
    "Uzbek": "uzb_Latn",
    "Tajik": "tgk_Cyrl",
    "Pashto": "pus_Arab",
    "Chinese (Simplified)": "zho_Hans",
    "Chinese (Traditional)": "zho_Hant",
    "Japanese": "jpn_Jpan",
    "Korean": "kor_Hang",
    "Thai": "tha_Thai",
    "Vietnamese": "vie_Latn",
    "Indonesian": "ind_Latn",
    "Malay": "zsm_Latn",
    "Filipino": "tgl_Latn",
    "Burmese": "mya_Mymr",
    "Khmer": "khm_Khmr",
    "Lao": "lao_Laoo",
    "Swahili": "swh_Latn",
    "Zulu": "zul_Latn",
    "Xhosa": "xho_Latn",
    "Yoruba": "yor_Latn",
    "Igbo": "ibo_Latn",
    "Hausa": "hau_Latn",
    "Amharic": "amh_Ethi",
    "Somali": "som_Latn",
    "Shona": "sna_Latn",
    "Spanish (Latin America)": "spa_Latn",
    "Quechua": "quy_Latn",
    "Guarani": "grn_Latn",
    "Icelandic": "isl_Latn",
    "Irish": "gle_Latn",
    "Welsh": "cym_Latn",
    "Scottish Gaelic": "gla_Latn",
    "Esperanto": "epo_Latn",
    "Latin": "lat_Latn"
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Language Translator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            overflow: hidden;
            position: relative;
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.3) 0%, transparent 50%);
            z-index: -1;
            pointer-events: none;
            animation: bgShift 15s ease-in-out infinite;
        }
        
        @keyframes bgShift {
            0%, 100% {
                background: 
                    radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.3) 0%, transparent 50%);
            }
            50% {
                background: 
                    radial-gradient(circle at 80% 50%, rgba(102, 126, 234, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 20% 80%, rgba(118, 75, 162, 0.3) 0%, transparent 50%);
            }
        }
        
        .floating-shape {
            position: fixed;
            z-index: -1;
            pointer-events: none;
        }
        
        .shape1 {
            width: 300px;
            height: 300px;
            background: linear-gradient(45deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15));
            border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
            top: -50px;
            left: -100px;
            animation: float1 20s ease-in-out infinite;
        }
        
        .shape2 {
            width: 250px;
            height: 250px;
            background: linear-gradient(135deg, rgba(118, 75, 162, 0.12), rgba(102, 126, 234, 0.12));
            border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
            bottom: 100px;
            right: -50px;
            animation: float2 25s ease-in-out infinite;
        }
        
        .shape3 {
            width: 200px;
            height: 200px;
            background: linear-gradient(45deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
            border-radius: 70% 30% 66% 34% / 33% 66% 34% 67%;
            top: 50%;
            right: 10%;
            animation: float3 30s ease-in-out infinite;
        }
        
        @keyframes float1 {
            0%, 100% {
                transform: translate(0, 0) scale(1);
            }
            25% {
                transform: translate(30px, -40px) scale(1.05);
            }
            50% {
                transform: translate(-20px, 40px) scale(0.95);
            }
            75% {
                transform: translate(50px, 20px) scale(1.1);
            }
        }
        
        @keyframes float2 {
            0%, 100% {
                transform: translate(0, 0) rotate(0deg);
            }
            33% {
                transform: translate(-40px, -30px) rotate(120deg);
            }
            66% {
                transform: translate(30px, 40px) rotate(240deg);
            }
        }
        
        @keyframes float3 {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            50% {
                transform: translateY(-60px) rotate(180deg);
            }
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 700px;
            width: 100%;
        }
        
        h2 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 0.95em;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            color: #555;
            font-weight: 600;
            margin-bottom: 8px;
            font-size: 0.95em;
        }
        
        textarea {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            resize: vertical;
            transition: border-color 0.3s;
        }
        
        textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .language-section {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
        }
        
        .language-group {
            flex: 1;
        }
        
        select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            background-color: white;
            color: #333;
            cursor: pointer;
            transition: border-color 0.3s;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        select:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .custom-select {
            position: relative;
            width: 100%;
        }
        
        .select-input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            background-color: white;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            cursor: pointer;
            transition: border-color 0.3s;
        }
        
        .select-input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .dropdown-menu {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 2px solid #e0e0e0;
            border-top: none;
            border-radius: 0 0 10px 10px;
            max-height: 250px;
            overflow-y: auto;
            display: none;
            z-index: 1000;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        }
        
        .dropdown-menu.open {
            display: block;
        }
        
        .dropdown-option {
            padding: 12px;
            cursor: pointer;
            transition: background-color 0.2s;
            color: #333;
        }
        
        .dropdown-option:hover {
            background-color: #f0f0f0;
        }
        
        .dropdown-option.selected {
            background-color: #667eea;
            color: white;
        }
        
        .dropdown-option.hidden {
            display: none;
        }
        
        .swap-button {
            align-self: flex-end;
            padding: 12px 15px;
            background: #f0f0f0;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 1.2em;
        }
        
        .swap-button:hover {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }
        
        button[type="submit"] {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 20px;
        }
        
        button[type="submit"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        button[type="submit"]:active {
            transform: translateY(0);
        }
        
        .result-container {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 15px;
            padding: 20px;
            margin-top: 30px;
            display: none;
        }
        
        .result-container.show {
            display: block;
            animation: slideIn 0.3s ease-out;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .result-container h3 {
            color: #333;
            margin-bottom: 12px;
            font-size: 1.2em;
        }
        
        .result-container p {
            color: #555;
            line-height: 1.6;
            font-size: 1.05em;
            word-wrap: break-word;
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 25px;
            }
            
            h2 {
                font-size: 2em;
            }
            
            .language-section {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="floating-shape shape1"></div>
    <div class="floating-shape shape2"></div>
    <div class="floating-shape shape3"></div>
    
    <div class="container">
        <h2>
            <svg width="45" height="45" viewBox="0 0 45 45" style="display: inline-block; margin-right: 15px; vertical-align: middle;">
                <circle cx="22.5" cy="22.5" r="20" fill="#667eea"/>
                <path d="M 22.5 5 A 17.5 17.5 0 0 1 35 15 M 22.5 40 A 17.5 17.5 0 0 1 10 30" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/>
                <circle cx="22.5" cy="22.5" r="17.5" fill="none" stroke="white" stroke-width="1.5" opacity="0.3"/>
                <text x="22.5" y="27" text-anchor="middle" font-size="14" font-weight="bold" fill="white">T</text>
            </svg>
            Language Translator
        </h2>
        <p class="subtitle">Translate text between 23 different languages instantly</p>
        
        <form method="post">
            <div class="form-group">
                <label for="text">Text to Translate:</label>
                <textarea name="text" id="text" rows="5" placeholder="Enter the text you want to translate..." required></textarea>
            </div>
            
            <div class="language-section">
                <div class="language-group">
                    <label for="src">From:</label>
                    <div class="custom-select">
                        <input type="text" class="select-input" id="src" placeholder="Search language...">
                        <div class="dropdown-menu" id="src-menu">
                            {% for k in langs %}<div class="dropdown-option" data-value="{{ langs[k] }}">{{ k }}</div>{% endfor %}
                        </div>
                    </div>
                </div>
                
                <div class="language-group">
                    <label for="tgt">To:</label>
                    <div class="custom-select">
                        <input type="text" class="select-input" id="tgt" placeholder="Search language...">
                        <div class="dropdown-menu" id="tgt-menu">
                            {% for k in langs %}<div class="dropdown-option" data-value="{{ langs[k] }}">{{ k }}</div>{% endfor %}
                        </div>
                    </div>
                </div>
            </div>
            
            <input type="hidden" name="src" id="src-hidden">
            <input type="hidden" name="tgt" id="tgt-hidden">
            
            <button type="submit">Translate</button>
        </form>
        
        {% if result %}
        <div class="result-container show">
            <h3>✓ Translated Text:</h3>
            <p>{{ result }}</p>
        </div>
        {% endif %}
    </div>
    
    <script>
        // Searchable dropdown functionality
        function setupSearchableSelect(inputId, menuId, hiddenInputId) {
            const input = document.getElementById(inputId);
            const menu = document.getElementById(menuId);
            const hiddenInput = document.getElementById(hiddenInputId);
            const options = menu.querySelectorAll('.dropdown-option');
            let currentFocus = -1;
            
            // Open menu on click
            input.addEventListener('click', (e) => {
                e.stopPropagation();
                menu.classList.toggle('open');
                currentFocus = -1;
            });
            
            // Filter options while typing
            input.addEventListener('input', (e) => {
                const searchTerm = e.target.value.toLowerCase();
                currentFocus = -1;
                
                options.forEach(option => {
                    const text = option.textContent.toLowerCase();
                    if (text.includes(searchTerm)) {
                        option.classList.remove('hidden');
                    } else {
                        option.classList.add('hidden');
                    }
                });
            });
            
            // Handle option selection
            options.forEach(option => {
                option.addEventListener('click', (e) => {
                    e.stopPropagation();
                    input.value = option.textContent;
                    hiddenInput.value = option.getAttribute('data-value');
                    menu.classList.remove('open');
                    
                    // Update selected state
                    options.forEach(opt => opt.classList.remove('selected'));
                    option.classList.add('selected');
                });
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', (e) => {
                if (!e.target.closest('.custom-select')) {
                    menu.classList.remove('open');
                }
            });
        }
        
        // Initialize both dropdowns
        setupSearchableSelect('src', 'src-menu', 'src-hidden');
        setupSearchableSelect('tgt', 'tgt-menu', 'tgt-hidden');
        
        // Set initial values if form was submitted
        document.addEventListener('DOMContentLoaded', () => {
            const form = document.querySelector('form');
            if (form) {
                form.addEventListener('submit', (e) => {
                    if (!document.getElementById('src-hidden').value) {
                        e.preventDefault();
                        alert('Please select a source language');
                        return;
                    }
                    if (!document.getElementById('tgt-hidden').value) {
                        e.preventDefault();
                        alert('Please select a target language');
                        return;
                    }
                });
            }
        });
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        result = translate(
            request.form["text"],
            request.form["src"],
            request.form["tgt"]
        )
    return render_template_string(HTML, result=result, langs=LANGUAGES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)