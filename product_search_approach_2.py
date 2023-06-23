from __future__ import annotations

from abc import ABC

from product_search import ProductSearch


# Approach #2 - go through products comparing to each other, if not find an occurrence , it is unique
class ProductSearchApproach2(ProductSearch, ABC):
    def first_unique_product(self, products: list[str]) -> str | None:
        # checks if list is empty
        if not products:
            return None
        # if it has only one item (saving some process and memory)
        if len(products) == 1:
            return products[0]

        unique_prod = None

        i = 0
        j = 0

        for i, pivot_prod in enumerate(products, start=0):
            found = False
            for j, prod in enumerate(products, start=0):
                if i == j:  # don't compare the product with itself (guardian statement pattern)
                    continue
                if pivot_prod == prod:
                    found = True
                    break
            if not found:  # case not found in other positions in the collection, it is unique, ends the search
                unique_prod = pivot_prod
                break
        return unique_prod
