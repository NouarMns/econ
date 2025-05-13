
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import numpy as np

# تعيين العنوان والتخطيط
st.set_page_config(
    page_title="مسار التخصص في القياس الاقتصادي وعلم البيانات",
    page_icon="📊",
    layout="wide"
)

# تحديد النمط العام للصفحة
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');

    * {
        font-family: 'Tajawal', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #1E3A8A;
        font-weight: 700;
        text-align: right;
    }

    p, li {
        text-align: right;
        font-size: 18px;
        line-height: 1.6;
    }

    .main {
        direction: rtl;
    }

    .stTabs [data-baseweb="tab-list"] {
        direction: rtl;
    }

    .stTabs [data-baseweb="tab"] {
        font-size: 20px;
        font-weight: bold;
    }

    .resource-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-right: 5px solid #4361ee;
    }

    .section-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .highlighted {
        background-color: #e6f3ff;
        padding: 10px;
        border-radius: 5px;
        border-right: 3px solid #3182ce;
    }
</style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center;'>الدليل الشامل للتخصص في القياس الاقتصادي وعلم البيانات</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>خريطة طريق متكاملة للباحثين والمتخصصين الطموحين</p>",
            unsafe_allow_html=True)

# إنشاء تبويبات للتنقل بين الأقسام المختلفة
tabs = st.tabs([
    "نظرة عامة",
    "القياس الاقتصادي",
    "علم البيانات",
    "المسارات التعليمية",
    "المهارات المطلوبة",
    "المصادر والمراجع"
])

