from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes
import base64

def rsa_key(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    return (e, n), (d, n)

def encrypt(m, key):
    k, n = key
    return pow(m, k, n)

def decrypt(c, key):
    k, n = key
    return pow(c, k, n)

def str_to_int(s):
    return bytes_to_long(s.encode())

def int_to_str(i):
    try:
        return long_to_bytes(i).decode()
    except:
        return str(i)
# 1.
print("1. GENERATE KEYS")
# Case 1
p1, q1, e1 = 11, 17, 7
PU1, PR1 = rsa_key(p1, q1, e1)

# Case 2
p2 = 20079993872842322116151219
q2 = 676717145751736242170789
e2 = 17
PU2, PR2 = rsa_key(p2, q2, e2)

# Case 3 (hex → int)
p3 = int("F7E75FDC469067FFDC4E847C51F452DF", 16)
q3 = int("E85CED54AF57E53E092113E62F436F4F", 16)
e3 = int("0D88C3", 16)
PU3, PR3 = rsa_key(p3, q3, e3)

print("KEYS:")
print("PU1:", PU1)
print("PR1:", PR1)
print("PU2:", PU2)
print("PR2:", PR2)
print("PU3:", PU3)
print("PR3:", PR3)

# 2.
print("\n2. ENCRYPT/DECRYPT M = 5")
M = 5

# Confidentiality
C = encrypt(M, PU1)
M_dec = decrypt(C, PR1)

print("Confidentiality:")
print("Cipher:", C)
print("Decrypted:", M_dec)

# Authentication (signature)
S = encrypt(M, PR1)
M_auth = decrypt(S, PU1)

print("\nAuthentication:")
print("Signature:", S)
print("Verified:", M_auth)

# 3. 
print("\n3. ENCRYPT A MESSAGE")

msg = "TheUniversityofInformationTechnology"
m_int = str_to_int(msg)

C_str = encrypt(m_int, PU1)
C_bytes = long_to_bytes(C_str)
C_b64 = base64.b64encode(C_bytes).decode()

print("Original:", msg)
print("Cipher (Base64):", C_b64)

# 4. DECRYPT ALL CIPHERTEXTS
print("\n4. DECRYPT ALL CIPHERTEXTS")

ciphertexts = [
    "raUcesUlOkx/8ZhgodMoo0Uu18sC20yXlQFevSu7W/FDxIy0YRHMyXcHdD9PBvIT2aUft5fCQEGomiVVPv4I",
    "C87F570FC4F699CEC24020C6F54221ABAB2CE0C3",
    "Z2BUSkJcg0w4XEpgm0JcMExEQmBlVH6dYEpNTHpMHptMQ7NgTHlgQrNMQ2BKTQ==",
    "001010000001010011111111101101110010111011001010111011000110011110111111001111110110100011001111001100001001010001010100111101010100110011101110111011110101101100000100"
]

keys = [PR1, PR2, PR3]

def try_decrypt(c, key):
    try:
        return int_to_str(decrypt(c, key))
    except:
        return None

for idx, ct in enumerate(ciphertexts):
    print(f"\nCiphertext {idx+1}")

    candidates = []

    # Try Base64
    try:
        raw = base64.b64decode(ct)
        c_int = bytes_to_long(raw)
        candidates.append(c_int)
    except:
        pass

    # Try HEX
    try:
        c_int = int(ct, 16)
        candidates.append(c_int)
    except:
        pass

    # Try BINARY
    try:
        c_int = int(ct, 2)
        candidates.append(c_int)
    except:
        pass

    # Try each candidate with each key
    for c_int in candidates:
        for i, key in enumerate(keys):
            result = try_decrypt(c_int, key)
            if result:
                print(f"Key {i+1} →", result)