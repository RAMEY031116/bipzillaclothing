
from pathlib import Path
import base64
import json
import urllib.parse
import streamlit as st

st.set_page_config(page_title="BIPZILLA | Clothing Brand Demo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")
ROOT = Path(__file__).parent
PRODUCTS = json.loads((ROOT / "products.json").read_text(encoding="utf-8"))

ROUTES = ["Home", "Shop", "New In", "Lookbook", "About", "Contact", "Cart", "Product"]

# ---------------------------- helpers ----------------------------
def mime(path: str) -> str:
    ext = Path(path).suffix.lower()
    return "image/png" if ext == ".png" else "image/jpeg"

def img64(path: str) -> str:
    p = ROOT / path
    return base64.b64encode(p.read_bytes()).decode("utf-8")

def image_src(path: str) -> str:
    return f"data:{mime(path)};base64,{img64(path)}"

def money(value) -> str:
    return f"£{float(value):,.2f}"

def current_theme() -> str:
    theme = st.query_params.get("theme", "pink")
    return theme if theme in ["pink", "dark"] else "pink"

def theme_url(theme: str) -> str:
    data = dict(st.query_params)
    data["theme"] = theme
    return "?" + urllib.parse.urlencode(data, doseq=True)

def nav_url(page: str, **kwargs) -> str:
    data = {"page": page, "theme": current_theme()}
    data.update(kwargs)
    return "?" + urllib.parse.urlencode(data)

def get_page() -> str:
    page = st.query_params.get("page", "Home")
    return page if page in ROUTES else "Home"

def product_by_id(pid: str):
    return next((p for p in PRODUCTS if p["id"] == pid), PRODUCTS[0])

def init_state():
    st.session_state.setdefault("cart", {})
    st.session_state.setdefault("notice", "")
init_state()

def cart_count():
    return sum(st.session_state.cart.values())

def add_to_cart(pid: str, size="M", colour=None, qty=1):
    p = product_by_id(pid)
    key = f"{pid}|{size}|{colour or p['colour']}"
    st.session_state.cart[key] = st.session_state.cart.get(key, 0) + int(qty)
    st.session_state.notice = f"Added {p['name']} to the demo cart."
    st.toast("Added to demo cart 🛒")

def go(page: str, **params):
    st.query_params.clear()
    st.query_params["page"] = page
    for k, v in params.items():
        st.query_params[k] = v
    st.rerun()

