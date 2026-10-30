---
name: creer-cartes-expressions
description: Tạo, chỉnh và mở rộng mặt trước minh họa và mặt bìa in hai mặt của thẻ board game thành ngữ tiếng Pháp từ danh sách, index hoặc tài liệu nguồn; giữ số gốc, minh họa nghĩa đen, rà lỗi cắt ảnh và xuất PDF chất lượng in với 10 thẻ đồng kích thước trên A4 ngang. Dùng cho bộ 150 expressions françaises hoặc bộ thẻ tương tự.
---
# Thẻ board game – Expressions françaises

## 1. Khóa nguồn và phạm vi
- Đọc nguồn mới nhất và lập manifest gồm `id`, `text`, `source_page`, `theme`; giữ nguyên số gốc, dấu tiếng Pháp và câu thành ngữ. Không đánh số lại theo chủ đề.
- Phân biệt mặt trước minh họa, mặt bìa chung và thẻ QCM. Với mặt trước minh họa, chỉ in số gốc và câu; bỏ số trang, định nghĩa và bản dịch. Không tự chuyển yêu cầu này sang QCM.
- Nếu người dùng yêu cầu thẻ QCM, xác minh nguồn đáp án và dùng định dạng riêng ở [references/qcm.md](references/qcm.md).
- Khi sửa một bộ đã có, giữ nội dung và tranh đã duyệt, chỉ sửa trong phạm vi yêu cầu; dùng đúng bản mới nhất, không quay lại bản cũ có lỗi cắt.
- Với bộ mới chưa duyệt phong cách, làm mẫu 10 thẻ đa dạng trước. Khi người dùng đã yêu cầu cả bộ hoặc đã duyệt, tiếp tục đủ số lượng, không hỏi duyệt lại.
- Đọc [references/design.md](references/design.md) để dùng thiết kế đã chốt; ưu tiên chỉ dẫn mới của người dùng nếu khác.

## 2. Lập ý tưởng nghĩa đen
- Với từng câu, xác định danh từ, hành động, số lượng và quan hệ không gian theo NGHĨA ĐEN trước khi tạo ảnh; lưu ý tưởng cùng manifest.
- Ví dụ: `Avoir deux mains gauches` phải có hai bàn tay trái, không thay bằng cảnh vụng về làm vỡ cốc; kiểm tra chiều ngón cái theo tư thế thật, không chấp nhận một cặp tay trái/phải thông thường.
- Ví dụ: `Être bien dans ses baskets` phải gợi trực tiếp việc ở bên trong đôi giày; không chỉ vẽ người tự tin mang giày.
- Không đánh đồng một tranh đẹp với một tranh đúng. Sửa các chi tiết làm sai nghĩa đen; tránh hình ảnh gây tổn thương hoặc phản cảm.

## 3. Tạo và đồng bộ minh họa
- Dùng imagegen theo skill liên quan; dùng tranh đã duyệt làm tham chiếu về nhân vật, nét vẽ và bảng màu. Giữ nhân vật, bối cảnh khi người dùng chỉ yêu cầu đổi màu.
- Dùng phong cách truyện tranh minh họa sách giáo khoa THPT: nét rõ, dễ nhận diện, nền trắng, cảnh vừa đủ; tránh thay phong cách tùy từng thẻ.
- Dùng màu tươi sáng vừa phải: xanh lam, xanh ngọc, san hô và điểm vàng ấm; giảm bóng tối và mảng nền kín. Giữ tương phản đường nét để in đen trắng vẫn đọc được.
- Không tạo chữ trong ảnh. Dàn câu bằng chữ vector để bảo đảm dấu tiếng Pháp và độ sắc nét.
- Ưu tiên ảnh riêng; nếu dùng atlas, chừa khoảng trắng giữa các cảnh và quanh chủ thể. Giữ bản ảnh gốc, không ghi đè bằng bản nén nhẹ.

## 4. Cắt và kiểm tra từng ảnh
- Không mặc định các ô atlas có ranh giới chia đều. Tìm khoảng trắng thực tế, lưu tọa độ cắt riêng theo số gốc.
- Kiểm tra bốn mép ở cỡ đủ lớn: giữ đủ đầu/tóc, tai/sừng, bàn tay, bàn chân và vật thể quyết định nghĩa đen; không để mảnh hình bên cạnh lọt vào.
- Chỉ bỏ khoảng trắng thừa sau khi biết đâu là nội dung. Không tự động xén cùng một lượng cho mọi ảnh, không cắt để che lỗi thiếu hình.
- Nếu nguồn đã mất hình hoặc hai cảnh không thể tách sạch, tạo lại riêng ảnh đó bằng imagegen. Không phóng ảnh hay thêm viền trắng rồi tuyên bố đã khôi phục phần mất.
- Tạo trang kiểm tra có số cho TOÀN BỘ ảnh; xem lại ảnh nghi vấn riêng. Chỉ đưa ảnh đã kiểm tra vào `assets/001.png`, v.v.

