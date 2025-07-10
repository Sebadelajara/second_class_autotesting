from flask import Flask, request, jsonify
from app.coupons import get_final_price

app = Flask(__name__)
@app.route('/precio', methods=['POST'])

def calcular():
    data = request.get_json()
    price = data.get("price")
    coupon = data.get("coupon")
    tax_rate = data.get("tax_rate", 0.19)
    final = get_final_price(price, coupon, tax_rate)
    return jsonify({"final_price": final})