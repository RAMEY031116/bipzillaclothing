from pathlib import Path
import base64, json, urllib.parse
import streamlit as st

st.set_page_config(page_title="BIPZILLA | Streetwear Demo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")
ROOT = Path(__file__).parent
PRODUCTS = json.loads((ROOT / "products.json").read_text(encoding="utf-8"))
ROUTES = ["Home", "Shop", "New In", "About", "Contact", "Cart", "Product"]

def mime(path: str) -> str:
    return "image/png" if Path(path).suffix.lower() == ".png" else "image/jpeg"

def img64(path: str) -> str:
    return base64.b64encode((ROOT / path).read_bytes()).decode("utf-8")

def image_src(path: str) -> str:
    return f"data:{mime(path)};base64,{img64(path)}"

def money(v): return f"£{float(v):,.2f}"

def current_theme():
    t = st.query_params.get("theme", "pink")
    return t if t in ["pink", "dark"] else "pink"

def nav_url(page="Home", **kwargs):
    data = {"page": page, "theme": current_theme()}
    data.update(kwargs)
    return "?" + urllib.parse.urlencode(data)

def theme_url(theme):
    data = dict(st.query_params); data["theme"] = theme
    return "?" + urllib.parse.urlencode(data, doseq=True)

def get_page():
    p = st.query_params.get("page", "Home")
    return p if p in ROUTES else "Home"

def product_by_id(pid):
    return next((p for p in PRODUCTS if p["id"] == pid), PRODUCTS[0])

def go(page, **params):
    st.query_params.clear(); st.query_params["page"] = page; st.query_params["theme"] = current_theme()
    for k, v in params.items(): st.query_params[k] = v
    st.rerun()

st.session_state.setdefault("cart", {})
st.session_state.setdefault("notice", "")

def cart_count(): return sum(st.session_state.cart.values())

def add_to_cart(pid, size="M", colour=None, qty=1):
    p = product_by_id(pid); key = f"{pid}|{size}|{colour or p['colour']}"
    st.session_state.cart[key] = st.session_state.cart.get(key, 0) + int(qty)
    st.session_state.notice = f"Added {p['name']} to your demo cart."
    st.toast("Added to demo cart 🛒")

hero1 = image_src("assets/hero_hoodie.jpg")
hero2 = image_src("assets/products/tokyo_nights_hoodie.jpg")
hero3 = image_src("assets/products/armoured_warlord_hoodie.jpg")
logo_src = image_src("assets/brand/bipzilla_wordmark.png")

