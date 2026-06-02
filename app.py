import base64
from pathlib import Path
from typing import Dict, List

import streamlit as st

# -----------------------------
# Basic setup
# -----------------------------
st.set_page_config(
    page_title="BIPZILLA | Art • Culture • Streetwear",
    page_icon="🧿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets" / "products"

PRODUCTS: List[Dict] = [
    {
        "slug": "kraken-warlord-sweatshirt-black",
        "name": "Kraken Warlord Sweatshirt",
        "category": "Sweatshirts",
        "price": 59.99,
        "colour": "Washed Black",
        "finish": "Large front graphic print",
        "drop": "Abyss Drop",
        "image": "kraken-warlord-sweatshirt-black.webp",
        "description": "A heavyweight washed crewneck with a dramatic sea-warrior print, BIPZILLA chest branding and vintage poster energy.",
        "badge": "Hero Piece",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "samurai-fish-tee-black",
        "name": "Samurai Riot Fish Tee",
        "category": "T-Shirts",
        "price": 34.99,
        "colour": "Vintage Black",
        "finish": "Watercolour print",
        "drop": "Fish Riot",
        "image": "samurai-fish-tee-black.webp",
        "description": "A relaxed black tee using your blue fish artwork with a clean BIPZILLA wordmark and minimal typography.",
        "badge": "New In",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "royal-bloom-tee-white",
        "name": "Royal Bloom Tee",
        "category": "T-Shirts",
        "price": 34.99,
        "colour": "White",
        "finish": "Front card print",
        "drop": "Royal Bloom",
        "image": "royal-bloom-tee-white.webp",
        "description": "A crisp white tee with the ace-of-heart bloom card print and BIPZILLA graphic type below the artwork.",
        "badge": "Best Seller",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "bloom-mark-tee-pink",
        "name": "Bloom Mark Embroidered Tee",
        "category": "T-Shirts",
        "price": 29.99,
        "colour": "Dusty Pink",
        "finish": "Small embroidery style",
        "drop": "Royal Bloom",
        "image": "bloom-mark-tee-pink.webp",
        "description": "A simple everyday tee with a small chest placement for a cleaner embroidered look.",
        "badge": "Embroidery",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "royal-bloom-hoodie-black",
        "name": "Royal Bloom Hoodie",
        "category": "Hoodies",
        "price": 64.99,
        "colour": "Black",
        "finish": "Back print + sleeve mark",
        "drop": "Royal Bloom",
        "image": "royal-bloom-hoodie-black.webp",
        "description": "Black hoodie with a large back ace-card print, small front logo hit and sleeve detail.",
        "badge": "Limited",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "tokyo-nights-hoodie-cream",
        "name": "Tokyo Nights Hoodie",
        "category": "Hoodies",
        "price": 69.99,
        "colour": "Cream",
        "finish": "Back graphic print",
        "drop": "Tokyo Nights",
        "image": "tokyo-nights-hoodie-cream.webp",
        "description": "Cream hoodie with a Japanese night-city back print, black ink texture and subtle sleeve mark.",
        "badge": "Tokyo Night",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "kraken-warlord-hoodie-black",
        "name": "Kraken Warlord Hoodie",
        "category": "Hoodies",
        "price": 74.99,
        "colour": "Washed Black",
        "finish": "Large back graphic print",
        "drop": "Abyss Drop",
        "image": "kraken-warlord-hoodie-black.webp",
        "description": "Heavy black hoodie with a dark kraken warrior back print and subtle front BIPZILLA logo.",
        "badge": "Dark Drop",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "ocean-drift-hoodie-navy",
        "name": "Ocean Drift Hoodie",
        "category": "Hoodies",
        "price": 69.99,
        "colour": "Navy",
        "finish": "Back artwork print",
        "drop": "Ocean Drift",
        "image": "ocean-drift-hoodie-navy.webp",
        "description": "Navy hoodie with the ocean artwork on the back, small chest logo and premium streetwear fit.",
        "badge": "Artist Drop",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "midnight-slice-sweatshirt-pink",
        "name": "Midnight Slice Sweatshirt",
        "category": "Sweatshirts",
        "price": 54.99,
        "colour": "Soft Pink",
        "finish": "Back print + small front icon",
        "drop": "Midnight Slice",
        "image": "midnight-slice-sweatshirt-pink.webp",
        "description": "Pink crewneck with a playful pizza back print, Japanese side text and small front BIPZILLA hit.",
        "badge": "Playful",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "koi-legend-sweatshirt-cream",
        "name": "Koi Legend Sweatshirt",
        "category": "Sweatshirts",
        "price": 59.99,
        "colour": "Sand Cream",
        "finish": "Large back print",
        "drop": "Koi Legend",
        "image": "koi-legend-sweatshirt-cream.webp",
        "description": "Sand coloured crewneck with a bright koi mythology back piece and small front logo.",
        "badge": "Premium Print",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "samurai-riot-tee-cream",
        "name": "Samurai Riot Tee",
        "category": "T-Shirts",
        "price": 36.99,
        "colour": "Natural Cream",
        "finish": "Full front graphic print",
        "drop": "Samurai Riot",
        "image": "samurai-riot-tee-cream.webp",
        "description": "Cream tee with a bold samurai artwork print, small back logo and Japanese inspired layout.",
        "badge": "Statement Tee",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "royal-bloom-hoodie-cream",
        "name": "Royal Bloom Cream Hoodie",
        "category": "Hoodies",
        "price": 66.99,
        "colour": "Cream",
        "finish": "Large back card print",
        "drop": "Royal Bloom",
        "image": "royal-bloom-hoodie-cream.webp",
        "description": "Cream version of the Royal Bloom hoodie with a large back card print and BIPZILLA wordmark.",
        "badge": "Clean Colourway",
        "sizes": ["S", "M", "L", "XL"],
    },
    {
        "slug": "royal-bloom-hoodie-mini-black",
        "name": "Royal Bloom Mini Hoodie",
        "category": "Hoodies",
        "price": 62.99,
        "colour": "Black",
        "finish": "Small chest print",
        "drop": "Royal Bloom",
        "image": "royal-bloom-hoodie-mini-black.webp",
        "description": "A minimal black hoodie with a smaller chest placement for people who want a quieter BIPZILLA piece.",
        "badge": "Minimal",
        "sizes": ["S", "M", "L", "XL"],
    },
]

# -----------------------------
# Utilities
# -----------------------------
def asset_path(filename: str) -> Path:
    return ASSET_DIR / filename

@st.cache_data(show_spinner=False)
def image_data_uri(filename: str) -> str:
    path = asset_path(filename)
    mime = "image/webp" if path.suffix.lower() == ".webp" else "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

def money(value: float) -> str:
    return f"£{value:,.2f}"

def get_query_value(key: str, default: str = "") -> str:
    try:
        value = st.query_params.get(key, default)
    except Exception:
        value = st.experimental_get_query_params().get(key, [default])[0]
    if isinstance(value, list):
        return value[0] if value else default
    return value or default

def nav_link(label: str, page: str, active: str) -> str:
    active_class = "active" if page.lower() == active.lower() else ""
    return f'<a class="nav-link {active_class}" href="?page={page}">{label}</a>'

def add_to_cart(product: Dict, size: str = "M", qty: int = 1):
    cart = st.session_state.setdefault("cart", [])
    cart.append({"slug": product["slug"], "size": size, "qty": qty})
    st.toast(f"Added {product['name']} to cart", icon="🛒")

def find_product(slug: str):
    return next((p for p in PRODUCTS if p["slug"] == slug), None)

def cart_count() -> int:
    return sum(item.get("qty", 1) for item in st.session_state.get("cart", []))

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    :root{
        --pink:#ef2f67;
        --pink-dark:#d91755;
        --ink:#09090b;
        --muted:#666672;
        --line:#e9e9ee;
        --soft:#f7f7f8;
        --cream:#fff7ef;
        --cyan:#00c2bd;
        --purple:#6e3cff;
    }
    html, body, [data-testid="stAppViewContainer"]{background:#fff; color:var(--ink);}
    [data-testid="stSidebar"]{display:none;}
    [data-testid="collapsedControl"]{display:none;}
    header[data-testid="stHeader"]{background:rgba(255,255,255,.78); backdrop-filter: blur(12px);}
    .block-container{max-width:1220px; padding-top:0.7rem; padding-bottom:3rem;}
    #MainMenu, footer{visibility:hidden;}

    .top-strip{
        width:100%; background:linear-gradient(90deg,#ef2f67,#ff5d83);
        color:white; text-align:center; font-size:12px; letter-spacing:2px; font-weight:800;
        padding:8px 10px; text-transform:uppercase; border-radius:0 0 16px 16px;
        box-shadow:0 10px 30px rgba(239,47,103,.18);
    }
    .site-header{
        display:flex; align-items:center; justify-content:space-between; gap:22px;
        padding:24px 0 22px; border-bottom:1px solid var(--line); position:sticky; top:0; z-index:10;
        background:rgba(255,255,255,.95); backdrop-filter:blur(14px);
    }
    .logo-wrap{display:flex; flex-direction:column; line-height:.78; min-width:170px;}
    .brand-logo{
        font-family: Impact, Haettenschweiler, 'Arial Black', sans-serif;
        font-size:38px; letter-spacing:-1px; color:#000; text-transform:uppercase;
        text-decoration:none; transform:skew(-8deg); display:inline-block;
        text-shadow:2px 0 #ef2f67, -2px 0 #00c2bd;
    }
    .logo-sub{font-size:10px; font-weight:900; letter-spacing:3px; color:var(--pink); margin-top:8px; text-transform:uppercase;}
    .nav{display:flex; align-items:center; justify-content:center; gap:30px; flex-wrap:wrap;}
    .nav-link{font-size:13px; font-weight:900; letter-spacing:.8px; color:#0b0b0d!important; text-decoration:none; text-transform:uppercase; position:relative; padding:12px 0;}
    .nav-link.active:after{content:""; height:3px; background:var(--pink); border-radius:4px; position:absolute; left:0; right:0; bottom:4px;}
    .header-icons{display:flex; gap:12px; align-items:center; justify-content:flex-end; min-width:170px; font-size:22px;}
    .cart-pill{display:inline-flex; align-items:center; justify-content:center; min-width:30px; height:30px; padding:0 8px; border-radius:999px; background:#111; color:#fff!important; font-size:12px; font-weight:900; text-decoration:none;}

    .hero{
        display:grid; grid-template-columns: .9fr 1.1fr; gap:28px; align-items:center;
        min-height:560px; padding:46px 0 34px; border-bottom:1px solid var(--line);
        background:
          radial-gradient(circle at 78% 28%, rgba(239,47,103,.22), transparent 28%),
          radial-gradient(circle at 92% 48%, rgba(0,194,189,.12), transparent 22%),
          linear-gradient(90deg, #fff 0%, #fff 52%, #fff6f8 100%);
    }
    .eyebrow{color:var(--pink); font-weight:900; letter-spacing:1.6px; font-size:13px; text-transform:uppercase; margin-bottom:14px;}
    .hero h1{font-family:Impact, Haettenschweiler, 'Arial Black', sans-serif; font-size:76px; line-height:.86; letter-spacing:-1px; margin:0 0 22px; text-transform:uppercase; color:#050506;}
    .hero h1 span{color:var(--pink);}
    .hero p{max-width:455px; color:#28282d; font-size:17px; line-height:1.65; margin-bottom:28px;}
    .button-row{display:flex; gap:18px; align-items:center; flex-wrap:wrap;}
    .primary-btn, .secondary-btn{
        display:inline-flex; align-items:center; gap:10px; text-decoration:none!important; border-radius:0; padding:16px 28px;
        font-weight:900; font-size:13px; text-transform:uppercase; letter-spacing:.7px;
    }
    .primary-btn{background:var(--pink); color:white!important; box-shadow:0 14px 30px rgba(239,47,103,.25);}
    .secondary-btn{border:1.6px solid #111; color:#111!important; background:white;}
    .hero-art{position:relative; padding:8px 12px;}
    .hero-card{
        background:rgba(255,255,255,.72); border:1px solid rgba(0,0,0,.05); box-shadow:0 26px 70px rgba(0,0,0,.12); padding:16px; border-radius:28px;
    }
    .hero-card img{width:100%; display:block; border-radius:20px;}
    .jp-vertical{position:absolute; right:0; top:42px; font-size:42px; font-weight:900; writing-mode:vertical-rl; letter-spacing:8px; color:#09090b; opacity:.85;}
    .splash{position:absolute; right:8%; top:14%; width:56%; height:40%; background:linear-gradient(135deg, rgba(239,47,103,.45), rgba(255,92,131,.05)); filter:blur(0px); transform:rotate(-10deg); z-index:-1; border-radius:60% 45% 55% 50%;}

    .benefits{display:grid; grid-template-columns:repeat(4,1fr); gap:0; border-bottom:1px solid var(--line);}
    .benefit{display:flex; gap:15px; align-items:center; padding:24px 20px; border-right:1px solid var(--line);}
    .benefit:last-child{border-right:0;}
    .benefit-icon{font-size:28px;}
    .benefit strong{font-size:13px; text-transform:uppercase; display:block;}
    .benefit span{font-size:12px; color:var(--muted);}

    .section-head{display:flex; justify-content:space-between; align-items:end; gap:20px; margin:44px 0 20px;}
    .section-head h2{font-family:Impact, Haettenschweiler, 'Arial Black', sans-serif; text-transform:uppercase; font-size:44px; margin:0; letter-spacing:-.5px;}
    .section-head .mini{font-size:12px; color:var(--pink); font-weight:900; text-transform:uppercase; letter-spacing:1.3px; margin-bottom:8px;}
    .view-all{font-weight:900; color:#111!important; text-transform:uppercase; text-decoration:none!important; font-size:13px;}

    .product-card{border:0; background:#fff; padding-bottom:24px; min-height:100%;}
    .product-img-wrap{background:#f4f4f5; border-radius:2px; overflow:hidden; aspect-ratio: 4 / 5; display:flex; align-items:center; justify-content:center;}
    .product-img-wrap img{width:100%; height:100%; object-fit:cover; display:block; transition:transform .35s ease;}
    .product-card:hover .product-img-wrap img{transform:scale(1.025);}
    .product-name{font-weight:950; font-size:16px; text-transform:uppercase; margin-top:15px; line-height:1.1;}
    .product-meta{font-size:12px; color:var(--muted); margin:6px 0 4px; text-transform:uppercase; letter-spacing:.6px;}
    .product-price{font-weight:900; font-size:15px; margin-top:6px;}
    .badge{display:inline-block; padding:5px 9px; background:#111; color:#fff; border-radius:999px; font-size:10px; font-weight:900; text-transform:uppercase; letter-spacing:.6px; margin-top:10px;}
    .colour-dots{display:flex; gap:8px; align-items:center; margin:10px 0 0;}
    .dot{width:15px; height:15px; border:1px solid #d6d6dc; border-radius:50%; display:inline-block;}
    .dot.black{background:#111}.dot.white{background:#fff}.dot.pink{background:#f3a9ba}.dot.cream{background:#efe3cf}.dot.navy{background:#0d1a2e}.dot.grey{background:#68686f}

    div[data-testid="stButton"] > button{
        border-radius:0 !important; border:1px solid #111 !important; background:#fff !important; color:#111 !important;
        font-weight:900 !important; text-transform:uppercase !important; letter-spacing:.6px !important; padding:.65rem 1rem !important;
        transition:all .2s ease; width:100%;
    }
    div[data-testid="stButton"] > button:hover{background:#111 !important; color:#fff !important; border-color:#111 !important;}
    .pink-button div[data-testid="stButton"] > button{background:var(--pink)!important; color:#fff!important; border-color:var(--pink)!important;}

    .story-block{display:grid; grid-template-columns:1.05fr .95fr; gap:44px; align-items:center; margin:56px 0; padding:0 0 36px; border-bottom:1px solid var(--line);}
    .story-img{border-radius:0; overflow:hidden; background:#f4f4f5; box-shadow:0 22px 60px rgba(0,0,0,.08);}
    .story-img img{width:100%; display:block;}
    .story-copy h2{font-family:Impact, Haettenschweiler, 'Arial Black', sans-serif; font-size:46px; line-height:.94; margin:0 0 16px; text-transform:uppercase;}
    .story-copy p{color:#3b3b42; line-height:1.7;}
    .ghost-kanji{font-size:120px; color:#e7e7ea; font-weight:900; position:absolute; right:4%; z-index:-1; opacity:.85;}

    .newsletter{display:grid; grid-template-columns:1fr 1.1fr; gap:28px; align-items:center; padding:28px 0 44px;}
    .newsletter h3{font-family:Impact, Haettenschweiler, 'Arial Black', sans-serif; font-size:34px; text-transform:uppercase; margin:0 0 6px;}
    .footer{background:#08080a; color:#fff; padding:42px 44px; margin:20px -10px 0; display:grid; grid-template-columns:1.4fr repeat(4,1fr); gap:30px; border-radius:24px 24px 0 0;}
    .footer h4{font-size:12px; letter-spacing:.8px; text-transform:uppercase; margin:0 0 12px; color:#fff;}
    .footer a,.footer p{display:block; color:#c9c9d1!important; text-decoration:none; font-size:12px; line-height:1.9; margin:0;}
    .footer .brand-logo{color:#fff; font-size:33px;}
    .footer-tag{color:var(--pink); font-weight:900; letter-spacing:2px; font-size:11px; text-transform:uppercase; align-self:end;}

    .page-title{padding:42px 0 22px; border-bottom:1px solid var(--line); margin-bottom:24px;}
    .page-title h1{font-family:Impact, Haettenschweiler, 'Arial Black', sans-serif; font-size:64px; line-height:.9; margin:0; text-transform:uppercase;}
    .page-title p{color:#555; max-width:620px; line-height:1.65;}

    .lookbook-grid{display:grid; grid-template-columns:repeat(2,1fr); gap:28px;}
    .lookbook-card{background:#f6f6f8; padding:14px; border-radius:22px; box-shadow:0 16px 40px rgba(0,0,0,.05);}
    .lookbook-card img{width:100%; border-radius:16px; display:block;}
    .lookbook-card h3{font-family:Impact, Haettenschweiler, 'Arial Black', sans-serif; text-transform:uppercase; font-size:28px; margin:16px 6px 4px;}
    .lookbook-card p{color:#666; margin:0 6px 12px; font-size:14px;}

    .pill-row{display:flex; flex-wrap:wrap; gap:10px; margin:14px 0 0;}
    .pill{border:1px solid #dedee3; padding:8px 12px; border-radius:999px; color:#26262b; font-size:12px; font-weight:800; background:#fff;}
    .notice{padding:16px 18px; background:#fff5f7; border:1px solid #ffd3df; color:#6b1930; font-weight:700; border-radius:16px;}

    @media(max-width:900px){
        .site-header{position:relative; flex-direction:column; align-items:flex-start;}
        .nav{justify-content:flex-start; gap:18px;}
        .header-icons{min-width:auto;}
        .hero{grid-template-columns:1fr; min-height:auto; padding-top:26px;}
        .hero h1{font-size:56px;}
        .benefits{grid-template-columns:1fr 1fr;}
        .story-block,.newsletter{grid-template-columns:1fr;}
        .footer{grid-template-columns:1fr 1fr;}
        .lookbook-grid{grid-template-columns:1fr;}
    }
    @media(max-width:560px){
        .hero h1{font-size:46px;}
        .benefits{grid-template-columns:1fr;}
        .footer{grid-template-columns:1fr; padding:32px 24px;}
        .brand-logo{font-size:32px;}
        .page-title h1{font-size:46px;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header / Footer
# -----------------------------
def render_header(active_page: str):
    st.markdown('<div class="top-strip">✦ Free UK shipping on all orders over £70 ✦ Limited demo drop live now ✦</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="site-header">
            <div class="logo-wrap">
                <a class="brand-logo" href="?page=Home">BIPZILLA</a>
                <span class="logo-sub">Art • Culture • Streetwear</span>
            </div>
            <nav class="nav">
                {nav_link("Home", "Home", active_page)}
                {nav_link("Shop", "Shop", active_page)}
                {nav_link("New In", "New In", active_page)}
                {nav_link("Lookbook", "Lookbook", active_page)}
                {nav_link("About", "About", active_page)}
                {nav_link("Contact", "Contact", active_page)}
            </nav>
            <div class="header-icons">
                <span title="Search">⌕</span>
                <a class="cart-pill" href="?page=Cart">Cart {cart_count()}</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_footer():
    year = 2026
    st.markdown(
        f"""
        <div class="footer">
            <div>
                <div class="brand-logo">BIPZILLA</div>
                <p style="margin-top:18px;">Original art-led streetwear. Limited drops, strong visuals and wearable stories.</p>
                <p style="margin-top:18px;">© {year} BIPZILLA. Demo website.</p>
            </div>
            <div><h4>Shop</h4><a href="?page=Shop">All Products</a><a href="?page=Shop&cat=T-Shirts">T-Shirts</a><a href="?page=Shop&cat=Hoodies">Hoodies</a><a href="?page=Shop&cat=Sweatshirts">Sweatshirts</a></div>
            <div><h4>Info</h4><a href="?page=About">About Us</a><a href="?page=Lookbook">Lookbook</a><a href="?page=Contact">Contact</a><a href="?page=Shop">Size Guide</a></div>
            <div><h4>Support</h4><a href="?page=Contact">FAQ</a><a href="?page=Cart">Track Order</a><a href="?page=Contact">Shipping</a><a href="?page=Contact">Returns</a></div>
            <div><h4>Follow</h4><a>Instagram</a><a>TikTok</a><a>Email</a><div class="footer-tag">Art • Culture • Streetwear</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Product rendering
# -----------------------------
def colour_dot_class(colour: str) -> str:
    lower = colour.lower()
    if "black" in lower: return "black"
    if "white" in lower: return "white"
    if "pink" in lower: return "pink"
    if "cream" in lower or "sand" in lower or "natural" in lower: return "cream"
    if "navy" in lower: return "navy"
    return "grey"

def render_product_card(product: Dict, key_prefix: str = "card"):
    img = image_data_uri(product["image"])
    st.markdown(
        f"""
        <div class="product-card">
            <a href="?page=Shop&product={product['slug']}" style="text-decoration:none;color:inherit;">
              <div class="product-img-wrap"><img src="{img}" alt="{product['name']}"></div>
              <span class="badge">{product['badge']}</span>
              <div class="product-name">{product['name']}</div>
              <div class="product-meta">{product['category']} • {product['colour']} • {product['finish']}</div>
              <div class="product-price">{money(product['price'])}</div>
              <div class="colour-dots"><span class="dot {colour_dot_class(product['colour'])}"></span><span class="dot black"></span><span class="dot pink"></span></div>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Add to cart", key=f"{key_prefix}_{product['slug']}"):
        add_to_cart(product)

def product_grid(products: List[Dict], columns: int = 4, key_prefix: str = "grid"):
    if not products:
        st.info("No products found. Try another filter.")
        return
    for start in range(0, len(products), columns):
        cols = st.columns(columns, gap="large")
        for col, product in zip(cols, products[start:start+columns]):
            with col:
                render_product_card(product, key_prefix=key_prefix)

# -----------------------------
# Pages
# -----------------------------
def home_page():
    hero = image_data_uri("tokyo-nights-hoodie-cream.webp")
    st.markdown(
        f"""
        <section class="hero">
            <div>
                <div class="eyebrow">Original drops • UK streetwear • Artist led</div>
                <h1>Wear<br>Your Story<span>.</span></h1>
                <p>BIPZILLA is a clothing brand built around original art, bold graphics and clean limited pieces. Hoodies, tees and sweatshirts made to look like proper streetwear, not just artwork on a page.</p>
                <div class="button-row">
                    <a class="primary-btn" href="?page=Shop">Shop the drop →</a>
                    <a class="secondary-btn" href="?page=Lookbook">View lookbook</a>
                </div>
                <div class="pill-row">
                    <span class="pill">Limited drops</span><span class="pill">Real clothing mockups</span><span class="pill">Print + embroidery</span>
                </div>
            </div>
            <div class="hero-art">
                <div class="splash"></div>
                <div class="jp-vertical">ビップジラ</div>
                <div class="hero-card"><img src="{hero}" alt="Tokyo Nights Hoodie"></div>
            </div>
        </section>
        <section class="benefits">
            <div class="benefit"><div class="benefit-icon">🌍</div><div><strong>Worldwide Shipping</strong><span>Demo shipping setup</span></div></div>
            <div class="benefit"><div class="benefit-icon">🏷️</div><div><strong>Limited Drops</strong><span>No boring restocks</span></div></div>
            <div class="benefit"><div class="benefit-icon">🔒</div><div><strong>Demo Checkout</strong><span>Cart works as a prototype</span></div></div>
            <div class="benefit"><div class="benefit-icon">👕</div><div><strong>Premium Look</strong><span>Realistic product mockups</span></div></div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-head">
            <div><div class="mini">Featured</div><h2>Latest Drops</h2></div>
            <a class="view-all" href="?page=Shop">View all →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    featured = [
        find_product("kraken-warlord-sweatshirt-black"),
        find_product("samurai-fish-tee-black"),
        find_product("royal-bloom-hoodie-black"),
        find_product("tokyo-nights-hoodie-cream"),
    ]
    product_grid([p for p in featured if p], columns=4, key_prefix="home_featured")

    story_img = image_data_uri("ocean-drift-hoodie-navy.webp")
    st.markdown(
        f"""
        <div class="story-block">
          <div class="story-img"><img src="{story_img}" alt="Ocean Drift Hoodie lookbook"></div>
          <div class="story-copy" style="position:relative;">
            <div class="ghost-kanji">夢</div>
            <div class="eyebrow">Our Story</div>
            <h2>More than clothes.<br>It’s a movement.</h2>
            <p>BIPZILLA mixes your own watercolour artwork, Japanese-inspired typography and streetwear silhouettes. The idea is simple: make wearable art that feels bold, limited and personal.</p>
            <a class="secondary-btn" href="?page=About">Read our story →</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-head">
            <div><div class="mini">Clean pieces</div><h2>Embroidery Style</h2></div>
            <a class="view-all" href="?page=Shop&cat=T-Shirts">View tees →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    product_grid([
        find_product("bloom-mark-tee-pink"),
        find_product("royal-bloom-hoodie-mini-black"),
        find_product("midnight-slice-sweatshirt-pink"),
        find_product("royal-bloom-tee-white"),
    ], columns=4, key_prefix="home_embroidery")

    newsletter_block()

def newsletter_block():
    st.markdown(
        """
        <div class="newsletter">
          <div>
            <div class="eyebrow">Join the movement</div>
            <h3>Be the first to know.</h3>
            <p style="color:#666;margin:0;">Early access to drops, mockups, offers and behind-the-scenes art.</p>
          </div>
          <div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns([3,1])
    with col1:
        email = st.text_input("Email address", placeholder="Enter your email address", label_visibility="collapsed", key="newsletter_email")
    with col2:
        if st.button("Subscribe", key="newsletter_btn"):
            st.success("Nice — you’re on the demo list." if email else "Add an email first.")
    st.markdown("</div></div>", unsafe_allow_html=True)

def shop_page(new_only: bool = False):
    selected_slug = get_query_value("product", "")
    if selected_slug:
        product_detail_page(selected_slug)
        return

    title = "New In" if new_only else "Shop the Drop"
    st.markdown(
        f"""
        <div class="page-title">
            <div class="eyebrow">BIPZILLA Store</div>
            <h1>{title}<span style="color:#ef2f67;">.</span></h1>
            <p>Browse the demo drop. Filter by tees, hoodies and sweatshirts. Prices are fake UK demo prices so you can preview how the store will feel before selling.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    categories = ["All", "T-Shirts", "Hoodies", "Sweatshirts"]
    query_cat = get_query_value("cat", "All")
    if query_cat not in categories:
        query_cat = "All"
    c1, c2, c3 = st.columns([1.2, 1.2, 1])
    with c1:
        category = st.selectbox("Category", categories, index=categories.index(query_cat))
    with c2:
        sort = st.selectbox("Sort by", ["Featured", "Price: Low to High", "Price: High to Low", "Name A-Z"])
    with c3:
        search = st.text_input("Search", placeholder="kraken, hoodie, pink...")

    filtered = PRODUCTS.copy()
    if new_only:
        filtered = [p for p in filtered if p["badge"] in ["New In", "Hero Piece", "Tokyo Night", "Statement Tee", "Artist Drop"]]
    if category != "All":
        filtered = [p for p in filtered if p["category"] == category]
    if search:
        s = search.strip().lower()
        filtered = [p for p in filtered if s in p["name"].lower() or s in p["colour"].lower() or s in p["drop"].lower() or s in p["finish"].lower()]
    if sort == "Price: Low to High":
        filtered.sort(key=lambda p: p["price"])
    elif sort == "Price: High to Low":
        filtered.sort(key=lambda p: p["price"], reverse=True)
    elif sort == "Name A-Z":
        filtered.sort(key=lambda p: p["name"])

    st.markdown(f"<p style='color:#666;font-weight:800;text-transform:uppercase;letter-spacing:1px;'>{len(filtered)} products</p>", unsafe_allow_html=True)
    product_grid(filtered, columns=4, key_prefix="shop")

    st.markdown("---")
    st.markdown("### Size guide")
    st.dataframe(
        {
            "Size": ["S", "M", "L", "XL"],
            "Chest": ["36–38 in", "38–40 in", "40–43 in", "43–46 in"],
            "Fit": ["Relaxed", "Relaxed", "Oversized", "Oversized"],
        },
        use_container_width=True,
        hide_index=True,
    )

def product_detail_page(slug: str):
    product = find_product(slug)
    if not product:
        st.error("Product not found.")
        st.markdown('<a class="secondary-btn" href="?page=Shop">Back to shop</a>', unsafe_allow_html=True)
        return

    st.markdown('<div style="padding:28px 0 10px;"><a class="view-all" href="?page=Shop">← Back to shop</a></div>', unsafe_allow_html=True)
    left, right = st.columns([1.05, .95], gap="large")
    with left:
        st.image(str(asset_path(product["image"])), use_container_width=True)
    with right:
        st.markdown(
            f"""
            <div class="eyebrow">{product['drop']} • {product['badge']}</div>
            <h1 style="font-family:Impact, Haettenschweiler, 'Arial Black', sans-serif; font-size:58px; line-height:.9; text-transform:uppercase; margin:0 0 10px;">{product['name']}<span style="color:#ef2f67;">.</span></h1>
            <h2 style="margin:0 0 18px;">{money(product['price'])}</h2>
            <p style="color:#444;line-height:1.75;font-size:16px;">{product['description']}</p>
            <div class="pill-row"><span class="pill">{product['category']}</span><span class="pill">{product['colour']}</span><span class="pill">{product['finish']}</span></div>
            """,
            unsafe_allow_html=True,
        )
        size = st.radio("Choose size", product["sizes"], horizontal=True, key=f"size_{slug}")
        qty = st.number_input("Quantity", min_value=1, max_value=5, value=1, step=1, key=f"qty_{slug}")
        if st.button("Add to cart", key=f"detail_add_{slug}"):
            add_to_cart(product, size=size, qty=qty)
        st.markdown(
            """
            <div class="notice" style="margin-top:20px;">Demo only: checkout and payment are placeholders. Use this site to show your brand, product idea and layout.</div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="section-head">
            <div><div class="mini">You may also like</div><h2>Similar Pieces</h2></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    similar = [p for p in PRODUCTS if p["slug"] != slug and p["category"] == product["category"]][:4]
    if len(similar) < 4:
        similar += [p for p in PRODUCTS if p["slug"] != slug and p not in similar][:4-len(similar)]
    product_grid(similar, columns=4, key_prefix="similar")

def lookbook_page():
    st.markdown(
        """
        <div class="page-title">
          <div class="eyebrow">Lookbook</div>
          <h1>Real mockup energy<span style="color:#ef2f67;">.</span></h1>
          <p>A clean product showcase using the clothing images you liked: front/back hoodies, tees and sweatshirt mockups with proper shadows and realistic garment shapes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cards = [
        ("Kraken Warlord", "Dark fantasy hoodie and sweatshirt direction with strong back print placement.", "kraken-warlord-hoodie-black.webp"),
        ("Royal Bloom", "Ace-card graphic with clean front/back placements and logo consistency.", "royal-bloom-hoodie-black.webp"),
        ("Tokyo Nights", "Cream hoodie with Japanese inspired city graphic for a premium streetwear feel.", "tokyo-nights-hoodie-cream.webp"),
        ("Ocean Drift", "Navy hoodie using your watercolour ocean artwork as a back print.", "ocean-drift-hoodie-navy.webp"),
        ("Midnight Slice", "Pink sweatshirt with a playful graphic and small front detail.", "midnight-slice-sweatshirt-pink.webp"),
        ("Samurai Riot", "Bold cream tee with a strong samurai illustration and Japanese text.", "samurai-riot-tee-cream.webp"),
    ]
    html = '<div class="lookbook-grid">'
    for title, desc, img in cards:
        html += f"""
        <div class="lookbook-card">
          <img src="{image_data_uri(img)}" alt="{title}">
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
        """
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def about_page():
    st.markdown(
        """
        <div class="page-title">
          <div class="eyebrow">About the brand</div>
          <h1>Art first. Clothing second. Culture always<span style="color:#ef2f67;">.</span></h1>
          <p>BIPZILLA is a streetwear concept built from original drawings, watercolour texture, bold Japanese-inspired layouts and wearable everyday blanks.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns([1,1], gap="large")
    with c1:
        st.image(str(asset_path("samurai-riot-tee-cream.webp")), use_container_width=True)
    with c2:
        st.markdown(
            """
            ### The idea
            BIPZILLA should feel like a proper clothing brand, not an art gallery. The artwork is the identity, but the product still needs realistic garment mockups, strong names, good prices and a clear drop system.

            ### Brand pillars
            - **Original art** — your drawings and generated concepts become wearable pieces.
            - **Limited drops** — smaller collections make the brand feel special.
            - **Print + embroidery** — bold back prints, small chest logos and simple embroidered pieces.
            - **Streetwear layout** — big product visuals, strong typography and clean navigation.
            """
        )
    st.markdown("---")
    st.markdown("### Suggested next drops")
    st.dataframe(
        {
            "Drop": ["Royal Bloom", "Tokyo Nights", "Abyss Drop", "Ocean Drift", "Midnight Slice"],
            "Main product": ["Hoodie + Tee", "Cream Hoodie", "Washed Hoodie + Sweatshirt", "Navy Hoodie", "Pink Sweatshirt"],
            "Finish": ["Card print + small embroidery", "Back graphic print", "Large dark print", "Back artwork print", "Back print + small icon"],
        },
        use_container_width=True,
        hide_index=True,
    )

def contact_page():
    st.markdown(
        """
        <div class="page-title">
          <div class="eyebrow">Contact</div>
          <h1>Talk to BIPZILLA<span style="color:#ef2f67;">.</span></h1>
          <p>This contact page works as a demo form inside Streamlit. Later you can connect it to email, Google Sheets or a real ecommerce platform.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns([1.05,.95], gap="large")
    with c1:
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            topic = st.selectbox("Topic", ["General question", "Order question", "Wholesale", "Collaboration", "Website feedback"])
            message = st.text_area("Message", height=160)
            submitted = st.form_submit_button("Send message")
            if submitted:
                if name and email and message:
                    st.success("Message saved in the demo. Connect this form to email later.")
                else:
                    st.warning("Please fill in name, email and message.")
    with c2:
        st.markdown(
            """
            ### Demo support details
            **Email:** hello@bipzilla.co.uk  
            **Instagram:** @bipzilla  
            **Location:** UK-based concept brand

            #### FAQ
            **Is this a real shop?**  
            Not yet. It is a working demo for your Streamlit Cloud site.

            **Can customers pay?**  
            No. The cart and checkout are placeholders.

            **Can I add real payment later?**  
            Yes, but for selling properly you may want Shopify, WooCommerce, Stripe Checkout, or a POD supplier flow.
            """
        )

def cart_page():
    st.markdown(
        """
        <div class="page-title">
          <div class="eyebrow">Cart</div>
          <h1>Your demo cart<span style="color:#ef2f67;">.</span></h1>
          <p>This cart is only for previewing the shop experience. It does not take payment.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cart = st.session_state.setdefault("cart", [])
    if not cart:
        st.info("Your cart is empty.")
        st.markdown('<a class="primary-btn" href="?page=Shop">Start shopping →</a>', unsafe_allow_html=True)
        return

    total = 0.0
    for index, item in enumerate(cart):
        product = find_product(item["slug"])
        if not product:
            continue
        line_total = product["price"] * item.get("qty", 1)
        total += line_total
        c1, c2, c3 = st.columns([1, 2.2, .9])
        with c1:
            st.image(str(asset_path(product["image"])), use_container_width=True)
        with c2:
            st.markdown(f"### {product['name']}")
            st.write(f"Size: **{item.get('size','M')}** · Quantity: **{item.get('qty',1)}**")
            st.write(product["finish"])
        with c3:
            st.markdown(f"### {money(line_total)}")
            if st.button("Remove", key=f"remove_{index}"):
                cart.pop(index)
                st.rerun()
        st.markdown("---")

    st.markdown(f"## Total: {money(total)}")
    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("Clear cart"):
            st.session_state["cart"] = []
            st.rerun()
    with c2:
        if st.button("Demo checkout"):
            st.success("Checkout placeholder. Add Stripe/Shopify/WooCommerce later for real orders.")

# -----------------------------
# Router
# -----------------------------
page = get_query_value("page", "Home")
if page not in ["Home", "Shop", "New In", "Lookbook", "About", "Contact", "Cart"]:
    page = "Home"

render_header(page)

if page == "Home":
    home_page()
elif page == "Shop":
    shop_page(new_only=False)
elif page == "New In":
    shop_page(new_only=True)
elif page == "Lookbook":
    lookbook_page()
elif page == "About":
    about_page()
elif page == "Contact":
    contact_page()
elif page == "Cart":
    cart_page()

render_footer()
