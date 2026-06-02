
import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="BIPZILLA — Art Culture Streetwear", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"

PRODUCTS = [{'sku': 'royal-bloom-hoodie', 'name': 'Royal Bloom Hoodie', 'category': 'Hoodies', 'price': 64.99, 'image': 'royal_bloom_hoodie', 'colour': 'Black', 'tag': 'Signature Drop', 'badge': 'Back Print', 'finish': 'Screen print + small embroidery sleeve detail', 'fit': 'Oversized heavyweight hoodie', 'story': 'The main BIPZILLA playing-card artwork on a black heavyweight hoodie. Clean front logo, bold back card print.'}, {'sku': 'kraken-warlord-hoodie', 'name': 'Kraken Warlord Hoodie', 'category': 'Hoodies', 'price': 72.99, 'image': 'kraken_warlord_hoodie', 'colour': 'Washed Black', 'tag': 'Limited', 'badge': 'Graphic Back', 'finish': 'Large back print with washed garment effect', 'fit': 'Oversized heavyweight hoodie', 'story': 'Dark mythic streetwear piece with purple kraken energy and a subtle front chest logo.'}, {'sku': 'tokyo-nights-hoodie', 'name': 'Tokyo Nights Hoodie', 'category': 'Hoodies', 'price': 69.99, 'image': 'tokyo_nights_hoodie', 'colour': 'Natural Cream', 'tag': 'New In', 'badge': 'Statement', 'finish': 'Back print + sleeve mark', 'fit': 'Boxy oversized hoodie', 'story': 'Cream hoodie with black ink city artwork, red sun detail and Japanese-style lettering.'}, {'sku': 'ocean-drift-hoodie', 'name': 'Ocean Drift Hoodie', 'category': 'Hoodies', 'price': 68.99, 'image': 'ocean_drift_hoodie', 'colour': 'Deep Navy', 'tag': 'Art Drop', 'badge': 'Back Print', 'finish': 'Large full-colour back print, woven hem label', 'fit': 'Relaxed heavyweight hoodie', 'story': 'Watercolour ocean chaos turned into a wearable back graphic with the BIPZILLA chest logo.'}, {'sku': 'royal-bloom-tee-white', 'name': 'Royal Bloom Tee', 'category': 'T-Shirts', 'price': 34.99, 'image': 'royal_bloom_tee_white', 'colour': 'White', 'tag': 'Core', 'badge': 'Front Print', 'finish': 'DTG front print with clean card layout', 'fit': 'Heavy boxy tee', 'story': 'A clean white tee version of the ace-card logo. Strong enough for the first physical drop.'}, {'sku': 'samurai-riot-tee', 'name': 'Samurai Riot Tee', 'category': 'T-Shirts', 'price': 39.99, 'image': 'samurai_riot_tee', 'colour': 'Vintage Cream', 'tag': 'New In', 'badge': 'Art Print', 'finish': 'Large front graphic + small back neck logo', 'fit': 'Boxy heavyweight tee', 'story': 'A loud samurai artwork tee with BIPZILLA branding and streetwear poster energy.'}, {'sku': 'fish-riot-tee', 'name': 'Fish Riot Tee', 'category': 'T-Shirts', 'price': 36.99, 'image': 'samurai_fish_tee', 'colour': 'Washed Black', 'tag': 'Studio Art', 'badge': 'Front Print', 'finish': 'Watercolour fish print + printed text', 'fit': 'Oversized washed tee', 'story': 'Uses your original fish artwork as a clean, unusual streetwear tee.'}, {'sku': 'pink-embroidery-tee', 'name': 'Bloom Mini Embroidery Tee', 'category': 'T-Shirts', 'price': 31.99, 'image': 'pink_embroidery_tee', 'colour': 'Dusty Pink', 'tag': 'Minimal', 'badge': 'Embroidery', 'finish': 'Small chest embroidery style logo', 'fit': 'Boxy soft cotton tee', 'story': 'Minimal version for people who want the brand, not a huge graphic.'}, {'sku': 'koi-legend-sweatshirt', 'name': 'Koi Legend Sweatshirt', 'category': 'Sweatshirts', 'price': 59.99, 'image': 'koi_legend_sweatshirt', 'colour': 'Stone', 'tag': 'Premium', 'badge': 'Back Print', 'finish': 'Full-colour back print + tiny chest logo', 'fit': 'Relaxed heavyweight sweatshirt', 'story': 'Koi artwork with mythology, water and Japanese-inspired typography. A premium sweatshirt drop.'}, {'sku': 'midnight-slice-sweatshirt', 'name': 'Midnight Slice Sweatshirt', 'category': 'Sweatshirts', 'price': 54.99, 'image': 'midnight_slice_sweatshirt', 'colour': 'Soft Pink', 'tag': 'Fun Drop', 'badge': 'Back Print', 'finish': 'Back print + tiny hem embroidery detail', 'fit': 'Relaxed crewneck sweatshirt', 'story': 'Playful pizza artwork on a pink sweatshirt with a small front logo and bold back graphic.'}, {'sku': 'kraken-warlord-sweatshirt', 'name': 'Kraken Warlord Sweatshirt', 'category': 'Sweatshirts', 'price': 58.99, 'image': 'kraken_sweatshirt', 'colour': 'Washed Black', 'tag': 'Dark Drop', 'badge': 'Poster Print', 'finish': 'Large front poster graphic', 'fit': 'Heavyweight crewneck sweatshirt', 'story': 'A dark poster-style sweatshirt using the kraken/warrior idea, made to feel like band merch.'}, {'sku': 'minimal-card-hoodie', 'name': 'Royal Bloom Mini Hoodie', 'category': 'Hoodies', 'price': 62.99, 'image': 'minimal_black_hoodie', 'colour': 'Black', 'tag': 'Minimal', 'badge': 'Embroidery', 'finish': 'Small embroidered chest card and BIPZILLA text', 'fit': 'Clean everyday hoodie', 'story': 'The simple daily wear version. Low-key front placement with the same BIPZILLA identity.'}]

