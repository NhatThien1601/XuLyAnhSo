# Nhập Môn Xử Lý Ảnh Số - Lab 4 - Lý Thuyết + Bài Tập Tăng Cường(Zalo)
# Biến đổi hình học (Tịnh tiến, xoay ảnh, chọn đối tượng, thay đổi kích thước, biến đổi cực)
Sinh viên thực hiện: Trần Nghiêm Nhật Thiện ; MSSV: 2174802010938
Môn học: Nhập môn Xử lý ảnh số
Giảng viên: Đỗ Hữu Quân
# Giới thiệu
Bài lab này nhằm mục đích giúp sinh viên có thể viết các chương trình biến đổi hình học cho ảnh trên nền ảnh xám cũng như màu.
# Công nghệ sử dụng
- Visual Studio Code, (Jupyer Notebook)
- Kernel: Python 
- Ngôn ngữ: Python (JSON file đuôi .ipynb)
- Thư viện: OpenCV, Numpy, Os, Matplotlib.pyplot, Matplotlib.pylab, scipy.ndimage, imageio.v2 v.v.

# Chi tiết một số phép biến đổi - công thức
1. scipy.ndimage :
Là module xử lý ảnh đa chiều (n-dimensional image). Là một phép biến đổi làm mờ hình ảnh dựa trên hàm Gauss , bao gồm các thao tác như lọc biến đổi hình học (tịnh tiến, xoay, phóng đại), phát hiện biên,...
- Công thức toán : g(x, y) = (1 / (2 * π * σ^2)) * e^(-(x^2 + y^2) / (2 * σ^2))
Trong đó:
  . g(x, y) là giá trị của hàm Gaussian tại điểm (x, y).
  . σ (sigma) là độ lệch chuẩn, xác định mức độ lan truyền của độ mờ. Giá trị σ càng lớn, độ mờ càng mạnh.
  . x và y là khoảng cách theo chiều ngang và chiều dọc từ tâm của bộ lọc.
  . e là cơ số của logarit tự nhiên (khoảng 2.71828).
  . π là hằng số Pi (khoảng 3.14159).
2. matplotlib.pylab :
Là tập con của matplotlib kết hợp matplotlib.pyplot và numpy giống như Matlab – dùng để vẽ đồ thị, hiển thị ảnh, và xử lý số liệu đơn giản.
3. ndimage.map_coordinates :
Nội suy (interpolate) ảnh tại các tọa độ tùy ý. Dùng để biến đổi hình học: xoay, biến dạng, dịch chuyển, v.v.
Dùng nội suy bậc 1 hoặc bậc 3. Với nội suy tuyến tính (linear):
y = y₀ + (x - x₀) * (y₁ - y₀) / (x₁ - x₀)
Trong đó:
  - y là giá trị cần tìm tại điểm x.
  - x₀ và y₀ là tọa độ của điểm dữ liệu thứ nhất.
  - x₁ và y₁ là tọa độ của điểm dữ liệu thứ hai.
  - x là giá trị cần tìm ở giữa x₀ và x₁.
Giải thích công thức:
  - (x - x₀) / (x₁ - x₀): Tính tỷ lệ khoảng cách của x so với khoảng cách giữa x₀ và x₁.
  - (y₁ - y₀) * (x - x₀) / (x₁ - x₀): Nhân tỷ lệ trên với độ chênh lệch giữa y₁ và y₀ để tìm độ chênh lệch tương ứng của y.
  - y₀ + (y₁ - y₀) * (x - x₀) / (x₁ - x₀): Cộng độ chênh lệch đó vào y₀ để có giá trị y tại điểm x.
