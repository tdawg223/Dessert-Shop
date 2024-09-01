import receipt
from payable import PayType
from enum import Enum
from typing import Protocol, runtime_checkable

@runtime_checkable
class Combinable(Protocol):
  def can_combine(self, other:"Combinable") -> bool:
    pass

  def combine(self, other:"Combinable") -> "Combinable":
    pass 