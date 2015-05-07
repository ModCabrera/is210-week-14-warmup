#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports data module, Returns total cost per item, Total Costs"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Returns Dictionary with fruits and total cost per item.
    Args:
    Returns:
    Examples:
        >>> get_cost_per_item({'Lime': 12,
                   'Red Pear': 4,
                   'Peach': 24,
                   'Beet': 1
                   })
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {fruit: (count*FRUIT[fruit]) for fruit, count in shoplist.iteritems()
            if fruit in FRUIT}


def get_total_cost(shoplist):
    """Returns Dictionary with fruits and total cost per item.
    Args:
        cart (dict)= Cost per Item.
        total (float)= Total cost for all items in cart.
    Returns:
        total (float) = Total cost for items in cart.
    Examples:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    cart = get_cost_per_item(shoplist)
    total = sum(item for item in cart.values())
    return total
