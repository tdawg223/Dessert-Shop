from typing import Protocol

from enum import Enum

class PayType(Enum):
    CASH = 'CASH'
    CARD = 'CARD'
    PHONE = 'PHONE'

class Payable(Protocol):
  def get_pay_type(self) -> PayType:
    """Get the paytype"""
    # Check if the current payment type is valid
    if self.get_pay_type() not in {PayType.CASH, PayType.CARD, PayType.PHONE}:
      raise ValueError("That is not a valid payment method")

  def set_pay_type(self, payment_method: PayType):
    """Set the paytype"""
    # Check if the provided payment method is valid
    if payment_method not in {PayType.CASH, PayType.CARD, PayType.PHONE}:
        raise ValueError("That is not a valid payment method")