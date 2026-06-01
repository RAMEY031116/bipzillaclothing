import streamlit as st
from PIL import Image
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="BIPZILLA | ビップジラ",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR STREETWEAR VIBE ---
st.markdown('''
    <style>
    /* Clean up the default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    /* Brand Colors and typography */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .brand-title {
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: -10px;
    }
    .japanese-text {
        font-size: 1.5rem;
        color: #E63946; /* Bipzilla Red */
        font-weight: bold;
        margin-bottom: 20px;
    }
    .drop-status {
        background-color: #000;
        color: #fff;
        padding: 4px 8px;
        font-size: 0.8rem;
        font-weight: bold;
        border-radius: 4px;
        letter-spacing: 1px;
    }
    .embroidery-tag {
        color: #E63946;
        font-weight: bold;
        font-size: 0.9rem;
    }
    </style>
''', unsafe_allow_html=True)

# --- HELPER FUNCTION TO LOAD IMAGES ---
def load_image(image_name):
    image_path = os.path.join("assets", image_name)
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        return None

# --- HEADER ---
st.markdown('<p class="brand-title">BIPZILLA</p>', unsafe_allow_html=True)
st.markdown('<p class="japanese-text">ビップジラ</p>', unsafe_allow_html=True)
st.caption("ART • CULTURE • STREETWEAR | FREE UK SHIPPING ON ALL ORDERS OVER £70")
st.divider()

# --- NAVIGATION ---
tab_home, tab_shop, tab_about = st.tabs(["HOME", "LIMITED DROPS", "OUR STORY"])

# --- TAB 1: HOME ---
with tab_home:
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.title("WEAR YOUR STORY.")
        st.write("Bipzilla is a streetwear brand built on original art, bold ideas, and self-expression.")
        st.write("**Limited drops. No restocks. Ever.**")
        if st.button("SHOP THE DROP ➔", type="primary"):
            st.success("Navigate to the 'LIMITED DROPS' tab to view the collection!")
            
    with col2:
        hero_img = load_image("hero_mockup.png")
        if hero_img:
            st.image(hero_img, use_container_width=True)
        else:
            st.info("Upload your hero image to assets/hero_mockup.png")

    st.divider()
    st.markdown("### 🌐 WORLDWIDE SHIPPING | 🏷️ SECURE CHECKOUT | 🧵 PREMIUM QUALITY")

# --- TAB 2: SHOP (THE DROPS) ---
with tab_shop:
    st.markdown("## LATEST DROPS")
    st.write("Exclusive runs. Once they are gone, they are gone.")
    
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    
    with row1_col1:
        img1 = load_image("samurai.jpg")
        if img1: st.image(img1, use_container_width=True)
        st.markdown('<span class="drop-status">LOW STOCK</span>', unsafe_allow_html=True)
        st.subheader("RONIN DEMON TEE")
        st.write("£34.99")
        st.markdown('<span class="embroidery-tag">✦ High-Density DTG Print</span>', unsafe_allow_html=True)
        st.write("100% Organic Heavyweight Cotton. Custom milled.")
        st.button("ADD TO CART", key="btn1")
        
    with row1_col2:
        img2 = load_image("koi_deity.png")
        if img2: st.image(img2, use_container_width=True)
        st.markdown('<span class="drop-status">JUST ADDED</span>', unsafe_allow_html=True)
        st.subheader("COSMIC KOI HOODIE")
        st.write("£64.99")
        st.markdown('<span class="embroidery-tag">✦ Front: 3D Embroidery | Back: Silk Screen</span>', unsafe_allow_html=True)
        st.write("400gsm French Terry. Drop shoulder oversized fit.")
        st.button("ADD TO CART", key="btn2")

    with row2_col1:
        img3 = load_image("marine.jpg")
        if img3: st.image(img3, use_container_width=True)
        st.markdown('<span class="drop-status">PRE-ORDER</span>', unsafe_allow_html=True)
        st.subheader("ABYSSAL ARMOR SWEATER")
        st.write("£54.99")
        st.markdown('<span class="embroidery-tag">✦ Full Chest Heavy Embroidery</span>', unsafe_allow_html=True)
        st.write("Knit sweater. Intricate tentacle detailing woven directly into the fabric.")
        st.button("ADD TO CART", key="btn3")

    with row2_col2:
        img4 = load_image("dreamscape.jpg")
        if img4: st.image(img4, use_container_width=True)
        st.markdown('<span class="drop-status">SELLING FAST</span>', unsafe_allow_html=True)
        st.subheader("LUCID DRIFT LONGSLEEVE")
        st.write("£39.99")
        st.markdown('<span class="embroidery-tag">✦ DTG Print with Embroidered Cuff Detailing</span>', unsafe_allow_html=True)
        st.write("Boxy fit. A surrealist escape on premium cotton.")
        st.button("ADD TO CART", key="btn4")

# --- TAB 3: ABOUT ---
with tab_about:
    st.markdown("## MORE THAN CLOTHES. IT'S A MOVEMENT.")
    st.write("Bipzilla (ビップジラ) was born from a love of art, culture, and self-expression. Every piece is designed in-house and made for those who move differently. We don't do mass production. We do limited runs of wearable canvases. Whether it's the high-density print of a Ronin Samurai or the heavy 3D embroidery of deep-sea armor, every stitch has intent.")
    st.divider()
    st.markdown("© 2026 BIPZILLA. ALL RIGHTS RESERVED.")
