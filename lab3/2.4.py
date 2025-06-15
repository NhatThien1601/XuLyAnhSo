import cv2
import numpy as np
import os
import random

# Hàm đổi thứ tự kênh màu RGB (ví dụ: hoán đổi R -> G -> B)
def shuffle_rgb(image):
    return image[:, :, np.random.permutation(3)]  # Hoán đổi ngẫu nhiên thứ tự kênh màu

# Hàm Fast Fourier Transform (FFT)
def fast_fourier_transform(image):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

    magnitude_spectrum = np.log(1 + magnitude_spectrum)
    magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
    return magnitude_spectrum.astype(np.uint8)

# Hàm tạo bộ lọc Butterworth Lowpass
def butterworth_lowpass_filter(shape, d0=30, n=2):
    rows, cols = shape
    center = (rows // 2, cols // 2)
    H = np.zeros((rows, cols), dtype=np.float32)
    for i in range(rows):
        for j in range(cols):
            D = np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2)
            H[i, j] = 1 / (1 + (D / d0) ** (2 * n))
    return H

# Hàm tạo bộ lọc Butterworth Highpass
def butterworth_highpass_filter(shape, d0=30, n=2):
    return 1 - butterworth_lowpass_filter(shape, d0, n)

# Hàm áp dụng bộ lọc Butterworth
def apply_butterworth_filter(image, filter_type="lowpass"):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    filter_func = butterworth_lowpass_filter if filter_type == "lowpass" else butterworth_highpass_filter
    H = filter_func(image.shape)
    
    dft_shift[:, :, 0] *= H
    dft_shift[:, :, 1] *= H

    dft_ishift = np.fft.ifftshift(dft_shift)
    img_back = cv2.idft(dft_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    
    return cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Hàm Min Filter (lọc làm mịn ảnh)
def min_filter(image, ksize=3):
    return cv2.erode(image, np.ones((ksize, ksize), np.uint8))

# Hàm Max Filter (tăng cường chi tiết ảnh)
def max_filter(image, ksize=3):
    return cv2.dilate(image, np.ones((ksize, ksize), np.uint8))

# Đọc ảnh từ thư mục exercise và xử lý ngẫu nhiên
def process_images():
    input_folder = "exercise"
    output_folder = "output_random"
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)  # Đọc ảnh màu
            
            # Thay đổi thứ tự màu RGB
            shuffled_image = shuffle_rgb(image)
            gray_image = cv2.cvtColor(shuffled_image, cv2.COLOR_BGR2GRAY)

            # Chọn ngẫu nhiên phương pháp biến đổi
            transform_type = random.choice(["FFT", "Lowpass", "Highpass"])
            print(f"Áp dụng {transform_type} cho {filename}")

            if transform_type == "FFT":
                transformed_image = fast_fourier_transform(gray_image)
            elif transform_type == "Lowpass":
                transformed_image = apply_butterworth_filter(gray_image, "lowpass")
                transformed_image = min_filter(transformed_image, ksize=3)
            elif transform_type == "Highpass":
                transformed_image = apply_butterworth_filter(gray_image, "highpass")
                transformed_image = max_filter(transformed_image, ksize=3)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, transformed_image)

            # Hiển thị ảnh sau khi biến đổi
            cv2.imshow(f"Transformed: {filename}", transformed_image)
            cv2.waitKey(0)  # Chờ người dùng nhấn phím để tiếp tục
    
    cv2.destroyAllWindows()

# Thực thi chương trình
process_images()
