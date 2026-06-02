
import streamlit as st
import json, base64
from pathlib import Path

st.set_page_config(page_title="Bipzilla Streetwear Demo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")
ROOT = Path(__file__).parent
PRODUCTS = json.loads((ROOT / "products.json").read_text())

if "page" not in st.session_state: st.session_state.page = "Home"
if "cart" not in st.session_state: st.session_state.cart = []
if "theme" not in st.session_state: st.session_state.theme = "Pink"

def img64(path):
    return base64.b64encode((ROOT / path).read_bytes()).decode()

def go(page):
    st.session_state.page = page

def css():
    dark = st.session_state.theme == "Dark"
    bg = "#0b0b0d" if dark else "#ffffff"
    text = "#f7f7f7" if dark else "#111111"
    muted = "#bdbdc4" if dark else "#66666b"
    card = "#151519" if dark else "#ffffff"
    line = "rgba(255,255,255,.12)" if dark else "rgba(0,0,0,.08)"
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;800;900&display=swap');
    .stApp {{ background:{bg}; color:{text}; }}
    header, [data-testid="stHeader"] {{ background: transparent; }}
    .block-container {{ padding-top:0 !important; max-width: 100%; }}
    div[data-testid="stToolbar"] {{ display:none; }}
    button[kind="secondary"] {{ border-radius:0 !important; border:1px solid {line} !important; font-family:Inter,sans-serif; font-weight:800; }}
    .topbar {{ margin-left:-5rem; margin-right:-5rem; background:#ec235b; color:white; text-align:center; padding:10px 0; font:800 13px Inter; letter-spacing:2px; }}
    .nav {{ margin-left:-5rem; margin-right:-5rem; height:92px; display:flex; align-items:center; justify-content:space-between; padding:0 70px; border-bottom:1px solid {line}; background:{bg}; position:sticky; top:0; z-index:9; }}
    .brand {{font-family:Bebas Neue, Impact; font-size:42px; letter-spacing:1px; transform:skew(-8deg); line-height:.8; color:{text};}}
    .brand span {{color:#ec235b; font-size:18px; display:block; transform:skew(8deg); letter-spacing:2px;}}
    .navlinks {{ display:flex; gap:36px; font:900 13px Inter; letter-spacing:.5px; align-items:center; }}
    .navpill {{padding:10px 0; border-bottom:3px solid transparent;}}
    .navpill.active {{border-bottom-color:#ec235b; color:#ec235b;}}
    .cart-bubble {{background:#ec235b;color:#fff;border-radius:999px;padding:3px 8px;margin-left:4px;font-size:12px;}}
    .heroWrap {{ margin-left:-5rem; margin-right:-5rem; height:720px; position:relative; overflow:hidden; border-bottom:1px solid {line}; }}
    .heroSlide {{ position:absolute; inset:0; background-size:cover; background-position:center; opacity:0; animation: fadeHero 18s infinite; }}
    .s1 {{ background-image:url('data:image/png;base64,{img64('assets/hero_slide_1.png')}'); animation-delay:0s; }}
    .s2 {{ background-image:url('data:image/png;base64,{img64('assets/hero_slide_2.png')}'); animation-delay:6s; }}
    .s3 {{ background-image:url('data:image/png;base64,{img64('assets/hero_slide_3.png')}'); animation-delay:12s; }}
    @keyframes fadeHero {{ 0%{{opacity:0}} 8%{{opacity:1}} 31%{{opacity:1}} 41%{{opacity:0}} 100%{{opacity:0}} }}
    .section {{ max-width:1180px; margin:0 auto; padding:60px 0; }}
    .eyebrow {{ color:#ec235b; font:900 13px Inter; letter-spacing:1px; text-transform:uppercase; }}
    h1,h2,h3 {{ font-family:Bebas Neue, Impact, sans-serif !important; letter-spacing:.5px; color:{text}; }}
    .section h2 {{ font-size:54px; margin:8px 0 24px; }}
    .benefits {{ max-width:1180px; margin:0 auto; display:grid; grid-template-columns:repeat(4,1fr); gap:0; border-bottom:1px solid {line}; }}
    .benefit {{ padding:28px 24px; border-right:1px solid {line}; display:flex; gap:14px; align-items:center; }}
    .benefit b {{ display:block; font:900 14px Inter; color:{text}; }} .benefit span {{ color:{muted}; font-size:13px; }}
    .product-card {{ background:{card}; border:1px solid {line}; padding:0; transition:.2s ease; height:100%; }}
    .product-card:hover {{ transform:translateY(-4px); box-shadow:0 18px 50px rgba(0,0,0,.12); }}
    .product-img {{ width:100%; aspect-ratio: 1/1.12; object-fit:cover; background:#f5f5f5; display:block; }}
    .product-info {{ padding:18px 0 0; }}
    .product-name {{ font:900 18px Inter; color:{text}; text-transform:uppercase; }}
    .price {{ font:900 16px Inter; color:{text}; margin:4px 0 8px; }}
    .tag {{ color:#ec235b; font:800 12px Inter; }}
    .swatches span {{ display:inline-block; width:16px; height:16px; border-radius:50%; border:1px solid {line}; margin-right:9px; }}
    .story {{ display:grid; grid-template-columns:1fr 1fr; gap:48px; align-items:center; background:{'#111114' if dark else '#f8f8f8'}; padding:48px; }}
    .storyImg {{ min-height:340px; background:linear-gradient(135deg,#111,#ec235b); display:flex; align-items:center; justify-content:center; color:white; font-family:Bebas Neue; font-size:72px; }}
    .newsletter {{ border-top:1px solid {line}; border-bottom:1px solid {line}; padding:48px 0; }}
    .footer {{ margin-left:-5rem; margin-right:-5rem; background:#070707; color:white; padding:52px 70px; display:grid; grid-template-columns:2fr 1fr 1fr 1fr; gap:40px; }}
    .footer a,.footer p {{ color:#aaa; font-size:13px; }}
    .pageHead {{ margin-left:-5rem; margin-right:-5rem; background:{'#111114' if dark else '#f7f7f7'}; padding:74px 70px 58px; border-bottom:1px solid {line}; }}
    .pageHead h1 {{font-size:76px; margin:0;}} .pageHead p {{color:{muted}; font-size:18px; max-width:680px;}}
    .cartLine {{ display:flex; align-items:center; justify-content:space-between; border-bottom:1px solid {line}; padding:14px 0; }}
    @media(max-width:900px) {{ .nav{{padding:0 24px}} .navlinks{{gap:12px;font-size:11px}} .heroWrap{{height:560px}} .benefits{{grid-template-columns:1fr 1fr}} .story{{grid-template-columns:1fr;padding:26px}} .footer{{grid-template-columns:1fr 1fr;padding:36px 24px}} }}
    </style>
    """, unsafe_allow_html=True)

def header():
    active=st.session_state.page
    st.markdown('<div class="topbar">♛ FREE UK SHIPPING ON ALL ORDERS OVER £70</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="nav"><div class="brand">BIPZILLA<span>ビップジラ</span></div>
    <div class="navlinks">
      <span class="navpill {'active' if active=='Home' else ''}">HOME</span>
      <span class="navpill {'active' if active=='Shop' else ''}">SHOP</span>
      <span class="navpill {'active' if active=='New In' else ''}">NEW IN</span>
      <span class="navpill {'active' if active=='About' else ''}">ABOUT</span>
      <span class="navpill {'active' if active=='Contact' else ''}">CONTACT</span>
      <span>🛒<span class="cart-bubble">{len(st.session_state.cart)}</span></span>
    </div></div>""", unsafe_allow_html=True)
    cols=st.columns([1,1,1,1,1,1,3,1])
    for label,col in zip(["Home","Shop","New In","About","Contact","Cart"],cols[:6]):
        with col:
            if st.button(label, key='nav_'+label, use_container_width=True): go(label)
    with cols[-1]:
        st.session_state.theme = st.toggle("Dark mode", value=st.session_state.theme=="Dark", help="Switch between the pink white store and dark version") and "Dark" or "Pink"

def footer():
    st.markdown("""
    <div class="footer"><div><div class="brand" style="color:white">BIPZILLA<span>ビップジラ</span></div><p>© 2026 Bipzilla demo. Art • culture • streetwear.</p></div>
    <div><b>SHOP</b><p>Hoodies<br>T-Shirts<br>Sweatshirts<br>Embroidery</p></div><div><b>INFO</b><p>About<br>Shipping<br>Returns<br>Size Guide</p></div><div><b>FOLLOW</b><p>Instagram · TikTok · Email</p></div></div>
    """, unsafe_allow_html=True)

def product_grid(items):
    cols = st.columns(4)
    for i,p in enumerate(items):
        with cols[i%4]:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(str(ROOT/p['image']), use_container_width=True)
            st.markdown(f"<div class='product-info'><div class='tag'>{p['tag']}</div><div class='product-name'>{p['name']}</div><div class='price'>{p['price']}</div><div style='color:#777;font-size:13px'>{p['colour']} · {p['category']}</div><div class='swatches'><span style='background:#111'></span><span style='background:#fff'></span><span style='background:#ec235b'></span><span style='background:#1c4778'></span></div></div>", unsafe_allow_html=True)
            c1,c2=st.columns(2)
            with c1:
                if st.button("Add", key='add_'+p['name'], use_container_width=True):
                    st.session_state.cart.append(p['name']); st.toast(f"Added {p['name']} to demo cart")
            with c2:
                if st.button("View", key='view_'+p['name'], use_container_width=True):
                    st.session_state.selected=p; go('Product')
            st.markdown('</div>', unsafe_allow_html=True)

def home():
    st.markdown('<div class="heroWrap"><div class="heroSlide s1"></div><div class="heroSlide s2"></div><div class="heroSlide s3"></div></div>', unsafe_allow_html=True)
    st.markdown("""<div class="benefits"><div class="benefit">🌍 <div><b>WORLDWIDE SHIPPING</b><span>Fast demo delivery</span></div></div><div class="benefit">🏷️ <div><b>LIMITED DROPS</b><span>No restocks. Ever.</span></div></div><div class="benefit">🧵 <div><b>EMBROIDERY PIECES</b><span>Caps, beanies and chest hits</span></div></div><div class="benefit">👕 <div><b>PREMIUM QUALITY</b><span>Built to feel like a brand</span></div></div></div>""", unsafe_allow_html=True)
    st.markdown('<div class="section"><div class="eyebrow">Featured</div><h2>Latest Drops</h2></div>', unsafe_allow_html=True)
    product_grid(PRODUCTS[:8])
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("""<div class="story"><div class="storyImg">ビップジラ<br/>DROP CULTURE</div><div><div class="eyebrow">Our Story</div><h2>More than clothes.<br>It’s a movement.</h2><p>Bipzilla is built as a clothing brand first: wearable streetwear, original graphics, embroidery essentials and limited capsules. This demo keeps your personal artwork private while showing how the brand can feel online.</p></div></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="section newsletter"><div class="eyebrow">Join the movement</div><h2>Be the first to know.</h2></div>', unsafe_allow_html=True)
    cols=st.columns([3,2,1])
    with cols[1]: st.text_input("Email", placeholder="Enter your email address", label_visibility="collapsed")
    with cols[2]: st.button("SUBSCRIBE", use_container_width=True)

def shop(page_title="Shop the Drop", category=None):
    st.markdown(f'<div class="pageHead"><div class="eyebrow">Bipzilla Clothing</div><h1>{page_title}</h1><p>Demo products using pizza, samurai, war-armour and ace-of-hearts themes, with realistic clothing mockups and embroidery pieces.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    cats=["All","T-Shirt","Hoodie","Sweatshirt","Embroidery"]
    picked = st.radio("Filter", cats, horizontal=True, label_visibility="collapsed", index=0 if category is None else cats.index(category))
    items=PRODUCTS if picked=="All" else [p for p in PRODUCTS if p['category']==picked]
    product_grid(items)
    st.markdown('</div>', unsafe_allow_html=True)

def about():
    st.markdown('<div class="pageHead"><div class="eyebrow">About</div><h1>Art. Culture. Streetwear.</h1><p>Bipzilla is a sample clothing brand concept, not just an art gallery. The store is built around wearable garments, limited drops and a strong visual identity.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        st.image(str(ROOT/'assets/hero_slide_2.png'), use_container_width=True)
    with c2:
        st.markdown("### Brand direction")
        st.write("The demo uses clean product photography style, bold pink/black branding, Japanese and English type, printed graphics and embroidery items. Your original uploaded art is not shown as a gallery, so the website feels like a proper clothing brand.")
        st.markdown("### Demo notes")
        st.write("Buttons and cart are dummy/demo only. No payment is connected. It is ready for Streamlit Cloud through GitHub.")
    st.markdown('</div>', unsafe_allow_html=True)

def contact():
    st.markdown('<div class="pageHead"><div class="eyebrow">Contact</div><h1>Talk to Bipzilla.</h1><p>Use this dummy form for wholesale, sample requests, collaborations or general messages.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    with st.form('contact_form'):
        name=st.text_input('Name')
        email=st.text_input('Email')
        topic=st.selectbox('Topic',['Order question','Collaboration','Wholesale','General'])
        msg=st.text_area('Message',height=140)
        ok=st.checkbox('I agree this is a demo form and no real message is sent.')
        submitted=st.form_submit_button('SEND MESSAGE')
        if submitted:
            if name and email and msg and ok: st.success('Demo message received. In a real website this would send to your email.')
            else: st.error('Please complete all fields and tick the box.')
    st.markdown('</div>', unsafe_allow_html=True)

def cart():
    st.markdown('<div class="pageHead"><div class="eyebrow">Demo Cart</div><h1>Your Bag</h1><p>This cart is a working front-end demo only. Refreshing may clear it.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    if not st.session_state.cart: st.info('Your demo cart is empty. Add products from the shop.')
    else:
        total=0
        for name in st.session_state.cart:
            p=next(x for x in PRODUCTS if x['name']==name); val=float(p['price'].replace('£','')); total+=val
            st.markdown(f"<div class='cartLine'><b>{name}</b><span>{p['price']}</span></div>", unsafe_allow_html=True)
        st.markdown(f"### Total: £{total:.2f}")
        if st.button('Clear cart'): st.session_state.cart=[]; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def product():
    p=st.session_state.get('selected',PRODUCTS[0])
    st.markdown(f'<div class="pageHead"><div class="eyebrow">{p["category"]}</div><h1>{p["name"]}</h1><p>{p["story"]}</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    c1,c2=st.columns([1.1,.9])
    with c1: st.image(str(ROOT/p['image']), use_container_width=True)
    with c2:
        st.markdown(f"## {p['price']}")
        st.write(f"**Colour:** {p['colour']}")
        st.write(f"**Finish:** {p['tag']}")
        st.selectbox('Size',['S','M','L','XL','XXL'])
        st.radio('Colour option',['Black','White','Navy','Pink','Stone'],horizontal=True)
        if st.button('ADD TO CART', use_container_width=True): st.session_state.cart.append(p['name']); st.success('Added to demo cart')
        st.button('BACK TO SHOP', on_click=go, args=('Shop',), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

css(); header()
page=st.session_state.page
if page=='Home': home()
elif page=='Shop': shop()
elif page=='New In': shop('New In', None)
elif page=='About': about()
elif page=='Contact': contact()
elif page=='Cart': cart()
elif page=='Product': product()
footer()
