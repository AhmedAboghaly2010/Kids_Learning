import streamlit as st
import random
import time

# ==========================================
# إعدادات الصفحة الرئيسية
# ==========================================
st.set_page_config(
    page_title="🚀 كودي - تعلم البرمجة",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# التصميم والألوان
# ==========================================
st.markdown("""
<style>
    /* استيراد خط عربي جميل */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap');

    /* إعدادات عامة */
    * {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
    }

    /* الشريط الجانبي */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%) !important;
        border-left: 3px solid #f9ca24;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* العنوان الرئيسي */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #f9ca24, #f0932b, #eb4d4b, #6c5ce7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { filter: drop-shadow(0 0 10px #f9ca2488); }
        to { filter: drop-shadow(0 0 25px #f0932b88); }
    }

    .hero-subtitle {
        font-size: 1.4rem;
        color: #dfe6e9;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* بطاقات الدروس */
    .lesson-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03));
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 0.8rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        text-align: center;
    }

    .lesson-card:hover {
        transform: translateY(-5px);
        border-color: #f9ca24;
        box-shadow: 0 10px 30px rgba(249, 202, 36, 0.2);
    }

    .lesson-emoji {
        font-size: 3rem;
        display: block;
        margin-bottom: 0.5rem;
    }

    .lesson-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: #f9ca24;
        margin-bottom: 0.3rem;
    }

    .lesson-desc {
        font-size: 0.95rem;
        color: #b2bec3;
    }

    /* بطاقة المعلومات */
    .info-box {
        background: linear-gradient(135deg, rgba(108, 92, 231, 0.3), rgba(72, 52, 212, 0.2));
        border: 2px solid #6c5ce7;
        border-radius: 15px;
        padding: 1.2rem;
        margin: 1rem 0;
        color: white;
    }

    .info-box h3 {
        color: #a29bfe !important;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }

    /* بطاقة النجاح */
    .success-box {
        background: linear-gradient(135deg, rgba(0, 184, 148, 0.3), rgba(0, 206, 201, 0.2));
        border: 2px solid #00b894;
        border-radius: 15px;
        padding: 1.2rem;
        margin: 1rem 0;
        color: white;
        text-align: center;
    }

    /* بطاقة التحذير */
    .tip-box {
        background: linear-gradient(135deg, rgba(253, 203, 110, 0.25), rgba(249, 202, 36, 0.15));
        border: 2px solid #f9ca24;
        border-radius: 15px;
        padding: 1.2rem;
        margin: 1rem 0;
        color: white;
    }

    .tip-box h3 {
        color: #f9ca24 !important;
        font-size: 1.2rem;
    }

    /* بطاقة الخطأ/التحدي */
    .challenge-box {
        background: linear-gradient(135deg, rgba(232, 67, 147, 0.25), rgba(225, 112, 85, 0.15));
        border: 2px solid #e84393;
        border-radius: 15px;
        padding: 1.2rem;
        margin: 1rem 0;
        color: white;
    }

    /* الكود */
    .code-display {
        background: #1e1e2e;
        border: 1px solid #6c5ce7;
        border-radius: 12px;
        padding: 1.2rem;
        font-family: 'Courier New', monospace !important;
        color: #cdd6f4;
        font-size: 1rem;
        direction: ltr;
        text-align: left;
        margin: 1rem 0;
        overflow-x: auto;
        line-height: 1.7;
    }

    /* شريط التقدم */
    .progress-container {
        background: rgba(255,255,255,0.1);
        border-radius: 50px;
        padding: 4px;
        margin: 0.5rem 0;
    }

    /* النجوم */
    .stars-display {
        font-size: 2rem;
        text-align: center;
        padding: 0.5rem;
    }

    /* زر كبير */
    .stButton > button {
        background: linear-gradient(135deg, #f9ca24, #f0932b) !important;
        color: #1a1a2e !important;
        font-family: 'Tajawal', sans-serif !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(249, 202, 36, 0.4) !important;
    }

    /* العنوان الجانبي */
    .sidebar-header {
        text-align: center;
        font-size: 1.8rem;
        font-weight: 900;
        color: #f9ca24;
        padding: 1rem 0;
        border-bottom: 2px solid rgba(249,202,36,0.3);
        margin-bottom: 1rem;
    }

    /* بطاقة الإنجاز */
    .achievement {
        background: linear-gradient(135deg, rgba(253,203,110,0.2), rgba(249,202,36,0.1));
        border: 1px solid #f9ca24;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        margin: 0.3rem 0;
        font-size: 0.9rem;
        color: #fdcb6e;
    }

    /* النص الأبيض العام */
    .white-text { color: white; }
    h1, h2, h3, h4 { color: white !important; }
    p { color: #dfe6e9; }

    /* البطاقة الكبيرة للدرس */
    .lesson-header {
        background: linear-gradient(135deg, rgba(108,92,231,0.4), rgba(72,52,212,0.2));
        border: 2px solid #6c5ce7;
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .lesson-header h1 {
        font-size: 2.5rem !important;
        font-weight: 900;
    }

    /* خيارات الكويز */
    .quiz-option {
        background: rgba(255,255,255,0.06);
        border: 2px solid rgba(255,255,255,0.15);
        border-radius: 12px;
        padding: 0.8rem 1.2rem;
        margin: 0.4rem 0;
        color: white;
        cursor: pointer;
        transition: all 0.2s;
        font-size: 1rem;
    }

    .quiz-option:hover {
        border-color: #f9ca24;
        background: rgba(249,202,36,0.1);
    }

    /* التصحيح */
    div[data-testid="stSelectbox"] {
        direction: rtl;
    }
    div[data-testid="stSelectbox"] * {
        color: white !important;
        background: #1a1a2e !important;
    }

    /* منطقة الكود */
    .stTextArea textarea {
        background: #1e1e2e !important;
        color: #cdd6f4 !important;
        font-family: 'Courier New', monospace !important;
        border: 1px solid #6c5ce7 !important;
        font-size: 1rem !important;
        direction: ltr;
    }

    /* radio buttons */
    .stRadio label {
        color: white !important;
        font-size: 1rem !important;
    }

    /* تنبيهات */
    .stAlert {
        border-radius: 12px !important;
        font-family: 'Tajawal', sans-serif !important;
    }

    /* ترقيم */
    .step-number {
        display: inline-block;
        width: 35px;
        height: 35px;
        background: linear-gradient(135deg, #f9ca24, #f0932b);
        border-radius: 50%;
        text-align: center;
        line-height: 35px;
        font-weight: 900;
        color: #1a1a2e;
        margin-left: 10px;
        font-size: 1rem;
    }

    /* Streamlit elements */
    [data-testid="stMarkdown"] p { color: #dfe6e9; }
    .element-container { margin: 0.3rem 0; }
</style>
""", unsafe_allow_html=True)


# ==========================================
# بيانات الدروس
# ==========================================
LESSONS = {
    "🏠 الرئيسية": "home",
    "📚 الدرس ١: ما هي البرمجة؟": "lesson1",
    "🎨 الدرس ٢: المتغيرات": "lesson2",
    "🔀 الدرس ٣: الشروط": "lesson3",
    "🔄 الدرس ٤: الحلقات": "lesson4",
    "🎯 الدرس ٥: الدوال": "lesson5",
    "🎮 ملعب الكود": "playground",
    "🏆 إنجازاتي": "achievements",
}

# ==========================================
# حالة البرنامج (تذكر التقدم)
# ==========================================
if "stars" not in st.session_state:
    st.session_state.stars = 0
if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = []
if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {}
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"


# ==========================================
# الشريط الجانبي
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-header">🤖 كودي</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#b2bec3; font-size:0.9rem;">مساعدك في تعلم البرمجة!</p>', unsafe_allow_html=True)

    # عرض النجوم
    stars_icons = "⭐" * min(st.session_state.stars, 20)
    st.markdown(f"""
    <div style="background: rgba(249,202,36,0.15); border: 1px solid #f9ca24;
         border-radius: 12px; padding: 0.8rem; text-align:center; margin-bottom:1rem;">
        <div style="font-size:1.8rem;">{stars_icons if stars_icons else "✨"}</div>
        <div style="color:#f9ca24; font-weight:900; font-size:1.3rem;">{st.session_state.stars} نجمة</div>
        <div style="color:#b2bec3; font-size:0.8rem;">نجومك المكتسبة</div>
    </div>
    """, unsafe_allow_html=True)

    # شريط التقدم
    total_lessons = 5
    completed = len(st.session_state.completed_lessons)
    progress_pct = int((completed / total_lessons) * 100)
    st.markdown(f"""
    <div style="margin-bottom:1rem;">
        <div style="color:#dfe6e9; font-size:0.9rem; margin-bottom:0.3rem;">
            📊 تقدمك: {completed}/{total_lessons} دروس
        </div>
        <div style="background:rgba(255,255,255,0.1); border-radius:50px; height:10px;">
            <div style="background:linear-gradient(90deg,#f9ca24,#f0932b);
                 width:{progress_pct}%; height:10px; border-radius:50px;
                 transition: width 0.5s ease;"></div>
        </div>
        <div style="color:#f9ca24; font-size:0.85rem; text-align:center; margin-top:0.3rem;">{progress_pct}%</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # قائمة التنقل
    for label, page_id in LESSONS.items():
        is_completed = page_id.replace("lesson", "") in [l.replace("lesson", "") for l in st.session_state.completed_lessons]
        completed_icon = " ✅" if page_id in st.session_state.completed_lessons else ""
        if st.button(f"{label}{completed_icon}", key=f"nav_{page_id}"):
            st.session_state.current_page = page_id
            st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; color:#636e72; font-size:0.8rem; padding:0.5rem;">
        🌟 صُنع بحب للأطفال العرب<br>
        للأعمار من ٦ إلى ١٠ سنوات
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# دالة إضافة النجوم
# ==========================================
def add_stars(n, reason=""):
    st.session_state.stars += n
    if reason:
        st.balloons()
        st.success(f"🌟 رائع! حصلت على {n} نجمة{'ات' if n > 1 else ''}! - {reason}")


# ==========================================
# الصفحة الرئيسية
# ==========================================
def show_home():
    st.markdown("""
    <div class="hero-title">🚀 مرحباً في كودي!</div>
    <div class="hero-subtitle">تعلم البرمجة بطريقة ممتعة وسهلة 🎉</div>
    """, unsafe_allow_html=True)

    # بطاقات ترحيبية
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="lesson-card">
            <span class="lesson-emoji">🎓</span>
            <div class="lesson-title">٥ دروس ممتعة</div>
            <div class="lesson-desc">تعلم البرمجة خطوة بخطوة</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="lesson-card">
            <span class="lesson-emoji">🎮</span>
            <div class="lesson-title">العب وتعلم</div>
            <div class="lesson-desc">اكتب كودك واشوف النتيجة مباشرة</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="lesson-card">
            <span class="lesson-emoji">🏆</span>
            <div class="lesson-title">اجمع النجوم</div>
            <div class="lesson-desc">اكسب نجوم لكل درس تكمله</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # الدروس المتاحة
    st.markdown('<h2 style="color:#f9ca24; text-align:center;">📚 الدروس المتاحة</h2>', unsafe_allow_html=True)

    lessons_info = [
        ("lesson1", "١", "📚", "ما هي البرمجة؟", "افهم ما هي البرمجة وكيف تعمل الحاسوب"),
        ("lesson2", "٢", "🎨", "المتغيرات", "تعلم كيف تحفظ المعلومات في البرنامج"),
        ("lesson3", "٣", "🔀", "الشروط", "خلّي برنامجك يتخذ قرارات ذكية"),
        ("lesson4", "٤", "🔄", "الحلقات", "كرر الأوامر بطريقة ذكية وسهلة"),
        ("lesson5", "٥", "🎯", "الدوال", "اصنع أوامرك الخاصة في البرنامج"),
    ]

    for page_id, num, emoji, title, desc in lessons_info:
        is_done = page_id in st.session_state.completed_lessons
        status = "✅ مكتمل" if is_done else "▶️ ابدأ"
        border_color = "#00b894" if is_done else "#6c5ce7"

        col_a, col_b = st.columns([4, 1])
        with col_a:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,rgba(255,255,255,0.07),rgba(255,255,255,0.02));
                 border:2px solid {border_color}; border-radius:15px; padding:1rem;
                 margin:0.4rem 0; display:flex; align-items:center; gap:1rem;">
                <span style="font-size:2.5rem;">{emoji}</span>
                <div>
                    <div style="color:#f9ca24; font-weight:800; font-size:1.1rem;">الدرس {num}: {title}</div>
                    <div style="color:#b2bec3; font-size:0.9rem;">{desc}</div>
                </div>
                <div style="margin-right:auto; color:{'#00b894' if is_done else '#a29bfe'}; font-weight:700;">{status}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            if st.button("🚀 ادخل", key=f"home_{page_id}"):
                st.session_state.current_page = page_id
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # نصيحة اليوم
    tips = [
        "💡 البرمجة مثل اللعبة، كل ما مارست كل ما بقيت أحسن!",
        "💡 لا تخاف من الأخطاء، الأخطاء بتعلمك أكتر!",
        "💡 كل البرامج الكبيرة بدأت بكود صغير!",
        "💡 المبرمج الجيد هو اللي بيسأل دايماً 'ليه؟'",
        "💡 خذ راحة كل ساعة لعقلك يشتغل أحسن!",
    ]
    st.markdown(f"""
    <div class="tip-box">
        <h3>💫 نصيحة اليوم</h3>
        <p>{random.choice(tips)}</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# الدرس الأول: ما هي البرمجة؟
# ==========================================
def show_lesson1():
    st.markdown("""
    <div class="lesson-header">
        <div style="font-size:4rem;">📚</div>
        <h1>الدرس الأول: ما هي البرمجة؟</h1>
        <p style="color:#a29bfe; font-size:1.1rem;">هنتعلم إيه هي البرمجة وليه هي مهمة</p>
    </div>
    """, unsafe_allow_html=True)

    # الشرح
    st.markdown("""
    <div class="info-box">
        <h3>🤔 البرمجة هي إيه؟</h3>
        <p>
        تخيل إنك بتكلم روبوت 🤖<br><br>
        الروبوت مش بيفهم عربي ولا إنجليزي... بيفهم بس <strong style="color:#a29bfe;">أوامر محددة</strong>!<br><br>
        البرمجة هي إننا بنكتب <strong style="color:#f9ca24;">أوامر</strong> للحاسوب بلغة يفهمها،
        علشان يعمل اللي إحنا عايزينه تمام! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    # مثال حياتي
    st.markdown("""
    <div class="tip-box">
        <h3>🎂 مثال من حياتنا: وصفة الكيكة!</h3>
        <p>
        لما ماما بتعمل كيكة، بتتبع خطوات محددة:<br>
        <strong>١.</strong> اجلب الطحين 🌾<br>
        <strong>٢.</strong> أضف البيض 🥚<br>
        <strong>٣.</strong> أضف السكر 🍚<br>
        <strong>٤.</strong> اخبز لمدة ٣٠ دقيقة 🔥<br><br>
        البرمجة نفس الفكرة تماماً! بنكتب خطوات للحاسوب يتبعها.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # أمر بايثون أول
    st.markdown('<h3 style="color:#f9ca24;">👨‍💻 أول أمر في البرمجة!</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <h3>الأمر print 🖨️</h3>
        <p>الأمر <strong style="color:#f9ca24;">print</strong> معناه "اطبع" أو "اعرض"<br>
        بيخلي الحاسوب يكتب أي كلام على الشاشة!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="code-display">
<span style="color:#cba6f7"># ده أول كود بتكتبه!</span>
<br>
<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"مرحباً يا عالم!"</span>)
<br>
<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"أنا بتعلم البرمجة"</span>)
<br>
<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"هأبقى مبرمج محترف 🚀"</span>)
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h4 style="color:#00b894;">📤 النتيجة اللي هتشوفها:</h4>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#1e1e2e; border:1px solid #00b894; border-radius:12px;
         padding:1rem; direction:rtl; margin:0.5rem 0;">
        <p style="color:#a6e3a1; margin:0; font-family:monospace; direction:rtl;">
        مرحباً يا عالم!<br>
        أنا بتعلم البرمجة<br>
        هأبقى مبرمج محترف 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)

    # حقائق ممتعة
    st.markdown('<h3 style="color:#f9ca24;">🌍 حقائق ممتعة عن البرمجة!</h3>', unsafe_allow_html=True)

    facts = [
        ("🎮", "الألعاب اللي بتلعبها زي فورتنايت وماينكرافت، كلها مبرمجة!"),
        ("📱", "التطبيقات على موبايلك زي يوتيوب وواتساب، كلها برمجة!"),
        ("🤖", "الروبوتات بتتحرك بسبب برمجة ذكية!"),
        ("🚗", "عربيات المستقبل بتسوق لوحدها بسبب البرمجة!"),
        ("🏥", "الأطباء بيستخدموا برمجة علشان يشخصوا الأمراض!"),
    ]

    for emoji, fact in facts:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.05); border-right:4px solid #6c5ce7;
             border-radius:0 12px 12px 0; padding:0.7rem 1rem; margin:0.4rem 0; color:white;">
            {emoji} {fact}
        </div>
        """, unsafe_allow_html=True)

    # كويز
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="challenge-box">
        <h3>🧠 اختبر نفسك!</h3>
        <p>جاوب السؤال الجاي وهتكسب نجوم! ⭐</p>
    </div>
    """, unsafe_allow_html=True)

    q1 = st.radio(
        "سؤال ١: الأمر print بيعمل إيه في البرمجة؟",
        ["🔴 بيمسح الكود", "🟡 بيطبع ويعرض كلام على الشاشة", "🔵 بيحسب الأرقام", "🟢 بيحفظ الملفات"],
        key="l1_q1"
    )

    q2 = st.radio(
        "سؤال ٢: البرمجة تشبه إيه من الأمثلة دي؟",
        ["🔴 اللعب بالكرة", "🟡 وصفة الطبخ اللي بنتبع خطواتها", "🔵 الرسم على الورق", "🟢 الغناء"],
        key="l1_q2"
    )

    if st.button("✅ تحقق من إجاباتي!", key="check_l1"):
        score = 0
        if "بيطبع ويعرض" in q1:
            score += 1
        if "وصفة الطبخ" in q2:
            score += 1

        if score == 2:
            st.markdown("""
            <div class="success-box">
                <h3>🎉 ممتاز جداً! إجاباتك كلها صح!</h3>
                <p>حصلت على ٣ نجوم! ⭐⭐⭐</p>
            </div>
            """, unsafe_allow_html=True)
            if "lesson1" not in st.session_state.completed_lessons:
                st.session_state.completed_lessons.append("lesson1")
                add_stars(3, "أكملت الدرس الأول!")
        elif score == 1:
            st.warning("🌟 إجابة واحدة صح! كمّل راجع الدرس وحاول تاني")
            add_stars(1, "مش بأس، حاول تاني!")
        else:
            st.error("😊 مش مهم! راجع الدرس كويس وحاول تاني. إنت تقدر!")