# ---------------------------- CSS ----------------------------
st.markdown('''
<style>
:root{--pink:#ee2c61;--pink2:#ff4f8a;--ink:#070707;--muted:#5d6470;--line:#e9e9e9;--soft:#f6f6f5;--cream:#fff9ef;--black:#050506;}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:#fff;}
[data-testid="stAppViewContainer"]{background:#fff;color:var(--ink);} 
.block-container{max-width:100%;padding:0 0 0 0!important;}
[data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer, .stDeployButton{display:none!important;}
section,div,p,h1,h2,h3,h4,a,span{font-family:Inter,Arial,Helvetica,sans-serif;}
.bz-topbar{height:36px;background:linear-gradient(90deg,#ef265f,#f13d75);display:flex;align-items:center;justify-content:center;color:white;font-size:12px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;}
.bz-nav{height:106px;background:white;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);padding:0 7vw;position:sticky;top:0;z-index:2000;box-shadow:0 8px 30px rgba(0,0,0,.035);} 
.logo-wrap{width:210px;display:flex;align-items:center}.logo-wrap img{height:72px;max-width:210px;object-fit:contain;}
.bz-menu{display:flex;align-items:center;gap:42px;}
.bz-menu a{height:106px;display:flex;align-items:center;color:#111;text-decoration:none;text-transform:uppercase;font-weight:900;font-size:13px;letter-spacing:.035em;border-bottom:4px solid transparent;}
.bz-menu a.active{border-bottom-color:var(--pink);color:#000;}
.bz-actions{display:flex;align-items:center;gap:14px;font-size:24px;min-width:230px;justify-content:flex-end;}.bz-actions a{color:#111;text-decoration:none}.theme-chip{height:30px!important;padding:0 12px!important;border:1px solid #111!important;border-radius:999px!important;font-size:11px!important;font-weight:900!important;text-transform:uppercase!important;display:inline-flex!important;align-items:center!important}.theme-chip.active{background:#111!important;color:#fff!important}.cart-badge{display:inline-flex;align-items:center;justify-content:center;background:var(--pink);color:#fff;font-size:11px;font-weight:900;border-radius:999px;min-width:20px;height:20px;margin-left:-20px;margin-top:26px;}
.hero{min-height:650px;display:grid;grid-template-columns:43% 57%;border-bottom:1px solid var(--line);background:#fff;overflow:hidden;}
.hero-copy{padding:92px 0 70px 7vw;display:flex;flex-direction:column;justify-content:center;}
.eyebrow{font-size:13px;font-weight:900;color:var(--pink);letter-spacing:.08em;text-transform:uppercase;}.headline{font-family:Impact,Arial Black,sans-serif;font-size:88px;line-height:.92;letter-spacing:.005em;margin:20px 0 22px;text-transform:uppercase;}.headline span{color:var(--pink);}.hero-copy p{font-size:17px;line-height:1.7;max-width:440px;color:#222;margin:0;}
.hero-art{position:relative;min-height:650px;background-size:cover;background-position:center;}
.hero-art:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.28) 16%,rgba(255,255,255,0) 36%);} 
.jp-vertical{position:absolute;right:6.5vw;top:110px;font-size:60px;font-weight:900;writing-mode:vertical-rl;letter-spacing:.05em;color:#080808;text-shadow:0 2px 0 #fff;}
.btn-row{display:flex;gap:28px;margin-top:42px;flex-wrap:wrap;}.btn-pink,.btn-outline{height:58px;padding:0 32px;display:inline-flex;align-items:center;justify-content:center;text-decoration:none;text-transform:uppercase;font-size:13px;font-weight:900;letter-spacing:.02em;}.btn-pink{background:var(--pink);color:#fff;box-shadow:0 12px 30px rgba(238,44,97,.22);}.btn-outline{background:#fff;color:#111;border:1.5px solid #111;}
.trust{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line);}.trust-card{min-height:92px;padding:25px 28px;border-right:1px solid var(--line);display:flex;align-items:center;gap:17px;}.trust-card:first-child{padding-left:7vw;}.trust-icon{font-size:33px;line-height:1}.trust-card b{display:block;text-transform:uppercase;font-size:14px;font-weight:900;}.trust-card span{font-size:13px;color:#666;}
.container{padding-left:7vw;padding-right:7vw;}.section-head{display:flex;justify-content:space-between;align-items:flex-end;margin:50px 0 20px;}.small-label{font-size:12px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--pink);}.section-title{font-family:Impact,Arial Black,sans-serif;text-transform:uppercase;font-size:48px;line-height:1;margin:8px 0 0;}.view-link{font-size:13px;font-weight:900;text-transform:uppercase;color:#111;text-decoration:none;}
.product-shell{margin-bottom:32px;}.product-card{background:#fff;}.product-image{background:#f6f6f5;position:relative;overflow:hidden;border:1px solid #f0f0f0;}.product-image img{width:100%;aspect-ratio:1/1.12;display:block;object-fit:contain;background:#f6f6f5;transition:transform .28s ease;}.product-shell:hover .product-image img{transform:scale(1.025);}.badge{position:absolute;top:14px;left:14px;background:#111;color:white;text-transform:uppercase;font-size:10px;font-weight:900;letter-spacing:.06em;padding:8px 10px;}.product-name{font-size:16px;font-weight:950;text-transform:uppercase;margin-top:15px;}.product-meta{font-size:12px;color:#686868;line-height:1.45;min-height:38px;margin-top:4px;}.product-price{font-size:15px;font-weight:950;margin-top:7px;}.swatches{margin-top:10px}.swatch{display:inline-block;width:16px;height:16px;border-radius:99px;border:1px solid rgba(0,0,0,.25);margin-right:8px;}.mini-actions{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:14px;}.mini-actions a,.mini-actions span{height:38px;border:1px solid #111;display:flex;align-items:center;justify-content:center;color:#111;text-decoration:none;font-size:12px;font-weight:900;text-transform:uppercase;}
.story{display:grid;grid-template-columns:42% 58%;min-height:335px;background:#f7f7f6;margin:42px 0 0;}.story-img{background-size:cover;background-position:center;min-height:335px;}.story-copy{position:relative;overflow:hidden;padding:54px 62px;background:radial-gradient(circle at right center,rgba(238,44,97,.12),transparent 36%),#f7f7f6;}.story-copy h2{font-family:Impact,Arial Black,sans-serif;font-size:48px;line-height:.95;text-transform:uppercase;margin:9px 0 17px;}.story-copy p{max-width:540px;line-height:1.65;color:#30343a;}.big-kanji{position:absolute;right:36px;top:20px;font-size:170px;font-weight:900;color:rgba(0,0,0,.08);line-height:1;}.brand-stamp{position:absolute;right:90px;bottom:48px;font-size:50px;font-weight:950;color:var(--pink);transform:rotate(-8deg);letter-spacing:.03em;}
.newsletter{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;border-top:1px solid var(--line);padding:46px 7vw;}.newsletter h3{font-family:Impact,Arial Black,sans-serif;text-transform:uppercase;font-size:34px;margin:6px 0 6px;}.signup{display:grid;grid-template-columns:1fr 170px;gap:12px}.signup input{height:54px;border:1px solid #ddd;padding:0 18px;font-size:14px;}.signup button{height:54px;background:var(--pink);border:none;color:white;text-transform:uppercase;font-weight:900;}
.footer{background:#070708;color:white;display:grid;grid-template-columns:1.6fr repeat(4,1fr);gap:40px;padding:48px 7vw 55px;}.footer img{height:62px;width:auto;filter:brightness(1.2);}.footer h4{font-size:13px;text-transform:uppercase;margin:0 0 12px;}.footer a,.footer p{display:block;color:#c9c9c9;font-size:13px;text-decoration:none;margin:7px 0;}.footer .tag{color:var(--pink);font-weight:900;margin-top:26px;text-transform:uppercase;}
.page-pad{padding:46px 7vw 20px;}.page-intro{max-width:840px;color:#505762;font-size:16px;line-height:1.7;}.filter-box{border:1px solid var(--line);background:#fafafa;padding:20px;margin-bottom:24px;}.detail-wrap{padding:50px 7vw;display:grid;grid-template-columns:55% 45%;gap:54px;}.detail-img{background:#f5f5f4;border:1px solid #eee;}.detail-img img{width:100%;display:block;}.detail h1{font-family:Impact,Arial Black,sans-serif;font-size:64px;text-transform:uppercase;line-height:.95;margin:14px 0 10px;}.detail p{font-size:16px;line-height:1.7;color:#343941;}.pill{display:inline-block;background:#111;color:white;font-size:10px;text-transform:uppercase;font-weight:900;padding:8px 10px;margin-right:6px;letter-spacing:.06em;}.pill.pink{background:var(--pink);}.notice{border:1px dashed #b99432;background:#fff7dd;color:#57410d;padding:16px;margin-top:18px;font-weight:800;}.gallery{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;}.gallery img{width:100%;aspect-ratio:1/1.22;object-fit:cover;background:#f3f3f3;border:1px solid #eee;}.brand-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:22px;}.brand-card{border:1px solid var(--line);background:#fafafa;padding:28px;min-height:200px;}.brand-card h3{font-family:Impact,Arial Black,sans-serif;text-transform:uppercase;font-size:34px;margin:0 0 10px;}.contact-card,.cart-box{border:1px solid var(--line);background:#fafafa;padding:28px;}.cart-line{border:1px solid #e4e4e4;background:#fff;padding:16px;margin-bottom:12px;}.muted{color:#686868;}.stButton>button{border-radius:0!important;border:1px solid #111!important;text-transform:uppercase!important;font-weight:900!important;min-height:42px!important;background:white!important;color:#111!important;}.stButton>button[kind="primary"]{background:var(--pink)!important;border-color:var(--pink)!important;color:white!important;}.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]{border-radius:0!important;}
@media(max-width:1050px){.bz-nav{height:auto;min-height:104px;align-items:flex-start;flex-direction:column;padding:18px 24px 10px}.logo-wrap img{height:60px}.bz-menu{gap:22px;flex-wrap:wrap}.bz-menu a{height:auto;padding:8px 0;border-bottom-width:2px}.bz-actions{position:absolute;right:24px;top:45px}.hero{grid-template-columns:1fr}.hero-copy{padding:56px 24px}.hero-art{min-height:520px}.container,.page-pad,.newsletter,.footer,.detail-wrap{padding-left:24px;padding-right:24px}.trust{grid-template-columns:repeat(2,1fr)}.trust-card:first-child,.trust-card{padding-left:24px}.story,.detail-wrap{grid-template-columns:1fr}.gallery{grid-template-columns:repeat(2,1fr)}.footer{grid-template-columns:1fr 1fr}.headline{font-size:68px}.jp-vertical{font-size:48px;right:30px}}
@media(max-width:620px){.headline{font-size:54px}.section-title{font-size:38px}.trust{grid-template-columns:1fr}.newsletter{grid-template-columns:1fr}.signup{grid-template-columns:1fr}.footer{grid-template-columns:1fr}.gallery,.brand-grid{grid-template-columns:1fr}.product-image img{aspect-ratio:1/1.05}.detail h1{font-size:46px}.bz-menu{gap:14px}.bz-menu a{font-size:12px}.hero-art{min-height:420px}.story-copy{padding:36px 24px}.big-kanji{display:none}}
</style>
''', unsafe_allow_html=True)

