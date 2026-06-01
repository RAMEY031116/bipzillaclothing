from pathlib import Path
import base64
import json
import streamlit as st

st.set_page_config(
    page_title="BIPZILLA Clothing Demo",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
PRODUCTS = json.loads((ROOT / "products.json").read_text(encoding="utf-8"))


def img64(path: str) -> str:
    return base64.b64encode((ROOT / path).read_bytes()).decode()


def money(value):
    return f"£{float(value):,.2f}"


def product_by_id(pid):
    return next((p for p in PRODUCTS if p["id"] == pid), None)


def init_state():
    st.session_state.setdefault("page", "Home")
    st.session_state.setdefault("cart", {})
    st.session_state.setdefault("selected_product", PRODUCTS[0]["id"])
    st.session_state.setdefault("wishlist", [])


init_state()


def add_to_cart(pid, size="M", colour=None, qty=1):
    p = product_by_id(pid)
    colour = colour or p["colour"]
    key = f"{pid}|{size}|{colour}"
    st.session_state.cart[key] = st.session_state.cart.get(key, 0) + int(qty)
    st.toast("Added to demo cart 🛒")


def cart_count():
    return sum(st.session_state.cart.values())


def go(page):
    st.session_state.page = page
    st.rerun()


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');
:root{--paper:#f7f0e6;--ink:#101114;--muted:#68707b;--line:#e5d9ca;--card:#fffaf2;--red:#e63d4f;--blue:#172b64;--mint:#0ba978;--gold:#f2a71b;--pink:#ff4f9a;}
*{font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif;}
[data-testid="stAppViewContainer"]{background:radial-gradient(circle at top left,rgba(255,79,154,.14),transparent 34%),radial-gradient(circle at top right,rgba(11,169,120,.10),transparent 30%),linear-gradient(180deg,#fffaf4 0%,var(--paper) 100%);color:var(--ink);}
.block-container{max-width:1320px;padding-top:1rem;padding-bottom:3rem;}
[data-testid="stSidebar"]{background:#111318;color:white;border-right:1px solid rgba(255,255,255,.08);}
[data-testid="stSidebar"] *{color:inherit;}
[data-testid="stSidebar"] img{border-radius:10px;}
.bz-top{position:sticky;top:0;z-index:100;backdrop-filter:blur(16px);background:rgba(255,250,242,.88);border:1px solid rgba(16,17,20,.08);border-radius:24px;padding:14px 18px;margin-bottom:20px;box-shadow:0 12px 40px rgba(32,18,8,.06);}
.nav-pill{display:inline-flex;padding:9px 12px;border:1px solid var(--line);border-radius:999px;background:#fff;color:#111;font-size:13px;font-weight:800;margin:4px;}
.brand-line{font-size:12px;letter-spacing:.16em;color:var(--muted);text-transform:uppercase;font-weight:900;}
.hero{border:1px solid var(--line);border-radius:34px;background:linear-gradient(135deg,rgba(255,255,255,.92),rgba(252,240,230,.82));padding:34px;box-shadow:0 24px 80px rgba(60,25,10,.10);overflow:hidden;}
.eyebrow{display:inline-flex;gap:8px;align-items:center;background:#111318;color:#fff;border-radius:999px;padding:8px 13px;font-size:12px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(46px,6.5vw,92px);line-height:.9;margin:18px 0 16px;letter-spacing:-.04em;}
.lead{font-size:18px;line-height:1.6;color:#364152;max-width:620px;}
.big-cta{display:inline-flex;align-items:center;gap:10px;padding:14px 20px;background:#111318;color:white;border-radius:14px;font-weight:900;box-shadow:0 16px 30px rgba(0,0,0,.18);}
.ghost-cta{display:inline-flex;padding:13px 18px;background:white;border:1px solid #111318;border-radius:14px;font-weight:900;}
.stat-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:20px 0;}
.stat{background:#fff;border:1px solid var(--line);border-radius:22px;padding:17px;box-shadow:0 10px 30px rgba(32,18,8,.05);}
.stat b{font-size:22px;display:block}.stat span{font-size:12px;color:var(--muted);font-weight:800;letter-spacing:.08em;text-transform:uppercase;}
.section-title{font-family:'Playfair Display',serif;font-size:42px;line-height:1;letter-spacing:-.03em;margin:28px 0 8px;}
.section-sub{color:var(--muted);margin-bottom:18px;}
.product-card{border:1px solid var(--line);border-radius:25px;background:#fffaf2;overflow:hidden;box-shadow:0 18px 45px rgba(45,24,8,.07);margin-bottom:18px;transition:.18s ease;}
.product-card:hover{transform:translateY(-3px);box-shadow:0 26px 64px rgba(45,24,8,.12);}
.product-card img{width:100%;display:block;aspect-ratio:4/5;object-fit:cover;background:#eee2d3;border-bottom:1px solid var(--line);}
.product-info{padding:16px}.badge{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border-radius:999px;font-size:11px;font-weight:900;background:#111318;color:#fff;letter-spacing:.05em;text-transform:uppercase;}.badge.print{background:var(--blue)}.badge.emb{background:var(--mint)}
.p-name{font-size:17px;font-weight:900;margin-top:10px}.p-meta{font-size:13px;color:var(--muted);min-height:38px}.price{font-size:18px;font-weight:900;margin-top:8px}.swatch{display:inline-block;width:17px;height:17px;border-radius:50%;border:1px solid rgba(0,0,0,.25);margin-right:5px;vertical-align:middle;}
.story{border:1px solid var(--line);border-radius:30px;background:linear-gradient(90deg,#fff,#fff2f7 50%,#effbf7);padding:28px;margin:24px 0;}
.collection{border:1px solid var(--line);border-radius:28px;overflow:hidden;background:#fff;box-shadow:0 15px 45px rgba(45,24,8,.07);}.collection img{width:100%;aspect-ratio:16/11;object-fit:cover;display:block}.collection div{padding:18px}.collection b{font-size:20px;}
.gallery-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}.gallery-grid img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:18px;border:1px solid var(--line);background:#fff;box-shadow:0 10px 24px rgba(0,0,0,.05);}
.detail{border:1px solid var(--line);border-radius:28px;background:#fffaf2;padding:24px;box-shadow:0 16px 48px rgba(45,24,8,.08);}.notice{border:1px dashed #c4a16e;background:#fff8e9;border-radius:18px;padding:14px;color:#6b4e16;font-weight:700;}.cart-line{border:1px solid var(--line);background:#fff;border-radius:18px;padding:14px;margin-bottom:10px;}.footer{border-top:1px solid var(--line);margin-top:35px;padding-top:24px;color:var(--muted);font-size:13px;}
@media(max-width:900px){.stat-row{grid-template-columns:repeat(2,1fr)}.gallery-grid{grid-template-columns:repeat(3,1fr)}}@media(max-width:640px){.stat-row{grid-template-columns:1fr}.gallery-grid{grid-template-columns:repeat(2,1fr)}.hero{padding:22px}.product-card img{aspect-ratio:1/1}}
</style>
""",
    unsafe_allow_html=True,
)


def sidebar_nav():
    with st.sidebar:
        st.image(str(ROOT / "assets/brand/bipzilla_wordmark.png"), use_container_width=True)
        st.markdown("**ビップジラ**")
        st.caption("Original art clothing demo")
        pages = ["Home", "Shop", "Product Detail", "Collections", "Lookbook", "About", "Contact", "Cart"]
        page = st.radio("Menu", pages, index=pages.index(st.session_state.page))
        if page != st.session_state.page:
            st.session_state.page = page
            st.rerun()
        st.divider()
        st.metric("Cart items", cart_count())
        st.caption("Demo only. Prices and checkout are fake.")


def top_header():
    logo = img64("assets/brand/bipzilla_wordmark.png")
    st.markdown(
        f"""
<div class="bz-top">
  <div style="display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;">
    <div style="display:flex;align-items:center;gap:16px;">
      <img src="data:image/png;base64,{logo}" style="height:52px;max-width:260px;object-fit:contain;"/>
      <div><div class="brand-line">ビップジラ • Clothing brand demo</div><div style="font-size:13px;color:#68707b;">T-shirts • Hoodies • Sweatshirts • Embroidery</div></div>
    </div>
    <div><span class="nav-pill">Cart: {cart_count()}</span><span class="nav-pill">UK £ GBP</span></div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


sidebar_nav()
top_header()


def product_card(p, prefix="card"):
    im = img64(p["image"])
    badge_class = "emb" if p["print_type"] == "Embroidered" else "print"
    st.markdown(
        f"""
<div class="product-card">
  <img src="data:image/jpeg;base64,{im}" alt="{p['name']}" />
  <div class="product-info">
    <span class="badge {badge_class}">{p['print_type']}</span>
    <div class="p-name">{p['name']}</div>
    <div class="p-meta">{p['category']} • {p['fit']}<br>{p['colour']}</div>
    <div class="price">{money(p['price'])}</div>
    <div style="margin-top:8px"><span class="swatch" style="background:#111318"></span><span class="swatch" style="background:#eee2d3"></span><span class="swatch" style="background:#d4d4d4"></span></div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        if st.button("View", key=f"{prefix}_view_{p['id']}", use_container_width=True):
            st.session_state.selected_product = p["id"]
            go("Product Detail")
    with c2:
        if st.button("Add", key=f"{prefix}_add_{p['id']}", use_container_width=True):
            add_to_cart(p["id"], "M", p["colour"], 1)


def product_grid(items, cols=3, prefix="grid"):
    if not items:
        st.info("No products match this filter yet.")
        return
    columns = st.columns(cols)
    for i, p in enumerate(items):
        with columns[i % cols]:
            product_card(p, f"{prefix}_{i}")


def home():
    hero = img64("assets/hero_collage.jpg")
    st.markdown(
        f"""
<div class="hero">
  <div style="display:grid;grid-template-columns:minmax(300px,.9fr) minmax(360px,1.15fr);gap:30px;align-items:center;">
    <div>
      <span class="eyebrow">Limited clothing drop</span>
      <h1>Wear the artwork, not just the logo.</h1>
      <p class="lead">BIPZILLA is a demo streetwear store built around your original watercolour, pen and character art. It is intentionally limited: a few T-shirts, hoodies and sweatshirts with print and embroidery styles.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px;"><span class="big-cta">Shop demo drop →</span><span class="ghost-cta">View lookbook</span></div>
    </div>
    <div><img src="data:image/jpeg;base64,{hero}" style="width:100%;border-radius:28px;border:1px solid #e5d9ca;" /></div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
<div class="stat-row">
  <div class="stat"><b>09</b><span>Demo products</span></div>
  <div class="stat"><b>£32–£64</b><span>Fake UK pricing</span></div>
  <div class="stat"><b>Print + Stitch</b><span>Mixed finishes</span></div>
  <div class="stat"><b>No checkout</b><span>Safe dummy cart</span></div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='section-title'>Featured pieces</div><div class='section-sub'>Clothing first: the product image is a garment mockup, with your original artwork kept in the product page.</div>", unsafe_allow_html=True)
    product_grid(PRODUCTS[:4], 4, "home")
    st.markdown("""
<div class="story"><div class="section-title" style="margin:0 0 8px;">Brand direction</div>
<p class="lead">Keep BIPZILLA as a clothing brand, not only an art shop. Use the artwork as the reason people care, but sell the product as wearable streetwear: heavy blanks, limited drops, clean logo pieces, and one or two loud statement graphics.</p></div>
""", unsafe_allow_html=True)


def shop():
    st.markdown("<div class='section-title'>Shop the demo drop</div><div class='section-sub'>Filter by clothing type, print style and price. All products are dummy examples.</div>", unsafe_allow_html=True)
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            categories = st.multiselect("Clothing type", sorted({p["category"] for p in PRODUCTS}))
        with c2:
            finishes = st.multiselect("Finish", sorted({p["print_type"] for p in PRODUCTS}))
        with c3:
            max_price = st.slider("Max price", 30, 70, 70, step=2)
    items = [p for p in PRODUCTS if (not categories or p["category"] in categories) and (not finishes or p["print_type"] in finishes) and float(p["price"]) <= max_price]
    product_grid(items, 3, "shop")


def product_detail():
    p = product_by_id(st.session_state.selected_product) or PRODUCTS[0]
    st.markdown("<div class='section-title'>Product detail</div>", unsafe_allow_html=True)
    left, right = st.columns([1.05, .95], gap="large")
    with left:
        st.image(str(ROOT / p["image"]), use_container_width=True)
        with st.expander("View original artwork used on this piece"):
            st.image(str(ROOT / p["art"]), use_container_width=True)
    with right:
        badge_class = "emb" if p["print_type"] == "Embroidered" else "print"
        st.markdown(f"""<div class='detail'><span class='badge {badge_class}'>{p['print_type']}</span><h1 style='margin:.7rem 0 .3rem'>{p['name']}</h1><h2>{money(p['price'])}</h2><p class='lead'>{p['description']}</p><p><b>Finish:</b> {p['finish']}<br><b>Fit:</b> {p['fit']}<br><b>Colour:</b> {p['colour']}<br><b>Stock:</b> {p['stock']} demo units</p></div>""", unsafe_allow_html=True)
        size = st.selectbox("Choose size", p["sizes"], index=min(2, len(p["sizes"]) - 1))
        colour = st.selectbox("Choose colour", [p["colour"], "Washed Black", "Stone", "Vintage White"])
        qty = st.number_input("Quantity", min_value=1, max_value=10, value=1, step=1)
        if st.button("Add to demo cart", type="primary", use_container_width=True):
            add_to_cart(p["id"], size, colour, qty)
        st.markdown("<div class='notice'>This is a demo ecommerce flow. It does not take payment and does not send orders.</div>", unsafe_allow_html=True)


def collections():
    st.markdown("<div class='section-title'>Collections</div><div class='section-sub'>This makes it feel like a clothing brand with drops, not just random art uploads.</div>", unsafe_allow_html=True)
    data = [
        ("Drop 01: Statement Graphics", "Large print T-shirts and hoodies using the strongest artwork.", "assets/mockups/samurai_tee.jpg"),
        ("Core Logo / Embroidery", "Minimal pieces with BIPZILLA wordmark, signature mark and Japanese detail.", "assets/mockups/logo_hoodie.jpg"),
        ("Street Sketches", "London/postbox/clock/urban sketch pieces for everyday products.", "assets/art/postbox.jpg"),
    ]
    cols = st.columns(3)
    for i, (title, desc, img) in enumerate(data):
        with cols[i]:
            im = img64(img)
            st.markdown(f"<div class='collection'><img src='data:image/jpeg;base64,{im}'/><div><b>{title}</b><p class='section-sub'>{desc}</p></div></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Suggested launch drop</div>", unsafe_allow_html=True)
    st.markdown("""
- **2 logo pieces:** one hoodie, one sweatshirt, embroidered style.
- **3 art statement pieces:** samurai tee, ocean hoodie, guitar or abstract tee.
- **2 softer everyday pieces:** Crofts Road sweatshirt and cow splash hoodie.
- **1 fun piece:** pizza tee for social content.
""")


def lookbook():
    st.markdown("<div class='section-title'>Artwork lookbook</div><div class='section-sub'>Use this page to show the art behind the clothing. Keep it secondary so the site still feels like fashion/ecommerce.</div>", unsafe_allow_html=True)
    imgs = sorted((ROOT / "assets/lookbook").glob("*.jpg"))
    html = '<div class="gallery-grid">'
    for img in imgs:
        html += f'<img src="data:image/jpeg;base64,{img64("assets/lookbook/" + img.name)}" />'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def about():
    st.markdown("<div class='section-title'>About BIPZILLA</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([.9, 1.1])
    with c1:
        st.image(str(ROOT / "assets/brand/bipzilla_wordmark.png"), use_container_width=True)
        st.markdown("### ビップジラ")
    with c2:
        st.markdown("""
BIPZILLA is a clothing-brand concept built around hand-made art, watercolour texture and streetwear silhouettes. The aim is not to upload hundreds of designs. The aim is to make a small drop feel premium and personal.

**Brand rules for this demo:**

1. Clothing first: every product page starts with a garment mockup.
2. Art stays authentic: do not over-edit the paintings.
3. Keep the range limited: tees, hoodies and sweatshirts only for now.
4. Use embroidery for simple logo pieces and print for detailed artwork.
5. Prices are in UK pounds and are fake for demo/testing.
""")


def contact():
    st.markdown("<div class='section-title'>Contact</div><div class='section-sub'>A dummy form for collabs, custom art and customer questions.</div>", unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        topic = st.selectbox("Topic", ["General question", "Sizing", "Collaboration", "Custom design", "Wholesale"])
        message = st.text_area("Message")
        privacy = st.checkbox("I agree this is a demo form and no real email is sent.")
        if st.form_submit_button("Send demo message", type="primary"):
            if not name or not email or not message or not privacy:
                st.error("Please fill in your name, email, message and tick the demo agreement.")
            else:
                st.success("Demo message saved in this session. In a real site this would send to your inbox.")
    st.markdown("<div class='notice'>Later you can connect this to Google Sheets, FormSubmit, Airtable, or your own email API.</div>", unsafe_allow_html=True)


def cart():
    st.markdown("<div class='section-title'>Demo cart</div><div class='section-sub'>This cart works inside the Streamlit session only.</div>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Your cart is empty. Add products from the shop.")
        if st.button("Go to shop"):
            go("Shop")
        return
    subtotal = 0
    remove_keys = []
    for key, qty in list(st.session_state.cart.items()):
        pid, size, colour = key.split("|")
        p = product_by_id(pid)
        if not p:
            continue
        subtotal += float(p["price"]) * qty
        c1, c2, c3, c4 = st.columns([1.2, 2.6, 1, 1])
        with c1:
            st.image(str(ROOT / p["image"]), use_container_width=True)
        with c2:
            st.markdown(f"<div class='cart-line'><b>{p['name']}</b><br>{size} • {colour}<br>{money(p['price'])} each</div>", unsafe_allow_html=True)
        with c3:
            st.write(f"Qty: {qty}")
        with c4:
            if st.button("Remove", key=f"remove_{key}"):
                remove_keys.append(key)
    for k in remove_keys:
        st.session_state.cart.pop(k, None)
        st.rerun()
    shipping = 3.99 if subtotal < 75 else 0
    total = subtotal + shipping
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"### Subtotal: {money(subtotal)}  \nShipping: {money(shipping)}  \n## Total: {money(total)}")
    with c2:
        with st.form("checkout"):
            st.text_input("Email")
            st.text_input("Postcode")
            st.selectbox("Payment", ["Demo only - no payment"])
            if st.form_submit_button("Place demo order", type="primary"):
                st.success("Demo order placed. No payment taken.")
                st.session_state.cart = {}


ROUTES = {
    "Home": home,
    "Shop": shop,
    "Product Detail": product_detail,
    "Collections": collections,
    "Lookbook": lookbook,
    "About": about,
    "Contact": contact,
    "Cart": cart,
}
ROUTES.get(st.session_state.page, home)()

st.markdown(
    """
<div class="footer"><b>BIPZILLA</b> — Clothing brand Streamlit demo • ビップジラ • Built for GitHub + Streamlit Cloud.<br>Demo only: images, products, prices and checkout are placeholders for testing your brand direction.</div>
""",
    unsafe_allow_html=True,
)
