import base64
from pathlib import Path
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="BIPZILLA | Streetwear Demo", page_icon="🧢", layout="wide", initial_sidebar_state="collapsed")

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"


def img_b64(name: str) -> str:
    path = ASSETS / name
    if not path.exists():
        return ""
    return base64.b64encode(path.read_bytes()).decode()


def img_path(name: str) -> str:
    return str(ASSETS / name)

PINK = "#f02c67"
BLACK = "#070707"
OFFWHITE = "#fbfaf7"

PRODUCTS = [
    {
        "name": "Royal Bloom Tee",
        "category": "T-Shirts",
        "price": 34.99,
        "image": "tee_black_card.png",
        "tag": "Print",
        "drop": "Ace Heart capsule",
        "colours": ["Black", "White", "Dusty Pink"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "Heavy cotton tee with a bold card-inspired back print, small Bipzilla chest mark and clean streetwear fit.",
    },
    {
        "name": "Oni Samurai Tee",
        "category": "T-Shirts",
        "price": 39.99,
        "image": "tee_samurai.png",
        "tag": "Print",
        "drop": "Samurai graphic",
        "colours": ["White", "Black", "Cream"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "A loud samurai mask graphic blended with English and Japanese style text. Made as a statement tee.",
    },
    {
        "name": "Warhammer Kraken Hoodie",
        "category": "Hoodies",
        "price": 69.99,
        "image": "hoodie_kraken.png",
        "tag": "Print",
        "drop": "Dark armour artwork",
        "colours": ["Black", "Charcoal"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "Oversized black hoodie with a dark fantasy armour back graphic and subtle Bipzilla chest logo.",
    },
    {
        "name": "Tokyo Night Hoodie",
        "category": "Hoodies",
        "price": 64.99,
        "image": "hoodie_tokyo_street.png",
        "tag": "Print",
        "drop": "City night capsule",
        "colours": ["Black", "Navy", "Washed Blue"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "A back-print hoodie with city-night energy, pink Japanese-style lettering and a premium streetwear mood.",
    },
    {
        "name": "Ocean Dream Hoodie",
        "category": "Hoodies",
        "price": 64.99,
        "image": "hoodie_cosmic.png",
        "tag": "Print",
        "drop": "Watercolour capsule",
        "colours": ["Navy", "Black"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "A navy hoodie using ocean colours, fish energy and soft watercolour style artwork for a calm but bold look.",
    },
    {
        "name": "Slice Heat Sweatshirt",
        "category": "Sweatshirts",
        "price": 54.99,
        "image": "sweat_pizza_pink.png",
        "tag": "Print",
        "drop": "Food-art capsule",
        "colours": ["Pastel Pink", "Cream", "Sand"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "A soft sweatshirt with a vibrant pizza graphic, playful text details and a small embroidered-style logo mark.",
    },
    {
        "name": "Penguin Winter Sweatshirt",
        "category": "Sweatshirts",
        "price": 52.99,
        "image": "sweat_penguin.png",
        "tag": "Print",
        "drop": "Winter character",
        "colours": ["Navy", "Grey", "Cream"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "Cosy sweatshirt with a friendly penguin illustration and clean Bipzilla mark. A softer streetwear piece.",
    },
    {
        "name": "Core Logo Sweatshirt",
        "category": "Embroidery",
        "price": 49.99,
        "image": "crop_core_sweatshirt.png",
        "tag": "Embroidery",
        "drop": "Minimal core",
        "colours": ["Brown", "Olive", "Black", "Cream"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "Minimal embroidered Bipzilla chest logo on a clean everyday sweatshirt. This is the simple premium piece.",
    },
    {
        "name": "Dragon Legacy Hoodie",
        "category": "Embroidery",
        "price": 67.99,
        "image": "crop_dragon_hoodie.png",
        "tag": "Embroidery",
        "drop": "Raised stitch look",
        "colours": ["Olive", "Black", "Charcoal"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "Olive hoodie with a stitched dragon-style back design and a small Bipzilla chest logo. Clean but still bold.",
    },
    {
        "name": "Fallen Angel Tee",
        "category": "T-Shirts",
        "price": 36.99,
        "image": "crop_fallen_tee.png",
        "tag": "Print",
        "drop": "Dark graphic",
        "colours": ["Black", "White"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "Black tee with high contrast fantasy artwork, red accents and a chest logo detail.",
    },
    {
        "name": "Patch Logo Cap",
        "category": "Accessories",
        "price": 24.99,
        "image": "crop_embroidery_patch.png",
        "tag": "Embroidery",
        "drop": "Accessories",
        "colours": ["Black", "Stone", "Olive"],
        "sizes": ["One Size"],
        "desc": "Structured cap concept with embroidered patch detail. Added so the brand feels like a full clothing line, not only art prints.",
    },
    {
        "name": "Bipzilla Core Hoodie",
        "category": "Embroidery",
        "price": 59.99,
        "image": "hoodie_tokyo_mockup.png",
        "tag": "Embroidery",
        "drop": "Core logo",
        "colours": ["White", "Black", "Grey"],
        "sizes": ["S", "M", "L", "XL"],
        "desc": "Clean hoodie with Japanese-style Bipzilla typography and small logo details for a minimal streetwear option.",
    },
]


def init_state():
    st.session_state.setdefault("page", "Home")
    st.session_state.setdefault("cart", [])
    st.session_state.setdefault("selected", None)
    st.session_state.setdefault("theme", "Pink")
    st.session_state.setdefault("category", "All")

init_state()

hero1 = img_b64("hero_slide_pink.png")
hero2 = img_b64("hero_slide_dark.png")
hero3 = img_b64("hero_slide_tokyo.png")
logo = img_b64("bipzilla_logo.png")

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap');
:root {{ --pink:{PINK}; --black:{BLACK}; --paper:{OFFWHITE}; --line:#e9e5df; }}
.stApp {{ background: var(--paper); font-family: Inter, sans-serif; color:#0b0b0b; }}
.block-container {{ padding-top: 0rem; padding-bottom: 0rem; max-width: 100% !important; }}
[data-testid="stSidebar"] {{ display:none; }}
header[data-testid="stHeader"] {{ background: transparent; }}
#MainMenu, footer {{ visibility:hidden; }}
.topbar {{ background:linear-gradient(90deg,#ef285f,#ff4f7f); color:white; text-align:center; padding:8px 10px; font-size:12px; font-weight:800; letter-spacing:2px; text-transform:uppercase; margin-left:-1rem; margin-right:-1rem; }}
.navwrap {{ display:flex; align-items:center; justify-content:space-between; gap:24px; padding:22px 5vw; background:#fff; border-bottom:1px solid var(--line); margin-left:-1rem; margin-right:-1rem; position:sticky; top:0; z-index:50; }}
.logoBox {{ display:flex; align-items:center; gap:12px; }}
.logoText {{ font-size:34px; font-weight:1000; letter-spacing:-2px; transform:skew(-8deg); line-height:1; color:#080808; text-shadow:2px 2px 0 #f02c67, -2px 1px 0 #00d4c7; }}
.logoSub {{ font-size:10px; font-weight:900; letter-spacing:2px; color:#f02c67; margin-top:3px; }}
.navBtns {{ display:flex; align-items:center; gap:22px; font-weight:900; font-size:13px; text-transform:uppercase; }}
.navBtns span {{ border-bottom:3px solid transparent; padding-bottom:8px; }}
.navBtns .active {{ color:var(--pink); border-color:var(--pink); }}
.cartPill {{ border:1px solid #111; border-radius:999px; padding:8px 14px; font-size:13px; font-weight:900; }}
.hero {{ position:relative; min-height:560px; overflow:hidden; background:#fff; margin-left:-1rem; margin-right:-1rem; border-bottom:1px solid var(--line); }}
.hero:before, .hero:after {{ content:""; position:absolute; inset:0; background-size:cover; background-position:center right; animation:heroFade 16s infinite; opacity:.94; }}
.hero:before {{ background-image:url('data:image/png;base64,{hero1}'); }}
.hero:after {{ background-image:url('data:image/png;base64,{hero2}'); animation-delay:8s; mix-blend-mode:multiply; opacity:0; }}
@keyframes heroFade {{ 0%,45% {{opacity:.96}} 50%,95% {{opacity:0}} 100% {{opacity:.96}} }}
.heroOverlay {{ position:absolute; inset:0; background:linear-gradient(90deg,rgba(255,255,255,.98) 0%,rgba(255,255,255,.92) 36%,rgba(255,255,255,.12) 70%,rgba(255,255,255,0) 100%); }}
.heroCopy {{ position:relative; z-index:2; width:min(520px, 90vw); padding:105px 0 0 6vw; }}
.kicker {{ color:var(--pink); font-weight:1000; font-size:13px; letter-spacing:1px; text-transform:uppercase; margin-bottom:14px; }}
.hero h1 {{ font-size:clamp(52px,8vw,92px); line-height:.88; margin:0 0 22px; font-weight:1000; letter-spacing:-4px; text-transform:uppercase; color:#060606; }}
.hero h1 b {{ color:var(--pink); }}
.hero p {{ font-size:17px; line-height:1.65; max-width:430px; color:#222; }}
.btnRow {{ display:flex; gap:18px; margin-top:28px; flex-wrap:wrap; }}
.cta {{ display:inline-flex; align-items:center; gap:10px; padding:16px 25px; background:var(--pink); color:white !important; border-radius:0; font-weight:1000; text-decoration:none; box-shadow:0 14px 35px rgba(240,44,103,.22); }}
.cta2 {{ display:inline-flex; align-items:center; gap:10px; padding:15px 25px; background:white; color:#111 !important; border:1.5px solid #111; font-weight:1000; text-decoration:none; }}
.strip {{ display:grid; grid-template-columns:repeat(4,1fr); border-bottom:1px solid var(--line); background:white; margin-left:-1rem; margin-right:-1rem; }}
.strip div {{ padding:22px 5vw; border-right:1px solid var(--line); display:flex; gap:14px; align-items:center; }}
.strip b {{ display:block; font-size:14px; text-transform:uppercase; }}
.strip small {{ color:#555; }}
.section {{ padding:46px 5vw 26px; }}
.sectionHeader {{ display:flex; align-items:flex-end; justify-content:space-between; gap:20px; margin-bottom:22px; }}
.sectionHeader h2 {{ margin:0; font-size:42px; font-weight:1000; letter-spacing:-2px; text-transform:uppercase; }}
.sectionHeader small {{ color:var(--pink); font-weight:1000; text-transform:uppercase; letter-spacing:.7px; }}
.productCard {{ background:white; border:1px solid #eee; box-shadow:0 12px 28px rgba(0,0,0,.05); padding:0 0 16px; transition:.2s; min-height:410px; }}
.productCard:hover {{ transform:translateY(-4px); box-shadow:0 20px 40px rgba(0,0,0,.10); }}
.productImg img {{ width:100%; height:280px; object-fit:cover; background:#f3f3f3; display:block; }}
.productBody {{ padding:14px 15px 0; }}
.productBody h3 {{ margin:0 0 4px; font-size:16px; font-weight:1000; text-transform:uppercase; letter-spacing:-.5px; }}
.price {{ font-weight:1000; margin-bottom:8px; }}
.badge {{ display:inline-block; background:#111; color:white; font-size:10px; font-weight:900; padding:5px 8px; text-transform:uppercase; margin-bottom:8px; }}
.badgePink {{ background:var(--pink); }}
.swatches {{ display:flex; gap:7px; margin-top:8px; }}
.swatch {{ width:14px; height:14px; border-radius:999px; border:1px solid #ccc; display:inline-block; }}
.story {{ display:grid; grid-template-columns:1fr 1fr; gap:48px; padding:48px 5vw; background:white; border-top:1px solid var(--line); border-bottom:1px solid var(--line); margin-left:-1rem; margin-right:-1rem; align-items:center; }}
.storyImg {{ min-height:340px; background-image:url('data:image/png;base64,{hero3}'); background-size:cover; background-position:center; border:1px solid #eee; }}
.story h2 {{ font-size:45px; line-height:.95; font-weight:1000; margin:0 0 20px; text-transform:uppercase; letter-spacing:-2px; }}
.newsletter {{ display:grid; grid-template-columns:1fr 1fr; gap:34px; align-items:center; padding:40px 5vw; background:#fff; }}
.footer {{ background:#060606; color:white; padding:36px 5vw; margin-left:-1rem; margin-right:-1rem; display:grid; grid-template-columns:2fr 1fr 1fr 1fr; gap:28px; }}
.footer h4 {{ color:white; margin:0 0 12px; font-size:13px; text-transform:uppercase; }}
.footer p,.footer li {{ color:#cfcfcf; font-size:13px; list-style:none; margin:5px 0; }}
.pageHero {{ padding:56px 5vw 26px; border-bottom:1px solid var(--line); background:#fff; margin-left:-1rem; margin-right:-1rem; }}
.pageHero h1 {{ font-size:58px; margin:0; font-weight:1000; letter-spacing:-3px; text-transform:uppercase; }}
.filterTabs {{ display:flex; gap:10px; flex-wrap:wrap; margin-top:20px; }}
.filterTabs span {{ border:1px solid #111; padding:10px 14px; font-weight:900; font-size:12px; text-transform:uppercase; }}
.detailBox {{ padding:40px 5vw; }}
.detailGrid {{ display:grid; grid-template-columns:1.1fr .9fr; gap:42px; align-items:start; }}
.detailGrid img {{ width:100%; border:1px solid #eee; background:#f6f6f6; }}
.detailGrid h1 {{ font-size:52px; line-height:.95; margin:0 0 14px; font-weight:1000; text-transform:uppercase; letter-spacing:-2px; }}
.infoCards {{ display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-top:24px; }}
.infoCards div {{ border:1px solid #eee; background:#fff; padding:20px; }}
.contactGrid {{ display:grid; grid-template-columns:1fr 1fr; gap:34px; padding:40px 5vw; }}
.darkMode .stApp, .darkMode {{ background:#080808; color:white; }}
@media(max-width:900px){{ .navwrap{{display:block}} .navBtns{{margin-top:18px; overflow:auto}} .hero{{min-height:620px}} .strip{{grid-template-columns:1fr 1fr}} .story,.newsletter,.detailGrid,.contactGrid{{grid-template-columns:1fr}} .footer{{grid-template-columns:1fr 1fr}} .productImg img{{height:240px}} }}
</style>
""", unsafe_allow_html=True)

# Header
cart_count = len(st.session_state.cart)
st.markdown(f"""
<div class="topbar">♛ Free UK shipping on all orders over £70</div>
<div class="navwrap">
  <div class="logoBox"><div><div class="logoText">BIPZILLA</div><div class="logoSub">ART • CULTURE • STREETWEAR</div></div></div>
  <div class="navBtns">
    <span class="{'active' if st.session_state.page=='Home' else ''}">Home</span>
    <span class="{'active' if st.session_state.page=='Shop' else ''}">Shop</span>
    <span class="{'active' if st.session_state.page=='New In' else ''}">New In</span>
    <span class="{'active' if st.session_state.page=='About' else ''}">About</span>
    <span class="{'active' if st.session_state.page=='Contact' else ''}">Contact</span>
  </div>
  <div class="cartPill">Bag • {cart_count}</div>
</div>
""", unsafe_allow_html=True)

# Actual same-page navigation buttons
nav_cols = st.columns([1,1,1,1,1,3,1])
for i, page in enumerate(["Home", "Shop", "New In", "About", "Contact"]):
    if nav_cols[i].button(page, use_container_width=True, key=f"nav_{page}"):
        st.session_state.page = page
        st.session_state.selected = None
        st.rerun()
with nav_cols[6]:
    if st.button(f"Bag ({cart_count})", use_container_width=True):
        st.session_state.page = "Bag"
        st.session_state.selected = None
        st.rerun()


def product_card(product, key_prefix="prod"):
    badge_class = "badge badgePink" if product["tag"] == "Embroidery" else "badge"
    st.markdown(f"""
    <div class="productCard">
      <div class="productImg"><img src="data:image/png;base64,{img_b64(product['image'])}" /></div>
      <div class="productBody">
        <span class="{badge_class}">{product['tag']}</span>
        <h3>{product['name']}</h3>
        <div class="price">£{product['price']:.2f}</div>
        <div style="font-size:12px;color:#666;min-height:34px;">{product['drop']}</div>
        <div class="swatches">
          <span class="swatch" style="background:#111"></span><span class="swatch" style="background:#fff"></span><span class="swatch" style="background:#e94273"></span><span class="swatch" style="background:#38583d"></span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button("View", key=f"{key_prefix}_view_{product['name']}", use_container_width=True):
        st.session_state.selected = product["name"]
        st.session_state.page = "Product"
        st.rerun()
    if c2.button("Add", key=f"{key_prefix}_add_{product['name']}", use_container_width=True):
        st.session_state.cart.append(product["name"])
        st.toast(f"Added {product['name']} to bag")


def product_grid(items, prefix="grid"):
    for start in range(0, len(items), 4):
        cols = st.columns(4)
        for col, product in zip(cols, items[start:start+4]):
            with col:
                product_card(product, prefix)


def home():
    st.markdown("""
    <section class="hero">
      <div class="heroOverlay"></div>
      <div class="heroCopy">
        <div class="kicker">Art • Culture • Streetwear</div>
        <h1>Wear<br>Your Story<b>.</b></h1>
        <p>Bipzilla is a clothing brand built on bold artwork, clean embroidery and limited streetwear drops. Tees, hoodies and sweatshirts designed to feel like a real brand, not just art pasted on fabric.</p>
        <div class="btnRow"><span class="cta">SHOP THE DROP →</span><span class="cta2">ABOUT BIPZILLA</span></div>
      </div>
    </section>
    <div class="strip">
      <div>🌍 <span><b>Worldwide Shipping</b><small>Demo delivery options</small></span></div>
      <div>🏷️ <span><b>Limited Drops</b><small>No restocks. Ever.</small></span></div>
      <div>🛡️ <span><b>Secure Checkout</b><small>Demo checkout flow</small></span></div>
      <div>👕 <span><b>Premium Quality</b><small>Built to last</small></span></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='section'><div class='sectionHeader'><div><small>Featured</small><h2>Latest Drops</h2></div><div style='font-weight:900'>VIEW ALL →</div></div></div>", unsafe_allow_html=True)
    product_grid(PRODUCTS[:8], "home")
    st.markdown("""
    <div class="story">
      <div class="storyImg"></div>
      <div><div class="kicker">Our story</div><h2>More than clothes.<br>It’s a movement.</h2><p>Bipzilla is built around original ideas, street culture, Japanese-inspired lettering, dark fantasy graphics and clean embroidered essentials. The demo keeps the products realistic and easy to understand so you can show the brand direction properly.</p><span class="cta2">READ OUR STORY →</span></div>
    </div>
    <div class="newsletter"><div><div class="kicker">Join the movement</div><h2 style="margin:0;font-size:30px;font-weight:1000;text-transform:uppercase;">Be the first to know.</h2><p>Early access to drops, colourways and offers.</p></div><div><input style="width:65%;padding:16px;border:1px solid #ddd" placeholder="Enter your email address"/><button style="padding:16px 28px;border:0;background:#f02c67;color:white;font-weight:900">SUBSCRIBE</button></div></div>
    """, unsafe_allow_html=True)


def shop(new_only=False):
    title = "New In" if new_only else "Shop"
    st.markdown(f"<div class='pageHero'><div class='kicker'>Bipzilla clothing brand demo</div><h1>{title}</h1><p>Choose from realistic tees, hoodies, sweatshirts and embroidery pieces. This is dummy ecommerce content with UK pricing.</p></div>", unsafe_allow_html=True)
    cats = ["All", "T-Shirts", "Hoodies", "Sweatshirts", "Embroidery", "Accessories"]
    cols = st.columns(len(cats))
    for i, cat in enumerate(cats):
        if cols[i].button(cat, use_container_width=True, key=f"cat_{cat}_{title}"):
            st.session_state.category = cat
    items = PRODUCTS[:6] if new_only else PRODUCTS
    if st.session_state.category != "All":
        items = [p for p in items if p["category"] == st.session_state.category]
    st.markdown(f"<div class='sectionHeader' style='padding:28px 5vw 0'><div><small>{st.session_state.category}</small><h2>{len(items)} items</h2></div></div>", unsafe_allow_html=True)
    product_grid(items, f"shop_{title}_{st.session_state.category}")


def product_detail():
    p = next((x for x in PRODUCTS if x["name"] == st.session_state.selected), PRODUCTS[0])
    st.markdown("<div class='detailBox'><div class='detailGrid'>", unsafe_allow_html=True)
    left, right = st.columns([1.1, .9])
    with left:
        st.image(img_path(p["image"]), use_container_width=True)
    with right:
        st.markdown(f"<div class='kicker'>{p['tag']} • {p['category']}</div><h1 style='font-size:52px;line-height:.95;margin:0 0 16px;font-weight:1000;text-transform:uppercase;letter-spacing:-2px;'>{p['name']}</h1><h2>£{p['price']:.2f}</h2><p style='font-size:17px;line-height:1.7'>{p['desc']}</p>", unsafe_allow_html=True)
        size = st.selectbox("Size", p["sizes"])
        colour = st.selectbox("Colour", p["colours"])
        qty = st.number_input("Quantity", min_value=1, max_value=10, value=1)
        if st.button("Add to bag", type="primary", use_container_width=True):
            for _ in range(qty): st.session_state.cart.append(p["name"])
            st.success(f"Added {qty} × {p['name']} ({colour}, {size})")
        if st.button("Back to shop", use_container_width=True):
            st.session_state.page = "Shop"; st.session_state.selected = None; st.rerun()
        st.markdown("<div class='infoCards'><div><b>Fit</b><br>Relaxed streetwear fit</div><div><b>Finish</b><br>Print or embroidery concept</div><div><b>Demo</b><br>No payment taken</div></div>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)


def about():
    st.markdown("""
    <div class='pageHero'><div class='kicker'>About Bipzilla</div><h1>Art first.<br>Clothing always.</h1><p>Bipzilla is a demo streetwear brand concept: limited drops, original illustrations, Japanese-style lettering, fantasy graphics and minimal embroidered essentials.</p></div>
    <div class='story'><div class='storyImg'></div><div><div class='kicker'>Brand direction</div><h2>Not an art shop.<br>A clothing brand.</h2><p>The products are built to look like real garments first. Artwork is blended into tees, hoodies and sweatshirts with shadows, scale and product context so the site feels like an ecommerce store.</p><p><b>Planned drops:</b> Ace Heart, Samurai/Oni, Tokyo Night, Warhammer Kraken, Pizza Heat and Core Embroidery.</p></div></div>
    """, unsafe_allow_html=True)


def contact():
    st.markdown("<div class='pageHero'><div class='kicker'>Contact</div><h1>Talk to Bipzilla</h1><p>Dummy contact form for the demo website. It will show a success message but it does not send email yet.</p></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Name")
        email = st.text_input("Email")
        reason = st.selectbox("Reason", ["General question", "Order question", "Wholesale", "Collaboration"])
        message = st.text_area("Message")
        agree = st.checkbox("I agree to be contacted about my message.")
        if st.button("Send message", type="primary"):
            if name and email and message and agree:
                st.success("Demo message submitted. Connect this to FormSubmit, Gmail API, or a backend later.")
            else:
                st.warning("Please complete the form and tick the privacy box.")
    with c2:
        st.markdown("""
        <div style='background:white;border:1px solid #eee;padding:28px;min-height:310px'>
        <h3 style='font-size:28px;text-transform:uppercase;margin-top:0'>Support</h3>
        <p><b>Email:</b> hello@bipzilla.demo</p>
        <p><b>Shipping:</b> UK demo shipping from £3.99</p>
        <p><b>Returns:</b> 14-day demo returns policy</p>
        <p><b>Social:</b> Instagram / TikTok / Pinterest</p>
        </div>
        """, unsafe_allow_html=True)


def bag():
    st.markdown("<div class='pageHero'><div class='kicker'>Demo checkout</div><h1>Your bag</h1><p>This is a dummy checkout. It shows the flow only.</p></div>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Your bag is empty.")
        if st.button("Go to shop"):
            st.session_state.page = "Shop"; st.rerun()
        return
    counts = {}
    for item in st.session_state.cart: counts[item] = counts.get(item,0)+1
    total = 0
    for name, qty in counts.items():
        p = next(x for x in PRODUCTS if x["name"] == name)
        total += p["price"]*qty
        c1,c2,c3=st.columns([1,3,1])
        c1.image(img_path(p["image"]), use_container_width=True)
        c2.markdown(f"### {name}\n{p['category']} • {p['tag']}  \nQty: **{qty}**")
        c3.markdown(f"### £{p['price']*qty:.2f}")
    st.markdown(f"## Total: £{total:.2f}")
    c1,c2=st.columns(2)
    if c1.button("Clear bag", use_container_width=True):
        st.session_state.cart=[]; st.rerun()
    if c2.button("Dummy checkout", type="primary", use_container_width=True):
        st.success("Demo checkout complete. No payment was taken.")

# Render page
if st.session_state.page == "Home": home()
elif st.session_state.page == "Shop": shop(False)
elif st.session_state.page == "New In": shop(True)
elif st.session_state.page == "Product": product_detail()
elif st.session_state.page == "About": about()
elif st.session_state.page == "Contact": contact()
elif st.session_state.page == "Bag": bag()

st.markdown("""
<div class='footer'>
  <div><div class='logoText' style='color:white;font-size:30px'>BIPZILLA</div><p>© 2026 BIPZILLA demo. Built for Streamlit Cloud.</p></div>
  <div><h4>Shop</h4><p>All Products</p><p>T-Shirts</p><p>Hoodies</p><p>Sweatshirts</p><p>Embroidery</p></div>
  <div><h4>Info</h4><p>About Us</p><p>Shipping</p><p>Returns</p><p>Size Guide</p></div>
  <div><h4>Support</h4><p>Contact Us</p><p>FAQ</p><p>Track Order</p><p>Privacy Policy</p></div>
</div>
""", unsafe_allow_html=True)
