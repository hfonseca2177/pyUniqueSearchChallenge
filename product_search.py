from __future__ import annotations
import abc


# Product search interface
class ProductSearch(abc.ABC):
    @abc.abstractmethod
    def first_unique_product(self, products: list[str]) -> str | None:
        pass
