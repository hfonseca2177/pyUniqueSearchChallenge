"""
Write a method that, efficiently with respect to time used, finds the first
unique product in a list of products.
If there are no unique products, None should be returned.

You can test your solution by running `python phx_test_unique_product.py`
"""
from __future__ import annotations


def first_unique_product(products: list[str]) -> str | None:
    """
    Return the first unique product in the list of products.

    >>> first_unique_product(['apple', 'cabbage', 'apple', 'banana'])
    'cabbage'
    >>> first_unique_product(['apple', 'cabbage', 'banana'])
    'apple'
    >>> first_unique_product(['apple', 'apple', 'apple'])
    None

    :param products: A list of products
    :return: The first unique product, or None if there are no unique products
    """
    # Implement this method


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
