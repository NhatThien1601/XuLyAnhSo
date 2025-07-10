# Nhập Môn Xử Lý Ảnh Số - Lab 6 - Lý Thuyết 
# XÁC ĐỊNH ĐỐI TƯỢNG TRONG ẢNH 
- Sinh viên thực hiện: Trần Nghiêm Nhật Thiện
- MSSV: 2174802010938
- Môn học: Nhập môn Xử lý ảnh số
- Giảng viên: Đỗ Hữu Quân
# Giới thiệu
Bài lab này nhằm mục đích giúp sinh viên có thể :
-	Viết được chương trình gán nhãn cho phân vùng ảnh
-	Viết được chương trình phân vùng ảnh theo Region
-	Viết được chương trình thay đổi ảnh

# Công nghệ sử dụng
- Visual Studio Code, (Jupyer Notebook)
- Kernel: Python 
- Ngôn ngữ: Python (JSON file đuôi .ipynb)
- Thư viện: OpenCV, Numpy, Matplotlib, v.v.

# `PIP INSTALL OPENCV-PYTHON`

# Chi tiết một số phép biến đổi - công thức và ví dụ:
# Xử lý Ảnh với OpenCV 

## 2.1.	Gán nhãn ảnh
Đoạn code thực hiện các bước xử lý ảnh nhị phân và phân tích hình học như sau:
1. Đọc ảnh và chuyển sang ảnh xám : 
Sử dụng PIL để mở ảnh và chuyển sang ảnh grayscale
2. Ngưỡng hóa bằng phương pháp Otsu :
- Tự động tìm ngưỡng tối ưu để phân tách nền và vật thể
- Áp dụng ngưỡng để tạo ảnh nhị phân
3. Gán nhãn các vùng liên thông:
Dùng skimage.label để đánh số từng vùng vật thể riêng biệt
4. Chuẩn hóa ảnh nhãn về 0–255:
Biến đổi ảnh nhãn thành ảnh 8-bit để dễ hiển thị và lưu trữ.
5. Lưu ảnh đã gán nhãn
Ghi ảnh kết quả ra file label_output.jpg.
6. Tính toán các thuộc tính hình học:
Sử dụng regionprops để lấy thông tin như sau:
- Diện tích (Area)
- Tâm (Centroid)
- Hộp bao (BoundingBox)
7. Hiển thị ảnh và vẽ hộp bao:
Dùng matplotlib để hiển thị ảnh và vẽ hình chữ nhật quanh từng vật thể

## 2.2 Phát hiện biên bằng phép dịch ảnh -	Dò tìm cạnh theo chiều dọc
1. Đọc ảnh và chuyển sang ảnh xám :
Mở ảnh và chuyển sang ảnh grayscale để xử lý cường độ sáng
Công thức: `$$ I = 0.299R + 0.587G + 0.114B $$`
2. Dịch ảnh sang phải 1 pixel :
Dịch toàn bộ ảnh sang phải 1 pixel (trục x), không nội suy (order=0)
3. Tính độ chênh lệch tuyệt đối giữa ảnh gốc và ảnh đã dịch:
Phát hiện biên theo phương ngang bằng cách lấy hiệu cường độ giữa ảnh gốc và ảnh đã dịch
4. Hiển thị ảnh
Hiển thị ảnh thể hiện các biên sáng tối — nơi có sự thay đổi cường độ mạnh
---

## 2.3 Dò tìm với cạnh Sobel Filter - Phát hiện biên bằng toán tử Sobel
1. Đọc ảnh
2. Tính đạo hàm theo trục dọc/ngang (Ox, Oy)
a = nd.sobel(data, axis=0)
- Ý nghĩa : phát hiện biên theo chiều dọc (thay đổi theo hàng) /chiều ngang (thay đổi theo cột)
- Công thức: Toán tử Sobel theo trục x, y
![Sobel Math]('[sobel_math.jpeg](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c805c831d304af433d5ec82423cf16cf78fa408)')
3. Tổng độ lớn đạo hàm để tạo ảnh biên
bmg = abs(a) + abs(b)
- Kết hợp biên theo cả hai hướng để tạo ảnh biên tổng hợp.
- Công thức :  `Biên(𝑥,𝑦)=∣𝐺𝑥(𝑥,𝑦)∣+∣𝐺𝑦(𝑥,𝑦)∣`
- Ví dụ: Nếu tại một điểm 𝐺𝑥 = 30 , 𝐺𝑦 = 40 → biên = 70

---
## 2.4.	Xác định góc của đối tượng
Sử dụng thuật toán `Harris` để phát hiện điểm góc
def Harris(indata, alpha=0.2):
    ...
    return R
1. Tính đạo hàm theo hai hướng
- Ý nghĩa : tính đạo hàm theo trục x (ngang) và y (dọc) bằng toán tử Sobel.
- Ký hiệu : 
    + 𝐼𝑥 : đạo hàm theo x
    + 𝐼𝑦 : đạo hàm theo y
2. Tính các tích đạo hàm
- Ý nghĩa: Tính các thành phần của ma trận cấu trúc (structure tensor).
- Công thức : 
`𝑀=[𝐼𝑥2 𝐼𝑥𝐼𝑦/𝐼𝑥𝐼𝑦 𝐼𝑦2]`
3. Làm mượt bằng bộ lọc Gaussian
- Làm mượt các thành phần của ma trận M để giảm nhiễu.
4. Tính giá trị phản hồi Harris
- Ý chính: Tính điểm góc dựa trên định thức và dấu vết của ma trận M
- Công thức: 
    + 𝑅=det⁡(𝑀)−𝛼⋅(trace(𝑀))2
