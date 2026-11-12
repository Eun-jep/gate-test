def decrease(stock, qty):
    if stock < qty:
        raise ValueError("재고 부족")
    return stock - qty
