from typing import Protocol

class Packaging(Protocol):
  def packaging(self) -> str:
    """Creates a string for packaging"""