st.markdown(f'''
<style>
:root{{--pink:#ee2c61;--hot:#ff4d86;--ink:#070707;--muted:#60646d;--line:#e9e9e9;--soft:#f7f7f6;--card:#ffffff;--cream:#fff7ef;}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{background:#fff;}}
[data-testid="stAppViewContainer"]{{background:#fff;color:var(--ink)}} .block-container{{max-width:100%;padding:0!important}}
[data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer, .stDeployButton{{display:none!important}}
section,div,p,h1,h2,h3,h4,a,span,label,input,textarea,button{{font-family:Inter,Arial,Helvetica,sans-serif}}
.bz-topbar{{height:35px;background:linear-gradient(90deg,#ef2f66,#ff5c8d);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:950;letter-spacing:.13em;text-transform:uppercase}}
.bz-nav{{height:104px;background:#fff;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);padding:0 7vw;position:sticky;top:0;z-index:999;box-shadow:0 12px 34px rgba(0,0,0,.04)}}
.logo-wrap{{display:flex;align-items:center;width:220px;text-decoration:none}} .logo-wrap img{{height:74px;max-width:220px;object-fit:contain}}
.bz-menu{{display:flex;gap:42px;align-items:center}} .bz-menu a{{height:104px;display:flex;align-items:center;text-decoration:none;color:#111;text-transform:uppercase;font-size:13px;font-weight:950;letter-spacing:.03em;border-bottom:4px solid transparent}}
.bz-menu a.active{{border-bottom-color:var(--pink)}} .bz-actions{{min-width:250px;display:flex;align-items:center;justify-content:flex-end;gap:12px}}
.bz-actions a{{text-decoration:none;color:#111}} .theme-chip{{height:31px!important;padding:0 12px!important;border:1px solid #111!important;border-radius:99px!important;text-transform:uppercase!important;font-size:11px!important;font-weight:950!important;display:inline-flex!important;align-items:center!important}}
.theme-chip.active{{background:#111!important;color:#fff!important}} .cart-badge{{display:inline-flex;align-items:center;justify-content:center;background:var(--pink);color:white;border-radius:99px;font-size:11px;font-weight:950;min-width:20px;height:20px;margin-left:-19px;margin-top:24px}}
.hero{{min-height:650px;display:grid;grid-template-columns:43% 57%;border-bottom:1px solid var(--line);overflow:hidden;background:#fff}}
.hero-copy{{padding:86px 0 64px 7vw;display:flex;flex-direction:column;justify-content:center;z-index:2}} .eyebrow{{font-size:13px;font-weight:950;color:var(--pink);letter-spacing:.08em;text-transform:uppercase}}
.headline{{font-family:Impact,Arial Black,sans-serif;font-size:92px;line-height:.91;letter-spacing:.005em;text-transform:uppercase;margin:18px 0 22px;color:#050505}} .headline span{{color:var(--pink)}}
.hero-copy p{{font-size:17px;line-height:1.7;max-width:470px;color:#222;margin:0}}
.btn-row{{display:flex;gap:26px;margin-top:42px;flex-wrap:wrap}} .btn-pink,.btn-outline{{height:58px;padding:0 33px;display:inline-flex;align-items:center;justify-content:center;text-decoration:none;text-transform:uppercase;font-size:13px;font-weight:950;letter-spacing:.02em}}
.btn-pink{{background:var(--pink);color:#fff;box-shadow:0 15px 34px rgba(238,44,97,.22)}} .btn-outline{{border:1.5px solid #111;color:#111;background:#fff}}
.hero-art{{position:relative;min-height:650px;background:#f7f7f7;overflow:hidden}} .hero-art:before{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.48) 18%,rgba(255,255,255,0) 46%);z-index:2}}
.hero-slide{{position:absolute;inset:0;background-repeat:no-repeat;background-position:center;background-size:contain;opacity:0;animation:fadeHero 15s infinite ease-in-out;filter:drop-shadow(0 24px 35px rgba(0,0,0,.18))}}
.hero-slide.s1{{background-image:url("{hero1}");animation-delay:0s}} .hero-slide.s2{{background-image:url("{hero2}");animation-delay:5s}} .hero-slide.s3{{background-image:url("{hero3}");animation-delay:10s}}
@keyframes fadeHero{{0%{{opacity:0;transform:scale(1.02)}}8%{{opacity:1;transform:scale(1)}}30%{{opacity:1;transform:scale(1)}}38%{{opacity:0;transform:scale(1.02)}}100%{{opacity:0}}}}
.paint-splash{{position:absolute;right:7%;top:13%;width:54%;height:58%;background:radial-gradient(circle at 45% 38%,rgba(238,44,97,.55),transparent 40%),linear-gradient(145deg,rgba(238,44,97,.28),rgba(0,0,0,.06));clip-path:polygon(5% 25%,48% 6%,94% 23%,72% 54%,92% 88%,40% 74%,8% 96%,20% 53%);z-index:0;filter:blur(.2px)}}
.jp-vertical{{position:absolute;right:6vw;top:92px;font-size:61px;font-weight:950;writing-mode:vertical-rl;letter-spacing:.06em;color:#060606;text-shadow:0 2px 0 #fff;z-index:3}}
.trust{{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line);background:#fff}} .trust-card{{min-height:94px;padding:24px 28px;border-right:1px solid var(--line);display:flex;align-items:center;gap:17px}} .trust-card:first-child{{padding-left:7vw}}
.trust-icon{{font-size:32px}} .trust-card b{{display:block;text-transform:uppercase;font-size:14px;font-weight:950}} .trust-card span{{font-size:13px;color:#666}}
.container{{padding-left:7vw;padding-right:7vw}} .section-head{{display:flex;justify-content:space-between;align-items:flex-end;margin:50px 0 20px}} .small-label{{font-size:12px;font-weight:950;letter-spacing:.08em;text-transform:uppercase;color:var(--pink)}} .section-title{{font-family:Impact,Arial Black,sans-serif;text-transform:uppercase;font-size:48px;line-height:1;margin:8px 0 0;color:#070707}}
.view-link{{font-size:13px;font-weight:950;text-transform:uppercase;text-decoration:none;color:#111}}
.product-shell{{margin-bottom:36px}} .product-card{{background:var(--card)}} .product-image{{background:#f4f4f3;position:relative;overflow:hidden;border:1px solid #eee}} .product-image img{{width:100%;aspect-ratio:1/1.12;display:block;object-fit:contain;background:#f4f4f3;transition:transform .25s ease}} .product-shell:hover .product-image img{{transform:scale(1.025)}}
.badge{{position:absolute;top:14px;left:14px;background:#111;color:#fff;font-size:10px;font-weight:950;letter-spacing:.05em;text-transform:uppercase;padding:8px 10px;z-index:3}} .product-name{{font-size:16px;font-weight:950;text-transform:uppercase;margin-top:15px;color:#111}} .product-meta{{font-size:12px;color:#686868;line-height:1.45;min-height:38px;margin-top:4px}} .product-price{{font-size:15px;font-weight:950;margin-top:7px;color:#111}} .swatches{{margin-top:10px}} .swatch{{display:inline-block;width:16px;height:16px;border-radius:50%;border:1px solid rgba(0,0,0,.25);margin-right:8px}}
.mini-actions{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:13px}} .mini-actions a,.mini-actions span{{height:38px;border:1px solid #111;color:#111;text-decoration:none;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:950;text-transform:uppercase}}
.story{{display:grid;grid-template-columns:42% 58%;min-height:340px;background:#f7f7f6;margin:42px 0 0}} .story-img{{background-size:cover;background-position:center;min-height:340px}} .story-copy{{position:relative;overflow:hidden;padding:55px 62px;background:radial-gradient(circle at right center,rgba(238,44,97,.12),transparent 38%),#f7f7f6}} .story-copy h2{{font-family:Impact,Arial Black,sans-serif;font-size:48px;line-height:.95;text-transform:uppercase;margin:9px 0 17px}} .story-copy p{{max-width:560px;line-height:1.65;color:#30343a}} .big-kanji{{position:absolute;right:36px;top:20px;font-size:170px;font-weight:950;color:rgba(0,0,0,.08);line-height:1}} .brand-stamp{{position:absolute;right:88px;bottom:44px;font-size:46px;font-weight:950;color:var(--pink);transform:rotate(-8deg)}}
.drop-strip{{margin:42px 0;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}} .drop-card{{background:#111;color:#fff;padding:26px;min-height:150px;position:relative;overflow:hidden}} .drop-card h3{{font-family:Impact,Arial Black,sans-serif;font-size:34px;text-transform:uppercase;margin:0 0 8px}} .drop-card p{{color:#ddd;margin:0;line-height:1.55}} .drop-card:after{{content:"BIPZILLA";position:absolute;right:-16px;bottom:-8px;color:rgba(255,255,255,.06);font-family:Impact;font-size:58px;transform:rotate(-6deg)}}
.newsletter{{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;border-top:1px solid var(--line);padding:46px 7vw}} .newsletter h3{{font-family:Impact,Arial Black,sans-serif;text-transform:uppercase;font-size:34px;margin:6px 0}} .muted{{color:#666}} .signup{{display:grid;grid-template-columns:1fr 170px;gap:12px}} .signup input{{height:54px;border:1px solid #ddd;padding:0 18px;font-size:14px}} .signup button{{height:54px;background:var(--pink);border:none;color:#fff;text-transform:uppercase;font-weight:950}}
.footer{{background:#060607;color:white;display:grid;grid-template-columns:1.6fr repeat(4,1fr);gap:40px;padding:48px 7vw 55px}} .footer img{{height:62px;filter:brightness(1.1)}} .footer h4{{font-size:13px;text-transform:uppercase;margin:0 0 12px}} .footer a,.footer p{{display:block;color:#c9c9c9;font-size:13px;text-decoration:none;margin:7px 0}} .footer .tag{{color:var(--pink);font-weight:950;margin-top:26px;text-transform:uppercase}}
.page-pad{{padding:46px 7vw 18px}} .page-intro{{max-width:900px;color:#505762;font-size:16px;line-height:1.7}} .detail-wrap{{padding:50px 7vw;display:grid;grid-template-columns:54% 46%;gap:42px}} .detail-img img{{width:100%;background:#f4f4f3;object-fit:contain;border:1px solid #eee}} .detail h1{{font-family:Impact,Arial Black,sans-serif;font-size:56px;text-transform:uppercase;line-height:.95;margin:0 0 16px}} .detail p{{line-height:1.7;color:#4c535d}} .price-big{{font-size:26px;font-weight:950;margin:12px 0 24px}} .brand-card,.contact-card{{border:1px solid var(--line);background:#fafafa;padding:25px;margin:18px 0}} .stButton>button{{border-radius:0!important;background:#111!important;color:white!important;text-transform:uppercase;font-weight:950;border:1px solid #111!important;height:44px!important}}
@media(max-width:900px){{.bz-nav{{height:auto;padding:16px 5vw;display:block}}.logo-wrap{{width:auto;justify-content:center}}.bz-menu{{overflow-x:auto;gap:22px;justify-content:flex-start}}.bz-menu a{{height:48px;white-space:nowrap}}.bz-actions{{min-width:0;justify-content:center;margin-top:10px}}.hero,.story,.newsletter,.detail-wrap{{grid-template-columns:1fr}}.hero-copy{{padding:58px 6vw}}.headline{{font-size:62px}}.hero-art{{min-height:450px}}.trust{{grid-template-columns:1fr 1fr}}.footer{{grid-template-columns:1fr 1fr}}}}
</style>
''', unsafe_allow_html=True)