# ==========================================
# الدرس الثاني: المتغيرات
# ==========================================
def show_lesson2():
    st.markdown("""
    <div class="lesson-header">
        <div style="font-size:4rem;">🎨</div>
        <h1>الدرس الثاني: المتغيرات</h1>
        <p style="color:#a29bfe; font-size:1.1rem;">تعلم كيف تحفظ المعلومات في برنامجك!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>📦 المتغير هو إيه؟</h3>
        <p>
        تخيل عندك <strong style="color:#f9ca24;">صندوق</strong> 📦 بتحط فيه أي حاجة!<br><br>
        المتغير هو صندوق في الحاسوب بتحط فيه معلومة وتديه اسم تعرفه بيه.<br><br>
        مثلاً: صندوق اسمه <strong style="color:#a29bfe;">"اسمي"</strong> وجواه كلمة <strong style="color:#a6e3a1;">"أحمد"</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # أنواع المتغيرات
    st.markdown('<h3 style="color:#f9ca24;">🎨 أنواع المتغيرات</h3>', unsafe_allow_html=True)

    types_data = [
        ("#a6e3a1", "📝 النص (String)", 'اسمي = "أحمد"', "بتحط فيه كلام أو جمل"),
        ("#89b4fa", "🔢 الرقم الصحيح (Integer)", "عمري = 8", "بتحط فيه أرقام بدون فواصل"),
        ("#fab387", "💯 الرقم العشري (Float)", "طولي = 1.35", "بتحط فيه أرقام بفاصلة"),
        ("#f38ba8", "✅ الصح والغلط (Boolean)", "أنا_طالب = True", "بتحط فيه صح True أو غلط False"),
    ]

    for color, type_name, example, desc in types_data:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.05); border:1px solid {color};
             border-radius:12px; padding:1rem; margin:0.5rem 0;">
            <div style="color:{color}; font-weight:800; font-size:1.1rem; margin-bottom:0.5rem;">{type_name}</div>
            <div style="color:#cdd6f4; font-family:monospace; direction:ltr; text-align:left;
                 background:#1e1e2e; padding:0.5rem; border-radius:8px; margin:0.3rem 0;">{example}</div>
            <div style="color:#b2bec3; font-size:0.9rem; margin-top:0.3rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    # مثال كامل
    st.markdown('<h3 style="color:#f9ca24;">👨‍💻 مثال كامل: بطاقة تعريف!</h3>', unsafe_allow_html=True)

    st.markdown("""
    <div class="code-display">
<span style="color:#cba6f7"># بطاقة تعريفي الشخصية</span>
<br><br>
<span style="color:#cdd6f4">اسمي</span> = <span style="color:#a6e3a1">"أحمد محمد"</span>
<br>
<span style="color:#cdd6f4">عمري</span> = <span style="color:#fab387">9</span>
<br>
<span style="color:#cdd6f4">مدرستي</span> = <span style="color:#a6e3a1">"مدرسة النيل"</span>
<br>
<span style="color:#cdd6f4">أحب_البرمجة</span> = <span style="color:#f38ba8">True</span>
<br><br>
<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"اسمي: "</span>, اسمي)
<br>
<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"عمري: "</span>, عمري, <span style="color:#a6e3a1">"سنوات"</span>)
<br>
<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"مدرستي: "</span>, مدرستي)
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h4 style="color:#00b894;">📤 النتيجة:</h4>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#1e1e2e; border:1px solid #00b894; border-radius:12px; padding:1rem; margin:0.5rem 0;">
        <p style="color:#a6e3a1; margin:0; font-family:monospace; direction:rtl;">
        اسمي: أحمد محمد<br>
        عمري: 9 سنوات<br>
        مدرستي: مدرسة النيل
        </p>
    </div>
    """, unsafe_allow_html=True)

    # تجربة تفاعلية
    st.markdown("""
    <div class="tip-box">
        <h3>✍️ اكتب بطاقتك الشخصية!</h3>
        <p>دخّل بياناتك وشوف برنامجك يشتغل!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        my_name = st.text_input("✏️ اسمك:", placeholder="مثلاً: أحمد", key="my_name")
        my_age = st.number_input("🎂 عمرك:", min_value=6, max_value=10, value=8, key="my_age")
    with col2:
        my_school = st.text_input("🏫 مدرستك:", placeholder="مثلاً: مدرسة الأمل", key="my_school")
        my_hobby = st.text_input("⚽ هوايتك:", placeholder="مثلاً: كرة القدم", key="my_hobby")

    if st.button("🚀 شغّل برنامجي!", key="run_l2"):
        if my_name:
            st.markdown(f"""
            <div style="background:#1e1e2e; border:2px solid #a6e3a1; border-radius:12px;
                 padding:1.5rem; margin:1rem 0; direction:rtl;">
                <div style="color:#a6e3a1; font-size:1.1rem; font-weight:700; margin-bottom:1rem;">
                    🖥️ ناتج برنامجك:
                </div>
                <div style="color:#cdd6f4; font-size:1.1rem; line-height:2;">
                    👤 اسمي: <strong style="color:#a6e3a1;">{my_name}</strong><br>
                    🎂 عمري: <strong style="color:#fab387;">{my_age}</strong> سنوات<br>
                    🏫 مدرستي: <strong style="color:#89b4fa;">{my_school if my_school else 'لم تكتب'}</strong><br>
                    ⚽ هوايتي: <strong style="color:#cba6f7;">{my_hobby if my_hobby else 'لم تكتب'}</strong><br>
                    💻 أحب البرمجة: <strong style="color:#f38ba8;">True ✅</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if "lesson2" not in st.session_state.completed_lessons:
                st.session_state.completed_lessons.append("lesson2")
                add_stars(3, "برنامجك شغّال! أكملت الدرس الثاني! 🎉")
        else:
            st.warning("✏️ اكتب اسمك الأول!")


# ==========================================
# الدرس الثالث: الشروط
# ==========================================
def show_lesson3():
    st.markdown("""
    <div class="lesson-header">
        <div style="font-size:4rem;">🔀</div>
        <h1>الدرس الثالث: الشروط</h1>
        <p style="color:#a29bfe; font-size:1.1rem;">خلّي برنامجك يفكر ويتخذ قرارات!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>🤔 الشروط هي إيه؟</h3>
        <p>
        تخيل إنك واقف قدام مطعم 🍕<br><br>
        <strong>لو</strong> عندك فلوس → تدخل وتاكل 🎉<br>
        <strong>غير كده</strong> → ترجع البيت جعان 😢<br><br>
        ده بالظبط اللي بتعمله <strong style="color:#f9ca24;">الشروط</strong> في البرمجة!<br>
        بتقول للبرنامج: <strong style="color:#a29bfe;">"لو كده اعمل كده... وإلا اعمل كده!"</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # الكلمات المفتاحية
    st.markdown('<h3 style="color:#f9ca24;">🔑 الكلمات المفتاحية</h3>', unsafe_allow_html=True)

    keywords = [
        ("#89dceb", "if", "لو / إذا", "لو الشرط صح، اعمل كده"),
        ("#a6e3a1", "elif", "أو لو / أو إذا", "لو الشرط التاني صح"),
        ("#f38ba8", "else", "غير كده / وإلا", "لو كل الشروط غلط"),
    ]

    cols = st.columns(3)
    for col, (color, keyword, arabic, desc) in zip(cols, keywords):
        with col:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.06); border:2px solid {color};
                 border-radius:15px; padding:1rem; text-align:center; height:140px;">
                <div style="color:{color}; font-size:1.8rem; font-weight:900; font-family:monospace;">{keyword}</div>
                <div style="color:#f9ca24; font-size:1.1rem; font-weight:800; margin:0.3rem 0;">{arabic}</div>
                <div style="color:#b2bec3; font-size:0.85rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # مثال
    st.markdown('<h3 style="color:#f9ca24;">👨‍💻 مثال: درجاتك في الامتحان</h3>', unsafe_allow_html=True)

    st.markdown("""
    <div class="code-display">
<span style="color:#cba6f7"># برنامج بيقولك نتيجتك في الامتحان</span>
<br><br>
<span style="color:#cdd6f4">درجتي</span> = <span style="color:#fab387">85</span>
<br><br>
<span style="color:#89b4fa">if</span> درجتي >= <span style="color:#fab387">90</span>:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"ممتاز! أنت نجم! ⭐"</span>)
<br>
<span style="color:#89b4fa">elif</span> درجتي >= <span style="color:#fab387">75</span>:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"جيد جداً! كمّل كده! 👍"</span>)
<br>
<span style="color:#89b4fa">elif</span> درجتي >= <span style="color:#fab387">60</span>:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"جيد! قدر على نفسك! 💪"</span>)
<br>
<span style="color:#89b4fa">else</span>:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"مش مهم! ذاكر أكتر! 📚"</span>)
    </div>
    """, unsafe_allow_html=True)

    # تجربة تفاعلية
    st.markdown("""
    <div class="tip-box">
        <h3>🎮 جرب بنفسك!</h3>
        <p>اختار درجة وشوف البرنامج يحكمله بنفسه!</p>
    </div>
    """, unsafe_allow_html=True)

    grade = st.slider("📊 اختار الدرجة:", 0, 100, 75, key="grade_slider")

    if st.button("🔍 اعرف نتيجتك!", key="check_grade"):
        if grade >= 90:
            result = "ممتاز! أنت نجم! ⭐"
            color = "#f9ca24"
            bg = "rgba(249,202,36,0.2)"
        elif grade >= 75:
            result = "جيد جداً! كمّل كده! 👍"
            color = "#00b894"
            bg = "rgba(0,184,148,0.2)"
        elif grade >= 60:
            result = "جيد! قدر على نفسك! 💪"
            color = "#74b9ff"
            bg = "rgba(116,185,255,0.2)"
        else:
            result = "مش مهم! ذاكر أكتر! 📚"
            color = "#fd79a8"
            bg = "rgba(253,121,168,0.2)"

        st.markdown(f"""
        <div style="background:{bg}; border:2px solid {color};
             border-radius:15px; padding:1.5rem; text-align:center; margin:1rem 0;">
            <div style="font-size:1.5rem; color:{color}; font-weight:900;">
                درجتك: {grade}/100
            </div>
            <div style="font-size:1.3rem; color:white; margin-top:0.5rem;">
                {result}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if "lesson3" not in st.session_state.completed_lessons:
            st.session_state.completed_lessons.append("lesson3")
            add_stars(3, "فهمت الشروط! عظيم! 🎉")

    # علامات المقارنة
    st.markdown('<h3 style="color:#f9ca24;">⚖️ علامات المقارنة</h3>', unsafe_allow_html=True)

    comparisons = [
        ("==", "يساوي بالظبط", '٥ == ٥'),
        ("!=", "مش يساوي", '٥ != ٦'),
        (">", "أكبر من", '١٠ > ٥'),
        ("<", "أصغر من", '٣ < ٧'),
        (">=", "أكبر من أو يساوي", '٥ >= ٥'),
        ("<=", "أصغر من أو يساوي", '٤ <= ٥'),
    ]

    cols = st.columns(3)
    for i, (symbol, meaning, example) in enumerate(comparisons):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.05); border:1px solid #6c5ce7;
                 border-radius:10px; padding:0.7rem; text-align:center; margin:0.3rem 0;">
                <div style="color:#a29bfe; font-size:1.5rem; font-weight:900; font-family:monospace;">{symbol}</div>
                <div style="color:#f9ca24; font-size:0.9rem; font-weight:700;">{meaning}</div>
                <div style="color:#74b9ff; font-size:0.85rem; font-family:monospace;">{example}</div>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# الدرس الرابع: الحلقات
# ==========================================
def show_lesson4():
    st.markdown("""
    <div class="lesson-header">
        <div style="font-size:4rem;">🔄</div>
        <h1>الدرس الرابع: الحلقات</h1>
        <p style="color:#a29bfe; font-size:1.1rem;">كرر الأوامر بذكاء بدون ما تتعب!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>🔄 الحلقات هي إيه؟</h3>
        <p>
        تخيل إن المدرس قالك اكتب جملة "سأذاكر بجد" ١٠٠ مرة! 📝<br><br>
        ده تعب كتير! الحلقات بتخلي الحاسوب يعمل ده في ثانية واحدة! ⚡<br><br>
        الحلقة بتقول للبرنامج: <strong style="color:#f9ca24;">"كرر الأمر ده ... مرة!"</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # نوعان من الحلقات
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background:rgba(137,180,250,0.15); border:2px solid #89b4fa;
             border-radius:15px; padding:1rem; height:160px;">
            <div style="color:#89b4fa; font-size:1.5rem; font-weight:900; font-family:monospace;">for</div>
            <div style="color:#f9ca24; font-weight:800; font-size:1.1rem;">حلقة for</div>
            <div style="color:#b2bec3; font-size:0.9rem; margin-top:0.5rem;">
                لما بتعرف عدد التكرارات<br>
                مثلاً: "كرر ١٠ مرات"
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:rgba(166,227,161,0.15); border:2px solid #a6e3a1;
             border-radius:15px; padding:1rem; height:160px;">
            <div style="color:#a6e3a1; font-size:1.5rem; font-weight:900; font-family:monospace;">while</div>
            <div style="color:#f9ca24; font-weight:800; font-size:1.1rem;">حلقة while</div>
            <div style="color:#b2bec3; font-size:0.9rem; margin-top:0.5rem;">
                لما مش عارف عدد التكرارات<br>
                مثلاً: "طول ما ... استمر"
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # مثال حلقة for
    st.markdown('<h3 style="color:#f9ca24;">👨‍💻 مثال ١: حلقة for</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class="code-display">
<span style="color:#cba6f7"># طباعة أرقام من ١ لـ ٥</span>
<br><br>
<span style="color:#89b4fa">for</span> رقم <span style="color:#89b4fa">in</span> <span style="color:#fab387">range</span>(<span style="color:#fab387">1</span>, <span style="color:#fab387">6</span>):
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"الرقم الحالي: "</span>, رقم)
<br><br>
<span style="color:#cba6f7"># النتيجة:</span>
<br>
<span style="color:#cba6f7"># الرقم الحالي: 1</span>
<br>
<span style="color:#cba6f7"># الرقم الحالي: 2</span>
<br>
<span style="color:#cba6f7"># الرقم الحالي: 3</span>
<br>
<span style="color:#cba6f7"># ... وهكذا لـ 5</span>
    </div>
    """, unsafe_allow_html=True)

    # تجربة تفاعلية
    st.markdown("""
    <div class="tip-box">
        <h3>🎮 شوف الحلقة تشتغل!</h3>
        <p>اختار عدد التكرارات وشوف البرنامج يطبعها!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        repeat_count = st.slider("🔢 كم مرة تكرر؟", 1, 10, 5, key="repeat_count")
    with col2:
        repeat_text = st.text_input("✏️ الجملة اللي تتكرر:", value="أنا بتعلم البرمجة! 🚀", key="repeat_text")

    if st.button("▶️ شغّل الحلقة!", key="run_loop"):
        output_lines = []
        for i in range(1, repeat_count + 1):
            output_lines.append(f"<span style='color:#fab387'>مرة {i}:</span> <span style='color:#a6e3a1'>{repeat_text}</span>")

        output_html = "<br>".join(output_lines)
        st.markdown(f"""
        <div style="background:#1e1e2e; border:2px solid #a6e3a1; border-radius:12px;
             padding:1.5rem; margin:1rem 0; direction:rtl; max-height:300px; overflow-y:auto;">
            <div style="color:#a6e3a1; font-weight:700; margin-bottom:0.8rem; font-size:1.1rem;">
                🖥️ ناتج الحلقة ({repeat_count} مرات):
            </div>
            <div style="font-family:monospace; line-height:1.8; font-size:0.95rem;">
                {output_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if "lesson4" not in st.session_state.completed_lessons:
            st.session_state.completed_lessons.append("lesson4")
            add_stars(3, "تعلمت الحلقات! برافو عليك! 🔄")

    # جدول الضرب
    st.markdown('<h3 style="color:#f9ca24;">🎯 تحدي: جدول الضرب!</h3>', unsafe_allow_html=True)

    num = st.selectbox("اختار رقم لجدول ضربه:", list(range(1, 11)), key="times_table")

    if st.button("📊 اعرض جدول الضرب!", key="show_table"):
        table_html = ""
        for i in range(1, 11):
            result = num * i
            table_html += f"""
            <div style="display:flex; justify-content:space-between; padding:0.4rem 1rem;
                 background:rgba({'249,202,36' if i % 2 == 0 else '108,92,231'}, 0.1);
                 border-radius:8px; margin:0.2rem 0; direction:ltr;">
                <span style="color:#fab387;">{num}</span>
                <span style="color:#b2bec3;">×</span>
                <span style="color:#89b4fa;">{i}</span>
                <span style="color:#b2bec3;">=</span>
                <span style="color:#a6e3a1; font-weight:900; font-size:1.1rem;">{result}</span>
            </div>
            """

        st.markdown(f"""
        <div style="background:#1e1e2e; border:2px solid #f9ca24; border-radius:15px;
             padding:1.5rem; margin:1rem 0; max-width:400px;">
            <div style="color:#f9ca24; font-weight:900; font-size:1.3rem;
                 text-align:center; margin-bottom:1rem;">
                📊 جدول ضرب {num}
            </div>
            {table_html}
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# الدرس الخامس: الدوال
# ==========================================
def show_lesson5():
    st.markdown("""
    <div class="lesson-header">
        <div style="font-size:4rem;">🎯</div>
        <h1>الدرس الخامس: الدوال</h1>
        <p style="color:#a29bfe; font-size:1.1rem;">اصنع أوامرك الخاصة وكودك هيبقى أسهل!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>🎯 الدالة هي إيه؟</h3>
        <p>
        تخيل إن عندك <strong style="color:#f9ca24;">زرار سحري</strong> 🪄<br><br>
        كل ما تضغط عليه، يعمل حاجات كتيرة في خطوة واحدة!<br><br>
        الدالة زي الزرار ده:
        <strong style="color:#a29bfe;">بتعمل مجموعة أوامر لما تناديها بالاسم!</strong><br><br>
        مثلاً: بدل ما تكتب كود الترحيب ١٠ مرات، تكتبه مرة في دالة وتناديها ١٠ مرات!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # طريقة كتابة الدالة
    st.markdown('<h3 style="color:#f9ca24;">📝 طريقة كتابة الدالة</h3>', unsafe_allow_html=True)

    steps = [
        ("#89b4fa", "def", "اكتب def - اختصار define يعني عرّف"),
        ("#f9ca24", "اسم_الدالة", "اختار اسم للدالة"),
        ("#a6e3a1", "()", "الأقواس - ممكن تحط فيها مدخلات"),
        ("#f38ba8", ":", "النقتين مهمة جداً! لا تنساها!"),
        ("#cba6f7", "    الكود", "اكتب الكود بمسافة 4 فراغات جوا الدالة"),
    ]

    for color, code, desc in steps:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:1rem; padding:0.5rem 0;
             border-bottom:1px solid rgba(255,255,255,0.05);">
            <span style="color:{color}; font-family:monospace; font-size:1.1rem;
                  font-weight:900; min-width:150px; direction:ltr;">{code}</span>
            <span style="color:#dfe6e9; font-size:0.95rem;">{desc}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # مثال بسيط
    st.markdown('<h3 style="color:#f9ca24;">👨‍💻 مثال: دالة الترحيب</h3>', unsafe_allow_html=True)

    st.markdown("""
    <div class="code-display">
<span style="color:#cba6f7"># تعريف الدالة</span>
<br>
<span style="color:#89b4fa">def</span> <span style="color:#f9ca24">رحّب</span>(اسم):
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"أهلاً يا "</span>, اسم, <span style="color:#a6e3a1">"! 👋"</span>)
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"يسعدنا إنك معانا في كودي!"</span>)
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"━━━━━━━━━━━━━━━━━━"</span>)
<br><br>
<span style="color:#cba6f7"># نادي الدالة</span>
<br>
<span style="color:#f9ca24">رحّب</span>(<span style="color:#a6e3a1">"أحمد"</span>)
<br>
<span style="color:#f9ca24">رحّب</span>(<span style="color:#a6e3a1">"سارة"</span>)
<br>
<span style="color:#f9ca24">رحّب</span>(<span style="color:#a6e3a1">"مريم"</span>)
    </div>
    """, unsafe_allow_html=True)

    # دالة بإرجاع قيمة
    st.markdown('<h3 style="color:#f9ca24;">⭐ دالة بترجع نتيجة</h3>', unsafe_allow_html=True)

    st.markdown("""
    <div class="code-display">
