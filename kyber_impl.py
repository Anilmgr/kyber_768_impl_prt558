from kyber import Kyber768
import time

def benchmark(func, iterations=1000):
    """
    Benchmark a given function by running it multiple times and measuring average performance.

    Args:
    func (callable): The function to benchmark.
    iterations (int): Number of times to run the function. Default is 1000.

    Returns:
    tuple: A tuple containing:
        - float: Average execution time in milliseconds.
        - float: Operations per second.
    """
    start_time = time.time()
    for _ in range(iterations):
        func()
    end_time = time.time()
    avg_time = (end_time - start_time) / iterations
    return avg_time * 1000, 1 / avg_time  # Return ms and ops/sec

# Benchmark key generation
keygen_time, keygen_ops = benchmark(Kyber768.keygen)

# Generate a single key pair for subsequent operations
pk, sk = Kyber768.keygen()

def encaps():
    """
    Perform Kyber768 encapsulation using the global public key.

    Returns:
    tuple: A tuple containing:
        - bytes: The shared key.
        - bytes: The ciphertext.
    """
    ciphertext, shared_key = Kyber768.enc(pk)
    return shared_key, ciphertext

# Benchmark encapsulation
encaps_time, encaps_ops = benchmark(encaps)

# Generate a single ciphertext and shared key for decryption
shared_key, ciphertext = encaps()


def safe_dec(sk, c):
    """
    Safely perform Kyber768 decapsulation, handling potential errors.

    Args:
    sk (bytes): The secret key.
    c (bytes): The ciphertext.

    Returns:
    bytes or None: The decrypted shared key if successful, None if an error occurs.
    """
    try:
        return Kyber768.dec(c, sk)
    except ValueError as e:
        print(f"Decryption error: {e}")
        return None

# Benchmark decapsulation
decaps_time, decaps_ops = benchmark(lambda: safe_dec(sk, ciphertext))

# Print benchmark results
print(f"Key Generation:  {keygen_time:.2f} ms ({keygen_ops:.2f} ops/sec)")
print(f"Encapsulation:  {encaps_time:.2f} ms ({encaps_ops:.2f} ops/sec)")
print(f"Decapsulation:  {decaps_time:.2f} ms ({decaps_ops:.2f} ops/sec)")

# Print key sizes
print(f"\nKey Sizes:")
print(f"Public key:  {len(pk)} bytes")
print(f"Secret key:  {len(sk)} bytes")
print(f"Ciphertext:  {len(ciphertext)} bytes")
print(f"Shared key:  {len(shared_key)} bytes")

# Verify correctness of the KEM
decrypted_key = safe_dec(sk, ciphertext)
if decrypted_key is not None and shared_key == decrypted_key:
    print("\nDecryption successful!")
else:
    print("\nDecryption failed or error occurred.")