if current_theme() == "dark":
    st.markdown('''
<style>
:root{--pink:#ff3f77;--ink:#f5f2ef;--muted:#bfb9b2;--line:#29252a;--soft:#111116;--card:#08080b;}
body,[data-testid="stAppViewContainer"]{background:#08080b!important;color:#f5f2ef!important}.bz-nav,.hero,.container,.newsletter,.page-pad{background:#08080b!important;color:#f5f2ef!important}.bz-nav{border-bottom-color:#28242b!important;box-shadow:0 12px 40px rgba(0,0,0,.45)!important}.bz-menu a,.bz-actions a,.headline,.section-title,.view-link,.product-name,.product-price,.detail h1,.newsletter h3,.trust-card b{color:#f5f2ef!important}.theme-chip{border-color:#f5f2ef!important;color:#f5f2ef!important}.theme-chip.active{background:#ff3f77!important;border-color:#ff3f77!important;color:#fff!important}.hero{background:radial-gradient(circle at 78% 28%,rgba(255,63,119,.16),transparent 36%),#08080b!important}.hero-art{background:#0b0b10!important}.hero-art:before{background:linear-gradient(90deg,#08080b 0%,rgba(8,8,11,.48) 21%,rgba(8,8,11,0) 53%)!important}.hero-copy p,.page-intro,.muted,.product-meta,.story-copy p,.trust-card span,.footer p,.detail p{color:#c8c2bd!important}.trust{background:#0d0d11!important;border-color:#28242b!important}.trust-card{border-color:#28242b!important}.product-image,.product-image img,.detail-img img{background:#111116!important;border-color:#242028!important}.product-card{background:#08080b!important}.story,.story-copy,.brand-card,.contact-card{background:#101015!important;border-color:#28242b!important}.story-copy{background:radial-gradient(circle at right center,rgba(255,63,119,.16),transparent 38%),#101015!important}.big-kanji{color:rgba(255,255,255,.07)!important}.btn-outline{background:#08080b!important;color:#f5f2ef!important;border-color:#f5f2ef!important}input,textarea,select,.stTextInput input,.stTextArea textarea{background:#121218!important;color:#f5f2ef!important;border-color:#29252a!important}.footer{background:#030304!important}.jp-vertical{color:#fff!important;text-shadow:0 2px 0 #000!important}
</style>
''', unsafe_allow_html=True)