NAV = [
    ("home", "HOME"),
    ("shop", "SHOP"),
    ("new", "NEW IN"),
    ("lookbook", "LOOKBOOK"),
    ("about", "ABOUT"),
    ("contact", "CONTACT"),
]

@st.cache_data(show_spinner=False)
def img64(filename: str) -> str:
    path = ASSET_DIR / filename
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def qp_get(name: str, default: str = "") -> str:
    try:
        val = st.query_params.get(name, default)
    except Exception:
        val = default
    if isinstance(val, list):
        return val[0] if val else default
    return val or default


def money(v: float) -> str:
    return f"£{v:,.2f}"


def cart_count() -> int:
    return sum(item.get("qty", 0) for item in st.session_state.get("cart", {}).values())


def add_to_cart(product, size="M"):
    st.session_state.setdefault("cart", {})
    key = f"{product['sku']}::{size}"
    if key not in st.session_state.cart:
        st.session_state.cart[key] = {"sku": product["sku"], "size": size, "qty": 0}
    st.session_state.cart[key]["qty"] += 1


def get_product(sku: str):
    return next((p for p in PRODUCTS if p["sku"] == sku), None)


def css():
    st.markdown('''
<style>
:root{
  --pink:#ee2d67; --pink2:#ff4d86; --ink:#050505; --muted:#696969; --line:#e7e7e7;
  --paper:#fbfbfb; --cream:#f8f2e8; --dark:#09090b; --teal:#00b8aa; --purple:#7b48d8;
}
#MainMenu, footer, header[data-testid="stHeader"]{visibility:hidden; height:0;}
[data-testid="stSidebar"]{display:none;}
.block-container{padding:0 0 3rem 0; max-width:100% !important;}
.stApp{background:#fff; color:var(--ink);}
*{box-sizing:border-box;}
a{text-decoration:none; color:inherit;}
.bz-topbar{height:34px; background:linear-gradient(90deg,#e7225e,#ff4b7f); color:#fff; display:flex; align-items:center; justify-content:center; gap:12px; font-size:12px; letter-spacing:2px; font-weight:800;}
.bz-header{position:sticky; top:0; z-index:99; background:rgba(255,255,255,.96); backdrop-filter:blur(14px); border-bottom:1px solid #ededed;}
.bz-navwrap{max-width:1280px; margin:0 auto; height:92px; padding:0 32px; display:flex; align-items:center; justify-content:space-between; gap:28px;}
.bz-logo{width:156px; height:auto; display:block;}
.bz-nav{display:flex; align-items:center; gap:34px; font-size:13px; font-weight:900; letter-spacing:.8px;}
.bz-nav a{position:relative; padding:36px 0 32px;}
.bz-nav a.active:after,.bz-nav a:hover:after{content:""; position:absolute; left:0; right:0; bottom:22px; height:3px; background:var(--pink);}
.bz-actions{display:flex; align-items:center; gap:18px; font-size:20px;}
.bz-cart{position:relative; font-size:20px;}
.bz-cart span{position:absolute; top:-9px; right:-12px; min-width:18px; height:18px; padding:0 5px; background:var(--pink); color:#fff; border-radius:999px; font-size:10px; display:flex; align-items:center; justify-content:center; font-weight:900;}
.bz-page{max-width:1280px; margin:0 auto; padding:0 32px;}
.bz-hero{min-height:600px; display:grid; grid-template-columns:0.85fr 1.15fr; align-items:center; border-bottom:1px solid #eee; overflow:hidden; background:radial-gradient(circle at 80% 45%, rgba(238,45,103,.20), transparent 28%), #fff;}
.hero-copy{padding:78px 0 78px 76px; z-index:2;}
.kicker{color:var(--pink); font-weight:900; letter-spacing:1.2px; font-size:13px; text-transform:uppercase;}
.hero-title{font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; font-size:74px; line-height:.88; letter-spacing:-1px; margin:18px 0 22px; color:#000;}
.hero-title b{color:var(--pink);}
.hero-p{font-size:17px; line-height:1.55; color:#333; max-width:430px; margin-bottom:30px;}
.hero-buttons{display:flex; gap:18px; flex-wrap:wrap;}
.btn-main,.btn-outline,.mini-link{display:inline-flex; align-items:center; gap:12px; justify-content:center; font-weight:900; letter-spacing:.3px; border:2px solid #111; padding:16px 24px; font-size:13px; text-transform:uppercase;}
.btn-main{background:var(--pink); border-color:var(--pink); color:#fff; box-shadow:0 12px 26px rgba(238,45,103,.22);}
.btn-outline{background:#fff; color:#000;}
.hero-art{height:600px; position:relative; display:flex; align-items:center; justify-content:center; overflow:hidden;}
.hero-art:before{content:""; position:absolute; width:760px; height:520px; right:88px; top:42px; background:radial-gradient(circle, rgba(238,45,103,.92), transparent 42%), radial-gradient(circle at 65% 50%, #111, transparent 33%); filter:blur(4px); opacity:.18; transform:rotate(-8deg);}
.hero-art:after{content:"ビップジラ"; position:absolute; right:34px; top:118px; writing-mode:vertical-rl; font-size:58px; font-weight:1000; letter-spacing:2px; color:#080808; font-family:Impact, sans-serif;}
.hero-image{position:relative; z-index:2; width:min(480px,72%); aspect-ratio:4/5; object-fit:cover; border-radius:0; box-shadow:0 34px 70px rgba(0,0,0,.24);}
.hero-logo-floating{position:absolute; left:90px; bottom:60px; width:210px; opacity:.22; transform:rotate(-4deg);}
.bz-benefits{border-bottom:1px solid #eee; background:#fff;}
.benefit-grid{max-width:1280px; margin:0 auto; padding:24px 32px; display:grid; grid-template-columns:repeat(4,1fr); gap:0;}
.benefit{display:flex; gap:16px; align-items:center; padding:0 22px; border-right:1px solid #eee;}
.benefit:last-child{border-right:0;}
.benefit-ico{font-size:30px; color:#111;}
.benefit b{display:block; font-size:13px; font-weight:1000; letter-spacing:.3px;}
.benefit span{font-size:12px; color:#555;}
.section-head{display:flex; justify-content:space-between; align-items:end; margin:38px 0 18px;}
.section-kicker{color:var(--pink); font-size:12px; font-weight:1000; text-transform:uppercase; letter-spacing:.8px;}
.section-title{font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; font-size:44px; line-height:1; letter-spacing:-.3px; margin:6px 0 0;}
.view-all{font-weight:900; font-size:13px;}
.product-card{background:#fff; border:1px solid transparent; padding:0; transition:.18s ease; min-height:100%;}
.product-card:hover{transform:translateY(-3px);}
.product-img-wrap{position:relative; overflow:hidden; background:#f5f5f5; aspect-ratio: 1/1.16; display:flex; align-items:center; justify-content:center;}
.product-img{width:100%; height:100%; object-fit:cover; display:block; transition:transform .25s ease;}
.product-card:hover .product-img{transform:scale(1.025);}
.badge{position:absolute; top:12px; left:12px; background:#111; color:#fff; padding:7px 10px; font-size:10px; font-weight:900; letter-spacing:.8px; text-transform:uppercase;}
.product-title{font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; font-size:20px; letter-spacing:.4px; margin:14px 0 2px; text-transform:uppercase;}
.product-price{font-weight:900; font-size:14px; margin-bottom:7px;}
.swatches{display:flex; gap:8px; margin:8px 0 14px;}
.swatch{width:15px; height:15px; border-radius:99px; border:1px solid #bbb; display:inline-block;}
.product-meta{font-size:12px; color:#666; line-height:1.45; min-height:35px;}
.story-band{display:grid; grid-template-columns:1fr 1.2fr; gap:52px; align-items:center; margin:58px 0; background:linear-gradient(90deg,#fff,#f7f7f7); border-top:1px solid #eee; border-bottom:1px solid #eee; padding:38px 0;}
.story-img{width:100%; height:360px; object-fit:cover;}
.story-copy h2{font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; font-size:48px; line-height:.98; margin:8px 0 18px;}
.story-copy p{max-width:470px; color:#333; line-height:1.55;}
.newsletter{display:grid; grid-template-columns:1fr 1.2fr; gap:42px; align-items:center; padding:42px 0; border-top:1px solid #eee;}
.newsletter h3{font-family:Impact, sans-serif; font-size:34px; margin:0;}
.fake-input{height:50px; border:1px solid #ddd; padding:0 18px; display:flex; align-items:center; color:#777; background:#fff;}
.form-row{display:grid; grid-template-columns:1fr 170px; gap:12px;}
.bz-footer{background:#070707; color:#fff; margin-top:38px;}
.footer-inner{max-width:1280px; margin:0 auto; padding:48px 32px; display:grid; grid-template-columns:1.2fr repeat(4,1fr); gap:36px;}
.footer-logo{width:150px; filter:brightness(1.2);}
.footer-col b{font-size:13px; letter-spacing:.8px;}
.footer-col a,.footer-col p{display:block; color:#cfcfcf; font-size:12px; margin:9px 0;}
.footer-bottom{max-width:1280px; margin:0 auto; padding:0 32px 28px; color:#999; font-size:11px; display:flex; justify-content:space-between;}
.page-title{font-family:Impact, sans-serif; font-size:62px; margin:36px 0 8px; line-height:1;}
.page-sub{color:#555; max-width:700px; line-height:1.55; margin-bottom:28px;}
.filter-box{background:#f8f8f8; border:1px solid #eee; padding:18px; margin:22px 0 30px;}
.product-detail{display:grid; grid-template-columns:1.05fr .95fr; gap:58px; align-items:start; padding-top:36px;}
.detail-img{width:100%; border:1px solid #eee; background:#f4f4f4;}
.detail-title{font-family:Impact, sans-serif; font-size:58px; line-height:.95; margin:0 0 10px;}
.detail-price{font-size:24px; font-weight:1000; margin:12px 0;}
.detail-pill{display:inline-block; border:1px solid #111; padding:7px 12px; font-size:11px; font-weight:900; text-transform:uppercase; margin:0 8px 8px 0;}
.info-grid{display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin:28px 0;}
.info-card{border:1px solid #eee; padding:20px; background:#fff;}
.info-card b{font-size:13px; display:block; margin-bottom:6px;}
.info-card span{font-size:12px; color:#666;}
.lookbook-grid{display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin:26px 0 60px;}
.lookbook-grid img{width:100%; height:430px; object-fit:cover; background:#f3f3f3;}
.about-hero{display:grid; grid-template-columns:.8fr 1.2fr; gap:48px; align-items:center; padding:42px 0;}
.about-card{background:#080808; color:#fff; padding:44px;}
.about-card h2{font-family:Impact, sans-serif; font-size:52px; line-height:1; margin:0 0 18px;}
.contact-panel{display:grid; grid-template-columns:.9fr 1.1fr; gap:42px; margin:36px 0 60px;}
.contact-side{background:#080808; color:#fff; padding:42px;}
.contact-side h2{font-family:Impact, sans-serif; font-size:46px; line-height:1;}
.cart-line{display:grid; grid-template-columns:90px 1fr 120px 120px; gap:18px; align-items:center; border-bottom:1px solid #eee; padding:18px 0;}
.cart-line img{width:90px; height:90px; object-fit:cover; background:#f5f5f5;}
.cart-total{background:#f8f8f8; padding:24px; border:1px solid #eee; margin-top:22px;}
button[kind="primary"], .stButton>button{border-radius:0 !important; border:2px solid var(--pink) !important; background:var(--pink) !important; color:#fff !important; font-weight:900 !important; letter-spacing:.3px !important; min-height:44px !important; text-transform:uppercase !important;}
.stButton>button:hover{border-color:#111 !important; background:#111 !important; color:#fff !important;}
.stSelectbox label,.stRadio label,.stTextInput label,.stTextArea label{font-weight:800 !important; color:#111 !important;}
hr{border:0; border-top:1px solid #eee; margin:34px 0;}
@media(max-width:900px){
 .bz-navwrap{height:auto; padding:18px; flex-wrap:wrap;} .bz-nav{order:3; width:100%; justify-content:space-between; gap:8px; overflow-x:auto;} .bz-nav a{padding:14px 0; font-size:12px;} .bz-logo{width:135px;}
 .bz-hero{grid-template-columns:1fr; min-height:auto;} .hero-copy{padding:48px 26px;} .hero-title{font-size:58px;} .hero-art{height:470px;} .hero-art:after{font-size:42px; right:18px;}
 .benefit-grid{grid-template-columns:1fr 1fr; gap:16px;} .benefit{border:0; padding:6px;}
 .story-band,.newsletter,.product-detail,.about-hero,.contact-panel,.footer-inner{grid-template-columns:1fr;} .lookbook-grid{grid-template-columns:1fr;} .footer-bottom{display:block;}
 .page-title{font-size:48px;} .detail-title{font-size:44px;} .cart-line{grid-template-columns:70px 1fr;}
}
</style>
''', unsafe_allow_html=True)


