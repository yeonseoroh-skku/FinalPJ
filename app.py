import streamlit as st
import os
import plotly.graph_objects as go  # 시각화를 위한 Plotly 라이브러리 추가

# --- 1. 페이지 기본 설정 및 스타일 (Soft Pink & Navy) ---
st.set_page_config(page_title="Core Trend Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFF0F2; color: #1A2A4A; }
    h1, h2, h3 {
        color: #1A2A4A !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(26, 42, 74, 0.15);
    }
    p, li { color: #1A2A4A !important; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# --- 2. 상단 네비게이션 바 (탭 메뉴) ---
st.title("✨ Core Trend Dashboard")
tabs = ["Home", "Gorpcore", "Balletcore", "GeekChic", "Barbiecore", "Cowboycore", "Royalcore"]
selected_tab = st.segmented_control("Trends", tabs, default="Home")

# --- 안전하게 이미지를 표시하는 함수 (에러 방지 치트키!) ---
def display_centered_image(image_path):
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        if os.path.exists(image_path):
            st.image(image_path, width=872, use_container_width=False)
        elif os.path.exists(image_path.lower()):
            st.image(image_path.lower(), width=872, use_container_width=False)
        elif os.path.exists(image_path.upper()):
            st.image(image_path.upper(), width=872, use_container_width=False)
        else:
            st.info(f"📷 [사진 준비 중: {image_path} 파일 업로드 필요]")

# --- 3. 각 페이지별 콘텐츠 구현 ---

# ==========================================
# HOME PAGE
# ==========================================
if selected_tab == "Home":
    st.markdown("<div style='text-align: center; padding: 30px 0;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 56px;'>Core Trend</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 22px; font-weight: 600;'>The \"Core\" trend refers to hyper-specific subcultures or micro-trends on TikTok and Instagram that define a distinct visual vibe or lifestyle.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.subheader("Social Media Aesthetics (The \"-core\" Trend)")
    st.write("Originating largely on platforms like TikTok and Tumblr, the suffix \"-core\" is slapped onto any word to describe a specific vibe, aesthetic, or visual identity.")
    st.write("**How it's used:** It creates hyper-specific internet subcultures. For example, 'lovecore' features hearts and pink motifs, while 'royalcore' pulls inspiration from historical European monarchies.")
    st.write("**The 'Corecore' trend:** This is an artistic, somewhat surreal editing style on TikTok that mashes together unrelated audio and video clips to evoke heavy, emotional, or nostalgic feelings about modern life.")

    # 📌 추가 요청 문구 반영
    st.subheader("What Makes the Core Trend Unique")
    st.write("Unlike previous fashion trends, which typically followed a top-down structure in which styles originated from luxury brands or haute couture fashion shows and then spread to the general public, core trends emerge from ordinary social media users. These trends are created and popularized by the public through social media platforms, ultimately influencing the fashion industry as a whole.")

    st.markdown("---") # 시각화 섹션 구분을 위한 구분선

    # 📈 1. 트렌드 형성 구조 비교 그래프 (Shift from Top-Down to Bottom-Up Fashion Trends)
    st.subheader("📊 Trend Formation Structure Comparison")
    
    sources = ['Luxury Brands', 'Fashion Media', 'Social Media Users']
    traditional_influence = [95, 85, 20]  # 전통 트렌드: 럭셔리/미디어 높음, 일반유저 낮음
    core_influence = [40, 50, 95]         # 코어 트렌드: 일반유저 압도적 높음

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=sources, y=traditional_influence,
        name='Traditional Trends (Top-Down)', marker_color='#1A2A4A' # Navy
    ))
    fig1.add_trace(go.Bar(
        x=sources, y=core_influence,
        name='Core Trends (Bottom-Up)', marker_color='#FF8DA1' # Darker Pink for contrast
    ))

    fig1.update_layout(
        title={
            'text': "<b>Shift from Top-Down to Bottom-Up Fashion Trends</b>",
            'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
        },
        font=dict(family="Helvetica Neue, Arial", size=14, color="#1A2A4A"),
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(title="Influence Level (%)", gridcolor="#F0D5D9"),
        xaxis=dict(title="Sources of Influence"),
        legend=dict(x=0.7, y=0.95)
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("**Explanation:** This chart illustrates the democratization of fashion. Traditional fashion strictly relied on a top-down mechanism driven by haute couture and editorial gatekeepers. Conversely, Core trends leverage decentralized digital networks, placing social media users at the epicenter of trend-setting propagation.")

    st.markdown("---")

    # 📉 2. Core Trend 성장 추세 그래프 (Growth of Core Fashion Trends)
    st.subheader("📈 Core Trend Growth Trajectory")

    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
    popularity = [10, 15, 35, 50, 70, 85, 95, 100]

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=years, y=popularity,
        mode='lines+markers',
        line=dict(color='#1A2A4A', width=4),
        marker=dict(size=10, color='#FF8DA1', line=dict(color='#1A2A4A', width=2)),
        name='Popularity Index'
    ))

    fig2.update_layout(
        title={
            'text': "<b>Growth of Core Fashion Trends</b>",
            'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
        },
        font=dict(family="Helvetica Neue, Arial", size=14, color="#1A2A4A"),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(title="Relative Popularity Index", gridcolor="#F0D5D9"),
        xaxis=dict(title="Year")
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("**Interpretation:** The exponential growth post-2020 highlights a paradigm shift towards aesthetic-based fashion identities. Driven by algorithmic personalization on social media and accelerated during global lockdowns, consumer behavior shifted away from singular brand loyalty toward fluid, niche aesthetic participation.")

# ==========================================
# GORPCORE PAGE
# ==========================================
elif selected_tab == "Gorpcore":
    display_centered_image("gorpcore1.png")
    st.header("Gorpcore")
    st.write("Gorpcore is a fashion aesthetic that takes high-performance outdoor, hiking, and camping gear and styles it for everyday streetwear. The name comes from 'gorp,' slang for trail mix (Good Ol' Raisins and Peanuts), mixed with 'normcore'. It celebrates utilitarian, weather-resistant clothing designed to be practical, comfortable, and versatile in urban environments.")

    st.subheader("Why People Love It")
    st.markdown("- **Climate Readiness:** Frequent freak weather has made water-resistant and windproof gear everyday city wear.\n- **Comfort and Utility:** Rejecting constricting clothing, Gen Z gravitates toward brands that allow easy movement and possess practical elements.\n- **Eco-Consciousness:** Many gorpcore labels utilize recycled materials and offer repair programs, which heavily appeal to environmentally aware youth.")

    with st.expander("Top Gen Z Brands", expanded=True):
        st.write("### Arc'teryx")
        display_centered_image("gorpcore2.png")
        st.write("The brand's XT-6 trail running shoe became an instant, global streetwear icon.")
        
        st.write("### Salomon")
        display_centered_image("gorpcore3.png")
        st.write("Known for minimalist tech.")
        
        st.write("### The North Face & Patagonia")
        display_centered_image("gorpcore4.png")
        st.write("Historic outdoor staples that have been heavily absorbed into youth closets.")
        
        st.write("### Uniqlo")
        display_centered_image("gorpcore5.png")
        st.write("Provides highly accessible, budget-friendly entry points for gorpcore vests and fleeces.")

    with st.expander("Key Elements of Gorpcore", expanded=True):
        items = [
            ("Hardshell & Rain Jackets", "gorpcore6.png", "Waterproof, breathable shells from technical specialists like Arc'teryx or durable classics like The North Face"),
            ("Fleece Pullovers & Cardigans", "gorpcore7.png", "Cozy layering pieces. Brands like Patagonia are the gold standard for retro and modern fleeces."),
            ("Utility & Cargo Pants", "gorpcore8.png", "Wide-leg, durable bottoms equipped with multiple pockets. Labels like Gramicci offer iconic climbing pants with built-in webbed belts."),
            ("Trail Shoes & Hiking Boots", "gorpcore9.png", "Chunky, rugged footwear designed for the trail but styled in the city. Look for Salomon for aesthetic trail runners or HOKA for highly cushioned options."),
            ("Accessories", "gorpcore10.png", "Ripstop crossbody slings, rugged bucket hats, and thick, chunky knit beanies.")
        ]
        for title, img, desc in items:
            st.write(f"### {title}")
            display_centered_image(img)
            st.write(desc)

# ==========================================
# BALLETCORE PAGE
# ==========================================
elif selected_tab == "Balletcore":
    display_centered_image("balletcore1.png")
    st.header("Balletcore")
    st.write("Balletcore is a viral fashion aesthetic and lifestyle trend that draws inspiration from the delicate, graceful world of classical ballet. It blends the functional beauty of dancewear—like leotards, wrap tops, and tulle skirts—with everyday elevated athleisure and streetwear.")

    with st.expander("Top Gen Z Brands", expanded=True):
        brands = [
            ("Miu Miu", "balletcore2.png", "Renowned for bringing ballet flats, wrap skirts, and delicate knitwear to the luxury high-fashion runway."),
            ("Bloch", "balletcore3.png", "An authentic dancewear authority that offers an everyday Ballet Core Collection of wrap tops and soft knitwear."),
            ("Shushu Tong", "balletcore4.png", "A designer brand specializing in romantic, structured tulle, and feminine silhouettes."),
            ("Repetto", "balletcore5.png", "Founded in Paris in 1947, they are the gold standard for authentic ballet footwear and apparel.")
        ]
        for title, img, desc in brands:
            st.write(f"### {title}")
            display_centered_image(img)
            st.write(desc)

    with st.expander("Key Elements of Balletcore", expanded=True):
        elements = [
            ("Color Palette", "balletcore6.png", "Dominated by soft, romantic hues like pale pinks, creams, whites, nudes, and soft grays. Hints of black or wine tones are often added for contrast."),
            ("Fabrics & Textures", "balletcore7.png", "Flowing, ethereal materials like tulle, chiffon, and sheer fabrics mixed with sleek satin, breathable jersey, and cozy knits."),
            ("Fitted Basics", "balletcore8.png", "Bodysuits and camisoles that act as base layers, emulating traditional leotards."),
            ("Layering", "balletcore9.png", "Wrap tops, shrugs, and oversized cardigans worn over fitted tanks to accentuate the waist."),
            ("Footwear", "balletcore10.png", "Delicate ballet flats (often with satin finishes or ankle ribbons), Mary Janes, or pointe shoes."),
            ("Accessories", "balletcore11.png", "Leg warmers, knit shrugs, hair ribbons, and bows."),
            ("Hair & Makeup", "balletcore12.png", "Sleek, slicked-back buns, soft rosy makeup, and dewy complexions.")
        ]
        for title, img, desc in elements:
            st.write(f"### {title}")
            display_centered_image(img)
            st.write(desc)

# ==========================================
# GEEKCHIC PAGE
# ==========================================
elif selected_tab == "GeekChic":
    display_centered_image("geek1.png")
    st.header("GeekChic")
    st.write("Geek chic is a fashion and lifestyle trend that recontextualizes traditionally 'nerdy' or 'uncool' clothing into trendy, stylish outfits.")

    with st.expander("Top Gen Z Brands", expanded=True):
        brands = [
            ("Thom Browne", "geek2.png", "Known for heavily preppy, academically inclined silhouettes, pleated skirts, and tailored blazers."),
            ("LEWKIN", "geek3.png", "A rapidly popular K-fashion brand offering distinctively smart, 'luxe-librarian' styled clothing."),
            ("Warby Parker", "geek4.png", "The go-to destination for stylish, intellectual, and vintage-inspired frames.")
        ]
        for title, img, desc in brands:
            st.write(f"### {title}")
            display_centered_image(img)
            st.write(desc)

    with st.expander("Key Elements of Geek Chic", expanded=True):
        elements = [
            ("Statement Eyewear", "geek5.png", "Oversized, thick black horn-rimmed frames, tortoiseshell patterns, or wire-rimmed glasses."),
            ("Vintage Layering", "geek6.png", "Cable-knit sweaters, sweater vests, argyle prints,
