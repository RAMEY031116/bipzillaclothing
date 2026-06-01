# BIPZILLA Streamlit Clothing Brand Demo v7

A complete Streamlit ecommerce-style demo for the BIPZILLA clothing brand.

Includes:
- Homepage similar to the reference layout
- Pink default theme plus Dark theme toggle
- Shop, New In, Lookbook, About, Contact and Demo Cart pages
- Realistic hoodie, T-shirt and sweatshirt mockups
- Large print pieces and embroidery-style pieces
- GBP demo prices and a working Streamlit session-state cart
- Dummy contact/checkout only; no real payment

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Unzip this folder.
2. Upload every file to a GitHub repository.
3. In Streamlit Cloud, select the repo.
4. Main file path: `app.py`.
5. Deploy.

## Edit products
Change names, prices, descriptions and images in `products.json`. Product images are in `assets/products/`.