def header(active):
    logo = img64("bipzilla_logo.png")
    nav_links = "".join([f'<a class="{"active" if key==active else ""}" href="?page={key}">{label}</a>' for key,label in NAV])
    count = cart_count()
    st.markdown(f'''
<div class="bz-topbar">FREE UK SHIPPING ON ALL ORDERS OVER £70 <span>•</span> LIMITED DEMO STORE</div>
<div class="bz-header">
  <div class="bz-navwrap">
    <a href="?page=home"><img class="bz-logo" src="{logo}" alt="BIPZILLA logo"></a>
    <nav class="bz-nav">{nav_links}</nav>
    <div class="bz-actions"><span>⌕</span><a class="bz-cart" href="?page=cart">🛒<span>{count}</span></a></div>
  </div>
</div>
''', unsafe_allow_html=True)


def footer():
    logo = img64("bipzilla_logo.png")
    st.markdown(f'''
<div class="bz-footer">
  <div class="footer-inner">
    <div><img class="footer-logo" src="{logo}" alt="BIPZILLA"><p style="color:#aaa;font-size:12px;max-width:260px;line-height:1.6;margin-top:18px;">Art-led streetwear demo store built for T-shirts, hoodies and sweatshirts. Limited drops. No generic blanks.</p></div>
    <div class="footer-col"><b>SHOP</b><a href="?page=shop">All Products</a><a href="?page=shop&category=T-Shirts">T-Shirts</a><a href="?page=shop&category=Hoodies">Hoodies</a><a href="?page=shop&category=Sweatshirts">Sweatshirts</a></div>
    <div class="footer-col"><b>INFO</b><a href="?page=about">About Us</a><a href="?page=lookbook">Lookbook</a><a href="?page=contact">Contact</a><a>Size Guide</a></div>
    <div class="footer-col"><b>SUPPORT</b><a>Shipping</a><a>Returns</a><a>Track Order</a><a>Privacy Policy</a></div>
    <div class="footer-col"><b>FOLLOW</b><a>Instagram</a><a>TikTok</a><a>Email</a><p style="color:#ee2d67;font-weight:900;letter-spacing:1px;">ART • CULTURE • STREETWEAR</p></div>
  </div>
  <div class="footer-bottom"><span>© 2026 BIPZILLA. Demo website only.</span><span>Built for Streamlit Cloud + GitHub deployment.</span></div>
</div>
''', unsafe_allow_html=True)


