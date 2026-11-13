"""주문 할인 계산."""

MAX_DISCOUNT_RATE = 0.30  # 한 주문에 줄 수 있는 최대 할인율


def apply_discount(price: int, rate: float, is_member: bool = False) -> int:
    """할인된 가격을 돌려준다. 회원이면 할인율을 5%p 더 올려 준다."""
    if price < 0:
        raise ValueError("가격은 0 이상이어야 해요")
    if not 0 <= rate <= 1:
        raise ValueError("할인율은 0과 1 사이여야 해요")
    if is_member:
        rate += 0.05
    rate = min(rate, MAX_DISCOUNT_RATE)
    return int(price * (1 - rate))
