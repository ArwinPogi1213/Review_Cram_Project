#End-to-end Ecommerce Data Analytics Pipeline

raw_orders = [
    
    {"id": 101, "item": "Laptop", "price": 1200.0, "qty": 2, "category": "Tech"},
    {"id": 102, "item" : "Mouse", "price": 25.0, "qty": 5, "category": "Tech"},
    {"id": 103, "item": "Desk", "price": 300.0, "qty": 1, "category": "Furniture"},
    {"id": 104, "item": "Chair", "price": 150.0, "qty": 4, "category": "Furniture"},
]

#Indexing muna
first_two_orders = raw_orders[0:2]

#Class Def

class Order:
    def __init__(self, order_id: int, item: str, price: float, qty: int):
        self.order_id = order_id
        self.item = item
        self.price = price
        self.qty = qty
        
        
    def calculate_total(self) -> float:
        return self.price * self.qty
    

#Conditions And Loops
high_value_items = []
for order in raw_orders: 
    total = order["price"] * order["qty"]
    if total > 100:
        high_value_items.append(order["item"])
        
        
    