# التبويب الأول: نظرة عامة
with tabs[0]:
    st.markdown("<h2>مقدمة في علم البيانات والقياس الاقتصادي</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        تتقاطع مجالات القياس الاقتصادي وتحليل البيانات وعلم البيانات في كثير من النقاط، وتشكل معًا مجموعة متكاملة من المهارات المطلوبة بشدة في سوق العمل الحديث.

        إن فهم العلاقة بين هذه المجالات واكتساب المهارات اللازمة لكل منها يمكن أن يفتح آفاقًا واسعة في عالم البحث العلمي والتطبيقات العملية في مختلف القطاعات.
        """)

        st.markdown('<div class="highlighted">', unsafe_allow_html=True)
        st.markdown("""
        **ملاحظة هامة**: يتطلب التميز في هذه المجالات مزيجًا من الأسس النظرية القوية والخبرة العملية المستمرة. هذا الدليل يهدف إلى تقديم خارطة طريق متكاملة تساعدك على بناء مسار مهني ناجح.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # إنشاء مخطط دائري لتوضيح تداخل المجالات
        labels = ['الإحصاء', 'الاقتصاد', 'علوم الحاسب', 'الرياضيات', 'معرفة المجال']
        values = [25, 20, 25, 15, 15]
        colors = ['#4361ee', '#3a0ca3', '#7209b7', '#f72585', '#4cc9f0']

        fig = px.pie(
            values=values,
            names=labels,
            title="المهارات الأساسية المطلوبة",
            color_discrete_sequence=colors,
            hole=0.4
        )
        fig.update_layout(
            font=dict(size=14, family="Tajawal"),
            legend=dict(orientation="h", y=-0.1)
        )
        st.plotly_chart(fig, use_container_width=True)

    # مقارنة بين المجالات
    st.markdown("<h3>مقارنة بين المجالات الثلاثة</h3>", unsafe_allow_html=True)

    comparison_data = {
        'المجال': ['القياس الاقتصادي', 'تحليل البيانات', 'علم البيانات'],
        'التركيز الأساسي': [
            'تحليل البيانات الاقتصادية واختبار النظريات الاقتصادية',
            'استخراج الرؤى والاتجاهات من البيانات',
            'بناء النماذج التنبؤية والخوارزميات المتقدمة'
        ],
        'المهارات الأساسية': [
            'إحصاء، اقتصاد، نمذجة قياسية',
            'إحصاء، برمجة، تصور البيانات',
            'إحصاء، تعلم آلي، برمجة متقدمة'
        ],
        'الأدوات': [
            'R, STATA, EViews, Python',
            'SQL, Excel, Power BI, Tableau, Python',
            'Python, R, TensorFlow, PyTorch, Spark'
        ]
    }

    df_comparison = pd.DataFrame(comparison_data)

    st.table(df_comparison.set_index('المجال'))

    # مخطط تطور الطلب على المهارات
    st.markdown("<h3>تطور الطلب على المهارات في سوق العمل</h3>", unsafe_allow_html=True)

    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    econometrics = [70, 75, 80, 83, 85, 88, 90, 92]
    data_analysis = [75, 82, 88, 92, 95, 97, 98, 99]
    data_science = [80, 85, 90, 93, 95, 97, 98, 99]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years, y=econometrics,
        mode='lines+markers',
        name='القياس الاقتصادي',
        line=dict(color='#4361ee', width=3)
    ))

    fig.add_trace(go.Scatter(
        x=years, y=data_analysis,
        mode='lines+markers',
        name='تحليل البيانات',
        line=dict(color='#3a0ca3', width=3)
    ))

    fig.add_trace(go.Scatter(
        x=years, y=data_science,
        mode='lines+markers',
        name='علم البيانات',
        line=dict(color='#7209b7', width=3)
    ))

    fig.update_layout(
        title='تطور الطلب على المهارات (2018-2025)',
        xaxis_title='السنة',
        yaxis_title='مؤشر الطلب (100-0)',
        legend=dict(orientation="h", y=1.1),
        font=dict(family="Tajawal", size=14),
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

# التبويب الثاني: القياس الاقتصادي
with tabs[1]:
    st.markdown("<h2>مسار التخصص في القياس الاقتصادي (Econometrics)</h2>", unsafe_allow_html=True)

    st.markdown("""
    القياس الاقتصادي هو فرع من الاقتصاد يركز على تطبيق الأساليب الإحصائية والرياضية لاختبار النظريات الاقتصادية وقياس العلاقات بين المتغيرات الاقتصادية.
    """)

    # تعريف مكونات القياس الاقتصادي
    components = {
        'النماذج الاقتصادية': 'بناء نماذج نظرية تمثل العلاقات الاقتصادية',
        'المنهجية الإحصائية': 'تطبيق الأدوات الإحصائية لتقدير معالم النماذج',
        'تحليل البيانات': 'معالجة وتحليل البيانات الاقتصادية المختلفة',
        'تفسير النتائج': 'شرح النتائج وتقديم توصيات للسياسات الاقتصادية'
    }

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("<h3>مكونات القياس الاقتصادي</h3>", unsafe_allow_html=True)

        for component, desc in components.items():
            st.markdown(f"**{component}**: {desc}")

    with col2:
        # مخطط للمهارات المطلوبة في القياس الاقتصادي
        skills = ['الإحصاء', 'النظرية الاقتصادية', 'الرياضيات', 'البرمجة', 'تحليل البيانات']
        importance = [95, 90, 85, 75, 80]

        fig = px.bar(
            x=importance,
            y=skills,
            orientation='h',
            title='أهمية المهارات في القياس الاقتصادي',
            color=importance,
            color_continuous_scale='blues',
            text=importance
        )

        fig.update_layout(
            xaxis_title='مستوى الأهمية (100-0)',
            yaxis_title='المهارة',
            font=dict(family="Tajawal", size=14)
        )

        st.plotly_chart(fig, use_container_width=True)

    # المواضيع الأساسية في القياس الاقتصادي
    st.markdown("<h3>المواضيع الأساسية في القياس الاقتصادي</h3>", unsafe_allow_html=True)

    topics = [
        {
            'title': 'الانحدار الخطي (Linear Regression)',
            'desc': 'أساس تحليل العلاقات بين المتغيرات، يشمل OLS، GLS، والمتغيرات الصورية.',
            'depth': 'أساسي'
        },
        {
            'title': 'نماذج السلاسل الزمنية (Time Series Models)',
            'desc': 'تحليل البيانات عبر الزمن، يشمل ARIMA، GARCH، اختبارات السكون، والتكامل المشترك.',
            'depth': 'متقدم'
        },
        {
            'title': 'نماذج البيانات المقطعية (Panel Data)',
            'desc': 'تحليل البيانات عبر الوحدات والزمن، يشمل الآثار الثابتة والعشوائية.',
            'depth': 'متقدم'
        },
        {
            'title': 'المعادلات الآنية (Simultaneous Equations)',
            'desc': 'نمذجة العلاقات المتبادلة بين المتغيرات، يشمل 2SLS، 3SLS.',
            'depth': 'متقدم'
        },
        {
            'title': 'الاقتصاد القياسي غير المعلمي (Nonparametric Econometrics)',
            'desc': 'أساليب تحليل دون افتراضات قوية حول توزيع البيانات.',
            'depth': 'متخصص'
        },
        {
            'title': 'تقييم الأثر (Impact Evaluation)',
            'desc': 'قياس تأثير السياسات والبرامج باستخدام مناهج مثل RCT، DID، RDD.',
            'depth': 'متقدم'
        }
    ]

    # عرض المواضيع في جدول
    topics_df = pd.DataFrame(topics)

    colors = {
        'أساسي': '#e6f3ff',
        'متقدم': '#d0e8ff',
        'متخصص': '#b8dcff'
    }

    # تطبيق تنسيق الألوان
    def highlight_depth(val):
        return f'background-color: {colors.get(val, "#ffffff")}'

    st.dataframe(
        topics_df.style.map(highlight_depth, subset=['depth']).set_properties(**{'text-align': 'right'}) # CORRECTED: applymap to map
    )

    # مسار التعلم المقترح
    st.markdown("<h3>المسار المقترح للتخصص في القياس الاقتصادي</h3>", unsafe_allow_html=True)

    learning_path = [
        {
            'المرحلة': 'المرحلة الأولى: الأساسيات',
            'المواد': 'الإحصاء، الاحتمالات، الجبر الخطي، الاقتصاد الجزئي والكلي',
            'المدة': '6-12 شهر'
        },
        {
            'المرحلة': 'المرحلة الثانية: أساسيات القياس',
            'المواد': 'نماذج الانحدار، الاختبارات الإحصائية، تفسير النتائج',
            'المدة': '3-6 أشهر'
        },
        {
            'المرحلة': 'المرحلة الثالثة: تقنيات متقدمة',
            'المواد': 'السلاسل الزمنية، البيانات المقطعية، المعادلات الآنية',
            'المدة': '6-12 شهر'
        },
        {
            'المرحلة': 'المرحلة الرابعة: التطبيقات',
            'المواد': 'دراسات حالة، مشاريع عملية، تحليلات لبيانات حقيقية',
            'المدة': '6+ أشهر'
        },
        {
            'المرحلة': 'المرحلة الخامسة: التخصص',
            'المواد': 'التعمق في مجال محدد (مالي، تنموي، بيئي، إلخ)',
            'المدة': 'مستمر'
        }
    ]

    learning_path_df = pd.DataFrame(learning_path)
    st.table(learning_path_df.set_index('المرحلة'))

    # نصائح للباحثين المبتدئين
    st.markdown("<h3>نصائح للباحثين المبتدئين في القياس الاقتصادي</h3>", unsafe_allow_html=True)

    st.markdown("""
    1. **ابدأ بالأساسيات النظرية**: تأكد من فهمك العميق للإحصاء والاقتصاد قبل الخوض في تقنيات متقدمة.

    2. **اتقن لغة برمجة واحدة على الأقل**: يفضل R أو Python، مع التركيز على الحزم المتخصصة.

    3. **اقرأ الأوراق البحثية**: اطلع باستمرار على الأبحاث الحديثة في مجال تخصصك.

    4. **مارس التطبيق العملي**: حاول تكرار نتائج الأبحاث المنشورة باستخدام نفس البيانات.

    5. **شارك في المجتمعات العلمية**: انضم للمؤتمرات والمنتديات الأكاديمية لتوسيع شبكة علاقاتك.
    """)

    # البرامج والأدوات الأساسية
    st.markdown("<h3>البرامج والأدوات الأساسية في القياس الاقتصادي</h3>", unsafe_allow_html=True)

    tools = {
        'STATA': ['برنامج شائع في البحوث الاقتصادية', 90],
        'R': ['مفتوح المصدر، يحوي حزم متخصصة للقياس الاقتصادي', 85],
        'EViews': ['متخصص في تحليل السلاسل الزمنية', 75],
        'Python': ['متعدد الاستخدامات مع مكتبات StatsModels, Scikit-learn', 80],
        'MATLAB': ['قوي في النمذجة الرياضية والمحاكاة', 65],
        'SPSS': ['يستخدم أحيانًا في التحليلات البسيطة', 50],
        'Julia': ['لغة حديثة سريعة خاصة بالحوسبة العلمية', 40]
    }

    tools_df = pd.DataFrame({
        'الأداة': list(tools.keys()),
        'الوصف': [v[0] for v in tools.values()],
        'الانتشار': [v[1] for v in tools.values()]
    })

    fig = px.bar(
        tools_df,
        x='الانتشار',
        y='الأداة',
        orientation='h',
        title='مدى انتشار الأدوات في مجال القياس الاقتصادي',
        text='الانتشار',
        color='الانتشار',
        color_continuous_scale='blues'
    )

    fig.update_layout(
        font=dict(family="Tajawal", size=14),
        xaxis_title='مستوى الانتشار (100-0)'
    )

    st.plotly_chart(fig, use_container_width=True)

# التبويب الثالث: علم البيانات
with tabs[2]:
    st.markdown("<h2>مسار التطور كمحلل بيانات وعالم بيانات</h2>", unsafe_allow_html=True)

    st.markdown("""
    يعتبر علم البيانات من المجالات سريعة النمو التي تجمع بين الإحصاء وعلوم الحاسب والخبرة المجالية. يتخصص محللو البيانات وعلماء البيانات في استخراج المعرفة والرؤى القيمة من البيانات.
    """)

    # الفرق بين محلل البيانات وعالم البيانات
    st.markdown("<h3>الفرق بين محلل البيانات وعالم البيانات</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h4 style='text-align: center;'>محلل البيانات</h4>", unsafe_allow_html=True)
        st.markdown("""
        - يركز على تحليل البيانات واستخراج الرؤى
        - يستخدم أدوات تحليلية وإحصائية
        - يعمل مع بيانات منظمة غالبًا
        - مهارات برمجة متوسطة
        - يركز على تحليل وتفسير البيانات الحالية
        - الخلفية غالبًا في الإحصاء أو إدارة الأعمال
        """)

    with col2:
        st.markdown("<h4 style='text-align: center;'>عالم البيانات</h4>", unsafe_allow_html=True)
        st.markdown("""
        - يبني نماذج تنبؤية وخوارزميات متقدمة
        - يعمل في التعلم الآلي والذكاء الاصطناعي
        - يتعامل مع بيانات منظمة وغير منظمة
        - مهارات برمجة متقدمة
        - يبني أنظمة تتنبأ بالمستقبل
        - الخلفية غالبًا في علوم الحاسب أو الرياضيات
        """)

    # مخطط فين لتوضيح التداخل
    st.markdown("<h3>العلاقة بين المجالات</h3>", unsafe_allow_html=True)

    # إنشاء بيانات لمخطط scatter لتمثيل مخطط فين
    n = 1000
    circles = pd.DataFrame({
        'x': np.concatenate([
            np.random.normal(-1, 0.5, n),  # دائرة محلل البيانات
            np.random.normal(1, 0.5, n),  # دائرة عالم البيانات
            np.random.normal(0, 0.3, n)  # التداخل
        ]),
        'y': np.concatenate([
            np.random.normal(0, 0.5, n),
            np.random.normal(0, 0.5, n),
            np.random.normal(0, 0.5, n)
        ]),
        'group': np.concatenate([
            ['محلل بيانات'] * n,
            ['عالم بيانات'] * n,
            ['مشترك'] * n
        ])
    })

    fig = px.scatter(
        circles,
        x='x',
        y='y',
        color='group',
        opacity=0.6,
        color_discrete_map={
            'محلل بيانات': '#4361ee',
            'عالم بيانات': '#7209b7',
            'مشترك': '#4cc9f0'
        },
        title='العلاقة بين محلل البيانات وعالم البيانات'
    )

    fig.update_layout(
        showlegend=True,
        font=dict(family="Tajawal", size=14),
        xaxis=dict(showticklabels=False),
        yaxis=dict(showticklabels=False)
    )

    # إضافة نصوص على المخطط
    fig.add_annotation(
        x=-1.5, y=0,
        text="تحليل البيانات<br>الإحصاء التقليدي<br>تصور البيانات",
        showarrow=False,
        font=dict(family="Tajawal", size=14)
    )

    fig.add_annotation(
        x=1.5, y=0,
        text="تعلم آلي متقدم<br>معالجة لغة طبيعية<br>رؤية حاسوبية",
        showarrow=False,
        font=dict(family="Tajawal", size=14)
    )

    fig.add_annotation(
        x=0, y=0,
        text="Python/R<br>إحصاء<br>SQL",
        showarrow=False,
        font=dict(family="Tajawal", size=14, color="white")
    )

    st.plotly_chart(fig, use_container_width=True)

    # المهارات المطلوبة لعالم البيانات
    st.markdown("<h3>المهارات الأساسية لعالم البيانات</h3>", unsafe_allow_html=True)

    skills = {
        'البرمجة': [
            'Python (النظام البيئي: NumPy, Pandas, Scikit-learn)',
            'R (ggplot2, dplyr, caret)',
            'SQL للتعامل مع قواعد البيانات',
            'Scala/Java (خاصة مع Apache Spark)'
        ],
        'الإحصاء والرياضيات': [
            'الإحصاء الاستدلالي والوصفي',
            'نظرية الاحتمالات',
            'الجبر الخطي',
            'حساب التفاضل والتكامل',
            'التحسين (Optimization)'
        ],
        'التعلم الآلي': [
            'تعلم خاضع للإشراف وغير خاضع للإشراف',
            'شبكات عصبية ونماذج عميقة',
            'معالجة اللغة الطبيعية',
            'الرؤية الحاسوبية',
            'ضبط النماذج وتقييمها'
        ],
        'معالجة البيانات': [
            'تنظيف البيانات وإعدادها',
            'هندسة الخصائص (Feature Engineering)',
            'التعامل مع البيانات غير المتوازنة والقيم المفقودة',
            'تقليل الأبعاد',
            'التعامل مع البيانات الكبيرة'
        ],
        'تصور البيانات': [
            'Matplotlib, Seaborn, Plotly في Python',
            'ggplot2 في R',
            'Tableau, Power BI',
            'D3.js للتصورات التفاعلية'
        ],
        'بيئة العمل': [
            'أنظمة التحكم بالإصدارات (Git)',
            'Docker والحاويات',
            'Cloud Computing (AWS, Azure, GCP)',
            'تطوير وتشغيل النماذج (MLOps)'
        ]
    }

    col1, col2 = st.columns(2)

    for i, (category, items) in enumerate(skills.items()):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"<h4>{category}</h4>", unsafe_allow_html=True)
            for item in items:
                st.markdown(f"- {item}")

    # مراحل مشروع علم البيانات النموذجي
    st.markdown("<h3>مراحل مشروع علم البيانات النموذجي</h3>", unsafe_allow_html=True)

    stages = [
        "فهم المشكلة",
        "جمع البيانات",
        "استكشاف البيانات وتحليلها",
        "تنظيف البيانات وإعدادها",
        "هندسة الخصائص",
        "بناء النموذج",
        "تقييم النموذج",
        "ضبط النموذج",
        "نشر النموذج",
        "المراقبة والصيانة"
    ]

    stages_desc = [
        "تحديد أهداف المشروع والمشكلة المراد حلها",
        "تحديد مصادر البيانات وجمعها من مختلف المصادر",
        "فهم البيانات وتحليل الخصائص والعلاقات",
        "معالجة القيم المفقودة والشاذة وتوحيد البيانات",
        "تحويل البيانات الخام إلى خصائص مفيدة",
        "اختيار خوارزميات مناسبة وتدريب النماذج",
        "قياس أداء النموذج باستخدام مقاييس مختلفة",
        "تحسين الخصائص ومعلمات النموذج",
        "تشغيل النموذج في بيئة الإنتاج",
        "متابعة أداء النموذج وتحديثه حسب الحاجة"
    ]

    # إنشاء مخطط لمراحل المشروع
    stages_df = pd.DataFrame({
        'المرحلة': stages,
        'الوصف': stages_desc,
        'المرحلة_رقم': list(range(1, len(stages) + 1))
    })

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=stages_df['المرحلة_رقم'],
        y=[1] * len(stages_df),
        mode='markers+text',
        marker=dict(
            size=30,
            color=['#4361ee', '#4361ee', '#3a0ca3', '#3a0ca3',
                   '#7209b7', '#7209b7', '#f72585', '#f72585',
                   '#4cc9f0', '#4cc9f0'],
            symbol='circle',
            line=dict(width=2, color='white')
        ),
        text=stages_df['المرحلة_رقم'],
        textfont=dict(color='white', size=14, family='Tajawal'),
        name=''
    ))

    # إضافة التسميات للمراحل
    for i, (stage, desc) in enumerate(zip(stages, stages_desc)):
        fig.add_annotation(
            x=i + 1,
            y=1.2 if i % 2 == 0 else 0.8,
            text=f"<b>{stage}</b><br>{desc}",
            showarrow=False,
            font=dict(size=12, family='Tajawal'),
            align='center',
            bgcolor='rgba(255, 255, 255, 0.8)',
            bordercolor='gray',
            borderwidth=1,
            borderpad=4,
            xanchor='center'
        )

    # إضافة السهم الذي يربط المراحل
    fig.add_shape(
        type='line',
        x0=0.5, y0=1,
        x1=len(stages) + 0.5, y1=1,
        line=dict(color='gray', width=2)
    )

    fig.update_layout(
        title='دورة حياة مشروع علم البيانات',
        showlegend=False,
        height=500,
        xaxis=dict(
            showticklabels=False,
            range=[0, len(stages) + 1]
        ),
        yaxis=dict(
            showticklabels=False,
            range=[0.5, 1.5]
        ),
        plot_bgcolor='white',
        font=dict(family='Tajawal')
    )

    st.plotly_chart(fig, use_container_width=True)

    # المسار الوظيفي المتدرج
    st.markdown("<h3>المسار الوظيفي المتدرج في مجال البيانات</h3>", unsafe_allow_html=True)

    career_path = [
        {
            'المنصب': 'محلل بيانات مبتدئ (Junior Data Analyst)',
            'الوصف': 'يركز على تنظيف البيانات وإعداد التقارير الأساسية وتصور البيانات.',
            'المهارات': 'SQL, Excel, أدوات تصور البيانات، إحصاء أساسي',
            'سنوات الخبرة': '0-2'
        },
        {
            'المنصب': 'محلل بيانات (Data Analyst)',
            'الوصف': 'يقوم بتحليلات أكثر تعقيدًا، استخراج رؤى متقدمة، وتطوير لوحات معلومات.',
            'المهارات': 'SQL متقدم، Python/R، إحصاء متوسط، تعلم آلي أساسي',
            'سنوات الخبرة': '2-4'
        },
        {
            'المنصب': 'محلل بيانات أول (Senior Data Analyst)',
            'الوصف': 'يقود مشاريع تحليلية، يدرب المحللين الجدد، ويضع استراتيجيات تحليلية.',
            'المهارات': 'برمجة متقدمة، تحليلات تنبؤية، مهارات قيادية',
            'سنوات الخبرة': '4-6'
        },
        {
            'المنصب': 'عالم بيانات مبتدئ (Junior Data Scientist)',
            'الوصف': 'يبني نماذج إحصائية وتعلم آلي بسيطة تحت إشراف.',
            'المهارات': 'تعلم آلي، إحصاء متقدم، برمجة جيدة، معرفة بالبيانات الكبيرة',
            'سنوات الخبرة': '1-3'
        },
        {
            'المنصب': 'عالم بيانات (Data Scientist)',
            'الوصف': 'يطور نماذج متقدمة، يعمل مع بيانات معقدة، يترجم المشاكل العملية إلى حلول بيانات.',
            'المهارات': 'تعلم آلي متقدم، تعلم عميق، تطوير نماذج قابلة للتشغيل',
            'سنوات الخبرة': '3-5'
        },
        {
            'المنصب': 'عالم بيانات أول (Senior Data Scientist)',
            'الوصف': 'يقود فرق علم البيانات، يضع استراتيجيات، يعمل على مشاكل بحثية متقدمة.',
            'المهارات': 'تقنيات بحثية متقدمة، إدارة الفرق، خبرة في المجال',
            'سنوات الخبرة': '5+'
        },
        {
            'المنصب': 'رئيس علماء البيانات (Chief Data Scientist)',
            'الوصف': 'يضع رؤية الشركة لاستخدام البيانات، يربط بين الأعمال والتحليلات.',
            'المهارات': 'فهم عميق للأعمال، قيادة استراتيجية، اتخاذ قرارات',
            'سنوات الخبرة': '8+'
        }
    ]

    career_df = pd.DataFrame(career_path)

    # CORRECTED: Commented out the px.timeline call as it caused an error and a table is already used.
    # fig = px.timeline(
    #     career_df,
    #     x_start='سنوات الخبرة',
    #     x_end='سنوات الخبرة',
    #     y='المنصب',
    #     color='المنصب',
    #     hover_name='المنصب',
    #     hover_data=['الوصف', 'المهارات']
    # )

    # لا يمكن استخدام timeline مع plotly express في هذه الحالة، لذا نستخدم جدول
    st.table(career_df[['المنصب', 'الوصف', 'المهارات', 'سنوات الخبرة']])

    # نصائح للمبتدئين
    st.markdown("<h3>نصائح للمبتدئين في مجال علم البيانات</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        1. **اتقن الأساسيات قبل التقنيات المتقدمة**:
           - تعلم الإحصاء والاحتمالات بشكل متين
           - اتقن Python أو R وليس مجرد المكتبات
           - افهم هيكلية البيانات وتنظيمها

        2. **ابن محفظة مشاريع شخصية**:
           - اعمل على مشاريع حقيقية حتى لو كانت صغيرة
           - شارك الكود على GitHub
           - وثق عملك ومنهجيتك

        3. **استفد من المنافسات والمجتمعات**:
           - شارك في منافسات Kaggle
           - انضم لمجتمعات مثل Stack Overflow، Reddit (r/datascience)
           - احضر مؤتمرات ولقاءات المجال
        """)

    with col2:
        st.markdown("""
        4. **تعلم باستمرار**:
           - تابع آخر الأبحاث والتقنيات
           - خذ دورات في المجالات التي تحتاج لتطوير
           - اقرأ كتب ومقالات متخصصة

        5. **انتقل من تحليل البيانات إلى علم البيانات تدريجيًا**:
           - ابدأ بمهام تحليل البيانات البسيطة
           - أضف تدريجيًا مهارات التعلم الآلي
           - تعلم أساليب النمذجة والتقييم

        6. **طور مهارات التواصل**:
           - تعلم كيفية شرح التحليلات لغير المتخصصين
           - اتقن تصور البيانات الفعال
           - عزز مهارات العرض والإقناع
        """)

# التبويب الرابع: المسارات التعليمية
with tabs[3]:
    st.markdown("<h2>المسارات التعليمية المتاحة</h2>", unsafe_allow_html=True)

    # المسارات الأكاديمية
    st.markdown("<h3>المسارات الأكاديمية</h3>", unsafe_allow_html=True)

    academic_paths = [
        {
            'المسار': 'درجة الماجستير في القياس الاقتصادي',
            'الوصف': 'برنامج متخصص يركز على النظرية والتطبيق في القياس الاقتصادي، مناسب لمن يرغب في مسار أكاديمي أو بحثي.',
            'المدة': '1-2 سنوات',
            'المميزات': 'تعمق نظري، توجيه من أكاديميين، فرص بحثية، شبكة علاقات أكاديمية',
            'النوع': 'أكاديمي'
        },
        {
            'المسار': 'درجة الدكتوراه في الاقتصاد (تخصص قياس اقتصادي)',
            'الوصف': 'مسار متقدم للغاية للباحثين الذين يرغبون في التخصص العميق والمساهمة في تطوير المجال.',
            'المدة': '4-6 سنوات',
            'المميزات': 'بحث أصيل، فرص أكاديمية، مكانة علمية، مؤهل للتدريس الجامعي',
            'النوع': 'أكاديمي'
        },
        {
            'المسار': 'ماجستير في علم البيانات',
            'الوصف': 'يجمع بين الرياضيات والإحصاء وعلوم الحاسب مع التركيز على تحليل البيانات والتعلم الآلي.',
            'المدة': '1-2 سنوات',
            'المميزات': 'أساس متكامل، مشاريع عملية، شبكة خريجين قوية، توازن بين النظرية والتطبيق',
            'النوع': 'أكاديمي'
        },
        {
            'المسار': 'ماجستير في الإحصاء التطبيقي',
            'الوصف': 'يركز على تطبيق الأساليب الإحصائية في مجالات مختلفة بما فيها الاقتصاد.',
            'المدة': '1-2 سنوات',
            'المميزات': 'أساس إحصائي قوي، مهارات تحليلية متقدمة، تطبيقات متنوعة',
            'النوع': 'أكاديمي'
        }
    ]

    # المسارات المهنية والتدريبية
    professional_paths = [
        {
            'المسار': 'شهادة محترف علم البيانات',
            'الوصف': 'برامج مكثفة تقدمها منصات متخصصة مثل Coursera وEdX والجامعات المرموقة.',
            'المدة': '3-12 شهر',
            'المميزات': 'مرونة في التعلم، تركيز على المهارات العملية، تكلفة أقل من الدرجات الأكاديمية',
            'النوع': 'مهني'
        },
        {
            'المسار': 'معسكرات تدريبية مكثفة (Bootcamps)',
            'الوصف': 'برامج مكثفة بدوام كامل تركز على المهارات العملية والمشاريع.',
            'المدة': '3-6 أشهر',
            'المميزات': 'سريع، عملي جدًا، تواصل مباشر، دعم في التوظيف',
            'النوع': 'مهني'
        },
        {
            'المسار': 'دورات متخصصة في القياس الاقتصادي',
            'الوصف': 'دورات متخصصة تقدمها مؤسسات مثل البنك الدولي وصندوق النقد الدولي.',
            'المدة': '1-4 أشهر',
            'المميزات': 'محتوى عالي الجودة، اعتراف دولي، شبكة مهنية قوية',
            'النوع': 'مهني'
        },
        {
            'المسار': 'التعلم الذاتي المنظم',
            'الوصف': 'مسار مخصص يعتمد على الدورات المفتوحة والكتب والمشاريع الشخصية.',
            'المدة': 'متغيرة (1-2 سنة)',
            'المميزات': 'مرونة كاملة، تكلفة منخفضة، تخصيص حسب الاحتياجات',
            'النوع': 'ذاتي'
        }
    ]

    all_paths = academic_paths + professional_paths
    paths_df = pd.DataFrame(all_paths)

    # تصفية حسب نوع المسار
    path_type = st.radio("اختر نوع المسار:", ["الكل", "أكاديمي", "مهني", "ذاتي"], horizontal=True)

    if path_type != "الكل":
        filtered_paths = paths_df[paths_df['النوع'] == path_type]
    else:
        filtered_paths = paths_df

    # عرض المسارات في جدول
    st.table(filtered_paths[['المسار', 'الوصف', 'المدة', 'المميزات']])

    # المنصات التعليمية الرئيسية
    st.markdown("<h3>منصات التعلم الرئيسية</h3>", unsafe_allow_html=True)

    platforms = [
        {
            'المنصة': 'Coursera',
            'التخصص': 'دورات معتمدة من جامعات عالمية في الاقتصاد والقياس وعلم البيانات',
            'التكلفة': 'مجانية للمشاهدة، مدفوعة للشهادات (~$50-$100 شهريًا)',
            'اللغة': 'الإنجليزية بشكل أساسي، بعض الدورات مترجمة'
        },
        {
            'المنصة': 'edX',
            'التخصص': 'مقررات أكاديمية معمقة من جامعات مثل MIT وHarvard في الإحصاء والاقتصاد',
            'التكلفة': 'مجانية للمشاهدة، مدفوعة للشهادات (~$50-$300 للدورة)',
            'اللغة': 'الإنجليزية بشكل أساسي'
        },
        {
            'المنصة': 'DataCamp',
            'التخصص': 'دورات تفاعلية في البرمجة وتحليل البيانات والتعلم الآلي',
            'التكلفة': 'اشتراك شهري (~$25-$33)',
            'اللغة': 'الإنجليزية'
        },
        {
            'المنصة': 'Udemy',
            'التخصص': 'دورات عملية متنوعة في الإحصاء والبرمجة وتحليل البيانات',
            'التكلفة': '$10-$20 للدورة (عند التخفيضات)',
            'اللغة': 'متعددة اللغات بما فيها العربية'
        },
        {
            'المنصة': 'LinkedIn Learning',
            'التخصص': 'دورات مهنية قصيرة في مهارات البيانات والتحليل',
            'التكلفة': 'اشتراك شهري (~$30)',
            'اللغة': 'الإنجليزية بشكل أساسي'
        },
        {
            'المنصة': 'إدراك',
            'التخصص': 'منصة عربية تقدم دورات في الإحصاء والبرمجة وعلم البيانات',
            'التكلفة': 'معظمها مجاني',
            'اللغة': 'العربية'
        },
        {
            'المنصة': 'رواق',
            'التخصص': 'محتوى عربي في مجالات متعددة بما فيها الاقتصاد والإحصاء',
            'التكلفة': 'مجاني ومدفوع',
            'اللغة': 'العربية'
        }
    ]

    platforms_df = pd.DataFrame(platforms)
    st.table(platforms_df)

    # الشهادات المهنية المعتمدة
    st.markdown("<h3>الشهادات المهنية المعتمدة</h3>", unsafe_allow_html=True)

    certifications = [
        {
            'الشهادة': 'Microsoft Certified: Data Analyst Associate',
            'الجهة': 'Microsoft',
            'الوصف': 'تؤكد القدرة على تحليل البيانات باستخدام Excel وPower BI',
            'المدة التقريبية للتحضير': '2-3 أشهر'
        },
        {
            'الشهادة': 'Google Data Analytics Professional Certificate',
            'الجهة': 'Google (via Coursera)',
            'الوصف': 'تغطي أساسيات تحليل البيانات من جمع البيانات إلى تصور النتائج',
            'المدة التقريبية للتحضير': '6 أشهر'
        },
        {
            'الشهادة': 'IBM Data Science Professional Certificate',
            'الجهة': 'IBM (via Coursera)',
            'الوصف': 'شهادة شاملة في مجال علم البيانات تغطي التحليل والخوارزميات',
            'المدة التقريبية للتحضير': '8-12 شهر'
        },
        {
            'الشهادة': 'Certified Data Scientist (CDS)',
            'الجهة': 'Data Science Council of America',
            'الوصف': 'شهادة احترافية تثبت الكفاءة في علم البيانات',
            'المدة التقريبية للتحضير': '6-9 أشهر'
        },
        {
            'الشهادة': 'SAS Certified Data Scientist',
            'الجهة': 'SAS',
            'الوصف': 'تؤكد الخبرة في تحليل البيانات باستخدام منتجات SAS',
            'المدة التقريبية للتحضير': '9-12 شهر'
        },
        {
            'الشهادة': 'Cloudera Certified Data Analyst',
            'الجهة': 'Cloudera',
            'الوصف': 'تركز على تحليل البيانات الكبيرة باستخدام نظام Hadoop',
            'المدة التقريبية للتحضير': '3-6 أشهر'
        }
    ]

    cert_df = pd.DataFrame(certifications)
    st.table(cert_df)

    # خريطة التعلم المقترحة
    st.markdown("<h3>خريطة التعلم المقترحة للمبتدئين</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        **المرحلة الأولى (3-6 أشهر): الأساسيات**
        - تعلم لغة برمجة واحدة (Python أو R)
        - أساسيات الإحصاء والاحتمالات
        - مقدمة في قواعد البيانات وSQL
        - أساسيات النظرية الاقتصادية (للمهتمين بالقياس الاقتصادي)

        **المرحلة الثانية (3-6 أشهر): التحليل والاستكشاف**
        - تعلم أدوات تنظيف ومعالجة البيانات
        - تصور البيانات والتحليل الاستكشافي
        - تطبيق الاختبارات الإحصائية
        - مقدمة في نماذج الانحدار وتقييمها

        **المرحلة الثالثة (6-9 أشهر): النمذجة والتطبيق**
        - التعلم الآلي الأساسي (للمهتمين بعلم البيانات)
        - نماذج السلاسل الزمنية (للمهتمين بالقياس الاقتصادي)
        - تطبيقات عملية ومشاريع واقعية
        - حل مشكلات عملية باستخدام البيانات

        **المرحلة الرابعة (مستمرة): التخصص**
        - التعمق في مجال محدد (تمويل، صحة، تسويق، إلخ)
        - التعلم المستمر والاطلاع على أحدث التقنيات
        - المشاركة في المجتمعات المهنية والمنافسات
        - بناء محفظة مشاريع قوية
        """)

    with col2:
        # إنشاء مخطط زمني للتعلم
        learning_timeline = {
            'المرحلة': ['الأساسيات', 'التحليل', 'النمذجة', 'التخصص'],
            'البداية': [0, 6, 12, 18],
            'النهاية': [6, 12, 18, 24],
            'المكتسبات': [3, 6, 8, 10]  # نقاط لتمثيل النمو المعرفي
        }

        df_timeline = pd.DataFrame(learning_timeline)

        fig = px.line(
            df_timeline,
            x='النهاية',
            y='المكتسبات',
            text='المرحلة',
            markers=True,
            line_shape='spline',
            title='تطور المعرفة والمهارات مع الوقت'
        )

        fig.update_traces(
            textposition='top center',
            line=dict(color='#4361ee', width=3)
        )

        fig.update_layout(
            xaxis_title='الأشهر',
            yaxis_title='مستوى المهارة',
            font=dict(family='Tajawal', size=14)
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        **ملاحظة**: هذه الخريطة مرنة، ويمكن تعديلها حسب:
        - الوقت المتاح للتعلم
        - الخلفية المعرفية السابقة
        - الأهداف المهنية
        - المجال المستهدف
        """)

# التبويب الخامس: المهارات المطلوبة
with tabs[4]:
    st.markdown("<h2>المهارات المطلوبة للتميز</h2>", unsafe_allow_html=True)

    # المهارات التقنية والمهارات الناعمة
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3>المهارات التقنية</h3>", unsafe_allow_html=True)

        technical_skills = {
            'البرمجة': [
                ('Python', 95),
                ('R', 90),
                ('SQL', 85),
                ('STATA/EViews', 75),
                ('Julia', 50)
            ],
            'الإحصاء': [
                ('إحصاء استدلالي', 95),
                ('اختبار الفرضيات', 90),
                ('نمذجة إحصائية', 90),
                ('تصميم التجارب', 80)
            ],
            'القياس الاقتصادي': [
                ('نماذج الانحدار', 95),
                ('تحليل السلاسل الزمنية', 90),
                ('اقتصاد قياسي هيكلي', 80),
                ('طرق قياسية غير معلمية', 70)
            ],
            'التعلم الآلي': [
                ('خوارزميات خاضعة للإشراف', 90),
                ('خوارزميات غير خاضعة للإشراف', 85),
                ('تعلم عميق', 75),
                ('تعلم معزز', 65)
            ],
            'هندسة البيانات': [
                ('معالجة البيانات', 90),
                ('تخزين البيانات', 80),
                ('تحليلات البيانات الكبيرة', 75),
                ('تدفقات البيانات', 70)
            ]
        }

        # إنشاء مخططات للمهارات التقنية
        skill_category = st.selectbox(
            'اختر فئة المهارات التقنية:',
            list(technical_skills.keys())
        )

        selected_skills = technical_skills[skill_category]

        skills_df = pd.DataFrame({
            'المهارة': [s[0] for s in selected_skills],
            'المستوى': [s[1] for s in selected_skills]
        })

        fig = px.bar(
            skills_df,
            x='المستوى',
            y='المهارة',
            orientation='h',
            text='المستوى',
            title=f'أهمية مهارات {skill_category}',
            color='المستوى',
            color_continuous_scale='blues'
        )

        fig.update_layout(
            font=dict(family='Tajawal', size=14),
            xaxis_title='مستوى الأهمية (100-0)'
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("<h3>المهارات الناعمة</h3>", unsafe_allow_html=True)

        soft_skills = [
            ('التفكير التحليلي', 95),
            ('التواصل الفعال', 90),
            ('حل المشكلات', 90),
            ('العمل الجماعي', 85),
            ('الفضول العلمي', 85),
            ('التنظيم وإدارة الوقت', 80),
            ('الابتكار', 80),
            ('التفكير النقدي', 90),
            ('تفسير النتائج للجمهور غير التقني', 85),
            ('القدرة على التعلم المستمر', 95)
        ]

        soft_skills_df = pd.DataFrame({
            'المهارة': [s[0] for s in soft_skills],
            'الأهمية': [s[1] for s in soft_skills]
        })

        fig = px.pie(
            soft_skills_df,
            values='الأهمية',
            names='المهارة',
            title='أهمية المهارات الناعمة',
            color_discrete_sequence=px.colors.sequential.Purples_r,
            hole=0.4
        )

        fig.update_layout(
            font=dict(family='Tajawal', size=14),
            legend=dict(
                orientation="v",
                yanchor="top",
                y=1,
                xanchor="left",
                x=-0.1
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        **أهمية المهارات الناعمة**:

        تعتبر المهارات الناعمة ضرورية للنجاح في مجال القياس الاقتصادي وعلم البيانات للأسباب التالية:

        - **التواصل**: القدرة على شرح النتائج المعقدة لغير المتخصصين
        - **التفكير النقدي**: تقييم المناهج والنتائج بموضوعية
        - **حل المشكلات**: تحويل المشكلات العملية إلى أسئلة يمكن حلها بالبيانات
        - **التعلم المستمر**: المجال يتطور بسرعة، والقدرة على التكيف ضرورية
        """)

    # تقييم ذاتي للمهارات
    st.markdown("<h3>أداة التقييم الذاتي للمهارات</h3>", unsafe_allow_html=True)

    st.markdown("""
    قيّم مستواك الحالي في المهارات الأساسية لتحديد المجالات التي تحتاج إلى تطوير:
    """)

    # إنشاء مجموعة من المهارات للتقييم
    skills_to_assess = [
        'البرمجة (Python/R)',
        'الإحصاء والاحتمالات',
        'نماذج القياس الاقتصادي',
        'التعلم الآلي',
        'تصور البيانات',
        'قواعد البيانات وSQL',
        'معالجة وتنظيف البيانات',
        'التواصل وعرض النتائج'
    ]

    # إنشاء شرائح التقييم
    user_ratings = {}

    col1, col2 = st.columns(2)

    for i, skill in enumerate(skills_to_assess):
        with col1 if i % 2 == 0 else col2:
            user_ratings[skill] = st.slider(
                f"{skill}",
                0, 100, 50,
                help="0 = مبتدئ، 50 = متوسط، 100 = خبير"
            )

    # إظهار المهارات في مخطط راداري
    if user_ratings:
        radar_df = pd.DataFrame({
            'المهارة': list(user_ratings.keys()),
            'المستوى': list(user_ratings.values())
        })

        fig = px.line_polar(
            radar_df,
            r='المستوى',
            theta='المهارة',
            line_close=True,
            title='تقييمك الذاتي للمهارات'
        )

        fig.update_traces(
            fill='toself',
            fillcolor='rgba(67, 97, 238, 0.3)',
            line=dict(color='#4361ee', width=3)
        )

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            font=dict(family='Tajawal', size=14)
        )

        st.plotly_chart(fig, use_container_width=True)

        # تقديم توصيات بناءً على التقييم
        st.markdown("<h4>توصيات بناءً على تقييمك</h4>", unsafe_allow_html=True)

        weak_skills = [skill for skill, rating in user_ratings.items() if rating < 50]
        medium_skills = [skill for skill, rating in user_ratings.items() if 50 <= rating < 80]
        strong_skills = [skill for skill, rating in user_ratings.items() if rating >= 80]

        if weak_skills:
            st.markdown("<h5>مهارات تحتاج إلى تطوير:</h5>", unsafe_allow_html=True)
            for skill in weak_skills:
                st.markdown(f"- **{skill}**: يوصى بالبدء بدورات أساسية وتدريبات عملية.")

        if medium_skills:
            st.markdown("<h5>مهارات يمكن تعزيزها:</h5>", unsafe_allow_html=True)
            for skill in medium_skills:
                st.markdown(f"- **{skill}**: يمكن الانتقال إلى دورات متقدمة أو مشاريع واقعية.")

        if strong_skills:
            st.markdown("<h5>نقاط قوتك:</h5>", unsafe_allow_html=True)
            for skill in strong_skills:
                st.markdown(f"- **{skill}**: يمكنك الآن التخصص أكثر أو مساعدة الآخرين في التعلم.")

    # تطوير المهارات حسب المستوى
    st.markdown("<h3>تطوير المهارات حسب المستوى</h3>", unsafe_allow_html=True)

    level_tabs = st.tabs(["مبتدئ", "متوسط", "متقدم"])

    with level_tabs[0]:
        st.markdown("""
        **موارد للمستوى المبتدئ**:

        **البرمجة**:
        - دورة "Python for Everybody" على Coursera
        - كتاب "Python Crash Course" لـ Eric Matthes
        - دورة "R Programming" من Johns Hopkins على Coursera

        **الإحصاء**:
        - دورة "Statistics with R" من Duke University على Coursera
        - كتاب "Introductory Statistics with R" لـ Peter Dalgaard

        **القياس الاقتصادي الأساسي**:
        - دورة "Econometrics: Methods and Applications" من Erasmus University على Coursera
        - كتاب "Introduction to Econometrics" لـ Stock and Watson

        **تصور البيانات**:
        - دورة "Data Visualization with Python" على Coursera
        - دورات Tableau الأساسية على موقعهم الرسمي
        """)

    with level_tabs[1]:
        st.markdown("""
        **موارد للمستوى المتوسط**:

        **البرمجة المتقدمة**:
        - كتاب "Python for Data Analysis" لـ Wes McKinney
        - دورة "Advanced R Programming" على Coursera

        **نماذج إحصائية متقدمة**:
        - دورة "Bayesian Statistics" من Duke University
        - كتاب "Statistical Rethinking" لـ Richard McElreath

        **القياس الاقتصادي المتوسط**:
        - كتاب "Econometric Analysis" لـ Greene
        - دورة "Econometrics: Methods and Applications" من Erasmus University Rotterdam

        **التعلم الآلي الأساسي**:
        - دورة "Machine Learning" من Stanford University على Coursera
        - كتاب "Introduction to Statistical Learning" لـ James وآخرون

        **قواعد البيانات**:
        - دورة "SQL for Data Science" على Coursera
        - كتاب "SQL in 10 Minutes a Day" لـ Ben Forta
        """)

    with level_tabs[2]:
        st.markdown("""
        **موارد للمستوى المتقدم**:

        **القياس الاقتصادي المتقدم**:
        - كتاب "Mostly Harmless Econometrics" لـ Angrist & Pischke
        - كتاب "Microeconometrics" لـ Cameron & Trivedi
        - أوراق بحثية من مجلات Journal of Econometrics وEconometrica

        **التعلم الآلي المتقدم**:
        - كتاب "Pattern Recognition and Machine Learning" لـ Bishop
        - دورة "Deep Learning Specialization" من deeplearning.ai

        **تحليل السلاسل الزمنية المتقدم**:
        - كتاب "Time Series Analysis" لـ Hamilton
        - دورة "Financial Engineering and Risk Management" من Columbia University

        **الاقتصاد القياسي لبيانات Panel**:
        - كتاب "Econometric Analysis of Panel Data" لـ Baltagi

        **البرمجة والتطبيقات المتقدمة**:
        - دورة "Big Data Analysis with Spark and Python" على edX
        - كتاب "Advanced R" لـ Hadley Wickham
        """)