# Theme override: default is the pink/white ecommerce look. Use the navbar toggle for dark mode.
if current_theme() == "dark":
    st.markdown('''
<style>
:root{--pink:#ff3f77;--pink2:#ff6aa0;--ink:#f5f2ef;--muted:#b9b3b0;--line:#29252a;--soft:#111116;--cream:#151319;--black:#050506;}
body,[data-testid="stAppViewContainer"]{background:#08080b!important;color:#f5f2ef!important;}
.bz-nav,.hero,.newsletter,.page-pad,.container{background:#08080b!important;color:#f5f2ef!important;}
.bz-nav{border-bottom:1px solid #262129!important;box-shadow:0 10px 36px rgba(0,0,0,.45)!important;}
.bz-menu a,.bz-actions a,.headline,.section-title,.view-link,.product-name,.product-price,.detail h1,.detail h2,.newsletter h3,.trust-card b{color:#f5f2ef!important;}
.theme-chip{border-color:#f5f2ef!important;color:#f5f2ef!important}.theme-chip.active{background:#ff3f77!important;border-color:#ff3f77!important;color:#fff!important;}
.hero{background:radial-gradient(circle at 75% 35%,rgba(255,63,119,.22),transparent 34%),#08080b!important;}
.hero-art:before{background:linear-gradient(90deg,#08080b 0%,rgba(8,8,11,.45) 22%,rgba(8,8,11,0) 52%)!important;}
.hero-copy p,.page-intro,.muted,.product-meta,.story-copy p,.trust-card span,.footer p,.detail p{color:#c8c2bd!important;}
.trust{background:#0d0d11!important;border-color:#262129!important;}.trust-card{border-color:#262129!important;}
.product-image,.product-image img,.detail-img img{background:#111116!important;border-color:#211d23!important;}
.product-card{background:#08080b!important;}
.story,.story-copy{background:#101015!important;}.story-copy{background:radial-gradient(circle at right center,rgba(255,63,119,.16),transparent 38%),#101015!important;}
.big-kanji{color:rgba(255,255,255,.07)!important;}.brand-card,.contact-card{background:#101015!important;border-color:#262129!important;}
input, textarea, select, .stTextInput input, .stTextArea textarea{background:#121218!important;color:#f5f2ef!important;border-color:#29252a!important;}
</style>
''', unsafe_allow_html=True)


