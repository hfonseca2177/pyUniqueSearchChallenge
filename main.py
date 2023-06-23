"""
Using REACTO framework to solve it

######  REPEAT -  check of understanding ######
Find first term that is unique in a collection
- No collection size specified
- Unique means there is no other term with same exactly string value


## EXAMPLES + Edge cases

-> None Case
    - All terms are equal:  [A, A, A]
    - Not ordered or in alternating : [B, A, B, A]
    - Empty list: []

-> Unique found case
    - All unique: [A, B, C] = A
    - Unique at beginning: [A, B, B, C, D, E, E, D, C] = A
    - Unique at end: [A, C, A, B, E, C, B, E, D] = D
    - Unique at middle: [A, E, A, D, E, B, B] = D

## APPROACH

-> At first glance
    Approach #1
    - go once in the list, adding each to a Map/Dictionary structure {term, count} structure
    - see if a can keep track of lower case count which must be = 1 (I'm not sure if it is possible to avoid a second time to check counts)
    - so in conclusion:
        Being n = number of terms,
        Being t = times to go through term list, first time add to the map and compute count, 2nd time to check if there is only one term with count = 1
        O (n) * t =  ignoring constant we would have a O(n) scenario

    Approach #2
    - get 1 term and check all the other members
    - I would get a O (n^2) scenario, but could get a chance to be faster, if one the first elements are already unique

-> a little thinking about what could make difference:
    - Ordered list? : I guess not because doesn't change the fact that I would need to test all terms.
    - Split list/parallel test? :  Would need to go through each member and merge the results, can help in the first approach idea if multithreading could be considered.
    - What happens with a Huge List? : if would be possible to have a benchmark/test average time results, maybe mix approaches depending on the size of the list.
    - think of best, worst, average and expected scenario(if there is one)

## CODE

-> implement Approach #1 idea of using a Map to see the count
-> Implement Approach #2 idea of using an optimistic search

## OPTIMIZE
-> see if there is a way to avoid the second loop on the map approach #1
-> approach #2 is very straight forward, but should take in consideration the worst case scenario as a base, and what could be done to improve it


#Approach #1 LOG
- seems practical, but not performance friendly, because you must check and retrieve from dictionary based on the key, so there is a cost involved
- spent some time to create an interface, and test suite for the implementations

### TESTS ###

>>> from product_search_approach_1 import ProductSearchApproach1
>>> prod_search_approach1 = ProductSearchApproach1()
>>> find_unique(prod_search_approach1, ['A']) #test 1 element
'A'
>>> find_unique(prod_search_approach1, ['A', 'B', 'C', 'A']) #test second element
'B'
>>> find_unique(prod_search_approach1, []) #test empty list
>>> find_unique(prod_search_approach1, ['D', 'B', 'C', 'A']) #All unique / gets first
'D'
>>> find_unique(prod_search_approach1, ['C', 'D', 'C', 'D']) #No unique
>>> find_unique(prod_search_approach1, ['C', 'C', 'C', 'C']) #All repeated
>>> find_unique(prod_search_approach1, ['A', 'C', 'A', 'B', 'E', 'E', 'B', 'C', 'D']) #Unique at the end
'D'
>>> find_unique(prod_search_approach1, ['A', 'C', 'A', 'B','D', 'E', 'E', 'B', 'C']) #Unique at the middle
'D'

"""
from __future__ import annotations

from product_search import ProductSearch


def find_unique(product_search: ProductSearch, products_list: list[str]):
    return product_search.first_unique_product(products_list)


if __name__ == '__main__':
    print("#####    Unique product search    #######")

    import doctest
    doctest.testmod(verbose=True)



