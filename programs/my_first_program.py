from nada_dsl import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the GCD of my_int1 and my_int2 using the Euclidean algorithm
    result = gcd(my_int1, my_int2)

    # Return the output with the computed result
    return [Output(result, "gcd_output", party1)]
