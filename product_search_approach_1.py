from __future__ import annotations

from abc import ABC

from product_search import ProductSearch


# Approach #1 - use a dictionary and store number of occurrences
class ProductSearchApproach1(ProductSearch, ABC):
    def first_unique_product(self, products: list[str]) -> str | None:
        # checks if list is empty
        if not products:
            return None
        # if it has only one item (saving some process and memory)
        if len(products) == 1:
            return products[0]

        # instantiate dictionary to store the count of each product occurrences
        product_catalog = {}

        for product in products:
            if product_catalog.__contains__(product):
                product_catalog[product] += 1
            else:
                product_catalog[product] = 1

        # now find the first product with count = 1 (python dictionaries keep insert order)
        for product in product_catalog:
            if product_catalog[product] == 1:
                return product

        return None