def top_nav(active="Home"):
    pages = ["Home", "Shop", "New In", "About", "Contact"]
    links = "".join([f'<a class="{"active" if p==active else ""}" href="{nav_url(p)}">{p}</a>' for p in pages])
    pink = "active" if current_theme() == "pink" else ""; dark = "active" if current_theme() == "dark" else ""
    st.markdown(f'''
<div class="bz-topbar">♛ FREE UK SHIPPING ON DEMO ORDERS OVER £70</div>
<nav class="bz-nav">
  <a class="logo-wrap" href="{nav_url('Home')}"><img src="{logo_src}" alt="BIPZILLA logo"></a>
  <div class="bz-menu">{links}</div>
  <div class="bz-actions"><a class="theme-chip {pink}" href="{theme_url('pink')}">Pink</a><a class="theme-chip {dark}" href="{theme_url('dark')}">Dark</a><a href="{nav_url('Shop')}">⌕</a><a href="{nav_url('Cart')}">🛒</a><span class="cart-badge">{cart_count()}</span></div>
</nav>
''', unsafe_allow_html=True)
    if st.session_state.notice:
        st.success(st.session_state.notice); st.session_state.notice = ""

def footer():
    st.markdown(f'''
<div class="footer">
  <div><img src="{logo_src}" alt="BIPZILLA"><p>© 2026 BIPZILLA demo. Built for Streamlit Cloud. Products, prices and checkout are placeholders.</p></div>
  <div><h4>Shop</h4><a href="{nav_url('Shop')}">All Products</a><a href="{nav_url('Shop')}">T-Shirts</a><a href="{nav_url('Shop')}">Hoodies</a><a href="{nav_url('Shop')}">Sweatshirts</a></div>
  <div><h4>Info</h4><a href="{nav_url('About')}">About Us</a><a>Shipping</a><a>Returns</a><a>Size Guide</a></div>
  <div><h4>Support</h4><a href="{nav_url('Contact')}">Contact Us</a><a>FAQ</a><a>Track Order</a><a>Privacy Policy</a></div>
  <div><h4>Follow</h4><a>Instagram</a><a>TikTok</a><a>Email</a><p class="tag">Art • Culture • Streetwear</p></div>
</div>
''', unsafe_allow_html=True)

