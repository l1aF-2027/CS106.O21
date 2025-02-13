# BT1 - DFS/BFS/UCS for Sokoban 

---

## Chào cả lớp,  

Trong bài tập 01 này chúng ta sẽ cài đặt thuật toán BFS và UCS để chơi game Sokoban. **Đây là bài tập cá nhân.**  

- Chúng ta sẽ cài đặt 2 hàm `breadthFirstSearch(gameState)` và `uniformCostSearch(gameState)` trong file `solver.py`. Hiện nay trong code đã có sẵn code gợi ý cài thuật toán DFS. Các em có thể tham khảo để tìm hiểu cách cài BFS và UCS tương tự (nhưng cũng có thể cài theo cách khác).  
- Để thay đổi thuật toán chạy thì cần **comment/uncomment** các dòng lệnh tương ứng trong hàm `auto_move()` trong file `game.py`.  

---

## **Lưu ý:**
- Sau khi cài đặt Python, cần cài đặt thêm **pygame** và **pyautogui** bằng:  `pip install pygame` và `pip install pyautogui` trong command line. (Thử **Python 3.6.2** nếu các phiên bản khác không hoạt động).  
- Chạy game bằng dòng lệnh:  `python Sokoban.py`
  

---

## **Bài nộp gồm có 2 file:**
1. **1 file zip chứa toàn bộ source code.**  
 - Trong đó, các dòng lệnh của 2 hàm `breadthFirstSearch` và `uniformCostSearch()` cần được **chú thích (comment) đầy đủ ý nghĩa của từng dòng lệnh**.  
 - **Đặt tên file:** `BT1_MSSV.zip` với **MSSV là mã số sinh viên**.  

2. **1 file PDF báo cáo:**  
 - Trình bày lại việc áp dụng các thuật toán tìm kiếm DFS, BFS, UCS cho Sokoban như thế nào.  
 - **Đặt tên file:** `BT1_MSSV.pdf` với **MSSV là mã số sinh viên**.  
 - **Báo cáo cần trả lời các câu hỏi sau:**  
   - **Mô tả Sokoban đã được mô hình hóa ra sao?**  
     - Trạng thái khởi đầu, trạng thái kết thúc, không gian trạng thái, các hành động hợp lệ, hàm tiến triển (successor function) là gì?  
   - **Bảng thống kê về độ dài đường đi (số bước đi) tìm được bởi 3 thuật toán DFS, BFS, UCS tại tất cả các bản đồ có sẵn.**  
     - Các em có nhận xét thế nào về lời giải (đường đi) tìm ra bởi mỗi thuật toán?  
     - Thuật toán nào là tốt hơn cả?  
     - Trong các bản đồ thì bản đồ nào khó giải nhất, tại sao?  
   - **Lưu ý:**  
     - Đối với **UCS**, trong `solver.py` đã có cài đặt sẵn 1 hàm tính chi phí `cost`.  
     - Khi gọi `cost(node_action[1:])`, chi phí đường đi là số bước đi **không dịch chuyển box**.  

---

## **Lưu ý quan trọng:**
- **File báo cáo không phải là PDF sẽ bị trừ 10/100 điểm.**  
- Báo cáo phải viết **cẩn thận, rõ ràng, mạch lạc**.  
- Cần **tự thiết kế cách trình bày** sao cho gọn gàng, sạch sẽ. Không nên dài quá **10 trang**.  
- **Tất cả bài làm có dấu hiệu sao chép sẽ nhận 0 điểm.**  

