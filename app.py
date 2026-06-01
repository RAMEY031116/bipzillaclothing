
from pathlib import Path
import base64
import json
import streamlit as st

st.set_page_config(
    page_title="BIPZILLA — Original Art Streetwear",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
PRODUCTS = json.loads((ROOT / "products.json").read_text(encoding="utf-8"))

# ------------------------- Helpers -------------------------
def img_b64(path: str) -> str:
    full = ROOT / path
    with open(full, "rb") as f:
        return base64.b64encode(f.read()).decode()

def money(value: float) -> str:
    return f"£{value:,.2f}"

def init_state():
    st.session_state.setdefault("page", "Home")
    st.session_state.setdefault("cart", {})
    st.session_state.setdefault("wishlist", set())
    st.session_state.setdefault("newsletter", [])
    st.session_state.setdefault("contact_messages", [])

init_state()

def add_to_cart(product_id: str, size="M", qty=1):
    key = f"{product_id}:{size}"
    st.session_state.cart[key] = st.session_state.cart.get(key, 0) + qty
    st.toast("Added to demo cart 🛒")

def get_product(pid):
    return next((p for p in PRODUCTS if p["id"] == pid), None)

def cart_count():
    return sum(st.session_state.cart.values())

# ------------------------- CSS -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
:root{
    --ink:#101419; --muted:#667085; --paper:#FBF8F2; --line:#E8E0D6;
    --blush:#F5E7E3; --sky:#EAF5FC; --blue:#0F2A44; --green:#0B6B45;
}
html, body, [data-testid="stAppViewContainer"] {background: var(--paper); color: var(--ink);}
.block-container {padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1320px;}
[data-testid="stSidebar"] {display:none;}
hr {border: none; border-top: 1px solid var(--line); margin: 1.4rem 0;}
.bip-topbar{
    position: sticky; top: 0; z-index: 999; background: rgba(251,248,242,.86); backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(16,20,25,.08); padding: 12px 0 10px; margin-bottom: 18px;
}
.bip-logo-wrap img{max-height:54px; object-fit:contain;}
.nav-note{font-size:12px; color:var(--muted); letter-spacing:.08em; text-transform:uppercase; margin-top:-6px;}
.hero-card{border:1px solid var(--line); border-radius:28px; padding:34px; background:linear-gradient(135deg, rgba(255,255,255,.84), rgba(242,236,228,.72)); box-shadow:0 24px 70px rgba(21,32,43,.08); overflow:hidden;}
.eyebrow{display:inline-flex; gap:8px; align-items:center; padding:7px 12px; border-radius:999px; background:#E9F1FF; color:#173B73; font-weight:800; font-size:12px; letter-spacing:.08em; text-transform:uppercase;}
h1.hero-title{font-family:'Playfair Display', serif; font-size: clamp(46px, 6.4vw, 84px); line-height:.92; margin:18px 0 14px; color:#0E1A2B;}
h2.section-title{font-family:'Playfair Display', serif; font-size:36px; margin:8px 0 8px;}
h3.card-title{font-family:'Playfair Display', serif; font-size:25px; margin:0;}
.lead{font-size:18px; line-height:1.55; max-width:560px; color:#2D3643;}
.muted{color:var(--muted);}
.btn-row{display:flex; gap:14px; flex-wrap:wrap; margin-top:24px;}
.primary-fake, .secondary-fake{padding:14px 22px; border-radius:12px; font-weight:800; display:inline-flex; align-items:center; gap:10px; text-decoration:none;}
.primary-fake{background:#111; color:#fff; box-shadow:0 14px 32px rgba(0,0,0,.18)}
.secondary-fake{border:1px solid #111; color:#111; background:#fff;}
.trust-row{display:grid; grid-template-columns:repeat(4,1fr); gap:0; border:1px solid var(--line); border-radius:20px; overflow:hidden; background:#fff8f1; margin:22px 0;}
.trust-item{padding:18px 20px; border-right:1px solid var(--line); display:flex; gap:12px; align-items:center;}
.trust-item:last-child{border-right:0}.trust-icon{font-size:24px}.trust-title{font-weight:800; font-size:13px}.trust-small{font-size:12px;color:var(--muted)}
.product-card{background:#fff; border:1px solid var(--line); border-radius:20px; overflow:hidden; box-shadow:0 14px 40px rgba(22,24,29,.06); margin-bottom:18px;}
.product-card img{width:100%; border-bottom:1px solid var(--line); display:block; background:#f6f1e9;}
.product-info{padding:14px 16px 16px}.product-name{font-weight:900; font-size:17px; margin-bottom:3px}.product-meta{color:var(--muted); font-size:13px}.price{font-weight:900; margin-top:8px}.badge{display:inline-block; padding:6px 10px; border-radius:999px; font-size:11px; font-weight:900; color:#fff; background:#14643F; margin-bottom:10px}.badge.blue{background:#1B5EA9}.badge.dark{background:#111}.swatch{width:16px; height:16px; display:inline-block; border-radius:50%; border:1px solid rgba(0,0,0,.25); margin-right:5px;}
.collection-card{border:1px solid var(--line); border-radius:22px; overflow:hidden; min-height:310px; background:#fff; box-shadow:0 14px 40px rgba(20,30,40,.06);}
.collection-card img{width:100%; height:220px; object-fit:cover; display:block}.collection-card .txt{padding:18px;}
.story-band{background:linear-gradient(90deg, #F8EFF5, #EDF7FC); border:1px solid var(--line); border-radius:28px; padding:28px; margin:24px 0;}
.studio-grid{display:grid; grid-template-columns: repeat(6, 1fr); gap:14px;}.studio-grid img{width:100%; aspect-ratio:1/1; object-fit:cover; border-radius:16px; border:1px solid var(--line); background:#fff;}
.footer{border-top:1px solid var(--line); margin-top:30px; padding:30px 0; color:#1f2937;}
.footer h4{margin:0 0 8px}.footer a{display:block;color:#667085;text-decoration:none;margin:4px 0;font-size:13px}.water-note{font-size:12px;color:#667085;}
.detail-box{border:1px solid var(--line); border-radius:24px; padding:24px; background:white; box-shadow:0 18px 50px rgba(20,30,40,.06);}
.cart-pill{background:#111;color:#fff;border-radius:999px;padding:4px 10px;font-size:12px;font-weight:800;}
@media (max-width: 900px){.trust-row{grid-template-columns:repeat(2,1fr)}.studio-grid{grid-template-columns:repeat(3,1fr)} h1.hero-title{font-size:52px}}
@media (max-width: 600px){.trust-row{grid-template-columns:1fr}.studio-grid{grid-template-columns:repeat(2,1fr)}}
</style>
""", unsafe_allow_html=True)

# ------------------------- Header / Navigation -------------------------
def header():
    logo64 = img_b64("assets/brand/bipzilla_logo.png")
    st.markdown('<div class="bip-topbar">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.5, 3.2, 1])
    with c1:
        st.markdown(f'<div class="bip-logo-wrap"><img src="data:image/png;base64,{logo64}" /></div><div class="nav-note">ビップジラ • wearable art</div>', unsafe_allow_html=True)
    with c2:
        page = st.radio(
            "Navigation",
            ["Home", "Shop", "Collections", "About", "Contact", "Cart"],
            horizontal=True,
            label_visibility="collapsed",
            index=["Home", "Shop", "Collections", "About", "Contact", "Cart"].index(st.session_state.page),
        )
        st.session_state.page = page
    with c3:
        st.markdown(f"<div style='text-align:right; padding-top:12px;'>🛒 <span class='cart-pill'>{cart_count()}</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------- Shared UI -------------------------
def trust_bar():
    st.markdown("""
<div class="trust-row">
  <div class="trust-item"><div class="trust-icon">🕒</div><div><div class="trust-title">LIMITED DROPS</div><div class="trust-small">Small batches only</div></div></div>
  <div class="trust-item"><div class="trust-icon">💎</div><div><div class="trust-title">PREMIUM QUALITY</div><div class="trust-small">Demo streetwear range</div></div></div>
  <div class="trust-item"><div class="trust-icon">✍️</div><div><div class="trust-title">ORIGINAL ART</div><div class="trust-small">Artwork-first brand</div></div></div>
  <div class="trust-item"><div class="trust-icon">🚚</div><div><div class="trust-title">UK SHIPPING</div><div class="trust-small">Dummy checkout demo</div></div></div>
</div>
""", unsafe_allow_html=True)

def product_card(product, key_prefix=""):
    img64 = img_b64(product["image"])
    badge_cls = "blue" if product["print_type"] == "Embroidered" else "dark" if "Logo" in product["badge"] else ""
    st.markdown(f"""
<div class="product-card">
  <img src="data:image/png;base64,{img64}" alt="{product['name']}" />
  <div class="product-info">
    <span class="badge {badge_cls}">{product['print_type']}</span>
    <div class="product-name">{product['name']}</div>
    <div class="product-meta">{product['fit']} • {product['badge']}</div>
    <div class="price">{money(product['price'])}</div>
    <div style="margin-top:8px;"><span class="swatch" style="background:#f2eadc"></span><span class="swatch" style="background:#111"></span><span class="swatch" style="background:#d7d7d7"></span></div>
  </div>
</div>
""", unsafe_allow_html=True)
    size = st.selectbox("Size", ["XS", "S", "M", "L", "XL", "XXL"], index=2, key=f"{key_prefix}_size_{product['id']}", label_visibility="collapsed")
    b1, b2 = st.columns([1.25, .75])
    with b1:
        if st.button("Add to cart", key=f"{key_prefix}_add_{product['id']}", use_container_width=True):
            add_to_cart(product["id"], size)
    with b2:
        if st.button("♡", key=f"{key_prefix}_wish_{product['id']}", use_container_width=True):
            st.session_state.wishlist.add(product["id"])
            st.toast("Saved to wishlist")

def footer():
    logo64 = img_b64("assets/brand/bipzilla_logo.png")
    st.markdown("""
<div class="footer">
""", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([1.6,1,1,1])
    with c1:
        st.markdown(f'<img src="data:image/png;base64,{logo64}" style="max-width:210px;" />', unsafe_allow_html=True)
        st.markdown("**Wearable original art.**  \\nDrawn by hand. Made to be worn.  \\n<span class='water-note'>Demo website only — no real payments are taken.</span>", unsafe_allow_html=True)
        st.write("Instagram • TikTok • Pinterest")
    with c2:
        st.markdown("#### Shop")
        st.markdown("All Products  \\nT-Shirts  \\nHoodies  \\nSweatshirts  \\nAccessories")
    with c3:
        st.markdown("#### Collections")
        st.markdown("New Drop  \\nPrinted Art  \\nEmbroidered  \\nStreet Sketches")
    with c4:
        st.markdown("#### Contact")
        st.markdown("hello@bipzilla.com  \\nManchester / London, UK  \\nWorldwide Shipping")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------- Pages -------------------------
def home_page():
    hero64 = img_b64("assets/hero_collage.png")
    st.markdown(f"""
<div class="hero-card">
  <div style="display:grid; grid-template-columns: minmax(320px, .9fr) minmax(360px, 1.3fr); gap:30px; align-items:center;">
    <div>
      <span class="eyebrow">Original art. Real threads.</span>
      <h1 class="hero-title">Wearable<br/>watercolour art</h1>
      <p class="lead">BIPZILLA turns original sketches, watercolour paintings and bold character art into limited T-shirts, hoodies and sweatshirts.</p>
      <div class="btn-row"><span class="primary-fake">Shop the drop →</span><span class="secondary-fake">View artwork</span></div>
      <p class="muted" style="margin-top:18px;">Logo style: uploaded Bipzilla text + Japanese ビップジラ. No crown in the main header.</p>
    </div>
    <div><img src="data:image/png;base64,{hero64}" style="width:100%; border-radius:26px;" /></div>
  </div>
</div>
""", unsafe_allow_html=True)
    trust_bar()
    st.markdown("<h2 class='section-title'>Featured Products</h2>", unsafe_allow_html=True)
    featured = PRODUCTS[:5]
    cols = st.columns(5)
    for i, p in enumerate(featured):
        with cols[i]:
            product_card(p, key_prefix="home")
    st.markdown("<h2 class='section-title'>Shop by Collection</h2>", unsafe_allow_html=True)
    collections = [
        ("Graphic Tees", "Bold prints. Original art.", "assets/art/samurai.png"),
        ("Hoodies & Sweatshirts", "Comfort meets creativity.", "assets/mockups/logo_hoodie.png"),
        ("Street Sketches", "London-inspired pieces.", "assets/art/postbox.png"),
        ("Playful Icons", "Small embroidered ideas.", "assets/art/pizza.png"),
    ]
    cc = st.columns(4)
    for col, (title, sub, image) in zip(cc, collections):
        with col:
            b = img_b64(image)
            st.markdown(f"""
<div class="collection-card">
  <img src="data:image/png;base64,{b}" />
  <div class="txt"><h3 class="card-title">{title}</h3><p class="muted">{sub}</p><b>Shop now →</b></div>
</div>
""", unsafe_allow_html=True)
    story_band()
    studio_strip()
    newsletter_block()

def story_band():
    sig64 = img_b64("assets/brand/signature_mark.png")
    st.markdown(f"""
<div class="story-band">
  <div style="display:grid; grid-template-columns: 160px 1.4fr repeat(4, 1fr); gap:22px; align-items:center;">
    <img src="data:image/png;base64,{sig64}" style="width:130px; opacity:.85;" />
    <div><div class="eyebrow" style="background:white;">Our story</div><h3 class="card-title">Art first. Always.</h3><p>BIPZILLA is a one-person art brand where every piece starts as a sketch or painting. This demo turns your originals into a clean streetwear shop layout.</p></div>
    <div><b>✍️ Original Art</b><br><span class="muted">Hand-drawn feel</span></div>
    <div><b>👕 Limited Drops</b><br><span class="muted">Small runs</span></div>
    <div><b>♡ Made with Care</b><br><span class="muted">Quality feel</span></div>
    <div><b>🌍 UK Brand</b><br><span class="muted">Worldwide demo</span></div>
  </div>
</div>
""", unsafe_allow_html=True)

def studio_strip():
    imgs = ["assets/art/samurai.png","assets/art/ocean.png","assets/art/warhammer.png","assets/art/pizza.png","assets/art/abstract.png","assets/art/postbox.png"]
    html = "<h2 class='section-title'>From the Studio</h2><div class='studio-grid'>"
    for img in imgs:
        html += f"<img src='data:image/png;base64,{img_b64(img)}' />"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def newsletter_block():
    st.markdown("---")
    c1, c2 = st.columns([1.2,2])
    with c1:
        st.markdown("### Join the drop list")
        st.write("Be first to know about new drops, restocks and behind-the-scenes art.")
    with c2:
        email = st.text_input("Email", placeholder="Enter your email", key="newsletter_email", label_visibility="collapsed")
        if st.button("Subscribe", use_container_width=True):
            if email and "@" in email:
                st.session_state.newsletter.append(email)
                st.success("Subscribed in demo mode ✅")
            else:
                st.warning("Add a valid email for the demo.")

def shop_page():
    st.markdown("<h1 class='hero-title' style='font-size:64px;'>Shop All</h1>", unsafe_allow_html=True)
    st.write("Original art turned into tees, hoodies and sweatshirts. Demo prices in UK pounds.")
    left, right = st.columns([1,4])
    with left:
        st.markdown("### Filter by")
        types = st.multiselect("Product Type", sorted(set(p["type"] for p in PRODUCTS)), default=sorted(set(p["type"] for p in PRODUCTS)))
        print_types = st.multiselect("Print Type", sorted(set(p["print_type"] for p in PRODUCTS)), default=sorted(set(p["print_type"] for p in PRODUCTS)))
        max_price = st.slider("Max price", 30, 60, 60)
        st.info("Free UK shipping on dummy orders over £75.")
    filtered = [p for p in PRODUCTS if p["type"] in types and p["print_type"] in print_types and p["price"] <= max_price]
    with right:
        top = st.columns([2,1])
        with top[0]:
            st.markdown(f"**{len(filtered)} products** found")
        with top[1]:
            sort = st.selectbox("Sort by", ["Featured", "Price low to high", "Price high to low"])
        if sort == "Price low to high":
            filtered = sorted(filtered, key=lambda p:p["price"])
        elif sort == "Price high to low":
            filtered = sorted(filtered, key=lambda p:p["price"], reverse=True)
        rows = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
        for row_i, row in enumerate(rows):
            cols = st.columns(3)
            for col, p in zip(cols, row):
                with col:
                    product_card(p, key_prefix=f"shop{row_i}")
    st.markdown("---")
    st.markdown("<h2 class='section-title'>Quick product preview</h2>", unsafe_allow_html=True)
    selected = st.selectbox("Choose a product to preview", [p["name"] for p in PRODUCTS])
    p = next(x for x in PRODUCTS if x["name"] == selected)
    product_detail(p)

def product_detail(p):
    c1, c2 = st.columns([1.1,1])
    with c1:
        st.image(str(ROOT / p["image"]), use_container_width=True)
    with c2:
        st.markdown(f"<div class='detail-box'><span class='eyebrow'>{p['print_type']}</span><h2 class='section-title'>{p['name']}</h2><p class='lead'>{p['desc']}</p><h2>{money(p['price'])}</h2><p><b>Fit:</b> {p['fit']}<br><b>Colours:</b> {', '.join(p['colors'])}</p></div>", unsafe_allow_html=True)
        size = st.radio("Size", ["XS","S","M","L","XL","XXL"], horizontal=True, index=2, key=f"detail_size_{p['id']}")
        if st.button("Add selected product to cart", key=f"detail_add_{p['id']}", use_container_width=True):
            add_to_cart(p["id"], size)
        st.caption("This is a demo product page. Replace prices, materials and shipping copy when you are ready.")

def collections_page():
    st.markdown("<h1 class='hero-title' style='font-size:64px;'>Collections</h1>", unsafe_allow_html=True)
    st.write("A simple brand structure: a few limited products, not too many. Clean and professional.")
    groups = {
        "The First Drop": ["samurai_tee", "ocean_tee", "warhammer_black_tee"],
        "Embroidered / Small Chest": ["pizza_sweatshirt", "logo_hoodie", "card_sweatshirt"],
        "Street Sketch Series": ["postbox_sweatshirt", "abstract_sweatshirt", "guitar_tee"],
    }
    for title, ids in groups.items():
        st.markdown(f"<h2 class='section-title'>{title}</h2>", unsafe_allow_html=True)
        cols = st.columns(3)
        for col, pid in zip(cols, ids):
            with col:
                product_card(get_product(pid), key_prefix=title.replace(' ','_'))
        st.markdown("---")
    studio_strip()

def about_page():
    st.markdown("<h1 class='hero-title' style='font-size:64px;'>About Bipzilla</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.15,1])
    with c1:
        st.markdown("""
### Drawn by hand. Worn by you.
BIPZILLA is a demo streetwear concept built around your original artwork. The brand should feel handmade, playful, slightly street, and clean enough to become a real shop later.

The best direction is not to upload too many products at the start. Keep the first drop tight: 6–10 pieces, with a mix of big printed artwork and small embroidered chest pieces.

**Suggested positioning:** original watercolour streetwear, limited drops, independent UK art brand.
""")
        st.markdown("#### Brand style")
        st.write("Cream paper background, black typography, blue watercolour accents, tiny pink/purple details, Japanese ビップジラ used as a small supporting mark.")
    with c2:
        st.image(str(ROOT / "assets/hero_collage.png"), use_container_width=True)
    story_band()
    st.markdown("### Launch notes")
    st.write("Start with 2 T-shirts, 1 hoodie and 1 sweatshirt as the first real sample order. Use mockups only for testing feedback, but print samples before selling.")

def contact_page():
    st.markdown("<h1 class='hero-title' style='font-size:64px;'>Get in touch</h1>", unsafe_allow_html=True)
    st.write("Dummy contact page for customer questions, collaboration ideas and wholesale enquiries.")
    c1, c2 = st.columns([1.15,1])
    with c1:
        with st.form("contact_form"):
            name = st.text_input("Name", placeholder="Your name")
            email = st.text_input("Email", placeholder="you@example.com")
            subject = st.selectbox("Subject", ["Order question", "Collaboration", "Wholesale", "Custom request", "Other"])
            msg = st.text_area("Message", placeholder="Tell us about your inquiry...", height=160)
            agree = st.checkbox("I agree this demo can store my message in session state only.")
            submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and msg and agree:
                st.session_state.contact_messages.append({"name":name,"email":email,"subject":subject,"message":msg})
                st.success("Message saved in demo mode ✅")
            else:
                st.warning("Please fill in name, email, message and tick the checkbox.")
    with c2:
        st.markdown("""
<div class="detail-box">
<h3 class="card-title">Other ways to reach us</h3><br>
<b>✉️ Email</b><br>hello@bipzilla.com<br><br>
<b>📸 Instagram</b><br>@bipzilla.art<br><br>
<b>🚚 Shipping help</b><br>shipping@bipzilla.com<br><br>
<b>⏱ Response time</b><br>Mon–Fri, 9am–6pm GMT
</div>
""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### FAQ")
    with st.expander("How much is shipping?"):
        st.write("Demo copy: UK shipping is £3.20 and free over £75. International rates are calculated at checkout.")
    with st.expander("Do you offer returns?"):
        st.write("Demo copy: unworn items can be returned within 14 days. Custom pieces are final sale.")
    with st.expander("How should I care for the garments?"):
        st.write("Wash inside out on cold. Hang dry. Do not iron directly over the artwork.")
    newsletter_block()

def cart_page():
    st.markdown("<h1 class='hero-title' style='font-size:64px;'>Demo Cart</h1>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Your demo cart is empty. Go to Shop and add a product.")
        return
    total = 0
    for key, qty in list(st.session_state.cart.items()):
        pid, size = key.split(":")
        p = get_product(pid)
        subtotal = p["price"] * qty
        total += subtotal
        c1, c2, c3, c4, c5 = st.columns([1,2,1,1,1])
        with c1:
            st.image(str(ROOT / p["image"]), use_container_width=True)
        with c2:
            st.markdown(f"### {p['name']}")
            st.write(f"{p['print_type']} • Size {size}")
        with c3:
            st.write("Qty")
            st.write(qty)
        with c4:
            st.write("Subtotal")
            st.write(money(subtotal))
        with c5:
            if st.button("Remove", key=f"remove_{key}"):
                st.session_state.cart.pop(key)
                st.rerun()
        st.markdown("---")
    shipping = 0 if total >= 75 else 3.20
    grand = total + shipping
    c1, c2 = st.columns([2,1])
    with c2:
        st.markdown(f"""
<div class="detail-box">
<h3 class="card-title">Order summary</h3><br>
Subtotal: <b>{money(total)}</b><br>
Shipping: <b>{'FREE' if shipping == 0 else money(shipping)}</b><br><hr>
Total: <h2>{money(grand)}</h2>
</div>
""", unsafe_allow_html=True)
        if st.button("Dummy checkout", use_container_width=True):
            st.success("Checkout demo complete — no payment taken.")
        if st.button("Clear cart", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

# ------------------------- Render -------------------------
header()
page = st.session_state.page
if page == "Home":
    home_page()
elif page == "Shop":
    shop_page()
elif page == "Collections":
    collections_page()
elif page == "About":
    about_page()
elif page == "Contact":
    contact_page()
elif page == "Cart":
    cart_page()
footer()
