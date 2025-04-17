import pandas as pd

def main():
    # Read input files
    product = pd.read_csv('product.csv')
    sales = pd.read_csv('sales.csv')

    # Merge sales data with products
    merged_data = pd.merge(product, sales, on='sku', how='left')

    # Calculate new price based on rules
    def apply_pricing_rules(row):
        current_price = row['current_price']
        cost_price = row['cost_price']
        stock = row['stock']
        quantity_sold = row['quantity_sold']

        # Rule 1: Low Stock + High Demand
        if stock < 20 and quantity_sold > 30:
            new_price = current_price * 1.15

        # Rule 2: Dead Stock
        elif stock > 200 and quantity_sold == 0:
            new_price = current_price * 0.70

        # Rule 3: Overstocked Inventory
        elif stock > 100 and quantity_sold < 20:
            new_price = current_price * 0.90

        # Default: 
        else:
            new_price = current_price

        # Rule 4: Ensure minimum 20% profit margin
        min_price = cost_price * 1.20
        if new_price < min_price:
            new_price = min_price

        return round(new_price, 2)

    merged_data['new_price'] = merged_data.apply(apply_pricing_rules, axis=1)

# Output to 2 decimal places 
    output = merged_data[['sku', 'current_price', 'new_price']].copy()
    output['current_price'] = output['current_price'].apply(lambda x: f"{x:.2f}")
    output['new_price'] = output['new_price'].apply(lambda x: f"{x:.2f}")
    output.columns = ['sku', 'old_price (INR)', 'new_price (INR)']
    
    output.to_csv('updated_prices.csv', index=False)
    print("Prices saved with 2 decimal places in 'updated_prices.csv'")

if __name__ == "__main__":
    main()