# ---------------------------- layout pieces ----------------------------
def top_nav(active="Home"):
    logo = image_src("assets/brand/bipzilla_wordmark.png")
    pages = ["Home", "Shop", "New In", "Lookbook", "About", "Contact"]
    links = "".join([f'<a class="{"active" if p==active else ""}" href="{nav_url(p)}">{p}</a>' for p in pages])
    pink_active = "active" if current_theme() == "pink" else ""
    dark_active = "active" if current_theme() == "dark" else ""
    st.markdown(f'''
<div class="bz-topbar">✦ Free UK shipping on demo orders over £70 • Limited demo drop</div>
<nav class="bz-nav">
  <a class="logo-wrap" href="{nav_url('Home')}"><img src="{logo}" alt="BIPZILLA logo"></a>
  <div class="bz-menu">{links}</div>
  <div class="bz-actions"><a class="theme-chip {pink_active}" href="{theme_url('pink')}">Pink</a><a class="theme-chip {dark_active}" href="{theme_url('dark')}">Dark</a><a href="{nav_url('Shop')}">⌕</a><a href="{nav_url('Cart')}">🛒</a><span class="cart-badge">{cart_count()}</span></div>
</nav>
''', unsafe_allow_html=True)
    if st.session_state.notice:
        st.success(st.session_state.notice)
        st.session_state.notice = ""


