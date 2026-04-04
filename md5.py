import hashlib
def compare(mess1, mess2):
    ms1 = bytes.fromhex(mess1)
    ms2 = bytes.fromhex(mess2)
    diff = sum(a != b for a, b in zip(ms1, ms2))
    return diff

def md5_hash(message):
    md5 = hashlib.md5()
    return md5.hexdigest()

if __name__ == "__main__":
    mess1 = input("Enter the first message: ")
    mess2 = input("Enter the second message: ")
    compare_result = compare(mess1, mess2)
    print(f"Number of differing bits in the MD5 hashes: {compare_result}")
    print(f"MD5 hash of the first message: {md5_hash(mess1)}")
    print(f"MD5 hash of the second message: {md5_hash(mess2)}")
    