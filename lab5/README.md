# Nhập Môn Xử Lý Ảnh Số - Lab 5 - Lý Thuyết + Bài Tập
# PHÂN VÙNG ẢNH (PHÂN VÙNG THEO HISTOGRAM/REGION) - BIẾN ĐỔI ĐỐI TƯỢNG TRONG ẢNH
Sinh viên thực hiện: Trần Nghiêm Nhật Thiện
MSSV: 2174802010938
Môn học: Nhập môn Xử lý ảnh số
Giảng viên: Đỗ Hữu Quân
# Giới thiệu
Bài lab này nhằm mục đích giúp sinh viên có thể viết các chương trình phân vùng ảnh theo Histogram/Region hoặc chương trình biến đổi đối tượng trong ảnh 
# Công nghệ sử dụng
- Visual Studio Code, (Jupyer Notebook)
- Kernel: Python 
- Ngôn ngữ: Python (JSON file đuôi .ipynb)
- Thư viện: OpenCV, Numpy, Os, Matplotlib, v.v.

# `PIP INSTALL OPENCV-PYTHON`

# Chi tiết một số phép biến đổi - công thức và ví dụ:
# Xử lý Ảnh với OpenCV 

## Geometric Transformation (Biến đổi hình học)

Các phép biến đổi này thay đổi vị trí, kích thước hoặc hình dạng của ảnh gốc.

| Phép biến đổi         | Ý nghĩa                                                  | Công thức toán học                                          | Ví dụ đơn giản                               |
|-----------------------|-----------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------|
| **Coordinate Mapping**| Ánh xạ lại điểm ảnh, ví dụ đảo ngược màu                 | `I'(x, y) = 255 - I(x, y)`                            | Chuyển vùng sáng → vùng tối và ngược lại     |
| **Rotate**            | Xoay ảnh quanh tâm                                       | ![Rotate formula](https://latex.codecogs.com/png.image?\dpi{120}&space;M=\begin{bmatrix}\cos\theta&-\sin\theta&t_x\\\sin\theta&\cos\theta&t_y\end{bmatrix}) | Xoay ảnh 45° theo chiều kim đồng hồ         |
| **Scale**             | Phóng to hoặc thu nhỏ ảnh                                | `I'(x, y) = I(s_x * x, s_y * y)`               | Giảm kích thước ảnh xuống còn 50%            |
| **Shift**             | Tịnh tiến ảnh theo trục x và y                           | ![Shift formula](https://latex.codecogs.com/png.image?\dpi{120}&space;M=\begin{bmatrix}1&0&\Delta%20x\\0&1&\Delta%20y\end{bmatrix})  | Dời ảnh sang phải và xuống 50 pixels        |

---

## Segment (Phân đoạn ảnh)

Phân đoạn ảnh tách các vùng quan tâm khỏi nền, tăng độ tương phản đối tượng.

| Phép biến đổi            | Ý nghĩa                                                       | Công thức toán học mô phỏng                             | Ví dụ minh họa                            |
|--------------------------|---------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| **Adaptive Thresholding**| Áp ngưỡng cục bộ cho từng vùng trên ảnh xám                  | Ngưỡng tính theo trung bình trong vùng lân cận           | Phân biệt nền không đều, ví dụ ảnh văn bản |
| **Binary Dilation**      | Giãn vùng trắng trong ảnh nhị phân                            | `A ⊕ B = { z | (B)_z ∩ A ≠ ∅ }`                           | Làm nổi bật đối tượng trắng               |
| **Binary Erosion**       | Thu hẹp vùng trắng, loại bỏ nhiễu                             | `A ⊖ B = { z | (B)_z ⊆ A }`                              | Xóa điểm trắng nhỏ không mong muốn        |
| **Otsu Thresholding**    | Tự động chọn ngưỡng tối ưu dựa trên phân bố histogram        | Dựa vào tối ưu độ lệch giữa các lớp                       | Phân đoạn đối tượng sáng khỏi nền tối      |

---

# Ghi chú: Các hàm `cv2.imread`, `cv2.cvtColor`, `cv2.getRotationMatrix2D`, `cv2.warpAffine`, `cv2.resize`, `cv2.adaptiveThreshold`,`cv2.threshold`,`cv2.dilate`,`cv2.erode`, `plt.figure`, `plt.imshow()`, `plt.axis()`, `plt.show()` được dùng trong toàn bộ quá trình xử lý ảnh. Bởi vì sử dụng thư viện Matplotlib cũng như OpenCV cho các công thức/hình ảnh hoạt động nên các hàm trên được sử dụng để thực thi code

# Tài liệu tham khảo thêm :
- [Geometric Transformation in Image Processing](https://www.geeksforgeeks.org/electronics-engineering/geometric-transformation-in-image-processing-1/)
- [OpenCV Adaptivethreshold](https://pyimagesearch.com/2021/05/12/adaptive-thresholding-with-opencv-cv2-adaptivethreshold/)
- [Google](https://www.google.com/)
- Slide bài giảng Nhập môn Xử lý ảnh số - Văn Lang University