(Tài liệu xem thêm ở bên dưới )
4. scipy.ndimage.zoom:
Phóng to hoặc thu nhỏ ảnh (rescale) bằng cách nội suy lại giá trị pixel. Có thể dùng để zoom ảnh theo một hệ số cụ thể
- scipy.ndimage.rotate :
Xoay ảnh một góc nhất định theo chiều kim đồng hồ (hoặc ngược lại). Có thể giữ kích thước gốc hoặc thay đổi (reshape=True)
- scipy.ndimage.binary_dilation : 
Thực hiện giãn nhị phân (morphological dilation) – làm mở rộng vùng trắng (1) trong ảnh nhị phân. Dùng trong xử lý ảnh để loại bỏ nhiễu, nối vật thể rời rạc
- scipy.ndimage.geometric_transform :
Áp dụng biến đổi hình học tùy chỉnh trên ảnh bằng cách viết hàm chuyển đổi tọa độ thủ công. Rất linh hoạt: dùng để warp, gợn sóng, lật, uốn cong ảnh,...
( Các công thức của scipy tham khảo thêm ở bên dưới )
# Câu 2.1 Tịnh tiến quả Kiwi
# Chức năng:
- Đọc ảnh xám kiwi có đuôi .jpg
- Áp dụng tịnh tiến dịch ảnh xuống 30 pixel và sang phải 50 pixel, áp dụng hiệu ứng sóng (wave effect) lên quả kiwi bằng cách sử dụng biến đổi tọa độ (map_coordinates) với hàm sin.
- Lưu ảnh đã biến đổi với file name = kiwi_wave.jpg
- Hiển thị ảnh đã biến đổi trên màn hình

# Các phương pháp biến đổi:
- **rows, cols**: số dòng (chiều cao ảnh) và số cột(chiều rộng ảnh)
- **x, y**: tạo lưới 2D các tọa độ pixel gốc ; x[i, j]: tọa độ cột của điểm ảnh (j) ; y[i, j]: tọa độ hàng (i)
- **amplitude**: độ cao của sóng ( biên độ)
- **frequency**: chu kỳ sóng
- **x_wave = x + amplitude * np.sin(frequency * y), y_wave = y**: tính tọa độ biến dạng
- **coords = np.array([y_wave, x_wave])**: tạo mảng tọa độ mới

# Tóm tắt:
- Đọc ảnh	        => Đọc ảnh thành ảnh xám dạng mảng
- Tạo sóng	      => Biến đổi tọa độ pixel theo sóng sin
- Áp dụng	        => Dùng nội suy để tính ảnh mới tại vị trí bị biến dạng
- Hiển thị + Lưu	=> Hiển thị ảnh kết quả và lưu ra file

---

# 2.2 Chọn quả đu đủ và dưa hấu từ google. Đổi màu đu đủ thành gradient từ đỏ sang xanh lá, và dưa hấu thành gradient từ vàng sang tím. Ghép hai quả lên một nền trong suốt (alpha channel) và lưu dưới dạng PNG

# Chức năng:
Tạo hiệu ứng gradient màu cho 2 ảnh (đu đủ và dưa hấu), sau đó ghép chúng lại trên nền trong suốt và lưu ảnh kết quả.

# Các phép biến đổi:
- Chuyển ảnh sang RGBA : để giữ thông tin trong suốt (alpha channel)
- Chuyển RGB -> Grayscale : dùng làm hệ số để pha trộn màu gradient
- Tạo gradient giữa 2 màu : dựa vào mức xám để nội suy giữa color_start -> color_end
- Ghép ảnh ngang : 	ghép 2 ảnh được tô màu vào một ảnh lớn hơn (canvas)
- Nền trong suốt : 	giữ nền ảnh là transparent để tiện sử dụng về sau

---

# 2.3 Chọn ảnh núi và thuyền . Xoay cả hai đối tượng 45 độ, giữ kích thước ban đầu (reshape=False). Tạo hiệu ứng phản chiếu dọc (vertical mirror) cho cả hai đối tượng sau khi xoay. Ghép cả hai đối tượng lên một canvas trắng và lưu vào mountain_boat_mirror.jpg

# Chức năng chính:
Tạo hiệu ứng nghệ thuật cho 2 ảnh (núi & thuyền) bằng cách:
- Xoay ảnh 45 độ
- Phản chiếu dọc (lật ngược)
- Ghép 2 ảnh lại trên nền trắng
- Lưu và hiển thị ảnh kết quả