# التبويب السادس: المصادر والمراجع
with tabs[5]:
    st.markdown("<h2>المصادر والمراجع</h2>", unsafe_allow_html=True)

    # تقسيم المراجع إلى فئات
    reference_tabs = st.tabs([
        "كتب",
        "دورات إلكترونية",
        "قنوات يوتيوب",
        "مواقع ومنتديات",
        "مدونات ونشرات"
    ])

    # كتب
    with reference_tabs[0]:
        st.markdown("<h3>كتب مرجعية في القياس الاقتصادي وتحليل البيانات</h3>", unsafe_allow_html=True)

        books = [
            {
                'العنوان': 'Introduction to Econometrics',
                'المؤلف': 'Stock & Watson',
                'المستوى': 'مبتدئ إلى متوسط',
                'الوصف': 'كتاب قياسي لتعليم أساسيات القياس الاقتصادي، يتميز بأسلوب سهل وأمثلة عملية.',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'العنوان': 'Econometric Analysis',
                'المؤلف': 'William H. Greene',
                'المستوى': 'متوسط إلى متقدم',
                'الوصف': 'مرجع شامل للنظرية والتطبيق في الاقتصاد القياسي، كثيرًا ما يُستخدم في الدراسات العليا.',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'العنوان': 'Mostly Harmless Econometrics',
                'المؤلف': 'Angrist & Pischke',
                'المستوى': 'متوسط إلى متقدم',
                'الوصف': 'كتاب مميز يركز على أساليب تقييم السببية والأثر في الاقتصاد القياسي التطبيقي.',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'العنوان': 'Time Series Analysis',
                'المؤلف': 'James D. Hamilton',
                'المستوى': 'متقدم',
                'الوصف': 'مرجع أساسي في تحليل السلاسل الزمنية، يغطي النظرية والتطبيقات بعمق.',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'العنوان': 'Python for Data Analysis',
                'المؤلف': 'Wes McKinney',
                'المستوى': 'مبتدئ إلى متوسط',
                'الوصف': 'دليل عملي لاستخدام Python في تحليل البيانات، مكتوب من قبل مطور Pandas.',
                'التصنيف': 'تحليل بيانات'
            },
            {
                'العنوان': 'R for Data Science',
                'المؤلف': 'Hadley Wickham & Garrett Grolemund',
                'المستوى': 'مبتدئ إلى متوسط',
                'الوصف': 'دليل عملي لاستخدام R في تحليل البيانات، يركز على سير العمل التحليلي.',
                'التصنيف': 'تحليل بيانات'
            },
            {
                'العنوان': 'Introduction to Statistical Learning',
                'المؤلف': 'James, Witten, Hastie & Tibshirani',
                'المستوى': 'مبتدئ إلى متوسط',
                'الوصف': 'مقدمة ممتازة للتعلم الآلي الإحصائي، مع أمثلة في R.',
                'التصنيف': 'علم بيانات'
            },
            {
                'العنوان': 'Pattern Recognition and Machine Learning',
                'المؤلف': 'Christopher Bishop',
                'المستوى': 'متقدم',
                'الوصف': 'مرجع أساسي في التعلم الآلي والإحصاء النمطي، مع أساس نظري قوي.',
                'التصنيف': 'علم بيانات'
            },
            {
                'العنوان': 'Data Science for Business',
                'المؤلف': 'Provost & Fawcett',
                'المستوى': 'مبتدئ إلى متوسط',
                'الوصف': 'يشرح مفاهيم علم البيانات من منظور أعمال، مفيد لربط التحليلات بالقيمة التجارية.',
                'التصنيف': 'علم بيانات'
            },
            {
                'العنوان': 'الإحصاء للاقتصاديين والتجاريين',
                'المؤلف': 'د. محمد صبحي أبو صالح',
                'المستوى': 'مبتدئ',
                'الوصف': 'كتاب باللغة العربية يشرح أساسيات الإحصاء للاقتصاديين، مع أمثلة عملية.',
                'التصنيف': 'إحصاء'
            }
        ]

        books_df = pd.DataFrame(books)

        # تصفية الكتب حسب التصنيف
        book_category = st.selectbox(
            "تصفية الكتب حسب المجال:",
            ["الكل", "قياس اقتصادي", "تحليل بيانات", "علم بيانات", "إحصاء"]
        )

        if book_category != "الكل":
            filtered_books = books_df[books_df['التصنيف'] == book_category]
        else:
            filtered_books = books_df

        # عرض الكتب في جدول
        st.table(filtered_books[['العنوان', 'المؤلف', 'المستوى', 'الوصف']])

    # دورات إلكترونية
    with reference_tabs[1]:
        st.markdown("<h3>دورات إلكترونية موصى بها</h3>", unsafe_allow_html=True)

        courses = [
            {
                'العنوان': 'Econometrics: Methods and Applications',
                'المنصة': 'Coursera',
                'المقدم': 'Erasmus University Rotterdam',
                'المستوى': 'متوسط',
                'المدة': '8 أسابيع',
                'الرابط': 'https://www.coursera.org/learn/erasmus-econometrics',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'العنوان': 'Machine Learning',
                'المنصة': 'Coursera',
                'المقدم': 'Stanford University (Andrew Ng)',
                'المستوى': 'مبتدئ إلى متوسط',
                'المدة': '11 أسبوع',
                'الرابط': 'https://www.coursera.org/learn/machine-learning',
                'التصنيف': 'علم بيانات'
            },
            {
                'العنوان': 'Data Science Specialization',
                'المنصة': 'Coursera',
                'المقدم': 'Johns Hopkins University',
                'المستوى': 'مبتدئ إلى متوسط',
                'المدة': '10 دورات (4-6 أشهر)',
                'الرابط': 'https://www.coursera.org/specializations/jhu-data-science',
                'التصنيف': 'علم بيانات'
            },
            {
                'العنوان': 'Applied Econometrics',
                'المنصة': 'edX',
                'المقدم': 'MIT',
                'المستوى': 'متوسط إلى متقدم',
                'المدة': '12 أسبوع',
                'الرابط': 'https://www.edx.org/course/applied-econometrics',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'العنوان': 'SQL for Data Science',
                'المنصة': 'Coursera',
                'المقدم': 'UC Davis',
                'المستوى': 'مبتدئ',
                'المدة': '4 أسابيع',
                'الرابط': 'https://www.coursera.org/learn/sql-for-data-science',
                'التصنيف': 'تحليل بيانات'
            },
            {
                'العنوان': 'Deep Learning Specialization',
                'المنصة': 'Coursera',
                'المقدم': 'deeplearning.ai (Andrew Ng)',
                'المستوى': 'متوسط إلى متقدم',
                'المدة': '5 دورات (3-4 أشهر)',
                'الرابط': 'https://www.coursera.org/specializations/deep-learning',
                'التصنيف': 'علم بيانات'
            },
            {
                'العنوان': 'Google Data Analytics Professional Certificate',
                'المنصة': 'Coursera',
                'المقدم': 'Google',
                'المستوى': 'مبتدئ',
                'المدة': '6 دورات (6 أشهر)',
                'الرابط': 'https://www.coursera.org/professional-certificates/google-data-analytics',
                'التصنيف': 'تحليل بيانات'
            },
            {
                'العنوان': 'Linear Regression in R for Public Health',
                'المنصة': 'Coursera',
                'المقدم': 'Imperial College London',
                'المستوى': 'متوسط',
                'المدة': '4 أسابيع',
                'الرابط': 'https://www.coursera.org/learn/linear-regression-r-public-health',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'العنوان': 'مقدمة في علم البيانات',
                'المنصة': 'إدراك',
                'المقدم': 'إدراك',
                'المستوى': 'مبتدئ',
                'المدة': '6 أسابيع',
                'الرابط': 'https://www.edraak.org/course/',
                'التصنيف': 'علم بيانات'
            },
            {
                'العنوان': 'أساسيات الإحصاء',
                'المنصة': 'رواق',
                'المقدم': 'جامعة الملك سعود',
                'المستوى': 'مبتدئ',
                'المدة': '8 أسابيع',
                'الرابط': 'https://www.rwaq.org/',
                'التصنيف': 'إحصاء'
            }
        ]

        courses_df = pd.DataFrame(courses)

        # تصفية الدورات حسب التصنيف
        course_category = st.selectbox(
            "تصفية الدورات حسب المجال:",
            ["الكل", "قياس اقتصادي", "تحليل بيانات", "علم بيانات", "إحصاء"],
            key="course_cat_filter" # Added key for uniqueness
        )

        if course_category != "الكل":
            filtered_courses = courses_df[courses_df['التصنيف'] == course_category]
        else:
            filtered_courses = courses_df

        # تصفية حسب المستوى
        course_level = st.radio(
            "تصفية حسب المستوى:",
            ["الكل", "مبتدئ", "متوسط", "متقدم"],
            horizontal=True,
            key="course_level_filter" # Added key for uniqueness
        )

        if course_level != "الكل":
            filtered_courses = filtered_courses[filtered_courses['المستوى'].str.contains(course_level)]

        # عرض الدورات في جدول
        st.table(filtered_courses[['العنوان', 'المنصة', 'المقدم', 'المستوى', 'المدة']])

    # قنوات يوتيوب
    with reference_tabs[2]:
        st.markdown("<h3>قنوات يوتيوب تعليمية موصى بها</h3>", unsafe_allow_html=True)

        youtube_channels = [
            {
                'القناة': 'StatQuest with Josh Starmer',
                'المحتوى': 'شرح مبسط ومرئي للمفاهيم الإحصائية والتعلم الآلي',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/joshstarmer',
                'التصنيف': 'إحصاء، تعلم آلي'
            },
            {
                'القناة': '3Blue1Brown',
                'المحتوى': 'تصورات رائعة للمفاهيم الرياضية المهمة في علم البيانات',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/3blue1brown',
                'التصنيف': 'رياضيات'
            },
            {
                'القناة': 'Corey Schafer',
                'المحتوى': 'دروس برمجة بلغة Python من الأساسيات إلى المتقدم',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/Coreyms',
                'التصنيف': 'برمجة'
            },
            {
                'القناة': 'sentdex',
                'المحتوى': 'برمجة Python مع تركيز على تحليل البيانات والتعلم الآلي',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/sentdex',
                'التصنيف': 'علم بيانات، برمجة'
            },
            {
                'القناة': 'Krish Naik',
                'المحتوى': 'مواضيع مختلفة في علم البيانات والتعلم الآلي مع التطبيقات',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/user/krishnaik06',
                'التصنيف': 'علم بيانات'
            },
            {
                'القناة': 'Ken Jee',
                'المحتوى': 'نصائح مهنية ودروس عملية في علم البيانات',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/KenJee1',
                'التصنيف': 'علم بيانات'
            },
            {
                'القناة': 'Econometrics Academy',
                'المحتوى': 'دروس في القياس الاقتصادي والإحصاء وتطبيقاتها',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/BenLambertStats',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'القناة': 'Keith Galli',
                'المحتوى': 'مشاريع عملية في تحليل البيانات باستخدام Python',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/KGMIT',
                'التصنيف': 'تحليل بيانات'
            },
            {
                'القناة': 'codebasics',
                'المحتوى': 'دروس في برمجة Python وعلم البيانات للمبتدئين',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/codebasics',
                'التصنيف': 'علم بيانات، برمجة'
            },
            {
                'القناة': 'خوارزمي',
                'المحتوى': 'دروس باللغة العربية في البرمجة وعلم البيانات',
                'اللغة': 'العربية',
                'الرابط': 'https://www.youtube.com/channel/UCU46Gujh4q68ZmahPGNOJZw',
                'التصنيف': 'علم بيانات، برمجة'
            },
            {
                'القناة': 'أكاديمية حسوب',
                'المحتوى': 'دروس برمجة باللغة العربية تشمل بايثون وقواعد البيانات',
                'اللغة': 'العربية',
                'الرابط': 'https://www.youtube.com/c/HsoubAcademy',
                'التصنيف': 'برمجة'
            },
            {
                'القناة': 'The Sound of AI',
                'المحتوى': 'تعلم آلي وتعلم عميق مع تطبيقات في معالجة الصوت',
                'اللغة': 'الإنجليزية',
                'الرابط': 'https://www.youtube.com/c/TheSoundofAI',
                'التصنيف': 'علم بيانات، تعلم آلي'
            }
        ]

        youtube_df = pd.DataFrame(youtube_channels)

        # تصفية حسب اللغة
        language = st.radio(
            "تصفية حسب اللغة:",
            ["الكل", "الإنجليزية", "العربية"],
            horizontal=True,
            key="yt_lang_filter" # Added key for uniqueness
        )

        if language != "الكل":
            filtered_channels = youtube_df[youtube_df['اللغة'] == language]
        else:
            filtered_channels = youtube_df

        # تصفية حسب التصنيف
        channel_category = st.multiselect(
            "تصفية حسب المحتوى:",
            ["علم بيانات", "برمجة", "إحصاء", "تعلم آلي", "قياس اقتصادي", "رياضيات"],
            default=[],
            key="yt_cat_filter" # Added key for uniqueness
        )

        if channel_category:
            # تصفية القنوات التي تحتوي على أي من التصنيفات المختارة
            mask = filtered_channels['التصنيف'].apply(lambda x: any(cat in x for cat in channel_category))
            filtered_channels = filtered_channels[mask]

        # عرض القنوات في جدول
        st.table(filtered_channels[['القناة', 'المحتوى', 'اللغة']])

    # مواقع ومنتديات
    with reference_tabs[3]:
        st.markdown("<h3>مواقع ومنتديات مفيدة</h3>", unsafe_allow_html=True)

        websites = [
            {
                'الموقع': 'Kaggle',
                'الوصف': 'منصة لمسابقات علم البيانات، توفر دورات مجانية ومجموعات بيانات وكود للتعلم',
                'الرابط': 'https://www.kaggle.com',
                'التصنيف': 'علم بيانات، تعلم ذاتي'
            },
            {
                'الموقع': 'Stack Overflow',
                'الوصف': 'منتدى لأسئلة وأجوبة البرمجة، يحوي آلاف الحلول للمشاكل البرمجية',
                'الرابط': 'https://stackoverflow.com',
                'التصنيف': 'برمجة، دعم تقني'
            },
            {
                'الموقع': 'Cross Validated',
                'الوصف': 'منتدى Stack Exchange متخصص في الإحصاء والتعلم الآلي',
                'الرابط': 'https://stats.stackexchange.com',
                'التصنيف': 'إحصاء، علم بيانات'
            },
            {
                'الموقع': 'GitHub',
                'الوصف': 'منصة استضافة الكود، تحوي آلاف المشاريع مفتوحة المصدر للتعلم منها',
                'الرابط': 'https://github.com',
                'التصنيف': 'برمجة، مشاريع'
            },
            {
                'الموقع': 'DataCamp',
                'الوصف': 'منصة تعليمية متخصصة في علم البيانات مع دورات تفاعلية',
                'الرابط': 'https://www.datacamp.com',
                'التصنيف': 'علم بيانات، تعلم تفاعلي'
            },
            {
                'الموقع': 'Econometrics Academy',
                'الوصف': 'موقع متخصص في تعليم القياس الاقتصادي مع شروحات ومصادر مجانية',
                'الرابط': 'https://sites.google.com/site/econometricsacademy',
                'التصنيف': 'قياس اقتصادي'
            },
            {
                'الموقع': 'Towards Data Science',
                'الوصف': 'منصة نشر مقالات متخصصة في علم البيانات والتعلم الآلي',
                'الرابط': 'https://towardsdatascience.com',
                'التصنيف': 'علم بيانات، مقالات'
            },
            {
                'الموقع': 'Real Python',
                'الوصف': 'مقالات ودروس متعمقة في لغة Python للبرمجة وتحليل البيانات',
                'الرابط': 'https://realpython.com',
                'التصنيف': 'برمجة بايثون'
            },
            {
                'الموقع': 'Data Science Central',
                'الوصف': 'منصة للمحتوى والموارد المتعلقة بعلم البيانات والتحليلات',
                'الرابط': 'https://www.datasciencecentral.com',
                'التصنيف': 'علم بيانات، مقالات'
            },
            {
                'الموقع': 'R-bloggers',
                'الوصف': 'مجموعة مقالات ومدونات حول استخدام R في تحليل البيانات',
                'الرابط': 'https://www.r-bloggers.com',
                'التصنيف': 'برمجة R، تحليل بيانات'
            },
            {
                'الموقع': 'Analytics Vidhya',
                'الوصف': 'منصة تعليمية متكاملة لعلم البيانات والتعلم الآلي',
                'الرابط': 'https://www.analyticsvidhya.com',
                'التصنيف': 'علم بيانات، تعلم آلي'
            },
            {
                'الموقع': 'KDnuggets',
                'الوصف': 'موقع رائد لأخبار ومقالات علم البيانات والتعلم الآلي',
                'الرابط': 'https://www.kdnuggets.com',
                'التصنيف': 'علم بيانات، أخبار'
            }
        ]

        websites_df = pd.DataFrame(websites)

        # تصفية حسب التصنيف
        website_category = st.multiselect(
            "تصفية حسب التصنيف:",
            ["علم بيانات", "برمجة", "إحصاء", "قياس اقتصادي", "تعلم آلي", "مقالات", "تعلم ذاتي", "دعم تقني"],
            default=[],
            key="website_cat_filter" # Added key for uniqueness
        )

        if website_category:
            # تصفية المواقع التي تحتوي على أي من التصنيفات المختارة
            mask = websites_df['التصنيف'].apply(lambda x: any(cat in x for cat in website_category))
            filtered_websites = websites_df[mask]
        else:
            filtered_websites = websites_df

        # عرض المواقع في جدول
        st.table(filtered_websites[['الموقع', 'الوصف', 'التصنيف']])

    # مدونات ونشرات
    with reference_tabs[4]:
        st.markdown("<h3>مدونات ونشرات إخبارية موصى بها</h3>", unsafe_allow_html=True)

        blogs = [
            {
                'المدونة': 'Machine Learning Mastery',
                'الكاتب': 'Jason Brownlee',
                'الوصف': 'مقالات عملية وكود في التعلم الآلي والتعلم العميق',
                'الرابط': 'https://machinelearningmastery.com',
                'التصنيف': 'تعلم آلي، عملي'
            },
            {
                'المدونة': 'Simply Statistics',
                'الكاتب': 'Roger Peng, Jeff Leek, Rafa Irizarry',
                'الوصف': 'مدونة أكاديمية تناقش مواضيع الإحصاء وعلم البيانات',
                'الرابط': 'https://simplystatistics.org',
                'التصنيف': 'إحصاء، أكاديمي'
            },
            {
                'المدونة': 'Statistical Modeling, Causal Inference, and Social Science',
                'الكاتب': 'Andrew Gelman',
                'الوصف': 'مدونة متخصصة في النمذجة الإحصائية والاستدلال السببي',
                'الرابط': 'https://statmodeling.stat.columbia.edu',
                'التصنيف': 'إحصاء، قياس، أكاديمي'
            },
            {
                'المدونة': 'The Data Scientist',
                'الكاتب': 'متعدد الكتّاب',
                'الوصف': 'مقالات عملية وإرشادات في علم البيانات والتحليلات',
                'الرابط': 'https://thedatascientist.com',
                'التصنيف': 'علم بيانات، عملي'
            },
            {
                'المدونة': 'R-bloggers',
                'الكاتب': 'مجتمع R',
                'الوصف': 'تجميع لمقالات حول استخدام R في التحليل والإحصاء',
                'الرابط': 'https://www.r-bloggers.com',
                'التصنيف': 'برمجة R، تحليل'
            },
            {
                'المدونة': 'Data Science Weekly',
                'الكاتب': 'Hannah Brooks & Sebastian Gutierrez',
                'الوصف': 'نشرة أسبوعية بأهم المقالات والأخبار في علم البيانات',
                'الرابط': 'https://www.datascienceweekly.org',
                'التصنيف': 'علم بيانات، نشرة'
            },
            {
                'المدونة': 'O\'Reilly Data Newsletter',
                'الكاتب': 'O\'Reilly Media',
                'الوصف': 'نشرة متخصصة في أخبار وتطورات علم البيانات والتعلم الآلي',
                'الرابط': 'https://www.oreilly.com/emails/newsletters/',
                'التصنيف': 'علم بيانات، نشرة'
            },
            {
                'المدونة': 'Econometrics Beat',
                'الكاتب': 'Dave Giles',
                'الوصف': 'مدونة متخصصة في القياس الاقتصادي والإحصاء',
                'الرابط': 'http://davegiles.blogspot.com',
                'التصنيف': 'قياس اقتصادي، أكاديمي'
            },
            {
                'المدونة': 'PyData',
                'الكاتب': 'مجتمع PyData',
                'الوصف': 'مدونة مجتمع Python لتحليل البيانات والتعلم الآلي',
                'الرابط': 'https://pydata.org/blog',
                'التصنيف': 'بايثون، علم بيانات'
            },
            {
                'المدونة': 'Flowing Data',
                'الكاتب': 'Nathan Yau',
                'الوصف': 'مدونة متخصصة في تصور البيانات وتصميم المعلومات',
                'الرابط': 'https://flowingdata.com',
                'التصنيف': 'تصور بيانات، تصميم'
            }
        ]

        blogs_df = pd.DataFrame(blogs)

        # تصفية حسب التصنيف
        blog_category = st.multiselect(
            "تصفية حسب التصنيف:",
            ["علم بيانات", "إحصاء", "تعلم آلي", "قياس اقتصادي", "برمجة", "تصور بيانات", "نشرة", "أكاديمي", "عملي"],
            default=[],
            key="blog_cat_filter" # Added key for uniqueness
        )

        if blog_category:
            # تصفية المدونات التي تحتوي على أي من التصنيفات المختارة
            mask = blogs_df['التصنيف'].apply(lambda x: any(cat in x for cat in blog_category))
            filtered_blogs = blogs_df[mask]
        else:
            filtered_blogs = blogs_df

        # عرض المدونات في جدول
        st.table(filtered_blogs[['المدونة', 'الكاتب', 'الوصف', 'التصنيف']])