def product_card(p, prefix="p"):
    badge = "EMBROIDERY" if "Embroidery" in p["print_type"] else "PRINT"
    st.markdown(f'''
<div class="product-shell"><div class="product-card">
  <div class="product-image"><span class="badge">{badge}</span><img src="{image_src(p['image'])}" alt="{p['name']}"></div>
  <div class="product-name">{p['name']}</div>
  <div class="product-meta">{p['category']} • {p['fit']}<br>{p['colour']}</div>
  <div class="product-price">{money(p['price'])}</div>
  <div class="swatches"><span class="swatch" style="background:#050505"></span><span class="swatch" style="background:#f7f1e7"></span><span class="swatch" style="background:#ee2c61"></span><span class="swatch" style="background:#14213d"></span></div>
  <div class="mini-actions"><a href="{nav_url('Product', product=p['id'])}">View</a><span>{p['stock']} left</span></div>
</div></div>
''', unsafe_allow_html=True)
    if st.button("Add to cart", key=f"{prefix}_{p['id']}", use_container_width=True): add_to_cart(p["id"])

def product_grid(items, columns=4, prefix="grid"):
    if not items:
        st.info("No products match that filter yet."); return
    cols = st.columns(columns)
    for i, p in enumerate(items):
        with cols[i % columns]: product_card(p, f"{prefix}_{i}")