def product_card(product, idx):
    im = img64(product["image"] + ".jpg")
    st.markdown(f'''
<div class="product-card">
  <a href="?page=product&sku={product['sku']}" class="product-img-wrap">
    <img class="product-img" src="{im}" alt="{product['name']}">
    <span class="badge">{product['badge']}</span>
  </a>
  <div class="product-title">{product['name']}</div>
  <div class="product-price">{money(product['price'])}</div>
  <div class="swatches"><span class="swatch" style="background:{swatch_colour(product['colour'])}"></span><span style="font-size:12px;color:#555;">{product['colour']}</span></div>
  <div class="product-meta">{product['finish']}</div>
  <a class="mini-link" style="margin-top:12px;padding:10px 12px;font-size:11px;" href="?page=product&sku={product['sku']}">View Product →</a>
</div>
''', unsafe_allow_html=True)
    if st.button("Add to cart", key=f"add_{product['sku']}_{idx}"):
        add_to_cart(product)
        st.toast(f"Added {product['name']} to cart")


def swatch_colour(name):
    m = {"Black":"#080808", "Washed Black":"#222", "White":"#fff", "Dusty Pink":"#d89aa5", "Natural Cream":"#eee4d1", "Vintage Cream":"#e9dfca", "Stone":"#cbc2ae", "Deep Navy":"#09142c", "Soft Pink":"#f2b4c3"}
    return m.get(name, "#ccc")


