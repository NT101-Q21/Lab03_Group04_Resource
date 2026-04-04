import os

def read_hex_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().replace('\n', '').replace(' ', '').strip()
    except FileNotFoundError:
        print(f"[LỖI] Không tìm thấy file: {filename}")
        exit(1)

def main():    
    # print("[*] Đang đọc dữ liệu từ các file...")
    n_hex = read_hex_from_file('modulus.txt')
    S_hex = read_hex_from_file('signature.txt')
    expected_hash = read_hex_from_file('expected_hash.txt')
    
    e = 65537 
    n = int(n_hex, 16)
    S = int(S_hex, 16)

    # print("[*] Đang thực hiện giải mã RSA (EM = S^e mod n)...")
    EM = pow(S, e, n)

    EM_hex = hex(EM)[2:] 

    calculated_hash = EM_hex[-64:]

    # 6. In kết quả và so sánh
    print("-" * 45)
    print(f"Mã băm trích xuất từ chữ ký : {calculated_hash.lower()}")
    print(f"Mã băm gốc (tính từ file)   : {expected_hash.lower()}")
    print("-" * 45)

    if calculated_hash.lower() == expected_hash.lower():
        print("Xác minh thành công! Chữ ký hợp lệ, chứng chỉ không bị giả mạo.")
    else:
        print("Xác minh thất bại! Chữ ký không khớp.")

if __name__ == "__main__":
    main()