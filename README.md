# 📊 Smart Pricing Engine

*"Because guessing prices is so boring"*

## 🧠 What's This All About?

This Python script automatically adjusts product prices based on:
- Current inventory levels
- Recent sales performance
- Minimum profit requirements

## 🛠️ How It Works

The engine applies these rules in order:

1. **🔥 Hot Sellers** (15% price increase)  
   When: Stock < 20 **and** Sales > 30

2. **💀 Dead Stock** (30% price decrease)  
   When: Stock > 200 **and** Sales == 0

3. **📦 Overstocked** (10% price decrease)  
   When: Stock > 100 **and** Sales < 20

4. **🛡️ Profit Protection**  
   Always ensures: New Price ≥ Cost Price × 1.2

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install pandas

# 2. Run the pricing engine
python python.py

# 3. Check your new prices
cat updated_prices.csv
```

## 📂 File Structure

```
.
├── python.py    # Main pricing logic
├── product.csv         # Input: Product catalog
├── sales.csv           # Input: Recent sales data
└── updated_prices.csv  # Output: Optimized prices
```

## 💡 Example Transformation

| SKU  | Old Price | New Price | Reason                |
|------|-----------|-----------|-----------------------|
| A123 | $649.99   | $600.00   | Overstock + Min Profit|
| B456 | $699.00   | $803.85   | High demand           |
| C789 | $999.00   | $600.00   | Dead stock clearance  |

## 🤝 Contributing

Found a bug? Want to improve something?  
1. Fork the repository  
2. Create your feature branch  
3. Submit a pull request

---

*Built with Python and ❤️*


