import streamlit as st
from dataclasses import dataclass
from typing import List

st.set_page_config(
    page_title="Bipzilla | First Drop",
    page_icon="🃏",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Brand / content data
# -----------------------------

@dataclass
class Product:
    name: str
    collection: str
    price: int
    colour: str
    garment: str
    fit: str
    image: str
    badge: str
    description: str
    print_placement: str

PRODUCTS: List[Product] = [
    Product(
        "Ace of Hearts Heavyweight Hoodie",
        "Ace of Hearts",
        58,
        "Washed Black",
        "Hoodie",
        "Oversized / 460 GSM",
        "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=1100&q=80",
        "Hero Piece",
        "A premium oversized hoodie built around the uploaded Ace of Hearts artwork. Large back print, small Bipzilla chest mark.",
        "Small front logo + large back Ace print",
    ),
    Product(
        "Ace of Hearts Vintage Tee",
        "Ace of Hearts",
        32,
        "Vintage Cream",
        "T-Shirt",
        "Boxy / 240 GSM",
        "https://images.unsplash.com/photo-1523398002811-999ca8dec234?auto=format&fit=crop&w=1100&q=80",
        "Best Seller",
        "A clean cream tee with a large card-inspired back design and subtle front Bipzilla logo placement.",
        "Left chest logo + full back card artwork",
    ),
    Product(
        "Pizza Samurai Black Tee",
        "Pizza Samurai",
        34,
        "Black",
        "T-Shirt",
        "Oversized / 240 GSM",
        "https://images.unsplash.com/photo-1503341504253-dff4815485f1?auto=format&fit=crop&w=1100&q=80",
        "New Graphic",
        "A fun statement graphic using pizza, samurai energy, pink highlights and Japanese streetwear layout.",
        "Small front hit + large illustrated back print",
    ),
    Product(
        "Last Knight Faded Hoodie",
        "Last Knight",
        62,
        "Faded Navy",
        "Hoodie",
        "Oversized / 460 GSM",
        "https://images.unsplash.com/photo-1578587018452-892bacefd3f2?auto=format&fit=crop&w=1100&q=80",
        "Premium",
        "A darker warrior-inspired piece for the Warhammer/knight style artwork, finished with muted colours and heavy fabric.",
        "Embroidered front logo + large back knight print",
    ),
    Product(
        "Bloom Logo Tee",
        "Bloom",
        30,
        "Off White",
        "T-Shirt",
        "Relaxed / 220 GSM",
        "https://images.unsplash.com/photo-1562157873-818bc0726f68?auto=format&fit=crop&w=1100&q=80",
        "Minimal",
        "A cleaner everyday piece using the tulip/Bipzilla identity with a soft pink detail.",
        "Small embroidered chest tulip + neck logo",
    ),
    Product(
        "Bipzilla Script Cap",
        "Bloom",
        24,
        "Washed Charcoal",
        "Cap",
        "One Size / Adjustable",
        "https://images.unsplash.com/photo-1521369909029-2afed882baee?auto=format&fit=crop&w=1100&q=80",
        "Accessory",
        "A washed cap with the uploaded Bipzilla logo text embroidered across the front.",
        "Front embroidered Bipzilla text",
    ),
]

COLLECTIONS = {
    "Ace of Hearts": "The signature first-drop design. Playing-card energy, luck, love and bold back prints.",
    "Pizza Samurai": "Playful, loud and memorable. Samurai attitude with vibrant pink and food-culture humour.",
    "Last Knight": "Darker warrior graphics, heavy hoodies, faded colours and premium streetwear styling.",
    "Bloom": "Minimal tulip-inspired pieces for daily wear, caps and embroidered basics.",
}

# -----------------------------
# CSS
# -----------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: #090909; color: #f7f1e8; }
    header[data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] { background: #0f0f0f; }
    .block-container { padding-top: 1.2rem; padding-bottom: 3rem; max-width: 1240px; }
    .nav-bar { display:flex; align-items:center; justify-content:space-between; padding: 16px 0 24px; border-bottom: 1px solid rgba(255,255,255,.09); }
    .brand { font-size: 28px; font-weight: 900; letter-spacing: -1px; }
    .brand span { color:#ffb3c7; }
    .nav-note { color:#a9a29a; font-size: 13px; }
    .hero { position:relative; min-height: 560px; border-radius: 34px; overflow:hidden; background: linear-gradient(120deg, rgba(0,0,0,.25), rgba(0,0,0,.86)), url('https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=1800&q=85'); background-size: cover; background-position:center; border: 1px solid rgba(255,255,255,.1); box-shadow: 0 30px 80px rgba(0,0,0,.45); }
    .hero-inner { position:absolute; left:48px; bottom:46px; max-width:720px; }
    .eyebrow { display:inline-flex; gap:8px; align-items:center; padding:8px 13px; border:1px solid rgba(255,255,255,.16); border-radius:999px; color:#ffd6df; background:rgba(0,0,0,.35); font-weight:700; font-size:13px; margin-bottom:18px; }
    h1.hero-title { font-size: clamp(48px, 8vw, 104px); line-height:.88; letter-spacing:-5px; margin:0; font-weight:900; color:#fff7ef; }
    .hero-copy { color:#ddd4ca; font-size:18px; max-width:620px; margin-top:18px; line-height:1.55; }
    .cta-row { display:flex; gap:12px; flex-wrap:wrap; margin-top:24px; }
    .button-like { padding:13px 18px; border-radius:999px; font-weight:800; display:inline-block; }
    .primary { background:#f7f1e8; color:#0b0b0b; }
    .secondary { border:1px solid rgba(255,255,255,.2); color:#f7f1e8; }
    .metric-grid { display:grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap:14px; margin:22px 0; }
    .metric { padding:18px; border:1px solid rgba(255,255,255,.09); border-radius:22px; background:#111; }
    .metric b { display:block; font-size:24px; color:#fff; }
    .metric span { color:#aaa; font-size:13px; }
    .section-title { font-size:38px; letter-spacing:-2px; margin: 52px 0 8px; color:#fff7ef; }
    .section-sub { color:#aaa29a; margin-bottom:20px; }
    .product-card { border:1px solid rgba(255,255,255,.1); background:#111; border-radius:28px; padding:12px; height:100%; box-shadow: 0 16px 40px rgba(0,0,0,.25); }
    .product-img { width:100%; height:360px; object-fit:cover; border-radius:22px; display:block; background:#222; }
    .product-info { padding:14px 5px 4px; }
    .badge { display:inline-block; font-size:11px; text-transform:uppercase; letter-spacing:.8px; padding:6px 9px; border-radius:999px; background:rgba(255,179,199,.12); color:#ffb3c7; border:1px solid rgba(255,179,199,.2); margin-bottom:10px; }
    .product-name { font-size:18px; font-weight:900; color:#fff; margin: 0 0 5px; }
    .muted { color:#aaa29a; font-size:13px; line-height:1.5; }
    .price { font-weight:900; color:#fff; font-size:20px; margin-top:8px; }
    .collection-card { padding:24px; border:1px solid rgba(255,255,255,.1); border-radius:28px; background: radial-gradient(circle at top right, rgba(255,179,199,.13), transparent 34%), #111; min-height:190px; }
    .collection-card h3 { margin:0 0 8px; font-size:26px; color:#fff; letter-spacing:-1px; }
    .detail-box { border:1px solid rgba(255,255,255,.1); background:#111; border-radius:26px; padding:22px; }
    .upload-box { border:1px dashed rgba(255,255,255,.26); border-radius:24px; padding:22px; background:#101010; }
    .lookbook { min-height:430px; border-radius:30px; background-size:cover; background-position:center; border:1px solid rgba(255,255,255,.1); position:relative; overflow:hidden; }
    .lookbook:after { content:""; position:absolute; inset:0; background:linear-gradient(180deg, transparent, rgba(0,0,0,.82)); }
    .lookbook p { position:absolute; z-index:2; left:24px; bottom:20px; color:#fff; font-weight:900; font-size:24px; max-width:330px; }
    .footer { margin-top:70px; padding-top:24px; border-top:1px solid rgba(255,255,255,.09); color:#888; font-size:13px; }
    div[data-testid="stButton"] button { border-radius:999px; font-weight:800; border:1px solid rgba(255,255,255,.14); background:#f7f1e8; color:#101010; }
    div[data-baseweb="select"] > div { background:#111; border-color:rgba(255,255,255,.16); color:#fff; }
    @media (max-width: 800px){ .hero-inner{left:24px; right:24px; bottom:28px;} .metric-grid{grid-template-columns:repeat(2,1fr);} .product-img{height:300px;} h1.hero-title{letter-spacing:-2px;} }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Helpers
# -----------------------------

def top_nav():
    st.markdown("""
    <div class="nav-bar">
      <div class="brand">BIP<span>ZILLA</span></div>
      <div class="nav-note">V12 premium streetwear demo · replace images with your final product photos</div>
    </div>
    """, unsafe_allow_html=True)


def product_card(p: Product):
    st.markdown(f"""
    <div class="product-card">
      <img src="{p.image}" class="product-img" />
      <div class="product-info">
        <span class="badge">{p.badge}</span>
        <p class="product-name">{p.name}</p>
        <div class="muted">{p.colour} · {p.fit}</div>
        <div class="price">£{p.price}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


def find_product(name: str) -> Product:
    return next(p for p in PRODUCTS if p.name == name)

# -----------------------------
# App
# -----------------------------

top_nav()

page = st.radio(
    "Navigation",
    ["Home", "Shop", "Product Detail", "Lookbook", "About", "Asset Upload Guide"],
    horizontal=True,
    label_visibility="collapsed",
)

if page == "Home":
    st.markdown("""
    <section class="hero">
      <div class="hero-inner">
        <div class="eyebrow">🃏 FIRST DROP · ACE OF HEARTS LEADS THE COLLECTION</div>
        <h1 class="hero-title">REAL CLOTHES.<br/>LOUD ART.</h1>
        <p class="hero-copy">Bipzilla is a premium streetwear concept built around real apparel photography, oversized fits, heavyweight blanks and signature graphic drops — Ace of Hearts, Pizza Samurai, Last Knight and Bloom.</p>
        <div class="cta-row"><span class="button-like primary">Shop First Drop</span><span class="button-like secondary">View Lookbook</span></div>
      </div>
    </section>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-grid">
      <div class="metric"><b>4</b><span>launch collections</span></div>
      <div class="metric"><b>240–460</b><span>GSM premium garment feel</span></div>
      <div class="metric"><b>Real</b><span>photo-based ecommerce layout</span></div>
      <div class="metric"><b>Ace</b><span>main hero artwork direction</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">Featured pieces</h2><p class="section-sub">The site is designed to look like real clothing first, with artwork printed onto the garments.</p>', unsafe_allow_html=True)
    cols = st.columns(3)
    for col, p in zip(cols, PRODUCTS[:3]):
        with col:
            product_card(p)

    st.markdown('<h2 class="section-title">First drop story</h2>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for col, (name, desc) in zip([c1,c2,c3,c4], COLLECTIONS.items()):
        with col:
            st.markdown(f'<div class="collection-card"><h3>{name}</h3><p class="muted">{desc}</p></div>', unsafe_allow_html=True)

elif page == "Shop":
    st.markdown('<h1 class="section-title">Shop First Drop</h1><p class="section-sub">Filter by collection, garment type and product vibe. Product images are realistic placeholders that should be replaced by your final mockups/photos.</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    collection = col1.selectbox("Collection", ["All"] + list(COLLECTIONS.keys()))
    garment = col2.selectbox("Garment", ["All"] + sorted(set(p.garment for p in PRODUCTS)))
    sort = col3.selectbox("Sort", ["Featured", "Price low to high", "Price high to low"])

    filtered = PRODUCTS
    if collection != "All":
        filtered = [p for p in filtered if p.collection == collection]
    if garment != "All":
        filtered = [p for p in filtered if p.garment == garment]
    if sort == "Price low to high":
        filtered = sorted(filtered, key=lambda p: p.price)
    elif sort == "Price high to low":
        filtered = sorted(filtered, key=lambda p: p.price, reverse=True)

    cols = st.columns(3)
    for i, p in enumerate(filtered):
        with cols[i % 3]:
            product_card(p)
            st.button("Add to cart demo", key=f"cart-{p.name}")

elif page == "Product Detail":
    chosen = st.selectbox("Choose product", [p.name for p in PRODUCTS])
    p = find_product(chosen)
    left, right = st.columns([1.05, .95], gap="large")
    with left:
        st.image(p.image, use_container_width=True)
        g1, g2, g3 = st.columns(3)
        for g in [g1,g2,g3]:
            with g:
                st.image(p.image, use_container_width=True)
    with right:
        st.markdown(f'<span class="badge">{p.collection}</span><h1 style="color:#fff;letter-spacing:-2px;margin:.4rem 0;">{p.name}</h1><div class="price">£{p.price}</div>', unsafe_allow_html=True)
        st.write(p.description)
        st.markdown(f"""
        <div class="detail-box">
          <b>Colour:</b> {p.colour}<br/>
          <b>Garment:</b> {p.garment}<br/>
          <b>Fit:</b> {p.fit}<br/>
          <b>Print placement:</b> {p.print_placement}<br/>
          <b>Style note:</b> Use your uploaded Bipzilla logo text, not a generic text logo.
        </div>
        """, unsafe_allow_html=True)
        size = st.radio("Size", ["S", "M", "L", "XL", "XXL"], horizontal=True)
        st.button(f"Add {size} to cart demo")
        st.info("Demo only: connect this later to Shopify, WooCommerce, Stripe, or a real checkout.")

elif page == "Lookbook":
    st.markdown('<h1 class="section-title">Lookbook</h1><p class="section-sub">This page sells the feeling of the brand: real models, real streetwear fits, real product photography.</p>', unsafe_allow_html=True)
    l1, l2 = st.columns(2)
    with l1:
        st.markdown("""<div class="lookbook" style="background-image:url('https://images.unsplash.com/photo-1529139574466-a303027c1d8b?auto=format&fit=crop&w=1200&q=85')"><p>Ace of Hearts hoodie as the hero product.</p></div>""", unsafe_allow_html=True)
    with l2:
        st.markdown("""<div class="lookbook" style="background-image:url('https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=1200&q=85')"><p>Oversized tees, clean styling, bold back prints.</p></div>""", unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Creative direction</h2>', unsafe_allow_html=True)
    st.write("Use dark studio shots, daylight street shots, fabric closeups, back-print photography and model-fit photos. The artwork should look printed, embroidered or screen-printed onto real garments — never floating on top.")

elif page == "About":
    st.markdown('<h1 class="section-title">About Bipzilla</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div class="detail-box">
    <h3 style="color:#fff;margin-top:0;">Bipzilla is a first-drop streetwear concept built around symbols.</h3>
    <p class="muted">The Ace of Hearts stands for luck, boldness and identity. The tulip brings the brand symbol. The samurai and knight pieces bring warrior energy. The result is a small but focused first collection that feels more like a real brand than random merch.</p>
    <p class="muted">The launch should stay limited: a few strong pieces, proper realistic photography, strong product pages and consistent Bipzilla logo placement.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">Launch checklist</h2>', unsafe_allow_html=True)
    st.checkbox("Replace placeholder photos with real clothing mockups/photos")
    st.checkbox("Upload real Ace of Hearts artwork")
    st.checkbox("Upload real Bipzilla logo text file")
    st.checkbox("Create front, back and close-up images for each product")
    st.checkbox("Connect checkout later using Shopify/WooCommerce/Stripe")

elif page == "Asset Upload Guide":
    st.markdown('<h1 class="section-title">Asset Upload Guide</h1><p class="section-sub">Use this page to understand exactly what to replace before showing the demo to people.</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="upload-box">
    <h3 style="color:#fff;margin-top:0;">1. Bipzilla logo text</h3>
    <p class="muted">Replace the text logo in the header with your uploaded Bipzilla logo image. Do not use a generic typed logo.</p>
    </div><br/>
    <div class="upload-box">
    <h3 style="color:#fff;margin-top:0;">2. Ace of Hearts artwork</h3>
    <p class="muted">Use this as the main hero back-print design. Put it on black hoodie, cream tee and washed charcoal hoodie.</p>
    </div><br/>
    <div class="upload-box">
    <h3 style="color:#fff;margin-top:0;">3. Real clothing images</h3>
    <p class="muted">Use real or realistic mockups: front, back, model shot and detail closeup. Avoid cartoon garments and flat shapes.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  BIPZILLA V12 Streamlit Website Demo · Built as a realistic ecommerce concept. Replace placeholders with your uploaded artwork and final product mockups.
</div>
""", unsafe_allow_html=True)