Trong đó: 
    + det⁡(𝑀)=𝐼𝑥2𝐼𝑦2−(𝐼𝑥𝐼𝑦)2
    + trace(𝑀)=𝐼𝑥2+𝐼𝑦2
    α : nằm trong khoảng 0.04–0.25 (ở đây là 0.2)

## 2.5.	Dò tìm hình dạng cụ thể trong ảnh với Hough Transform
# 2.5.1.	Dò tìm đường thẳng trong ảnh
`Phát hiện đường thẳng bằng biến đổi Hough`
1. Khởi tạo không gian Hough
- Ý chính: Tạo không gian Hough 2D với:
    + Trục ρ (khoảng cách từ gốc đến đường thẳng)
    + Trục θ (góc nghiêng của đường thẳng, từ 0° đến 89°)
- Công thức: `𝜌=𝑥cos⁡(𝜃)+𝑦sin⁡(𝜃)`
- Ví dụ : Với ảnh 256×256 → bán kính tối đa 𝑅 = 256 2 + 256 2 ≈ 362
2. Tạo bản sao ảnh và mảng góc
- Ý nghĩa : 
    + w: bản sao ảnh để xử lý
    + theta: mảng góc từ 0 đến 89 độ (đổi sang radian)
    + tp: chỉ số góc để truy cập mảng Hough
3. Lặp qua các điểm ảnh có giá trị lớn hơn ngưỡng
- Ý nghĩa : Duyệt qua các điểm ảnh có cường độ lớn hơn gamma (ngưỡng)
- Ví dụ: Nếu gamma = 0.5, chỉ xét các điểm có giá trị ≥ 0.5
4. Tính giá trị ρ cho từng θ và cập nhật không gian Hough
- Ý nghĩa : Tìm điểm ảnh có giá trị lớn nhất, tính các giá trị ρ tương ứng với từng góc θ
- Công thức : `𝜌=𝑥cos⁡(𝜃)+𝑦sin⁡(𝜃)`
- Ví dụ : Với điểm (x=128, y=128), tính ρ cho mọi θ từ 0° đến 89°
5. Cộng dồn vào không gian Hough
- Ý nghĩa : Với mỗi cặp (ρ, θ), cộng giá trị điểm ảnh vào không gian Hough.
- Ví dụ: Nếu điểm tại (128,128) có giá trị 1, nó sẽ góp phần vào nhiều đường thẳng trong không gian Hough
Lưu ý : `Nếu ảnh gốc có một điểm duy nhất tại (128,128), không gian Hough sẽ là một đường cong sin.`
# 2.5.2.	Dò tìm đường tròn trong ảnh
`Phát hiện điểm góc bằng corner_harris (Scikit-Image)`
1. Đọc ảnh và chuyển sang ảnh xám
- Ý chính: Đọc ảnh màu và chuyển sang ảnh xám để xử lý cường độ sáng
- Công thức chuyển đổi: `𝐼=0.2125𝑅+0.7154𝐺+0.0721𝐵`
- Ví dụ: Pixel màu (255, 0, 0) → xám ≈ 0.2125 (giá trị chuẩn hóa từ 0 đến 1)
2. Phát hiện điểm góc bằng Corner Harris
- Ý chính: Tính bản đồ phản hồi điểm góc bằng thuật toán Harris
- Công thức : `𝑅=det⁡(𝑀)−𝑘⋅(trace(𝑀))2`
- Trong đó : 
    + 𝑀 là ma trận cấu trúc tại mỗi điểm ảnh
    + 𝑘 là hệ số nhạy (thường từ 0.04 đến 0.06, ở đây dùng 0.001 để tăng độ nhạy)
    + Kết quả: Ma trận coordinate chứa giá trị phản hồi — càng lớn thì càng có khả năng là điểm góc
3. Hiển thị bản đồ phản hồi góc
- Ý nghĩa : Hiển thị ảnh phản hồi Harris — các điểm sáng thể hiện vị trí có khả năng là góc
- Ví dụ: Các góc của cánh chim, mắt, hoặc các chi tiết sắc nét sẽ có giá trị cao trong ảnh

# Ghi chú: Các hàm `np.asarray`, `nd.sobel`,`nd.gaussian_filter`,`iio.imread`, `plt.figure`, `plt.imshow()`, `plt.axis()`, `plt.show()` được dùng trong toàn bộ quá trình xử lý ảnh. Bởi vì sử dụng thư viện Matplotlib, Scipy cũng như OpenCV cho các công thức/hình ảnh hoạt động nên các hàm trên được sử dụng để thực thi code

# Tài liệu tham khảo thêm :
- [Harris Corner Detection](https://docs.opencv.org/4.x/dc/d0d/tutorial_py_features_harris.html)
- [Hough Transform](https://www.vietanh.dev/blog/2019-10-24-hough-transform-phat-hien-duong-thang)
- [Google](https://www.google.com/)
- Slide bài giảng Nhập môn Xử lý ảnh số - Văn Lang University