def footer():
    logo = image_src("assets/brand/bipzilla_wordmark.png")
    st.markdown(f'''
<div class="footer">
  <div><img src="{logo}" alt="BIPZILLA"><p>© 2026 BIPZILLA demo. Built for Streamlit Cloud. Prices, stock and checkout are placeholders for the demo.</p></div>
  <div><h4>Shop</h4><a href="{nav_url('Shop')}">All Products</a><a href="{nav_url('Shop')}">T-Shirts</a><a href="{nav_url('Shop')}">Hoodies</a><a href="{nav_url('Shop')}">Sweatshirts</a></div>
  <div><h4>Info</h4><a href="{nav_url('About')}">About Us</a><a>Shipping</a><a>Returns</a><a>Size Guide</a></div>
  <div><h4>Support</h4><a href="{nav_url('Contact')}">Contact Us</a><a>FAQ</a><a>Track Order</a><a>Privacy Policy</a></div>
  <div><h4>Follow</h4><a>Instagram</a><a>TikTok</a><a>Email</a><p class="tag">Art • Culture • Streetwear</p></div>
</div>
''', unsafe_allow_html=True)

def product_card(p, prefix="product"):
    badge = "EMBROIDERY" if "Embroidery" in p["print_type"] else "PRINT"
    st.markdown(f'''
<div class="product-shell">
  <div class="product-card">
    <div class="product-image"><span class="badge">{badge}</span><img src="{image_src(p['image'])}" alt="{p['name']}"></div>
    <div class="product-name">{p['name']}</div>
    <div class="product-meta">{p['category']} • {p['fit']}<br>{p['colour']}</div>
    <div class="product-price">{money(p['price'])}</div>
    <div class="swatches"><span class="swatch" style="background:#050505"></span><span class="swatch" style="background:#f7f1e7"></span><span class="swatch" style="background:#ee2c61"></span></div>
    <div class="mini-actions"><a href="{nav_url('Product', product=p['id'])}">View</a><span>Demo</span></div>
  </div>
</div>
''', unsafe_allow_html=True)
    if st.button("Add to cart", key=f"{prefix}_add_{p['id']}", use_container_width=True):
        add_to_cart(p["id"])

