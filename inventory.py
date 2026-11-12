class SoldOutError(Exception):
    pass


def decrease_stock(stock, qty):
    """재고에서 qty만큼 뺀 값을 돌려준다."""
    if qty <= 0:
        raise ValueError("수량은 1 이상이어야 합니다")
    if stock < qty:
        raise SoldOutError("재고가 부족합니다")
    return stock - qty


def restock(stock, qty, limit=100):
    """재고를 채우되 limit을 넘지 않게 한다. 넘친 만큼은 버린다."""
    if qty < 0:
        raise ValueError("입고 수량은 0 이상이어야 합니다")
    return min(stock + qty, limit)
