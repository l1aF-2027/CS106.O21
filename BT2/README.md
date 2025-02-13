# BT2 - Heuristics & A* search
---

## Chào cả lớp,  

Chúng ta tiếp tục giải các game Sokoban như trong BT1. Trong bài tập này chúng ta cần cài đặt thuật toán A* và so sánh hiệu suất của A* với UCS.  

---

## **Một số lưu ý như sau:**  
- Hiện tại trong code mẫu định kèm đã cài sẵn một hàm heuristic. Các em có thể sử dụng hoặc tự thiết kế các heuristic khác tốt hơn.  
- Hoàn thành cài đặt thuật toán A* trong hàm `starSearch` trong file `solver.py` (lưu ý sử dụng cấu trúc dữ liệu tự định nghĩa).  
- Để thay đổi thuật toán chạy thì cần **comment/uncomment** các dòng lệnh tương ứng trong hàm `auto_move()` trong file `game.py`.  
- Cài đặt **đo thời gian** chạy của mỗi thuật toán (**UCS và A***). (Gợi ý: Sử dụng `time()` để đo xem thuật toán tốn bao nhiêu thời gian (tính theo số giây) để giải mỗi màn chơi).  

---

## **Bài nộp gồm có 2 file:**
1. **1 file zip** chứa source code trong đó cài đặt UCS và A* với **comment chi tiết** mô tả thuật toán.  
   - **Đặt tên file:** `BT2_MSSV.zip` với **MSSV là mã số sinh viên**.  
   
2. **1 file PDF báo cáo:**  
   - Trình bày lại **heuristics đã sử dụng** và thử nghiệm so sánh thêm với **heuristics mới** thì sẽ **được cộng điểm**  
     (**Cần phải so sánh với heuristics đang có trong code mẫu**).  
   - Trong file báo cáo cần có **Bảng thống kê** so sánh **thời gian chạy** của thuật toán UCS và A* cho mỗi level.  
   - Cần trả lời câu hỏi: **Lời giải trả về của A* có phải lời giải tối ưu hay không theo lý thuyết không?**  

---

## **Lưu ý:**  
- **File báo cáo không phải là PDF sẽ bị trừ 10/100 điểm.**  
- Báo cáo phải viết **cẩn thận, rõ ràng, mạch lạc**.  
- Cần **tự thiết kế cách trình bày** sao cho gọn gàng, sạch sẽ. Không nên dài quá **10 trang**.  

---

## **Deadline:**  
- **31/03/2024**.  
- **Sau ngày 3/4/2024 nộp bài sẽ bị trừ điểm dần dần. Sau ngày 7/4/2024 sẽ không chấm bài nộp mới.**  