def product_grid(products, columns=4, prefix="grid"):
    if not products:
        st.info("No products match this filter yet.")
        return
    cols = st.columns(columns)
    for i, p in enumerate(products):
        with cols[i % columns]:
            product_card(p, f"{prefix}_{i}")

# ---------------------------- pages ----------------------------
def home():
    st.markdown(f'''
<section class="hero">
  <div class="hero-copy">
    <div class="eyebrow">ART • CULTURE • STREETWEAR</div>
    <h1 class="headline">WEAR<br>YOUR STORY<span>.</span></h1>
    <p>BIPZILLA is a clothing brand built on original art, bold graphics and limited streetwear drops. T-shirts, hoodies and sweatshirts designed as real products, not just art on a blank page.</p>
    <div class="btn-row"><a class="btn-pink" href="{nav_url('Shop')}">Shop the drop →</a><a class="btn-outline" href="{nav_url('About')}">About BIPZILLA</a></div>
  </div>
  <div class="hero-art" style="background-image:url('{image_src('assets/hero_hoodie.jpg')}');"><div class="jp-vertical">ビップジラ</div></div>
</section>
<section class="trust">
  <div class="trust-card"><div class="trust-icon">◎</div><div><b>Worldwide Shipping</b><span>Demo delivery options</span></div></div>
  <div class="trust-card"><div class="trust-icon">◇</div><div><b>Limited Drops</b><span>No restocks. Ever.</span></div></div>
  <div class="trust-card"><div class="trust-icon">◷</div><div><b>Secure Checkout</b><span>Demo only, no payment</span></div></div>
  <div class="trust-card"><div class="trust-icon">♙</div><div><b>Premium Quality</b><span>Heavy cotton feel</span></div></div>
</section>
''', unsafe_allow_html=True)
    st.markdown(f'''<div class="container"><div class="section-head"><div><div class="small-label">Featured</div><div class="section-title">Latest Drops</div></div><a class="view-link" href="{nav_url('Shop')}">View all →</a></div></div>''', unsafe_allow_html=True)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    product_grid(PRODUCTS[:4], 4, "home")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f'''
<div class="container">
  <section class="story">
    <div class="story-img" style="background-image:url('{image_src('assets/story_hoodie.jpg')}');"></div>
    <div class="story-copy">
      <div class="small-label">Our story</div>
      <h2>MORE THAN CLOTHES.<br>IT'S A MOVEMENT.</h2>
      <p>BIPZILLA takes sketchbook energy and turns it into wearable streetwear. Big print pieces carry the artwork, while cleaner logo pieces can become embroidery ideas.</p>
      <a class="btn-outline" href="{nav_url('About')}">Read our story →</a>
      <div class="big-kanji">夢</div><div class="brand-stamp">BIP</div>
    </div>
  </section>
</div>
<section class="newsletter">
  <div><div class="small-label">Join the movement</div><h3>Be the first to know.</h3><p class="muted">Early access to drops, size releases and new artwork.</p></div>
  <form class="signup"><input placeholder="Enter your email address"><button type="button">Subscribe</button></form>
</section>
''', unsafe_allow_html=True)

