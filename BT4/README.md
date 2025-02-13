
# BT4 - Evaluation functions for Minimax/AlphaBeta/Expectimax 
---

## **Nội dung bài tập:**
Trong bài tập này, chúng ta chủ yếu thực hành trong file `multiAgents.py` với các nội dung sau:  
- **Minimax** (trong source code tham khảo đính kèm đã có sẵn đoạn 2 phiên bản).  
- **Minimax với Alpha-Beta pruning**.  
- **Expectimax** (xem như các ghost agents lựa chọn hành động với xác suất ngẫu nhiên đồng đều).  
- **Thiết kế hàm lượng giá (evaluation function)** để ước lượng giá trị trạng thái (source code tham khảo có sẵn hàm `betterEvaluationFunction`).  
  - ⚠️ **Nếu không thiết kế hàm `betterEvaluationFunction` mới mà chỉ sử dụng hàm có sẵn thì sẽ không đạt tối đa điểm.**  

---

## **Chạy pacman với các tùy chọn sau đây:**
- **Tự tương tác điều khiển:**  
  ```bash
  python pacman.py
  ```
- **Tự tương tác điều khiển một chế độ layout tùy chọn** (sử dụng thêm `-l flag`):  
  ```bash
  python pacman.py -l trickyClassic
  ```
- **Chạy một thuật toán nào đó** (sử dụng `-p flag`):  
  ```bash
  python pacman.py -l mediumClassic -p ExpectimaxAgent
  ```
- **Chạy một thuật toán với một độ sâu giới hạn:**  
  ```bash
  python pacman.py -l mediumClassic -p MinimaxAgent -a depth=3
  ```
- **Chạy một thuật toán với một hàm lượng giá tùy chỉnh:**  
  ```bash
  python pacman.py -l mediumClassic -p MinimaxAgent -a depth=3,evalFn=betterEvaluationFunction
  ```
- **Thiết lập random seed để chạy nhiều lần giống nhau:**  
  ```bash
  python pacman.py -p MinimaxAgent -a depth=3,evalFn=betterEvaluationFunction -s 2252000
  ```
- **Chạy thời gian ngắn hơn:**  
  ```bash
  python pacman.py -frameTime 0
  ```
- **Tham khảo thêm các tùy chỉnh khác bằng lệnh:**  
  ```bash
  python pacman.py -h
  ```

---

## **Yêu cầu nộp bài (2 files: `BT4_MSSV.pdf`, source code `BT4_MSSV.zip`)**
1. **File zip chứa source code.**  
   - File pdf báo cáo **mô tả ý tưởng/chiến thuật đánh giá trạng thái**.  
   - **Những đặc trưng chính** sử dụng để **ước lượng giá trị trạng thái** là gì?  
   - **Trọng số của các đặc trưng đó như thế nào?** **Tại sao?**  

2. **Submit 1 video record lại 1 ván chơi**  
   - Link video (Google Drive) cần phải **public access** để chấm bài.  

3. **Bảng thống kê kết quả:**  
   - **So sánh giữa các thuật toán Minimax, AlphaBeta, Expectimax.**  
   - So sánh với `scoreEvaluationFunction` trong đó chỉ sử dụng điểm số của trạng thái để ước lượng giá trị trạng thái.  
   - **Hiệu năng và hiểu quả của Minimax vs AlphaBeta vs Expectimax**.  
   - **Chạy trên 2 maps khác nhau**, mỗi map **chạy thử nghiệm ít nhất 5 lần** (mỗi lần có random seed khác nhau).  

4. **Cụ thể:**  
   - **Đối với `scoreEvaluationFunction`**, chạy Minimax, AlphaBeta và Expectimax **5 lần trên 1 map** với **random seed từ `MSSV+0` đến `MSSV+4`**.  
   - **Đối với `betterEvaluationFunction`**, chạy Minimax, AlphaBeta và Expectimax **5 lần trên 1 map** với **random seed từ `MSSV+0` đến `MSSV+4`**.  