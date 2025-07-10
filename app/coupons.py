def apply_coupon(price, coupon):
    discounts = {
            "SALES10": 0.10,
            "SUPER20": 0.20,
            "WELCOME": 0.15 ## delete 
            }
    if coupon in discounts:
        return round(price * (1 - discounts[coupon]), 2)
    return price
def get_final_price(base_price, coupon, tax_rate=0.19):
    discounts_price = apply_coupon(base_price, coupon)
    return round(discounts_price * (1 + tax_rate), 2)