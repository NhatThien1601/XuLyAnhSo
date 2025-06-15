import cv2
import numpy as np
import os

# Định nghĩa các hàm biến đổi ảnh
def inverse_transform(image):
    return cv2.bitwise_not(image)

def gamma_correction(image, gamma=1.5):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

def log_transformation(image):
    image = image.astype(np.float32)  # Chuyển sang kiểu float trước khi dùng log
    c = 255 / np.log(1 + np.max(image))
    return (c * (np.log(image + 1))).astype(np.uint8)

def histogram_equalization(image):
    if len(image.shape) == 2:  # Ảnh grayscale
        return cv2.equalizeHist(image)
    else:  # Ảnh màu
        channels = cv2.split(image)
        eq_channels = [cv2.equalizeHist(ch) for ch in channels]
        return cv2.merge(eq_channels)

def contrast_stretching(image):
    min_val, max_val = np.min(image), np.max(image)
    return ((image - min_val) * (255 / (max_val - min_val))).astype(np.uint8)

# Đọc ảnh từ thư mục exercise và thực hiện biến đổi
def process_images(transformation_func, output_folder):
    input_folder = "exercise"
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Đọc ảnh grayscale
            transformed_image = transformation_func(image)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, transformed_image)

            # Hiển thị ảnh đã biến đổi
            cv2.imshow(f"Transformed: {filename}", transformed_image)
            cv2.waitKey(1000)  # Hiển thị từng ảnh trong 1 giây
    
    cv2.destroyAllWindows()

# Hiển thị menu
while True:
    print("\nChọn phương pháp biến đổi ảnh:")
    print("I - Image Inverse Transformation")
    print("G - Gamma Correction")
    print("L - Log Transformation")
    print("H - Histogram Equalization")
    print("C - Contrast Stretching")
    print("Q - Thoát")

    choice = input("Nhập phím lựa chọn: ").upper()

    if choice == "I":
        process_images(inverse_transform, "output_inverse")
    elif choice == "G":
        process_images(lambda img: gamma_correction(img, 1.5), "output_gamma")
    elif choice == "L":
        process_images(log_transformation, "output_log")
    elif choice == "H":
        process_images(histogram_equalization, "output_histogram")
    elif choice == "C":
        process_images(contrast_stretching, "output_contrast")
    elif choice == "Q":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")