def home():
    st.markdown(f'''
<section class="hero">
  <div class="hero-copy">
    <div class="eyebrow">ART • CULTURE • STREETWEAR</div>
    <h1 class="headline">WEAR<br>YOUR STORY<span>.</span></h1>
    <p>BIPZILLA is a streetwear clothing brand built around bold graphic drops, cleaner embroidered staples, Japanese-English typography and limited runs. This demo keeps it focused like a proper ecommerce brand.</p>
    <div class="btn-row"><a class="btn-pink" href="{nav_url('Shop')}">Shop the drop →</a><a class="btn-outline" href="{nav_url('About')}">About BIPZILLA</a></div>
  </div>
  <div class="hero-art"><div class="paint-splash"></div><div class="hero-slide s1"></div><div class="hero-slide s2"></div><div class="hero-slide s3"></div><div class="jp-vertical">ビップジラ</div></div>
</section>
<section class="trust">
  <div class="trust-card"><div class="trust-icon">◎</div><div><b>Worldwide Shipping</b><span>Fast demo delivery</span></div></div>
  <div class="trust-card"><div class="trust-icon">◇</div><div><b>Limited Drops</b><span>No restocks. Ever.</span></div></div>
  <div class="trust-card"><div class="trust-icon">▣</div><div><b>Print + Embroidery</b><span>Different finishes</span></div></div>
  <div class="trust-card"><div class="trust-icon">♙</div><div><b>Premium Quality</b><span>Heavy cotton feel</span></div></div>
</section>
''', unsafe_allow_html=True)
    st.markdown(f'<div class="container"><div class="section-head"><div><div class="small-label">Featured</div><div class="section-title">Latest Drops</div></div><a class="view-link" href="{nav_url("Shop")}">View all →</a></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="container">', unsafe_allow_html=True); product_grid(PRODUCTS[:4], 4, "home"); st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f'''
<div class="container"><section class="story">
  <div class="story-img" style="background-image:url('{image_src('assets/story_hoodie.jpg')}')"></div>
  <div class="story-copy"><div class="small-label">Our direction</div><h2>MORE THAN CLOTHES.<br>IT'S A MOVEMENT.</h2><p>Built as a clothing brand first: hoodies, tees and sweatshirts with realistic garment mockups, BIPZILLA logo hits, bold typography and a mix of loud print pieces plus subtle embroidery essentials.</p><a class="btn-outline" href="{nav_url('About')}">Read our story →</a><div class="big-kanji">夢</div><div class="brand-stamp">BIP</div></div>
</section>
<div class="drop-strip"><div class="drop-card"><h3>Graphic Drops</h3><p>Samurai, Tokyo night, fantasy armour and painterly print pieces.</p></div><div class="drop-card"><h3>Embroidery</h3><p>Minimal chest-logo hoodies and sweatshirts for everyday wear.</p></div><div class="drop-card"><h3>Colour Range</h3><p>Black, white, navy, cream and pink mockups so the site does not feel flat.</p></div></div></div>
<section class="newsletter"><div><div class="small-label">Join the movement</div><h3>Be the first to know.</h3><p class="muted">Early access to drops, size releases and new artwork.</p></div><form class="signup"><input placeholder="Enter your email address"><button type="button">Subscribe</button></form></section>
''', unsafe_allow_html=True)

