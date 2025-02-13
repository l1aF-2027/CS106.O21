# BT3 - Solving Knapsack Problems Using Google OR Tools

---

## **1) Solving knapsack with OR-Tools:**  
🔗 [Google OR-Tools Knapsack](https://developers.google.com/optimization/bin/knapsack)  

## **2) Knapsack test instances:**  
🔗 [Knapsack Test Instances](https://github.com/likr/kplib)  

---

Có tổng cộng **13 nhóm test cases** (00-12) cho bài toán knapsack trong link (2).  
Trong bài này, chúng ta sẽ chọn ra **ít nhất 5 test cases** (càng nhiều test cases càng tốt) có kích thước khác nhau  
(**ví dụ:** 50 items, 100 items, 200 items, 500 items, 1000 items...), và giải các test cases này bằng OR Tools.  

### **Các bước thực hiện:**  
1. **Chọn một mốc thời gian tối đa** để giải một bài toán (ví dụ 5 phút là hợp lý).  
2. **Thiết lập thử nghiệm sao cho OR Tools sẽ dừng** khi thời gian tính toán lớn hơn mức đã chọn.  
   - **Hint:** Sử dụng hàm `set_time_limit` của solver hoặc kiểm tra nếu thời gian vượt quá giới hạn cho phép thì dừng thuật toán.  
3. **Lưu lại kết quả của mỗi lần chạy mỗi test case.**  
   - Liệu giải tìm ra có phải giải tối ưu hay không?  
4. **Lập bảng thống kê:**  
   - Tên nhóm test case, giá trị tối ưu, giá trị tìm được, thời gian chạy.  
5. **Dựa vào kết quả thống kê, kết luận:**  
   - **Trong 13 nhóm test cases, nhóm nào khó nhất?**  
   - **Lời giải tìm ra có phải là tối ưu hay không?**  

---

## **Bài nộp gồm 2 file sau đây:**  
1. **1 file zip** (**đặt tên `BT3_MSSV.zip`**) chứa toàn bộ kết quả lưu lại khi chạy test cases.  
2. **1 file PDF báo cáo** (bảng thống kê và nhận xét thời gian thực hiện).  

