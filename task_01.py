#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01, Week 14"""

import pet


class Dog(pet.Pet):
    """Class is a Dog pet, subclassed from pet.Pet
    Attributes:
        None
    """
    def __init__(self, has_shots=False, **kwargs):
        """Constructor for Dog Class.
        Args:
            self.has_shots (Default = False): If dog has shots True.
            **kwargs: Arbitrary Argument.
        Returns:
            None
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
        self.kwargs = kwargs
