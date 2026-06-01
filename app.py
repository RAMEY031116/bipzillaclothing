
from pathlib import Path
import base64, json, urllib.parse
import streamlit as st

st.set_page_config(page_title="BIPZILLA Clothing", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")
ROOT = Path(__file__).parent
PRODUCTS = json.loads((ROOT / "products.json").read_text(encoding="utf-8"))

# ---------- helpers ----------
def img64(path: str) -> str:
    return base64.b64encode((ROOT / path).read_bytes()).decode()

def money(value):
    return f"£{float(value):,.2f}"

def get_page():
    try:
        page = st.query_params.get("page", "Home")
    except Exception:
        page = "Home"
    return page if page in ROUTES else "Home" if "ROUTES" in globals() else page

def nav_url(page):
    return "?" + urllib.parse.urlencode({"page": page})

def product_by_id(pid):
    return next((p for p in PRODUCTS if p["id"] == pid), PRODUCTS[0])

def init_state():
    st.session_state.setdefault("cart", {})
    st.session_state.setdefault("selected_product", PRODUCTS[0]["id"])
    st.session_state.setdefault("wishlist", [])
init_state()

def cart_count():
    return sum(st.session_state.cart.values())

def add_to_cart(pid, size="M", colour=None, qty=1):
    p = product_by_id(pid)
    colour = colour or p["colour"]
    key = f"{pid}|{size}|{colour}"
    st.session_state.cart[key] = st.session_state.cart.get(key, 0) + int(qty)
    st.toast("Added to demo cart 🛒")

def go(page):
    st.query_params["page"] = page
    st.rerun()

# ---------- CSS ----------
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800;900&display=swap');
:root{--pink:#ef285e;--ink:#08080a;--muted:#636873;--line:#e7e7e7;--soft:#f8f8f7;--cream:#fffaf1;--dark:#09090b;}
*{font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif;}
[data-testid="stAppViewContainer"]{background:#fff;color:var(--ink);} 
.block-container{max-width:1440px;padding:0 0 2.5rem 0;}
[data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer{display:none!important;}
.stDeployButton{display:none!important;}
.bz-announcement{height:36px;background:linear-gradient(90deg,#f02461,#ef2c61);color:white;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;}
.bz-nav{height:104px;background:#fff;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;padding:0 84px;position:sticky;top:0;z-index:1000;box-shadow:0 8px 22px rgba(0,0,0,.03);} 
.bz-logo{display:flex;align-items:center;gap:10px;min-width:220px}.bz-logo img{height:74px;max-width:225px;object-fit:contain;}
.bz-menu{display:flex;align-items:center;gap:42px}.bz-menu a{color:#111;text-decoration:none;font-size:13px;font-weight:900;letter-spacing:.04em;text-transform:uppercase;padding:41px 0 34px;border-bottom:4px solid transparent}.bz-menu a.active{border-bottom-color:var(--pink);color:#000}.bz-icons{display:flex;gap:25px;font-size:24px;align-items:center}.cart-badge{background:var(--pink);color:white;border-radius:999px;padding:2px 7px;font-size:12px;font-weight:900;margin-left:-18px;margin-top:18px;}
.container{padding-left:84px;padding-right:84px;}.hero{min-height:670px;display:grid;grid-template-columns:44% 56%;align-items:center;border-bottom:1px solid var(--line);background:#fff;overflow:hidden}.hero-left{padding:72px 0 72px 84px}.eyebrow{font-size:14px;font-weight:900;color:var(--pink);text-transform:uppercase;letter-spacing:.08em}.hero h1{font-family:Anton,Impact,sans-serif;font-size:88px;line-height:.93;letter-spacing:.01em;margin:22px 0 24px;}.hero h1 span{color:var(--pink)}.hero p{max-width:420px;line-height:1.65;color:#343944;font-size:17px}.hero-img{height:670px;background-size:cover;background-position:center right;}
.btn-row{display:flex;gap:28px;margin-top:40px;flex-wrap:wrap}.btn-pink,.btn-outline{display:inline-flex;align-items:center;justify-content:center;gap:14px;height:58px;padding:0 32px;text-transform:uppercase;font-weight:900;font-size:13px;text-decoration:none}.btn-pink{background:var(--pink);color:white}.btn-outline{border:1.5px solid #111;color:#111;background:white}.trust{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line);}.trust-card{padding:28px 84px 28px 28px;border-right:1px solid var(--line);display:flex;gap:16px;align-items:center}.trust-card:first-child{padding-left:84px}.trust-icon{font-size:35px}.trust-card b{display:block;font-size:15px;text-transform:uppercase}.trust-card span{font-size:13px;color:#666}.section-head{display:flex;align-items:end;justify-content:space-between;margin-top:42px;margin-bottom:20px}.small-label{color:var(--pink);font-size:13px;font-weight:900;text-transform:uppercase;letter-spacing:.06em}.section-title{font-family:Anton,Impact,sans-serif;font-size:48px;line-height:1;margin:8px 0 0;letter-spacing:.01em}.view-link{font-size:14px;font-weight:900;text-transform:uppercase;color:#111;text-decoration:none}.product-card{background:#fff;margin-bottom:28px}.product-img-wrap{background:#f4f4f3;display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative;min-height:360px}.product-img-wrap img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;transition:transform .25s ease}.product-card:hover img{transform:scale(1.025)}.drop-badge{position:absolute;left:14px;top:14px;background:#111;color:#fff;font-size:11px;font-weight:900;text-transform:uppercase;padding:8px 10px}.product-name{font-size:17px;font-weight:900;text-transform:uppercase;margin-top:16px}.product-meta{font-size:13px;color:#666;min-height:42px;line-height:1.45}.price{font-size:16px;font-weight:900;margin-top:6px}.swatch{display:inline-block;width:16px;height:16px;border-radius:50%;border:1px solid rgba(0,0,0,.22);margin-right:8px;margin-top:10px}.story-band{margin:36px 0 0;display:grid;grid-template-columns:42% 58%;background:#f7f7f7;min-height:340px}.story-band img{width:100%;height:100%;object-fit:cover}.story-text{padding:54px 64px;background:radial-gradient(circle at right,#fbe2ea,transparent 42%),#f7f7f7}.story-text h2{font-family:Anton,Impact,sans-serif;font-size:49px;line-height:.96;margin:10px 0 18px}.newsletter{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:30px;padding:46px 84px;border-top:1px solid var(--line);}.newsletter h3{font-family:Anton,Impact,sans-serif;font-size:36px;margin:0}.newsletter input{height:54px;border:1px solid #ddd;padding:0 18px;width:100%;}.footer{background:#070708;color:white;padding:48px 84px 54px;display:grid;grid-template-columns:1.5fr repeat(4,1fr);gap:40px}.footer img{height:76px;filter:invert(0)}.footer h4{font-size:13px;text-transform:uppercase}.footer a,.footer p{font-size:13px;color:#c8c8c8;text-decoration:none;display:block;margin:7px 0}.page-pad{padding:42px 84px 20px}.filter-box{border:1px solid var(--line);background:#fafafa;padding:20px;margin-bottom:24px}.detail-wrap{display:grid;grid-template-columns:53% 47%;gap:50px;padding:48px 84px}.detail-image{background:#f4f4f3}.detail-image img{width:100%;display:block}.detail-box h1{font-family:Anton,Impact,sans-serif;font-size:64px;line-height:.95;margin:10px 0 14px}.detail-box .description{font-size:17px;line-height:1.7;color:#3b4049}.pill{display:inline-block;padding:8px 12px;background:#111;color:white;font-size:11px;text-transform:uppercase;font-weight:900;margin-right:6px}.pill.pink{background:var(--pink)}.notice{border:1px dashed #bd9c4c;background:#fff7df;padding:16px;margin-top:20px;color:#5f4511;font-weight:700}.gallery{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.gallery img{width:100%;aspect-ratio:1/1.18;object-fit:cover;background:#f4f4f3}.cart-line{border:1px solid var(--line);padding:18px;margin-bottom:12px;background:#fff}.cart-line b{text-transform:uppercase}.muted{color:#666}.story-copy{max-width:920px;font-size:18px;line-height:1.8;color:#333}.brand-card{border:1px solid var(--line);padding:28px;background:#fafafa;height:100%} .brand-card h3{font-family:Anton,Impact,sans-serif;font-size:34px;margin:0 0 10px}.contact-card{border:1px solid var(--line);padding:28px;background:#fafafa}.stButton>button{border-radius:0!important;border:1px solid #111!important;text-transform:uppercase!important;font-weight:900!important;min-height:44px!important}.stButton>button[kind="primary"]{background:var(--pink)!important;border-color:var(--pink)!important;color:white!important}
@media(max-width:1050px){.bz-nav{padding:0 22px;height:auto;min-height:94px;align-items:flex-start;flex-direction:column;gap:8px}.bz-menu{gap:20px;flex-wrap:wrap}.bz-menu a{padding:8px 0;border-bottom-width:2px}.bz-icons{position:absolute;right:24px;top:44px}.container,.page-pad,.newsletter,.footer,.detail-wrap{padding-left:24px;padding-right:24px}.hero{grid-template-columns:1fr}.hero-left{padding:44px 24px}.hero-img{height:520px}.trust{grid-template-columns:repeat(2,1fr)}.trust-card,.trust-card:first-child{padding:22px}.story-band{grid-template-columns:1fr}.detail-wrap{grid-template-columns:1fr}.gallery{grid-template-columns:repeat(2,1fr)}.footer{grid-template-columns:1fr 1fr}.hero h1{font-size:68px}}
@media(max-width:620px){.hero h1{font-size:54px}.section-title{font-size:38px}.trust{grid-template-columns:1fr}.newsletter{grid-template-columns:1fr}.footer{grid-template-columns:1fr}.bz-logo img{height:62px}.product-img-wrap{min-height:260px}.gallery{grid-template-columns:1fr}}
</style>
''', unsafe_allow_html=True)

def top_nav(active="Home"):
    logo = img64("assets/brand/bipzilla_wordmark.png")
    pages = ["Home","Shop","New In","Lookbook","About","Contact"]
    links = ''.join([f'<a class="{ "active" if p==active else ""}" href="{nav_url(p)}">{p}</a>' for p in pages])
    cart_link = nav_url("Cart")
    st.markdown(f'''
<div class="bz-announcement">♛ Free UK shipping on all demo orders over £70</div>
<div class="bz-nav">
  <div class="bz-logo"><img src="data:image/png;base64,{logo}" alt="BIPZILLA" /></div>
  <div class="bz-menu">{links}</div>
  <div class="bz-icons"><a style="color:#111;text-decoration:none" href="{nav_url('Shop')}">⌕</a><a style="color:#111;text-decoration:none" href="{cart_link}">🛒</a><span class="cart-badge">{cart_count()}</span></div>
</div>
''', unsafe_allow_html=True)

def footer():
    logo=img64("assets/brand/bipzilla_wordmark.png")
    st.markdown(f'''
<div class="footer">
  <div><img src="data:image/png;base64,{logo}"/><p>© 2026 BIPZILLA demo. Built for Streamlit Cloud. Prices, checkout and stock are placeholders.</p></div>
  <div><h4>Shop</h4><a href="{nav_url('Shop')}">All Products</a><a>T-Shirts</a><a>Hoodies</a><a>Sweatshirts</a></div>
  <div><h4>Info</h4><a href="{nav_url('About')}">About Us</a><a>Shipping</a><a>Returns</a><a>Size Guide</a></div>
  <div><h4>Support</h4><a href="{nav_url('Contact')}">Contact Us</a><a>FAQ</a><a>Track Order</a><a>Privacy Policy</a></div>
  <div><h4>Follow</h4><a>Instagram</a><a>TikTok</a><a>Email</a><p style="color:#ef285e;font-weight:900;margin-top:28px">ART • CULTURE • STREETWEAR</p></div>
</div>
''', unsafe_allow_html=True)

def product_card(p, key_prefix="product"):
    img = img64(p["image"])
    badge = "EMBROIDERY" if p["print_type"] == "Embroidered" else "PRINT"
    st.markdown(f'''
<div class="product-card">
  <div class="product-img-wrap"><span class="drop-badge">{badge}</span><img src="data:image/jpeg;base64,{img}" alt="{p['name']}" /></div>
  <div class="product-name">{p['name']}</div>
  <div class="product-meta">{p['category']} • {p['fit']}<br>{p['colour']}</div>
  <div class="price">{money(p['price'])}</div>
  <div><span class="swatch" style="background:#111"></span><span class="swatch" style="background:#f3eee5"></span><span class="swatch" style="background:#ef285e"></span></div>
</div>
''', unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("View", key=f"{key_prefix}_view_{p['id']}", use_container_width=True):
            st.session_state.selected_product=p["id"]
            go("Product")
    with c2:
        if st.button("Add", key=f"{key_prefix}_add_{p['id']}", use_container_width=True):
            add_to_cart(p["id"], "M", p["colour"], 1)

def product_grid(products, columns=4, prefix="grid"):
    if not products:
        st.info("No products match this filter yet.")
        return
    cols=st.columns(columns)
    for i,p in enumerate(products):
        with cols[i%columns]:
            product_card(p, f"{prefix}_{i}")

def home():
    hero=img64("assets/hero_streetwear.jpg")
    st.markdown(f'''
<section class="hero">
  <div class="hero-left">
    <div class="eyebrow">ART • CULTURE • STREETWEAR</div>
    <h1>WEAR<br>YOUR STORY<span>.</span></h1>
    <p>Bipzilla is a clothing brand demo built on original artwork, bold ideas and self-expression. Limited drops. No restocks.</p>
    <div class="btn-row"><a class="btn-pink" href="{nav_url('Shop')}">Shop the drop →</a><a class="btn-outline" href="{nav_url('About')}">About Bipzilla</a></div>
  </div>
  <div class="hero-img" style="background-image:url(data:image/jpeg;base64,{hero});"></div>
</section>
<section class="trust">
  <div class="trust-card"><div class="trust-icon">◎</div><div><b>Worldwide shipping</b><span>Demo delivery options</span></div></div>
  <div class="trust-card"><div class="trust-icon">◇</div><div><b>Limited drops</b><span>No restocks. Ever.</span></div></div>
  <div class="trust-card"><div class="trust-icon">◷</div><div><b>Secure checkout</b><span>Demo only, no payment</span></div></div>
  <div class="trust-card"><div class="trust-icon">♙</div><div><b>Premium quality</b><span>Built to look like a brand</span></div></div>
</section>
''', unsafe_allow_html=True)
    st.markdown('<div class="container"><div class="section-head"><div><div class="small-label">Featured</div><div class="section-title">Latest Drops</div></div><a class="view-link" href="?page=Shop">View all →</a></div></div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="container">', unsafe_allow_html=True)
        product_grid(PRODUCTS[:4], 4, "home")
        st.markdown('</div>', unsafe_allow_html=True)
    story=img64("assets/story_hoodie.jpg")
    st.markdown(f'''
<div class="container">
  <div class="story-band">
    <img src="data:image/jpeg;base64,{story}" />
    <div class="story-text">
      <div class="small-label">Our story</div>
      <h2>MORE THAN CLOTHES.<br>IT'S A MOVEMENT.</h2>
      <p>Bipzilla was born from original art and streetwear. Every piece is designed to make the artwork feel wearable, not like a random print slapped on a blank.</p>
      <a class="btn-outline" href="{nav_url('About')}">Read our story →</a>
    </div>
  </div>
</div>
<div class="newsletter">
  <div><div class="small-label">Join the movement</div><h3>BE THE FIRST TO KNOW.</h3><p class="muted">Early access to drops, exclusive offers and new art releases.</p></div>
  <div style="display:flex;gap:12px"><input placeholder="Enter your email address"/><a class="btn-pink">Subscribe</a></div>
</div>
''', unsafe_allow_html=True)

def shop(new_only=False):
    title = "New In" if new_only else "Shop the Drop"
    items = PRODUCTS[:6] if new_only else PRODUCTS
    st.markdown(f'<div class="page-pad"><div class="small-label">BIPZILLA STORE</div><div class="section-title">{title}</div><p class="muted">A proper clothing-brand layout with T-shirts, hoodies and sweatshirts. Product images are garment mockups with your artwork printed on the clothes.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    with st.container():
        c1,c2,c3=st.columns(3)
        with c1:
            cat=st.multiselect("Clothing type", sorted({p["category"] for p in items}), default=[])
        with c2:
            finish=st.multiselect("Finish", sorted({p["print_type"] for p in items}), default=[])
        with c3:
            maxp=st.slider("Max price", 30, 70, 70, step=1)
    filtered=[p for p in items if (not cat or p["category"] in cat) and (not finish or p["print_type"] in finish) and p["price"] <= maxp]
    product_grid(filtered, 4, "shop" + ("new" if new_only else ""))
    st.markdown('</div>', unsafe_allow_html=True)

def product():
    p=product_by_id(st.session_state.selected_product)
    st.markdown('<div class="detail-wrap">', unsafe_allow_html=True)
    left,right=st.columns([1.05,.95], gap="large")
    with left:
        st.markdown(f'<div class="detail-image"><img src="data:image/jpeg;base64,{img64(p["image"])}"/></div>', unsafe_allow_html=True)
        with st.expander("Original artwork used for this product"):
            st.image(str(ROOT/p["art"]), use_container_width=True)
    with right:
        st.markdown(f'''
<div class="detail-box">
  <span class="pill pink">{p['category']}</span><span class="pill">{p['print_type']}</span>
  <h1>{p['name']}</h1>
  <h2>{money(p['price'])}</h2>
  <p class="description">{p['description']}</p>
  <p><b>Finish:</b> {p['finish']}<br><b>Colour:</b> {p['colour']}<br><b>Fit:</b> {p['fit']}<br><b>Demo stock:</b> {p['stock']} units</p>
</div>
''', unsafe_allow_html=True)
        size=st.selectbox("Size", p["sizes"], index=1)
        colour=st.selectbox("Colour", [p["colour"], "Black", "Vintage White", "Stone"])
        qty=st.number_input("Quantity", min_value=1, max_value=10, value=1, step=1)
        if st.button("Add to demo cart", type="primary", use_container_width=True):
            add_to_cart(p["id"], size, colour, qty)
        st.markdown('<div class="notice">Demo only: this does not take payment or create a real order.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def lookbook():
    st.markdown('<div class="page-pad"><div class="small-label">Artwork archive</div><div class="section-title">Lookbook</div><p class="muted">This page shows the art behind the clothing. Keep this secondary, because the main site should sell clothes first.</p></div>', unsafe_allow_html=True)
    art_files=["samurai.jpg","ocean.jpg","warrior_colour.jpg","pizza.jpg","abstract.jpg","lamp_clock.jpg","postbox.jpg","cow.jpg","guitar.jpg","koi_2.jpg","card_black.jpg","card_white.jpg"]
    html='<div class="page-pad"><div class="gallery">'
    for f in art_files:
        html += f'<img src="data:image/jpeg;base64,{img64("assets/art/"+f)}" />'
    html+='</div></div>'
    st.markdown(html, unsafe_allow_html=True)

def about():
    st.markdown('''
<div class="page-pad">
  <div class="small-label">About</div><div class="section-title">BIPZILLA is a clothing brand.</div>
  <p class="story-copy">The website is designed to feel like a streetwear/ecommerce brand, not just an art portfolio. The art is the identity, but the product comes first: strong mockups, limited drops, simple navigation, prices in GBP, a cart flow and a contact page.</p>
</div>
<div class="page-pad" style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;">
  <div class="brand-card"><h3>01. Limited</h3><p class="muted">Small drops make the brand feel focused. Start with 6–10 pieces, not hundreds.</p></div>
  <div class="brand-card"><h3>02. Wearable</h3><p class="muted">Use big prints for statement pieces and embroidery for clean logo pieces.</p></div>
  <div class="brand-card"><h3>03. Original</h3><p class="muted">Keep your artwork recognisable. Do not over-edit the paintings just to fit trends.</p></div>
</div>
''', unsafe_allow_html=True)

def contact():
    st.markdown('<div class="page-pad"><div class="small-label">Contact</div><div class="section-title">Talk to BIPZILLA</div><p class="muted">Dummy contact form for collabs, sizing, wholesale or custom design.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-pad"><div class="contact-card">', unsafe_allow_html=True)
    with st.form("contact"):
        c1,c2=st.columns(2)
        with c1:
            name=st.text_input("Name")
            email=st.text_input("Email")
        with c2:
            topic=st.selectbox("Topic", ["Sizing", "Collaboration", "Custom design", "Wholesale", "General question"])
            order=st.text_input("Order number (optional)")
        msg=st.text_area("Message")
        ok=st.checkbox("I understand this is a demo form and no email will be sent.")
        submitted=st.form_submit_button("Send demo message", type="primary")
        if submitted:
            if not name or not email or not msg or not ok:
                st.error("Please complete the required fields and tick the demo checkbox.")
            else:
                st.success("Demo message submitted. Later you can connect this form to email, Google Sheets or Airtable.")
    st.markdown('</div></div>', unsafe_allow_html=True)

def cart():
    st.markdown('<div class="page-pad"><div class="small-label">Checkout</div><div class="section-title">Demo Cart</div><p class="muted">This cart works inside Streamlit session state only.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-pad">', unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Your cart is empty. Add a product from the shop.")
        if st.button("Go to shop", use_container_width=True): go("Shop")
        st.markdown('</div>', unsafe_allow_html=True)
        return
    subtotal=0
    remove=[]
    for key,qty in list(st.session_state.cart.items()):
        pid,size,colour=key.split("|")
        p=product_by_id(pid)
        subtotal += p["price"]*qty
        c1,c2,c3,c4=st.columns([1,3,1,1])
        with c1: st.image(str(ROOT/p["image"]), use_container_width=True)
        with c2: st.markdown(f'<div class="cart-line"><b>{p["name"]}</b><br>{size} • {colour}<br>{money(p["price"])} each</div>', unsafe_allow_html=True)
        with c3: st.write(f"Qty: {qty}")
        with c4:
            if st.button("Remove", key=f"remove_{key}"): remove.append(key)
    for k in remove:
        st.session_state.cart.pop(k, None); st.rerun()
    shipping=0 if subtotal>=70 else 3.99
    total=subtotal+shipping
    st.divider()
    c1,c2=st.columns([1,1])
    with c1:
        st.markdown(f"### Subtotal: {money(subtotal)}  \nShipping: {money(shipping)}  \n## Total: {money(total)}")
    with c2:
        with st.form("checkout"):
            st.text_input("Email")
            st.text_input("UK postcode")
            st.selectbox("Payment method", ["Demo only - no payment"])
            if st.form_submit_button("Place demo order", type="primary"):
                st.success("Demo order placed. No payment was taken.")
                st.session_state.cart={}
    st.markdown('</div>', unsafe_allow_html=True)

ROUTES={"Home":home,"Shop":shop,"New In":lambda:shop(True),"Lookbook":lookbook,"About":about,"Contact":contact,"Cart":cart,"Product":product}
page = get_page()
top_nav(active=page if page in ["Home","Shop","New In","Lookbook","About","Contact"] else "Shop")
ROUTES.get(page, home)()
footer()