# Các phương pháp biến đổi:
- Xoay ảnh (rotate) : quay ảnh 45 độ theo chiều kim đồng hồ, giữ nguyên kích thước cũ
- Phản chiếu dọc (vertical flip) : lật ảnh từ trên xuống dưới như hình phản chiếu qua mặt nước
- Tạo canvas (nền trắng) : ảnh nền mới đủ rộng để chứa cả 2 ảnh
- Ghép ảnh : dán từng ảnh vào vị trí phù hợp để có bố cục cân đối trên canvas


# Giải thích thêm:
- Import các thư viện: PIL (xử lý ảnh), matplotlib (hiển thị)
- Đọc 2 ảnh "mountain.jpg" và "boat.jpg" ở dạng RGBA (có alpha)
- Định nghĩa hàm rotate_image() để xoay ảnh 45 độ -> kết quả là ảnh bị nghiêng
- Dùng ImageOps.flip() để phản chiếu dọc (ảnh bị lật ngược từ trên xuống)
- Tạo một nền trắng (RGB) đủ lớn để chứa cả 2 ảnh đã biến đổi
- Ghép 2 ảnh lên nền: ảnh núi bên trái, thuyền bên phải – căn giữa theo chiều cao
- Lưu ảnh kết quả thành file "mountain_boat_mirror.jpg"
---

# 2.4 Chọn ngôi chùa bất kì. Phóng to ngôi chùa lên 5 lần. Áp dụng một biến đổi hình học tùy chỉnh (geometric transform) để tạo hiệu ứng "uốn cong" (warping) ngôi chùa. Lưu ảnh kết quả vào pagoda_warped.jpg.

# Chức năng chính :
Phóng to ảnh ngôi chùa rồi áp dụng hiệu ứng uốn cong sóng sin (wave warp) theo trục dọc, tạo hiệu ứng mềm mại giống như ảnh bị gợn sóng

# Các kỹ thuật được dùng
- Phóng to ảnh (resize) : mở rộng ảnh gấp 5 lần để nhìn rõ hơn hiệu ứng
- Biến dạng hình học (warp) : dùng hàm sin để làm cong ảnh theo chiều dọc
- Nội suy ảnh (interpolation) : dùng nội suy tuyến tính để làm mượt hiệu ứng khi biến đổi
- Tạo bản đồ ánh xạ (mapping) : sử dụng cv2.remap() để biến đổi từng điểm ảnh đến vị trí mới

# Giải thích thêm:
- Import thư viện: cv2 (OpenCV), numpy, PIL, matplotlib (hiển thị ảnh)
- Đọc ảnh "chua.jpg" bằng OpenCV (ảnh gốc ở dạng BGR) → chuyển sang RGB để hiển thị đúng màu đối tượng
- Phóng to ảnh gấp 5 lần bằng cv2.resize() với nội suy INTER_CUBIC để giữ độ mượt
- Định nghĩa hàm warp_image() để tạo hiệu ứng uốn cong ảnh theo sóng sin:
  . Duyệt qua từng điểm ảnh
  . Dịch chuyển vị trí theo trục y bằng sin(x)
- Áp dụng hiệu ứng biến dạng lên ảnh đã phóng to
- Chuyển ảnh về lại BGR để ghi ra file (cv2.imwrite)

---

# Ghi chú: Các hàm `cv2.imread`, `os.makedirs`, `cv2.cvtColor`, `cv2.getRotationMatrix2D`, `cv2.warpAffine`, `cv2.resize`, `os.listdir`, `plt.figure`, `plt.imshow()`, `plt.axis()`, `plt.show()` được dùng trong toàn bộ quá trình xử lý ảnh. Bởi vì sử dụng thư viện Matplotlib cho file hoạt động nên các hàm trên được sử dụng để thực thi code

# Tài liệu tham khảo thêm :
- [multidimensional-image-processing-using-scipy-in-python](https://www.geeksforgeeks.org/machine-learning/multidimensional-image-processing-using-scipy-in-python/)
- [Các phương pháp Interpolation trong xử lý ảnh](https://www.toolify.ai/vi/ai-news-vn/cc-phng-php-interpolation-trong-x-l-nh-2303164)
- [Google](https://www.google.com/)
- Slide bài giảng Nhập môn Xử lý ảnh số - Văn Lang University