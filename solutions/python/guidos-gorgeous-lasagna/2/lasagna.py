"""
Lasagna cooking time calculator.

This module provides constants and functions to help calculate
the preparation and baking time for a lasagna recipe.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time in minutes."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Return preparation time in minutes (2 minutes per layer)."""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


    
# Example usage
print(EXPECTED_BAKE_TIME)                 # 40
print(bake_time_remaining(30))            # 10
print(preparation_time_in_minutes(2))     # 4
print(elapsed_time_in_minutes(3, 20))     # 26