import streamlit as st

st.set_page_config(page_title="Food Price Calculator")

st.title("Simple Food Price Calculator")

st.write("Select food items and enter quantity to calculate total price.")

menu = {
    "Pizza ": 200,
    "Burger ": 120,
    "Pasta ": 150,
    "Sandwich ": 80,
    "Coffee ": 60
}

total_price = 0

st.subheader("Menu")

for item, price in menu.items():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        quantity = st.number_input(
            f"{item} (₹{price})",
            min_value=0,
            step=1,
            key=item
        )
    
    total_price += quantity * price

st.markdown("---")

st.subheader("Total Bill")

st.success(f"Total Price: ₹{total_price}")
