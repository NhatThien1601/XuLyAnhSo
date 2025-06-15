import cv2
import numpy as np
import os
import random

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

# Hàm thay đổi thứ tự màu RGB ngẫu nhiên
def shuffle_rgb(image):
    channels = list(cv2.split(image))  # Chuyển tuple thành list để có thể thay đổi
    random.shuffle(channels)  # Xáo trộn thứ tự các kênh màu
    return cv2.merge(channels)  # Gộp lại thành ảnh mới


# Đọc ảnh từ thư mục exercise và thực hiện biến đổi
def process_images(output_folder):
    input_folder = "exercise"
    os.makedirs(output_folder, exist_ok=True)

    transformations = [inverse_transform, gamma_correction, log_transformation, histogram_equalization, contrast_stretching]

    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)  # Đọc ảnh màu

            # Thay đổi thứ tự màu RGB
            shuffled_image = shuffle_rgb(image)

            # Chọn phép biến đổi ngẫu nhiên
            transformation_func = random.choice(transformations)

            # Áp dụng phép biến đổi
            transformed_image = transformation_func(cv2.cvtColor(shuffled_image, cv2.COLOR_BGR2GRAY))  # Chuyển về grayscale trước khi biến đổi
            
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, transformed_image)
            cv2.imshow("Transformed Image", transformed_image)
            cv2.waitKey(1000)  # Hiển thị ảnh trong 1s

    cv2.destroyAllWindows()

# Thực hiện chương trình
process_images("output_transformed")