def render_grid(items, columns=4):
    if not items:
        st.info("No products match this filter yet.")
        return
    for start in range(0, len(items), columns):
        cols = st.columns(columns, gap="large")
        for offset, product in enumerate(items[start:start+columns]):
            with cols[offset]:
                product_card(product, start+offset)


def benefits():
    st.markdown('''
<div class="bz-benefits"><div class="benefit-grid">
  <div class="benefit"><div class="benefit-ico">◎</div><div><b>WORLDWIDE SHIPPING</b><span>UK-first demo delivery setup</span></div></div>
  <div class="benefit"><div class="benefit-ico">◇</div><div><b>LIMITED DROPS</b><span>No restocks. Ever.</span></div></div>
  <div class="benefit"><div class="benefit-ico">◈</div><div><b>SECURE CHECKOUT</b><span>Dummy checkout for testing</span></div></div>
  <div class="benefit"><div class="benefit-ico">▱</div><div><b>PREMIUM QUALITY</b><span>Built to feel like a real brand</span></div></div>
</div></div>
''', unsafe_allow_html=True)


def home():
    logo = img64("bipzilla_logo.png")
    hero = img64("hero_lifestyle.jpg")
    st.markdown(f'''
<section class="bz-hero">
  <div class="hero-copy">
    <div class="kicker">ART • CULTURE • STREETWEAR</div>
    <div class="hero-title">WEAR<br>YOUR STORY<b>.</b></div>
    <p class="hero-p">BIPZILLA is a streetwear brand built on original artwork, bold ideas and self-expression. T-shirts, hoodies and sweatshirts made for limited drops.</p>
    <div class="hero-buttons"><a class="btn-main" href="?page=shop">SHOP THE DROP →</a><a class="btn-outline" href="?page=about">ABOUT BIPZILLA</a></div>
  </div>
  <div class="hero-art"><img class="hero-image" src="{hero}" alt="BIPZILLA hoodie streetwear hero"><img class="hero-logo-floating" src="{logo}" alt="BIPZILLA"></div>
</section>
''', unsafe_allow_html=True)
    benefits()
    st.markdown('<div class="bz-page">', unsafe_allow_html=True)
    st.markdown('<div class="section-head"><div><div class="section-kicker">Featured</div><div class="section-title">LATEST DROPS</div></div><a class="view-all" href="?page=shop">VIEW ALL →</a></div>', unsafe_allow_html=True)
    featured_skus = ['royal-bloom-hoodie','samurai-riot-tee','kraken-warlord-hoodie','tokyo-nights-hoodie']
    render_grid([get_product(x) for x in featured_skus if get_product(x)], 4)
    story_img = img64("tokyo_nights_hoodie.jpg")
    st.markdown(f'''
<div class="story-band">
  <img class="story-img" src="{story_img}" alt="BIPZILLA Tokyo Nights hoodie">
  <div class="story-copy"><div class="section-kicker">Our story</div><h2>MORE THAN CLOTHES.<br>IT’S A MOVEMENT.</h2><p>BIPZILLA starts from your original artwork and turns it into wearable drops. Some pieces are loud full-back prints, others are minimal chest embroidery style designs. The brand should feel artistic, collectable and street-ready.</p><a class="btn-outline" href="?page=lookbook">OPEN LOOKBOOK →</a></div>
</div>
''', unsafe_allow_html=True)
    st.markdown('''
<div class="newsletter"><div><div class="section-kicker">Join the movement</div><h3>BE THE FIRST TO KNOW.</h3><p class="page-sub">Early access to drops, exclusive offers and new design previews.</p></div><div class="form-row"><div class="fake-input">Enter your email address</div><a class="btn-main" href="?page=contact">SUBSCRIBE</a></div></div>
''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def shop(new_only=False):
    st.markdown('<div class="bz-page">', unsafe_allow_html=True)
    st.markdown(f'<div class="page-title">{"NEW IN" if new_only else "SHOP"}</div>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">A clean ecommerce-style product page using realistic mockups, fake UK prices, product filtering and a working demo cart. This is still a demo, but it behaves like a proper shop front.</p>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="filter-box">', unsafe_allow_html=True)
        c1,c2,c3 = st.columns([1,1,1.2])
        with c1:
            default_cat = qp_get('category', 'All') or 'All'
            cats = ['All','T-Shirts','Hoodies','Sweatshirts']
            if default_cat not in cats: default_cat='All'
            category = st.selectbox('Category', cats, index=cats.index(default_cat))
        with c2:
            finish = st.selectbox('Finish', ['All','Back Print','Front Print','Embroidery','Statement'])
        with c3:
            query = st.text_input('Search product', placeholder='Search hoodie, samurai, koi, card...')
        st.markdown('</div>', unsafe_allow_html=True)
    items = PRODUCTS[:]
    if new_only:
        items = [p for p in items if p['tag'] in ['New In','Limited','Premium','Art Drop']]
    if category != 'All':
        items = [p for p in items if p['category'] == category]
    if finish != 'All':
        f = finish.lower()
        items = [p for p in items if f in (p['finish']+p['badge']+p['name']).lower()]
    if query.strip():
        q = query.strip().lower()
        items = [p for p in items if q in (p['name']+' '+p['category']+' '+p['story']+' '+p['tag']).lower()]
    render_grid(items, 4)
    st.markdown('</div>', unsafe_allow_html=True)


def lookbook():
    st.markdown('<div class="bz-page">', unsafe_allow_html=True)
    st.markdown('<div class="page-title">LOOKBOOK</div><p class="page-sub">Use this page as the visual direction for the brand: clean studio mockups, real hoodie shapes, bold art placement, and a mix of loud and minimal pieces.</p>', unsafe_allow_html=True)
    names = ['hero_lifestyle','royal_bloom_hoodie','kraken_warlord_hoodie','samurai_riot_tee','koi_legend_sweatshirt','ocean_drift_hoodie','midnight_slice_sweatshirt','tokyo_nights_hoodie','royal_bloom_tee_white']
    html = '<div class="lookbook-grid">' + ''.join([f'<img src="{img64(n+".jpg")}" alt="{n}">' for n in names]) + '</div>'
    st.markdown(html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def about():
    st.markdown('<div class="bz-page">', unsafe_allow_html=True)
    img = img64('ace_dark_card.jpg')
    st.markdown(f'''
<div class="about-hero">
  <div class="about-card"><div class="section-kicker">BIPZILLA</div><h2>ART FIRST.<br>CLOTHES SECOND.<br>BRAND ALWAYS.</h2><p style="line-height:1.65;color:#ddd;">The idea is not to look like a random print shop. BIPZILLA should feel like a clothing brand with a clear identity: original art, Japanese-inspired typography, bold card motifs, streetwear silhouettes and limited drops.</p></div>
  <img src="{img}" style="width:100%;border:1px solid #eee;box-shadow:0 30px 70px rgba(0,0,0,.15);" alt="BIPZILLA card art">
</div>
''', unsafe_allow_html=True)
    st.markdown('<div class="section-title">DROP PHILOSOPHY</div>', unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    for c,title,text in [(c1,'01 / ORIGINAL ART','Use your own drawings and mockups as the centre of the product.'),(c2,'02 / LIMITED FEEL','Small drops, fake scarcity for demo, and strong product names.'),(c3,'03 / MIXED FINISHES','Some large prints, some minimal embroidery-style pieces for everyday wear.')]:
        with c:
            st.markdown(f'<div class="info-card"><b>{title}</b><span>{text}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def contact():
    st.markdown('<div class="bz-page">', unsafe_allow_html=True)
    st.markdown('<div class="page-title">CONTACT</div><p class="page-sub">A working demo contact page. Messages are not emailed yet, but the form works and shows confirmation inside Streamlit.</p>', unsafe_allow_html=True)
    st.markdown('<div class="contact-panel">', unsafe_allow_html=True)
    left,right = st.columns([0.9,1.1], gap='large')
    with left:
        st.markdown('<div class="contact-side"><div class="section-kicker">Support</div><h2>NEED HELP?</h2><p style="line-height:1.7;color:#ddd;">For drop questions, sizing, wholesale ideas or design feedback, use the form. This can later connect to email, Airtable, Google Sheets or Shopify.</p><p>📍 London / UK demo brand</p><p>✉️ hello@bipzilla.demo</p></div>', unsafe_allow_html=True)
    with right:
        with st.form('contact_form'):
            name = st.text_input('Name')
            email = st.text_input('Email')
            topic = st.selectbox('Topic', ['Order question','Sizing','Wholesale','Design feedback','Other'])
            msg = st.text_area('Message', height=170)
            submitted = st.form_submit_button('Send message')
            if submitted:
                st.success(f'Thanks {name or "there"}. Demo message received — this can be connected to email later.')
    st.markdown('</div></div>', unsafe_allow_html=True)


def product_detail(sku):
    product = get_product(sku) or PRODUCTS[0]
    st.markdown('<div class="bz-page">', unsafe_allow_html=True)
    st.markdown('<a class="view-all" href="?page=shop">← BACK TO SHOP</a>', unsafe_allow_html=True)
    im = img64(product['image']+'.jpg')
    st.markdown('<div class="product-detail">', unsafe_allow_html=True)
    l,r = st.columns([1.05,.95], gap='large')
    with l:
        st.markdown(f'<img class="detail-img" src="{im}" alt="{product["name"]}">', unsafe_allow_html=True)
    with r:
        st.markdown(f'<div class="section-kicker">{product["tag"]}</div><div class="detail-title">{product["name"]}</div><div class="detail-price">{money(product["price"])}</div>', unsafe_allow_html=True)
        st.markdown(f'<span class="detail-pill">{product["category"]}</span><span class="detail-pill">{product["colour"]}</span><span class="detail-pill">{product["badge"]}</span>', unsafe_allow_html=True)
        st.write(product['story'])
        st.markdown('<hr>', unsafe_allow_html=True)
        size = st.selectbox('Size', ['XS','S','M','L','XL','XXL'], index=2)
        st.caption('Demo sizing only: oversized fit, streetwear shape.')
        if st.button('Add to cart', key=f'detail_add_{sku}'):
            add_to_cart(product, size)
            st.success(f'Added {product["name"]} / {size} to cart')
        st.markdown(f'''
<div class="info-grid">
  <div class="info-card"><b>Finish</b><span>{product['finish']}</span></div>
  <div class="info-card"><b>Fit</b><span>{product['fit']}</span></div>
  <div class="info-card"><b>Shipping</b><span>Free UK shipping over £70</span></div>
</div>
''', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)


def cart():
    st.markdown('<div class="bz-page">', unsafe_allow_html=True)
    st.markdown('<div class="page-title">CART</div><p class="page-sub">Demo cart only. This is not connected to payment yet.</p>', unsafe_allow_html=True)
    cart = st.session_state.setdefault('cart', {})
    if not cart:
        st.info('Your cart is empty. Add a hoodie, tee or sweatshirt from the shop.')
        st.markdown('<a class="btn-main" href="?page=shop">SHOP THE DROP →</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        return
    total = 0
    for key,item in list(cart.items()):
        p = get_product(item['sku'])
        if not p: continue
        subtotal = p['price'] * item['qty']
        total += subtotal
        cols = st.columns([.12,.48,.15,.15,.10])
        with cols[0]: st.image(str(ASSET_DIR/(p['image']+'.jpg')), use_container_width=True)
        with cols[1]:
            st.markdown(f'**{p["name"]}**')
            st.caption(f"Size {item['size']} • {p['colour']}")
        with cols[2]: st.write(money(p['price']))
        with cols[3]: st.write(f"Qty: {item['qty']}")
        with cols[4]:
            if st.button('Remove', key=f'remove_{key}'):
                del cart[key]
                st.rerun()
        st.markdown('<hr>', unsafe_allow_html=True)
    shipping = 0 if total >= 70 else 4.99
    st.markdown(f'<div class="cart-total"><h3>Subtotal: {money(total)}</h3><p>Shipping: {"FREE" if shipping == 0 else money(shipping)}</p><h2>Total: {money(total+shipping)}</h2></div>', unsafe_allow_html=True)
    if st.button('Demo checkout'):
        st.success('Demo checkout clicked. Later this can be connected to Shopify, Stripe, WooCommerce or a simple payment link.')
    st.markdown('</div>', unsafe_allow_html=True)


def main():
    css()
    page = qp_get('page', 'home')
    valid_pages = {k for k,_ in NAV} | {'cart','product'}
    if page not in valid_pages: page='home'
    header('shop' if page == 'product' else page)
    if page == 'home': home()
    elif page == 'shop': shop(False)
    elif page == 'new': shop(True)
    elif page == 'lookbook': lookbook()
    elif page == 'about': about()
    elif page == 'contact': contact()
    elif page == 'product': product_detail(qp_get('sku', PRODUCTS[0]['sku']))
    elif page == 'cart': cart()
    footer()

if __name__ == '__main__':
    main()
