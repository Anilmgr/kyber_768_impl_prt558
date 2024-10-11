import pytest
from kyber import Kyber768
import pytest_html

# Fixture to generate a key pair for use in multiple tests
@pytest.fixture
def key_pair():
    return Kyber768.keygen()

# Test to verify the correct sizes of public and secret keys
def test_key_sizes(key_pair):
    pk, sk = key_pair
    assert len(pk) == 1184, "Public key should be 1184 bytes"
    assert len(sk) == 2400, "Secret key should be 2400 bytes"

# Test the full encapsulation and decapsulation process
def test_encapsulation_decapsulation(key_pair):
    pk, sk = key_pair
    # Perform encapsulation
    ciphertext, shared_key_enc = Kyber768.enc(pk)
    # Perform decapsulation
    shared_key_dec = Kyber768.dec(ciphertext, sk)

    # Check ciphertext and shared key sizes
    assert len(ciphertext) == 1088, "Ciphertext should be 1088 bytes"
    assert len(shared_key_enc) == 32, "Shared key should be 32 bytes"
    # Verify that encapsulated and decapsulated keys match
    assert shared_key_enc == shared_key_dec, "Encapsulated and decapsulated keys should match"

# Test decapsulation with an incorrect secret key
def test_decapsulation_with_wrong_key(key_pair):
    pk, _ = key_pair
    # Generate a different key pair
    _, wrong_sk = Kyber768.keygen()
    # Encapsulate with the original public key
    ciphertext, shared_key_enc = Kyber768.enc(pk)
    # Attempt to decapsulate with the wrong secret key
    wrong_shared_key = Kyber768.dec(ciphertext, wrong_sk)
    # Verify that the decrypted key is different from the original shared key
    assert wrong_shared_key != shared_key_enc, "Decrypted key and Shared Key should be different"

# Test multiple encapsulations with the same public key
def test_multiple_encapsulations(key_pair):
    pk, _ = key_pair
    # Perform two separate encapsulations
    ciphertext1, shared_key1 = Kyber768.enc(pk)
    ciphertext2, shared_key2 = Kyber768.enc(pk)

    # Verify that the results are different each time
    assert ciphertext1 != ciphertext2, "Ciphertexts should be different"
    assert shared_key1 != shared_key2, "Shared keys should be different"

# Benchmark the performance of key functions
def test_benchmark_functions():
    from kyber_impl import benchmark, encaps, safe_dec

    # Benchmark key generation
    keygen_time, keygen_ops = benchmark(Kyber768.keygen)
    assert keygen_ops > 0, "Key generation operations per second should be positive"

    # Benchmark encapsulation
    encaps_time, encaps_ops = benchmark(encaps)
    assert encaps_ops > 0, "Encapsulation operations per second should be positive"

    # Benchmark decapsulation
    pk, sk = Kyber768.keygen()
    ciphertext, _ = Kyber768.enc(pk)
    decaps_time, decaps_ops = benchmark(lambda: safe_dec(sk, ciphertext))
    assert decaps_ops > 0, "Decapsulation operations per second should be positive"