def shop(new_only=False):
    items = [p for p in PRODUCTS if p.get('new')] if new_only else PRODUCTS
    title = "New In" if new_only else "Shop The Drop"
    st.markdown(f'<div class="page-pad"><div class="small-label">BIPZILLA Store</div><div class="section-title">{title}</div><p class="page-intro">Browse the demo collection. It now behaves more like an ecommerce site, with same-page navigation, product detail pages, filters, a demo cart, print pieces and embroidery pieces.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: cats = st.multiselect("Clothing type", sorted({p['category'] for p in items}), default=[])
    with c2: finishes = st.multiselect("Finish", sorted({p['print_type'] for p in items}), default=[])
    with c3: max_price = st.slider("Max price", 30, 75, 75)
    filtered = [p for p in items if (not cats or p['category'] in cats) and (not finishes or p['print_type'] in finishes) and p['price'] <= max_price]
    product_grid(filtered, 4, "new" if new_only else "shop")
    st.markdown('</div>', unsafe_allow_html=True)

def product_page():
    p = product_by_id(st.query_params.get('product', PRODUCTS[0]['id']))
    st.markdown('<div class="detail-wrap">', unsafe_allow_html=True)
    left, right = st.columns([1.08, .92], gap='large')
    with left:
        st.markdown(f'<div class="detail-img"><img src="{image_src(p["image"])}" alt="{p["name"]}"></div>', unsafe_allow_html=True)
        st.caption('Realistic product mockup preview for the demo. Source design files are not included separately.')
    with right:
        st.markdown(f'<div class="detail"><div class="small-label">{p["category"]} • {p["print_type"]}</div><h1>{p["name"]}</h1><div class="price-big">{money(p["price"])} GBP</div><p>{p["description"]}</p><div class="brand-card"><b>Finish:</b> {p["finish"]}<br><b>Fit:</b> {p["fit"]}<br><b>Colour:</b> {p["colour"]}<br><b>Stock:</b> {p["stock"]} demo units left</div></div>', unsafe_allow_html=True)
        size = st.selectbox('Size', p['sizes'], index=min(1, len(p['sizes'])-1))
        qty = st.number_input('Quantity', min_value=1, max_value=5, value=1, step=1)
        if st.button('Add to demo cart', use_container_width=True): add_to_cart(p['id'], size=size, qty=qty)
        if st.button('Back to shop', use_container_width=True): go('Shop')
    st.markdown('</div>', unsafe_allow_html=True)

def about():
    st.markdown('''
<div class="page-pad"><div class="small-label">About BIPZILLA</div><div class="section-title">Original energy. Wearable drops.</div><p class="page-intro">BIPZILLA is a demo streetwear brand direction built around limited garments, strong identity and bold culture-inspired visuals. The website is set up to feel like a clothing label, not a loose art gallery.</p></div>
<div class="container"><div class="drop-strip"><div class="drop-card"><h3>Brand First</h3><p>Every item has BIPZILLA identity, product naming, price, stock and finish details.</p></div><div class="drop-card"><h3>Two Finishes</h3><p>Louder graphic print pieces sit beside clean embroidery staples.</p></div><div class="drop-card"><h3>Demo Ready</h3><p>Upload to GitHub and Streamlit Cloud. No payment integration needed.</p></div></div></div>
<section class="newsletter"><div><div class="small-label">Public repo note</div><h3>Protect the originals.</h3><p class="muted">For a public GitHub demo, only upload product mockups. Keep raw artwork, PSD/PNG design files and high-resolution print files private.</p></div><form class="signup"><input placeholder="brand@bipzilla.co.uk"><button type="button">Demo</button></form></section>
''', unsafe_allow_html=True)

def contact():
    st.markdown('<div class="page-pad"><div class="small-label">Contact</div><div class="section-title">Talk to BIPZILLA</div><p class="page-intro">This form is a demo. On a real site you would connect it to email, Google Sheets, Airtable or a proper backend.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    with st.form('contact_form'):
        name = st.text_input('Name')
        email = st.text_input('Email')
        topic = st.selectbox('Topic', ['General question', 'Sizing', 'Wholesale', 'Collaboration', 'Order help'])
        msg = st.text_area('Message', height=140)
        sent = st.form_submit_button('Send demo message')
    if sent:
        st.success(f'Thanks {name or "there"}. This demo captured your {topic.lower()} message locally, but it did not send a real email.')
    st.markdown('</div>', unsafe_allow_html=True)

def cart():
    st.markdown('<div class="page-pad"><div class="small-label">Demo Cart</div><div class="section-title">Your Bag</div><p class="page-intro">This is a dummy ecommerce cart so you can test the flow on Streamlit Cloud.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info('Your demo cart is empty.')
        if st.button('Go shopping'): go('Shop')
    else:
        total = 0
        for key, qty in list(st.session_state.cart.items()):
            pid, size, colour = key.split('|', 2); p = product_by_id(pid); total += p['price'] * qty
            c1, c2, c3, c4 = st.columns([1.3, 3, 1, 1])
            with c1: st.image(str(ROOT / p['image']))
            with c2: st.markdown(f'**{p["name"]}**  \nSize {size} • {colour}  \n{money(p["price"])} each')
            with c3: st.write(f'Qty: {qty}')
            with c4:
                if st.button('Remove', key='remove_' + key):
                    del st.session_state.cart[key]; st.rerun()
        st.markdown(f'### Total: {money(total)}')
        st.button('Demo checkout - coming soon', use_container_width=True)
        if st.button('Clear cart'):
            st.session_state.cart.clear(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

page = get_page()
top_nav("New In" if page == "New In" else page)
if page == "Home": home()
elif page == "Shop": shop(False)
elif page == "New In": shop(True)
elif page == "Product": product_page()
elif page == "About": about()
elif page == "Contact": contact()
elif page == "Cart": cart()
footer()