## 5. Dàn 10 thẻ đồng kích thước trên A4
- Dùng A4 ngang 297 × 210 mm, 5 cột × 2 hàng; thẻ 54,2 × 98 mm; lề ngoài 5 mm; khe giữa thẻ 4 mm. Dàn đều toàn trang; mẫu 10 thẻ này thay thế mẫu 8 thẻ và tỷ lệ 9:16 cũ.
- Dùng thẻ trắng, khung xám mờ bo góc, vùng an toàn tối thiểu 2 mm. Giữ ảnh đúng tỷ lệ, không kéo giãn để lấp thẻ.
- Phóng từng tranh tối đa trong vùng cho phép; không để tranh nhỏ vì khoảng trắng trong file. Cân bằng thị giác giữa các thẻ.
- Đặt số và toàn bộ câu IN ĐẬM ngay dưới tranh, cách nét tranh 3–4 mm. Căn giữa cả cụm tranh + khoảng cách + chữ theo chiều ngang và chiều dọc; không neo chữ sát đáy.
- Với thẻ expression minh họa, ưu tiên mới: chữ đậm 20 pt, tối đa hai dòng, ngay dưới tranh. Đây là mục tiêu cần thử trên kích thước in thật, không phải bảo đảm mọi câu đều vừa. Đo các câu dài nhất với font thật và vùng an toàn; nếu không vừa, trình mẫu đề xuất cỡ nhỏ hơn hoặc điều chỉnh bố cục để người dùng chốt. Không cắt câu, thêm dòng thứ ba hay ép ngang quá mức để tuyên bố đạt 20 pt. Bản 12 pt trước đây là mẫu lịch sử, không tự áp lại thay chỉ dẫn mới.
- Đặt dấu cắt nhỏ ngoài thẻ, tránh chồng dấu trong khe 4 mm. Không đặt dòng thông tin kỹ thuật chiếm diện tích in hoặc chồng lên thẻ.
- Dùng `python3 scripts/render_cards.py WORKSPACE OUTPUT.pdf`; WORKSPACE chứa `manifest.json` và `assets/NNN.png`. Script không kiểm định được nghĩa đen hoặc lỗi cắt, phải kiểm tra ảnh trước.

## 6. Thiết kế mặt bìa và in hai mặt
- Phân biệt hai loại bìa theo yêu cầu mới: QCM dùng atisô trong trái tim; thẻ expression dùng tranh tổng hợp hoặc ảnh người dùng cung cấp. Dùng hướng dẫn ở [references/card-back.md](references/card-back.md). Với phong cách bìa mới, tạo trước một ảnh để người dùng xem; khi đã duyệt, dàn trang mà không tạo lại ảnh làm thay đổi mẫu.
- Tiêu đề bìa ưu tiên 30 pt, đậm; đo font thật trên thẻ 54,2 mm trước khi xuất. Nếu không vừa hai dòng `Expressions` / `françaises`, trình mẫu cỡ nhỏ hơn hoặc font gọn hơn để chốt; không âm thầm thu nhỏ hay làm biến dạng chữ.
- Giữ cùng tọa độ tâm và ô thẻ với mặt trước: 54,2 × 98 mm, 5 cột × 2 hàng trên A4 ngang. Dùng ảnh đúng tỷ lệ, không tự cắt khoảng trắng đã duyệt hoặc kéo giãn hình.
- Gọi thống nhất hai mặt là “mặt bìa” và “mặt nội dung”; mặt nội dung QCM có câu hỏi và ba lựa chọn, mặt nội dung expression có tranh và câu thành ngữ.
- Lặp đúng 10 bản bìa giống nhau; nền trắng, không viền/khung để giảm cảm giác lệch khi in hai mặt. Chừa khoảng an toàn quanh chữ và biểu tượng.
- Xuất một trang bìa dùng lại cho 15 tờ mặt trước; chỉ lặp thành 15 trang hoặc ghép xen kẽ trước/sau khi người dùng cần file in hoàn chỉnh.
- Kiểm tra kích thước trang, lề và tâm 10 ô trùng với mặt trước. Bìa giống nhau không cần đảo thứ tự cột; không lật gương chữ/hình. Nếu mặt sau mang nội dung riêng theo từng thẻ, xác định cách lật giấy để ghép đúng cặp.
- Hướng dẫn in A4 ngang, `Actual size / 100%`, không co giãn; với bộ trước/sau cùng chiều dùng lật cạnh ngắn. Khuyên in thử một tờ để kiểm tra hướng và sai lệch máy in; không bảo đảm khớp cơ học tuyệt đối.

## 7. Kiểm định và giao file
- Áp dụng skill PDF và đánh dấu thao tác trước khi xuất. Render mọi trang; kiểm tra không che/cắt tranh hoặc chữ, không lẫn cảnh, đủ số thẻ và số gốc, đúng thứ tự.
- Với 150 thẻ: xuất đúng 15 trang, mỗi trang đủ 10 thẻ theo thứ tự trái sang phải, hàng trên rồi hàng dưới. Không lặp hoặc bỏ thẻ.
- Kiểm tra độ phân giải HIỆU DỤNG ở kích thước in: mục tiêu ít nhất 300 ppi. Giữ nguyên ảnh nếu đủ; với ảnh nhỏ, tạo lại độ phân giải cao khi cần. Nội suy không tạo thêm chi tiết thật.
- Giữ chữ vector và nhúng font; giữ ảnh gốc hoặc nén không mất dữ liệu. Không dùng bản 150 dpi/ebook làm bản chất lượng in. Nếu cần bản tải nhẹ, tạo riêng và ghi rõ đó là bản nhẹ.
- Lưu PDF hoàn chỉnh và PNG xem trước theo skill Library; cập nhật đúng file đã có, không tạo bản trùng không cần thiết. Dùng cơ chế đính kèm trực tiếp khi các đường dẫn cũ không tải được; không lặp lại cùng link lỗi và khẳng định đã sửa.
- Giao file kèm kích thước thẻ, số thẻ/trang, hướng dẫn `100% / Actual size`, không `Fit to page`. Không khẳng định đã kiểm tra đủ ảnh/trang nếu mới xem mẫu.