def shop(new_only=False):
    items = [p for p in PRODUCTS if p.get("new")] if new_only else PRODUCTS
    title = "New In" if new_only else "Shop the Drop"
    st.markdown(f'''
<div class="page-pad"><div class="small-label">BIPZILLA Store</div><div class="section-title">{title}</div>
<p class="page-intro">A proper clothing-brand ecommerce demo with realistic garment mockups, GBP prices, product pages, filters, a working demo cart and a contact form. No real payment is connected.</p></div>
''', unsafe_allow_html=True)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    with st.container():
        c1, c2, c3 = st.columns(3)
        with c1:
            cat = st.multiselect("Clothing type", sorted({p["category"] for p in items}), default=[])
        with c2:
            finish = st.multiselect("Artwork finish", sorted({p["print_type"] for p in items}), default=[])
        with c3:
            max_price = st.slider("Max price", 30, 70, 70, step=1)
    filtered = [p for p in items if (not cat or p["category"] in cat) and (not finish or p["print_type"] in finish) and p["price"] <= max_price]
    product_grid(filtered, 4, "shopnew" if new_only else "shop")
    st.markdown('</div>', unsafe_allow_html=True)

def product_page():
    pid = st.query_params.get("product", PRODUCTS[0]["id"])
    p = product_by_id(pid)
    st.markdown('<div class="detail-wrap">', unsafe_allow_html=True)
    left, right = st.columns([1.08, .92], gap="large")
    with left:
        st.markdown(f'<div class="detail-img"><img src="{image_src(p["image"])}" alt="{p["name"]}"></div>', unsafe_allow_html=True)
        with st.expander("View the original artwork used for this piece"):
            st.image(str(ROOT / p["art"]), use_container_width=True)
    with right:
        st.markdown(f'''
<div class="detail">
  <span class="pill pink">{p['category']}</span><span class="pill">{p['print_type']}</span>
  <h1>{p['name']}</h1>
  <h2>{money(p['price'])}</h2>
  <p>{p['description']}</p>
  <p><b>Colour:</b> {p['colour']}<br><b>Fit:</b> {p['fit']}<br><b>Finish:</b> {p['finish']}<br><b>Demo stock:</b> {p['stock']} pieces</p>
</div>
''', unsafe_allow_html=True)
        size = st.selectbox("Size", p["sizes"], index=1)
        colour = st.selectbox("Colour", [p["colour"], "Black", "Vintage White", "Stone", "Soft Pink"])
        qty = st.number_input("Quantity", min_value=1, max_value=10, value=1, step=1)
        if st.button("Add to demo cart", type="primary", use_container_width=True):
            add_to_cart(p["id"], size, colour, qty)
        st.markdown('<div class="notice">Demo checkout only. No payment is taken and no real order is created.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def lookbook():
    st.markdown('''<div class="page-pad"><div class="small-label">Artwork Archive</div><div class="section-title">Lookbook</div><p class="page-intro">This page keeps the art visible, but the site still feels like a clothing brand first. Use this for Instagram-style storytelling and drop previews.</p></div>''', unsafe_allow_html=True)
    art_files = ["samurai.jpg","ocean.jpg","warrior_colour.jpg","warrior_bw.jpg","pizza.jpg","abstract.jpg","cow.jpg","guitar.jpg","lamp_clock.jpg","postbox.jpg","city_night.jpg","card_black.jpg","card_white.jpg"]
    html = '<div class="page-pad"><div class="gallery">'
    for f in art_files:
        path = f"assets/art/{f}"
        if (ROOT / path).exists():
            html += f'<img src="{image_src(path)}" alt="BIPZILLA artwork">'
    html += '</div></div>'
    st.markdown(html, unsafe_allow_html=True)

def about():
    st.markdown('''
<div class="page-pad">
  <div class="small-label">About</div><div class="section-title">BIPZILLA is a clothing brand.</div>
  <p class="page-intro">This demo is set up as a proper clothing-brand ecommerce site: a strong homepage, product grid, product pages, lookbook, contact page and a working demo cart, pink/dark theme switch, realistic clothing mockups and embroidery-style items. The artwork is the identity, but the website sells clothes first.</p>
  <div class="brand-grid">
    <div class="brand-card"><h3>01. Limited</h3><p class="muted">Start with a small collection. A tight drop looks stronger than too many random products.</p></div>
    <div class="brand-card"><h3>02. Wearable</h3><p class="muted">Use large back prints for statement hoodies and simple chest-logo pieces for embroidery ideas. No generic crown mark is used; the identity is the BIPZILLA wordmark and Japanese-style typography.</p></div>
    <div class="brand-card"><h3>03. Original</h3><p class="muted">Keep your uploaded artwork recognisable. The mockups show the art printed on real-looking garments.</p></div>
  </div>
</div>
''', unsafe_allow_html=True)

def contact():
    st.markdown('''<div class="page-pad"><div class="small-label">Contact</div><div class="section-title">Talk to BIPZILLA</div><p class="page-intro">Dummy contact form for sizing, collaborations, wholesale or custom artwork. Later this can connect to email, Google Sheets or Airtable.</p></div>''', unsafe_allow_html=True)
    st.markdown('<div class="page-pad"><div class="contact-card">', unsafe_allow_html=True)
    with st.form("contact_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        with c2:
            topic = st.selectbox("Topic", ["Sizing", "Collaboration", "Custom design", "Wholesale", "General question"])
            order = st.text_input("Order number (optional)")
        message = st.text_area("Message")
        ok = st.checkbox("I understand this is a demo form and no email will be sent.")
        if st.form_submit_button("Send demo message", type="primary"):
            if not name or not email or not message or not ok:
                st.error("Please complete the required fields and tick the demo checkbox.")
            else:
                st.success("Demo message submitted. This is where you would connect real email later.")
    st.markdown('</div></div>', unsafe_allow_html=True)

def cart():
    st.markdown('''<div class="page-pad"><div class="small-label">Checkout</div><div class="section-title">Demo Cart</div><p class="page-intro">This cart works in Streamlit session state only. It is useful for showing the full shopping flow before building a real shop.</p></div>''', unsafe_allow_html=True)
    st.markdown('<div class="page-pad">', unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Your cart is empty. Add a product from the shop.")
        if st.button("Go to shop", use_container_width=True):
            go("Shop")
        st.markdown('</div>', unsafe_allow_html=True)
        return
    subtotal = 0
    to_remove = []
    for key, qty in list(st.session_state.cart.items()):
        pid, size, colour = key.split("|")
        p = product_by_id(pid)
        subtotal += p["price"] * qty
        c1, c2, c3, c4 = st.columns([1, 3, 1, 1])
        with c1:
            st.image(str(ROOT / p["image"]), use_container_width=True)
        with c2:
            st.markdown(f'<div class="cart-line"><b>{p["name"]}</b><br>{size} • {colour}<br>{money(p["price"])} each</div>', unsafe_allow_html=True)
        with c3:
            st.write(f"Qty: {qty}")
        with c4:
            if st.button("Remove", key=f"remove_{key}"):
                to_remove.append(key)
    for k in to_remove:
        st.session_state.cart.pop(k, None)
        st.rerun()
    shipping = 0 if subtotal >= 70 else 3.99
    total = subtotal + shipping
    st.divider()
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(f"### Subtotal: {money(subtotal)}  \nShipping: {money(shipping)}  \n## Total: {money(total)}")
    with c2:
        with st.form("checkout_form"):
            st.text_input("Email")
            st.text_input("UK postcode")
            st.selectbox("Payment method", ["Demo only - no payment"])
            if st.form_submit_button("Place demo order", type="primary"):
                st.success("Demo order placed. No payment was taken.")
                st.session_state.cart = {}
    st.markdown('</div>', unsafe_allow_html=True)

PAGE_FUNCS = {
    "Home": home,
    "Shop": lambda: shop(False),
    "New In": lambda: shop(True),
    "Lookbook": lookbook,
    "About": about,
    "Contact": contact,
    "Cart": cart,
    "Product": product_page,
}

page = get_page()
top_nav(active=page if page in ["Home","Shop","New In","Lookbook","About","Contact"] else "Shop")
PAGE_FUNCS.get(page, home)()
footer()