<span style="color:#cba6f7"># دالة بتحسب مجموع عددين</span>
<br>
<span style="color:#89b4fa">def</span> <span style="color:#f9ca24">اجمع</span>(رقم١, رقم٢):
<br>
&nbsp;&nbsp;&nbsp;&nbsp;المجموع = رقم١ + رقم٢
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#89b4fa">return</span> المجموع  <span style="color:#cba6f7"># return معناها "أرجع النتيجة"</span>
<br><br>
<span style="color:#cba6f7"># استخدام الدالة</span>
<br>
ناتج = <span style="color:#f9ca24">اجمع</span>(<span style="color:#fab387">5</span>, <span style="color:#fab387">3</span>)
<br>
<span style="color:#89b4fa">print</span>(<span style="color:#a6e3a1">"المجموع: "</span>, ناتج)  <span style="color:#cba6f7"># ناتج: 8</span>
    </div>
    """, unsafe_allow_html=True)

    # تجربة تفاعلية
    st.markdown("""
    <div class="tip-box">
        <h3>🧮 آلة حاسبة بالدوال!</h3>
        <p>جرب تشتغل مع الدوال بنفسك!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("الرقم الأول:", value=10, key="func_n1")
    with col2:
        operation = st.selectbox("العملية:", ["➕ جمع", "➖ طرح", "✖️ ضرب", "➗ قسمة"], key="func_op")
    with col3:
        num2 = st.number_input("الرقم الثاني:", value=5, key="func_n2")

    if st.button("🎯 نادي الدالة!", key="call_func"):
        if "جمع" in operation:
            result = num1 + num2
            op_symbol = "+"
        elif "طرح" in operation:
            result = num1 - num2
            op_symbol = "-"
        elif "ضرب" in operation:
            result = num1 * num2
            op_symbol = "×"
        else:
            if num2 != 0:
                result = round(num1 / num2, 2)
                op_symbol = "÷"
            else:
                st.error("⚠️ ما ينفعش نقسم على صفر!")
                return

        st.markdown(f"""
        <div class="success-box">
            <div style="font-size:1.3rem; font-weight:900;">🎉 الدالة شغّالت!</div>
            <div style="font-size:2rem; margin:0.5rem 0; font-family:monospace; color:#00b894;">
                {num1} {op_symbol} {num2} = <strong>{result}</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if "lesson5" not in st.session_state.completed_lessons:
            st.session_state.completed_lessons.append("lesson5")
            add_stars(3, "تعلمت الدوال! أنت مبرمج حقيقي! 🎯")


# ==========================================
# ملعب الكود
# ==========================================
def show_playground():
    st.markdown("""
    <div class="lesson-header">
        <div style="font-size:4rem;">🎮</div>
        <h1>ملعب الكود</h1>
        <p style="color:#a29bfe; font-size:1.1rem;">اكتب كودك وشوف النتيجة مباشرة!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
        <h3>💡 تعليمات ملعب الكود</h3>
        <p>
        ١. اكتب كود بايثون في المساحة الجوه ⬇️<br>
        ٢. اضغط زرار "شغّل الكود" ▶️<br>
        ٣. شوف النتيجة على الشاشة 🖥️<br><br>
        <strong style="color:#f9ca24;">⚠️ ملاحظة: الكود يشتغل على السيرفر، مش على جهازك مباشرة</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # أمثلة جاهزة
    st.markdown('<h3 style="color:#f9ca24;">📋 أمثلة جاهزة - اضغط عليها!</h3>', unsafe_allow_html=True)

    examples = {
        "👋 مرحباً بالعالم": '# أول برنامج في تاريخ البرمجة!\nprint("مرحباً يا عالم!")\nprint("أنا بتعلم بايثون!")',
        "🔢 الجمع والطرح": 'a = 15\nb = 7\nprint("الجمع:", a + b)\nprint("الطرح:", a - b)\nprint("الضرب:", a * b)',
        "🔄 جدول الضرب": 'num = 5\nprint(f"جدول ضرب {num}:")\nfor i in range(1, 11):\n    print(f"{num} x {i} = {num * i}")',
        "⭐ نجوم متصاعدة": 'for i in range(1, 6):\n    print("⭐" * i)',
        "🎲 رقم عشوائي": 'import random\nprint("أرقام عشوائية:")\nfor i in range(5):\n    num = random.randint(1, 100)\n    print(f"رقم {i+1}: {num}")',
    }

    cols = st.columns(len(examples))
    for col, (label, code) in zip(cols, examples.items()):
        with col:
            if st.button(label, key=f"example_{label}"):
                st.session_state.playground_code = code
                st.rerun()

    # منطقة الكود
    default_code = getattr(st.session_state, 'playground_code',
                           '# اكتب كودك هنا!\n# مثلاً:\nprint("مرحباً يا عالم! 🌍")\n\n# جرب تكتب كودك الخاص 👇\n')

    code_input = st.text_area(
        "✏️ اكتب كودك هنا:",
        value=default_code,
        height=200,
        key="code_editor"
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        run_btn = st.button("▶️ شغّل الكود!", key="run_code")

    if run_btn and code_input:
        st.markdown('<h4 style="color:#00b894;">📤 ناتج الكود:</h4>', unsafe_allow_html=True)

        # تشغيل الكود بأمان
        import io
        import contextlib

        output_capture = io.StringIO()
        error_occurred = False
        error_msg = ""

        try:
            with contextlib.redirect_stdout(output_capture):
                exec(code_input, {"__builtins__": {
                    "print": print,
                    "range": range,
                    "len": len,
                    "int": int,
                    "float": float,
                    "str": str,
                    "bool": bool,
                    "list": list,
                    "dict": dict,
                    "input": lambda x="": "",
                    "abs": abs,
                    "max": max,
                    "min": min,
                    "sum": sum,
                    "round": round,
                    "type": type,
                    "__import__": __import__,
                }})
            output = output_capture.getvalue()
        except Exception as e:
            error_occurred = True
            error_msg = str(e)
            output = output_capture.getvalue()

        if output:
            # تحويل النص لـ HTML
            output_html = output.replace("\n", "<br>").replace(" ", "&nbsp;")
            st.markdown(f"""
            <div style="background:#1e1e2e; border:2px solid #a6e3a1; border-radius:12px;
                 padding:1.5rem; margin:0.5rem 0; direction:rtl; min-height:80px;">
                <div style="color:#cdd6f4; font-family:monospace; font-size:1rem;
                     direction:rtl; line-height:1.8;">
                    {output_html}
                </div>
            </div>
            """, unsafe_allow_html=True)

        if error_occurred:
            st.markdown(f"""
            <div style="background:rgba(243,139,168,0.2); border:2px solid #f38ba8;
                 border-radius:12px; padding:1rem; margin:0.5rem 0;">
                <div style="color:#f38ba8; font-weight:700; margin-bottom:0.5rem;">❌ في خطأ في الكود:</div>
                <div style="color:#cdd6f4; font-family:monospace; direction:ltr;">{error_msg}</div>
                <div style="color:#b2bec3; font-size:0.9rem; margin-top:0.5rem;">
                    💡 تحقق من الكتابة وحاول تاني - الأخطاء بتعلم!
                </div>
            </div>
            """, unsafe_allow_html=True)

        if not error_occurred:
            add_stars(1, "كتبت كوداً شغّال! 💻")


# ==========================================
# صفحة الإنجازات
# ==========================================
def show_achievements():
    st.markdown("""
    <div class="lesson-header">
        <div style="font-size:4rem;">🏆</div>
        <h1>إنجازاتي</h1>
        <p style="color:#a29bfe; font-size:1.1rem;">شوف كل اللي حققته لحد دلوقتي!</p>
    </div>
    """, unsafe_allow_html=True)

    # ملخص النجوم
    stars = st.session_state.stars
    level = "مبتدئ 🌱" if stars < 5 else "متوسط ⚡" if stars < 10 else "متقدم 🔥" if stars < 20 else "خبير 🚀"

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,rgba(249,202,36,0.3),rgba(240,147,43,0.2));
         border:3px solid #f9ca24; border-radius:25px; padding:2rem; text-align:center; margin:1rem 0;">
        <div style="font-size:4rem; margin-bottom:0.5rem;">⭐</div>
        <div style="font-size:3rem; font-weight:900; color:#f9ca24;">{stars} نجمة</div>
        <div style="font-size:1.5rem; color:#fdcb6e; font-weight:700; margin-top:0.5rem;">
            مستواك: {level}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # الدروس المكتملة
    st.markdown('<h3 style="color:#f9ca24;">📚 الدروس المكتملة</h3>', unsafe_allow_html=True)

    lesson_names = {
        "lesson1": ("📚", "الدرس الأول: ما هي البرمجة؟"),
        "lesson2": ("🎨", "الدرس الثاني: المتغيرات"),
        "lesson3": ("🔀", "الدرس الثالث: الشروط"),
        "lesson4": ("🔄", "الدرس الرابع: الحلقات"),
        "lesson5": ("🎯", "الدرس الخامس: الدوال"),
    }

    for lesson_id, (emoji, name) in lesson_names.items():
        is_done = lesson_id in st.session_state.completed_lessons
        if is_done:
            st.markdown(f"""
            <div style="background:rgba(0,184,148,0.2); border:2px solid #00b894;
                 border-radius:12px; padding:1rem; margin:0.4rem 0;
                 display:flex; align-items:center; gap:1rem;">
                <span style="font-size:2rem;">{emoji}</span>
                <span style="color:white; font-weight:700; font-size:1.1rem; flex:1;">{name}</span>
                <span style="color:#00b894; font-size:1.5rem;">✅</span>
                <span style="color:#f9ca24; font-weight:900;">+٣ ⭐</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1);
                 border-radius:12px; padding:1rem; margin:0.4rem 0;
                 display:flex; align-items:center; gap:1rem; opacity:0.6;">
                <span style="font-size:2rem; filter:grayscale(1);">{emoji}</span>
                <span style="color:#b2bec3; font-size:1.1rem; flex:1;">{name}</span>
                <span style="color:#636e72;">🔒 لم يكتمل</span>
            </div>
            """, unsafe_allow_html=True)

    # الإنجازات الخاصة
    st.markdown('<h3 style="color:#f9ca24; margin-top:1.5rem;">🏅 الأوسمة والميداليات</h3>', unsafe_allow_html=True)

    badges = [
        (stars >= 1, "🌱", "أول خطوة", "كسبت أول نجمة!"),
        (stars >= 5, "⭐", "نجم متألق", "جمعت ٥ نجوم!"),
        (stars >= 10, "🔥", "على النار", "جمعت ١٠ نجوم!"),
        (stars >= 15, "💎", "ماسي", "جمعت ١٥ نجمة!"),
        (len(st.session_state.completed_lessons) >= 3, "📚", "محب العلم", "أكملت ٣ دروس!"),
        (len(st.session_state.completed_lessons) == 5, "🏆", "بطل البرمجة", "أكملت كل الدروس!"),
        ("lesson1" in st.session_state.completed_lessons, "👶", "أول خطواتي", "فهمت ما هي البرمجة!"),
        ("lesson5" in st.session_state.completed_lessons, "🧙", "مبرمج حقيقي", "تعلمت الدوال!"),
    ]

    cols = st.columns(4)
    for i, (earned, emoji, title, desc) in enumerate(badges):
        with cols[i % 4]:
            opacity = "1" if earned else "0.3"
            border = "#f9ca24" if earned else "#636e72"
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.05); border:2px solid {border};
                 border-radius:15px; padding:1rem; text-align:center;
                 margin:0.4rem 0; opacity:{opacity};">
                <div style="font-size:2.5rem;">{emoji}</div>
                <div style="color:#f9ca24; font-weight:800; font-size:0.9rem; margin:0.3rem 0;">{title}</div>
                <div style="color:#b2bec3; font-size:0.75rem;">{desc}</div>
                {"<div style='color:#00b894; font-size:0.8rem; margin-top:0.3rem;'>✅ مكتسب!</div>" if earned else "<div style='color:#636e72; font-size:0.8rem; margin-top:0.3rem;'>🔒 لم تكسبه</div>"}
            </div>
            """, unsafe_allow_html=True)

    # تشجيع
    if len(st.session_state.completed_lessons) < 5:
        remaining = 5 - len(st.session_state.completed_lessons)
        st.markdown(f"""
        <div class="info-box" style="margin-top:1.5rem; text-align:center;">
            <h3>💪 استمر يا بطل!</h3>
            <p>بقيلك {remaining} درس{'وس' if remaining > 2 else ''} بس وتكمل رحلتك! 🚀</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.balloons()
        st.markdown("""
        <div class="success-box" style="margin-top:1.5rem;">
            <h3>🎉🏆🎉 مبروك! أكملت كل الدروس!</h3>
            <p>أنت الآن مبرمج صغير حقيقي! استمر في التعلم والتطوير! 🚀</p>
        </div>
        """, unsafe_allow_html=True)

    # زرار إعادة التعيين
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 ابدأ من جديد (مسح التقدم)", key="reset"):
        st.session_state.stars = 0
        st.session_state.completed_lessons = []
        st.session_state.quiz_scores = {}
        st.rerun()


# ==========================================
# عرض الصفحة المختارة
# ==========================================
page = st.session_state.current_page

if page == "home":
    show_home()
elif page == "lesson1":
    show_lesson1()
elif page == "lesson2":
    show_lesson2()
elif page == "lesson3":
    show_lesson3()
elif page == "lesson4":
    show_lesson4()
elif page == "lesson5":
    show_lesson5()
elif page == "playground":
    show_playground()
elif page == "achievements":
    show_achievements()
