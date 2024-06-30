from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the product of my_int1 and my_int2
    result = my_int1 * my_int2

    # Return the output with the computed result
    return [Output(result, "product_output", party1)]