# قسم ختامي
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>هل تحتاج إلى مساعدة إضافية؟</h2>", unsafe_allow_html=True)

# مربع النص للأسئلة
user_question = st.text_area("اطرح سؤالًا محددًا حول القياس الاقتصادي أو علم البيانات:")

if user_question:
    st.info(
        "يمكنك البحث عن إجابات مفصلة في المصادر المذكورة أعلاه، أو طرح السؤال في المنتديات المتخصصة مثل Stack Overflow أو Cross Validated.")

# رسالة ختامية تحفيزية
st.markdown("<div style='background-color: #e6f3ff; padding: 20px; border-radius: 10px; margin-top: 20px;'>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>رحلة الألف ميل تبدأ بخطوة</h3>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center;'>
تذكر أن التخصص في القياس الاقتصادي وعلم البيانات هو رحلة مستمرة من التعلم والتطبيق.
لا تتوقف عن التعلم، وابدأ بمشاريع صغيرة لتطبيق ما تتعلمه.
الممارسة المستمرة هي المفتاح الأساسي للنجاح في هذه المجالات.
</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# معلومات التطبيق
st.markdown("<div style='text-align: center; margin-top: 30px; font-size: 12px; color: gray;'>", unsafe_allow_html=True)
st.markdown("تم تطوير هذا التطبيق باستخدام Python و Streamlit © 2025", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
