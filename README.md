# Lab03_Group04_Resource

## MỤC TIÊU
- Hiểu và vận dụng thuật toán RSA: Nắm vững nguyên lý sinh khóa, mã hóa (đảm bảo tính bảo mật) và ký số (đảm bảo tính xác thực).
- Phân tích đặc tính hàm băm: Đánh giá tính chất của các thuật toán MD5, SHA-1 và khả năng chống xung đột (collision resistance) của chúng.
- Thực hành xác thực chứng chỉ số: Hiểu quy trình kiểm tra tính toàn vẹn và nguồn gốc của chứng chỉ X.509 thông qua chữ ký số.

## NỘI DUNG
1. Mã hóa bất đối xứng RSA (Nhiệm vụ 2.1)
- Sinh khóa: Lập trình tạo cặp khóa công khai $PU(e, n)$ và khóa riêng $PR(d, n)$ từ các số nguyên tố đầu vào $p, q$ và số mũ $e$.
-  Mã hóa & Giải mã: Thực hiện mã hóa thông điệp số ($M=5$) và thông điệp chuỗi văn bản bằng khóa công khai, sau đó giải mã bằng khóa riêng để kiểm tra tính bảo mật.
- Xác thực (Ký số): Thử nghiệm dùng khóa riêng để ký và dùng khóa công khai để xác minh.Phá mã thử nghiệm: Xây dựng vòng lặp để thử giải mã các bản mã khác nhau (định dạng Base64, Hex, nhị phân) với các cặp khóa đã tạo.

2. Đánh giá tính chất hàm băm (Nhiệm vụ 2.2)
- So sánh thông điệp: Viết code so sánh sự khác biệt giữa hai thông điệp dựa trên số byte khác nhau.
- Kiểm tra xung đột: Sử dụng các công cụ trên Linux để chứng minh rằng hai file khác nhau có thể cho ra cùng một giá trị băm MD5 hoặc SHA-1.

3. Tạo xung đột MD5 (Nhiệm vụ 2.3)
- Sử dụng công cụ md5collgen: Tạo ra hai tệp tin nhị phân có cùng giá trị băm MD5 dù nội dung dữ liệu khác nhau.
- Phân tích khối dữ liệu: Quan sát cách thuật toán xử lý theo từng khối 64 byte và cách công cụ tự động thêm byte đệm (padding) nếu tệp tiền tố không đủ độ dài.

4. Xác minh chứng chỉ X.509 (Nhiệm vụ 2.4)
- Trích xuất dữ liệu: Tải chứng chỉ từ máy chủ, trích xuất Modulus, Exponent và chữ ký số.
- Phân tích ASN.1: Xác định offset của phần thân chứng chỉ để trích xuất dữ liệu gốc cần xác thực.
- Lập trình xác minh: Viết chương trình Python thực hiện giải mã RSA chữ ký của CA và so sánh mã băm thu được với mã băm của phần thân chứng chỉ để kết luận tính hợp lệ.