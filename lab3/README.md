# Công nghệ sử dụng
- Visual Studio Code, (Jupyer Notebook)
- Kernel: Python 
- Ngôn ngữ: Python (JSON file đuôi .ipynb)
- Thư viện: OpenCV, Numpy, Os, Random, Matplotlib.pyplot, v.v.


# Câu 2.1 Biến đổi ảnh bằng các phương pháp cơ bản

# Chức năng:
- Đọc ảnh từ thư mục `exercise`
- Áp dụng một trong năm phương pháp biến đổi ảnh do người dùng chọn
- Lưu ảnh đã biến đổi vào thư mục đầu ra
- Hiển thị ảnh đã biến đổi trên màn hình

# Các phương pháp biến đổi:
- **I**: Đảo ngược màu (`inverse_transform`)
- **G**: Điều chỉnh Gamma (`gamma_correction`)
- **L**: Biến đổi Log (`log_transformation`)
- **H**: Cân bằng Histogram (`histogram_equalization`)
- **C**: Kéo giãn độ tương phản (`contrast_stretching`)
- **Q**: Thoát chương trình

# Giải thích:
- `inverse_transform(image)`: Đảo màu (0 ↔ 255)
- `gamma_correction(image, gamma=1.5)`: Gamma > 1 làm sáng ảnh, < 1 làm tối ảnh
- `log_transformation(image)`: Làm sáng vùng tối, dùng log nên cần chuyển ảnh sang float
- `histogram_equalization(image)`: Cân bằng sáng (grayscale: `cv2.equalizeHist`; ảnh màu: cân bằng từng kênh)
- `contrast_stretching(image)`: Chuẩn hóa giá trị pixel từ [min, max] về [0, 255]
- `process_images()`: Đọc và xử lý toàn bộ ảnh trong thư mục `exercise`

Sử dụng log transformation giúp ảnh rõ hơn nhiều khi xử lý ảnh đen/trắng

---

# 2.2 Biến đổi ảnh bằng Fourier và Butterworth Filter

# Chức năng:
- Đọc ảnh từ folder `exercise` và xử lí
- Chọn 1 trong 3 phương pháp biến đổi:
  - FFT
  - Butterworth Lowpass
  - Butterworth Highpass
- Lưu và hiển thị ảnh

# Giải thích:
- `fast_fourier_transform(image)`: phép biến đổi nén ảnh, lọc ảnh hoặc nhận diện đối tượng
- `butterworth_lowpass_filter(shape, d0=30, n=2)`: lọc tần số thấp
- `butterworth_highpass_filter(shape, d0=30, n=2)`: 1 - lowpass (lọc tần số cao - tức là ngược lại với lowpass)
- `apply_butterworth_filter(image, filter_type="lowpass/highpass")`: áp dụng filter và chuyển ảnh ngược lại bằng `cv2.idft`
- `process_images()`: đọc ảnh trong folder và áp dụng phép biến đổi tùy chọn
- Phím chọn: 'F', 'L', 'H', ngược lại in ra " không hợp lệ"

---

# 2.3 Biến đổi ảnh ngẫu nhiên + đổi thứ tự RGB

# Chức năng:
- Đọc ảnh màu từ `exercise`
- Hoán đổi RGB ngẫu nhiên
- Áp dụng ngẫu nhiên 1 trong 5 phương pháp biến đổi ảnh
- Lưu vào `output_transformed` và hiển thị ảnh gốc lẫn ảnh sau khi biến đổi

# Phương pháp biến đổi:
- `inverse_transform(image)`
- `gamma_correction(image)`
- `log_transformation(image)`
- `histogram_equalization(image)`
- `contrast_stretching(image)`

# Giải thích thêm:
- `shuffle_rgb(image)`: Đổi RGB ngẫu nhiên
- `process_images(output_folder)`: Lưu và hiển thị ảnh đã biến đổi
- Ảnh sẽ được in ra gồm ảnh gốc và ảnh đã qua xử lý

---

# 2.4 Biến đổi ảnh bằng FFT hoặc Butterworth + Max/Min Filter

# Chức năng:
- Đọc từng ảnh trong thư mục `exercise`
- Xáo trộn màu RGB (đổi thứ tự kênh màu)
- Chuyển sang ảnh xám
- Áp dụng ngẫu nhiên một trong ba biến đổi tần số:
  + FFT (biến đổi Fourier)
  + Butterworth Lowpass + làm mịn (Min Filter)
  + Butterworth Highpass + tăng chi tiết (Max Filter)
- Hiển thị ảnh gốc và ảnh đã xử lý song song
- Lưu ảnh kết quả vào thư mục output_random

# Các kỹ thuật được dùng
- `cv2.dft`, `np.fft.fftshift`	: Biến ảnh sang miền tần số (FFT)
- `Butterworth Filter`	Lọc tần số thấp/cao (Lowpass/Highpass)
- `cv2.erode`, `cv2.dilate` :	Làm mịn (Min Filter) hoặc tăng nét (Max Filter)
- `matplotlib.pyplot` :	Hiển thị ảnh ngay trong notebook
# Giải thích:
- `shuffle_rgb(image)`: Đổi thứ tự kênh màu
- `fast_fourier_transform(image)` : Phép biến đổi nén ảnh, lọc ảnh hoặc nhận diện đối tượng
- `min_filter`: Làm mịn ảnh
- `max_filter`: Tăng chi tiết ảnh
- `process_images()`: Chạy toàn bộ chương trình

---

# Ghi chú: Các hàm `cv2.imread`, `os.makedirs`, `cv2.imwrite`, `os.listdir`, `plt.figure`, `plt.imshow()`, `plt.axix()`, `plt.show()` được dùng trong toàn bộ quá trình xử lý ảnh. Bởi vì sử dụng thư viện Matplotlib cho file hoạt động nên các hàm trên được sử dụng để thực thi code
