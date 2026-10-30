# creer-cartes-expressions

Skill tạo thẻ board game **Expressions françaises** từ danh sách, Word, PDF hoặc hình ảnh; hỗ trợ thẻ minh họa nghĩa đen và thẻ QCM với ba lựa chọn, một đáp án đúng.

Bố cục **10 thẻ/A4 ngang, 5 × 2**; mỗi thẻ **54,2 × 98 mm**, khe **4 mm**, lề ngoài **5 mm**. Minh họa phong cách sách giáo khoa, nền trắng; chữ đậm ngay dưới tranh. Bìa không khung, đồng bộ vị trí để in hai mặt.

Quy trình gồm trích xuất nội dung, giữ số gốc, tạo mẫu duyệt, sản xuất hàng loạt, kiểm tra tiếng Pháp và lỗi cắt ảnh, rồi xuất PDF để in **100% / Actual size**.

## Sử dụng

Đọc [SKILL.md](SKILL.md), hướng dẫn trong `references/` và công cụ trong `scripts/`.

Ví dụ: « Dùng skill này tạo trước 10 thẻ expression từ tài liệu đính kèm để tôi duyệt. »

Python: `reportlab`, `Pillow`, `numpy`; script mặc định dùng font DejaVu Sans Bold trên Linux. Cần công cụ tạo ảnh cho minh họa mới và công cụ render PDF để kiểm tra.
