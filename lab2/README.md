# Nhập Môn Xử Lý Ảnh Số - Lab 2 - Lý Thuyết 
#  ẢNH KỸ THUẬT SỐ VÀ MÀU
- Sinh viên thực hiện: Trần Nghiêm Nhật Thiện
- MSSV: 2174802010938
- Môn học: Nhập môn Xử lý ảnh số
- Giảng viên: Đỗ Hữu Quân
# Giới thiệu
Bài lab này nhằm mục đích giúp sinh viên có thể :
-	Viết được chương trình xử lý điểm ảnh sử dụng kỹ thuật biến đổi logarith
-	Viết được chương trình xử lý điểm ảnh sử dụng kỹ thuật biến đổi power law
-	Viết được chương trình xử lý điểm ảnh sử dụng kỹ thuật ảnh ngược
-   Viết được chương trình xử lý điểm ảnh sử dụng kỹ thuật histogram equalization
-   Viết được chương trình xử lý điểm ảnh sử dụng kỹ thuật contrast stretching
# Công nghệ sử dụng
- Visual Studio Code, (Jupyer Notebook)
- Kernel: Python 
- Ngôn ngữ: Python (JSON file đuôi .ipynb)
- Thư viện: OpenCV, Numpy, Matplotlib, v.v.

# `pip install pillow numpy matplotlib scipy imageio`

# Chi tiết một số phép biến đổi - công thức và ví dụ:

# Xử lý Ảnh với OpenCV 

##  Công nghệ sử dụng

| Thư viện        | Mục đích sử dụng                                                 |
|-----------------|------------------------------------------------------------------|
| `PIL` / `Pillow`| Đọc và xử lý ảnh                                                |
| `NumPy`         | Xử lý ảnh dưới dạng mảng số và phép toán nhanh                  |
| `Matplotlib`    | Hiển thị ảnh sau xử lý                                          |
| `SciPy`         | Hỗ trợ các phép toán khoa học                                   |
| `imageio`       | Đọc ảnh vào dưới dạng dữ liệu số                                |

---

##  Giải thích các chức năng xử lý ảnh

### 1 Negative Transformation (Đảo ngược màu)

```python
im_2 = 255 - im_1
I_{new} = 255 - I
```
- Tác dụng: Tạo hiệu ứng ảnh âm bản, làm nổi bật các chi tiết hoặc dùng cho xử lý chuyên sâu
### 2 Gamma Correction (Hiệu chỉnh gamma)
```gamma = 5
b3 = im_1 / max_value
corrected = np.exp(np.log(b3) * gamma) * 255
```
#### Công thức toán học:
I_{new} = 255 \cdot \exp(\gamma \cdot \log(\frac{I}{I_{max}}))
- Tác dụng: Tăng giảm độ sáng ảnh theo cấp lũy thừa, giúp cải thiện chi tiết vùng tối hoặc sáng
---
### 3 Log Transformation (Biến đổi logarithmic)
`c = (128.0 * np.log(1 + b1)) / np.log(1 + b2)`
#### Công thức toán học:
I_{new} = \frac{128 \cdot \log(1 + I)}{\log(1 + I_{max})}
- Tác dụng: Làm sáng vùng tối, có lợi khi cần phát hiện chi tiết mờ nhạt trong ảnh
### 4 Histogram Equalization (Cân bằng histogram)
```cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
equalized = cdf[b1]
```
#### Công thức toán học:
I_{new} = \frac{cdf(I) - cdf_{min}}{(N - cdf_{min})} \times 255
- Tác dụng: Cải thiện độ tương phản toàn cục ảnh, giúp hình ảnh trở nên rõ ràng hơn
### 5 Contrast Stretching (Kéo dãn độ tương phản)
`im2 = 255 * (im1 - a) / (b - a)`
#### Công thức toán học:
I_{new} = \frac{(I - I_{min})}{I_{max} - I_{min}} \cdot 255
- Tác dụng: Mở rộng độ tương phản của ảnh bằng cách chuẩn hóa giá trị điểm ảnh về khoảng 0–255

# Tài liệu tham khảo thêm :
- [Greeks](https://www.geeksforgeeks.org/python/negative-transformation-of-an-image-using-python-and-opencv/)
- [Google](https://www.google.com/)
- Slide bài giảng Nhập môn Xử lý ảnh số - Văn Lang University
