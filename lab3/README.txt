Công nghệ sử dụng là Visual Studio Code dùng Python để code và tải các thư viện liên quan đến bài học như là OpenCV, Numpy, Os, Random v.v
Thuật toán sử dụng sẽ nói chi tiết bên dưới.
2.1
Chương trình này thực hiện biến đổi ảnh theo nhiều phương pháp khác nhau, bao gồm:
	Đọc ảnh từ thư mục "exercise"
	Áp dụng một trong năm phương pháp biến đổi ảnh mà người dùng chọn
	Lưu ảnh đã biến đổi vào thư mục đầu ra
	Hiển thị ảnh đã biến đổi trên màn hình
Người dùng có thể chọn các phương pháp như:
	Đảo ngược màu (inverse_transform)
	Điều chỉnh Gamma (gamma_correction)
	Biến đổi Log (log_transformation)
	Cân bằng Histogram (histogram_equalization)
	Kéo giãn độ tương phản (contrast_stretching)
Giải thích:
. Gọi hàm inverse_transform(image) để đảo ngược màu. vd pixel có giá trị 0(đen) -> chuyển thành 255(trắng) và ngược lại 255(trắng) -> 0(đen)
. Gọi hàm gamma_correction(image, gamma=1.5) để điều chỉnh mức gamma, nếu gamma > 1 thì làm sáng ảnh, gamma < 1 thì làm tối ảnh và gamma = 1 thì không thay đổi ảnh
. Gọi hàm log_transformation(image) để biến đổi log tăng cường độ sáng của vùng tối trong ảnh, làm rõ chi tiết ảnh, nên chuyển ảnh sang kiểu float trước khi dùng log để không bị lỗi chia không được khi chạy code. Pixel tối có giá trị nhỏ sau khi áp dụng hàm Log sẽ sáng hơn, còn pixel sáng thì vẫn giữ nguyên. Trong đó c là hệ số điều chỉnh để giữ giá trị pixel nằm trong khoảng [0, 255]
. Gọi hàm histogram_equalization(image) là hàm cân bằng sáng của ảnh, giúp ảnh rõ nét hơn. Nếu là ảnh grayscale thì áp dụng cv2.equalizeHist() . Nếu là ảnh màu thì thực hiện cân bằng từng kênh màu rồi ghép lại
. Gọi hàm contrast_stretching(image) là hàm tăng cường độ tương phản bằng cách chuẩn hóa giá trị pixel, lấy giá trị pixel nhỏ nhất (min) và giá trị pixel lớn nhất (max) xong kéo giãn toàn bộ ảnh trong khoảng [0, 255]
. Gọi hàm process_images để đọc tất cả ảnh trong folder 'exercise' và tạo output tương ứng với đầu ra. Đọc ảnh với cv2.imread và hiển thị = cv2.imshow, thời gian hiển thị các ảnh trong 1s là cv2.waitKey(1000). Sau đó đóng các ảnh lại cv2.destroyAllWindows()
. Sử dụng while True: để nhập phím lựa chọn input đầu vào tương ứng với phép biến đổi tùy theo người dùng mong muốn là chữ cái đầu trong tên các phép biến đổi ( I, G, L, H, C) và Q là thoát chương trình. Nếu nhập phím lựa chọn sẽ báo lỗi không hợp lệ và yêu cầu thử lại.
2.2
Chương trình này thực hiện các phép biến đổi ảnh bằng cách sử dụng Biến đổi Fourier (FFT) và bộ lọc Butterworth (Lowpass & Highpass) để thay đổi tần số của ảnh với 3 bước:
	Đọc ảnh từ folder 'exercise'
	Chọn 1 trong 3 phương pháp biến đổi mà bạn muốn (FFT, Butterworth Lowpass hoặc Highpass)
	Lưu ảnh đã biến đổi vào 1 thư mục và hiển thị trên màn hình
Giải thích:
. Gọi hàm fast_fourier_transform(image) sử dụng cv2.dft để đưa ảnh về miền tần số, dịch chuyển trung tâm tần số = np.fft.fftshift để phân tích, sau đó tính toán biên độ phổ tần số = cv2.magnitude và rồi chuẩn hóa cũng như hiển thị bằng cách lấy giá trị log (numpy.log) và chuẩn hóa (cv2.normalize)
. Gọi hàm butterworth_lowpass_filter(shape, d0=30, n=2) trong đó d0=30 là bán kính vùng tần số thấp, n= 2 là bậc của bộ lọc
. Gọi hàm butterworth_highpass_filter(shape, d0=30, n=2) trong đó dùng 1 -butterworth_lowpass_filter do ngược lại với lowpass, bộ lọc highpass giữ lại tần số cao để làm rõ chi tiết ảnh.
. Gọi hàm  apply_butterworth_filter(image, filter_type="lowpass") như tên gọi áp dụng bộ lọc butterworth chuyển đổi ảnh sang miền tần số bằng Fourier và dùng bộ lọc butterworth low/highpass để giữ lại tần số thấp/cao. Sau đó dùng cv2.idft để chuyển ảnh về miền không gian bằng biến đổi nghịch Fourier.
. Gọi hàm process_images để xử lí ảnh trong folder 'exercise' bằng cách đọc các ảnh trong folder 'exercise' và áp dụng phép biến đổi tùy chọn ( 1 trong 3 ). Hiển thị các ảnh liên tiếp trong 1s và đóng lại. dùng cv2.imwrite để lưu ảnh đã biến đổi được trong folder output tương ứng.
. dùng while True để chọn 1 trong 3 phép biến đổi với input đầu vào nhập = phím tương ứng chữ cái đầu của tên phép ( F, L, H) và Q là thoát chương trình. Nếu người nhập sai sẽ in thông báo lựa chọn không hợp lệ.

2.3
Chương trình sẽ thực hiện biến đổi các ảnh trong folder 'exercise' theo 3 bước:
 - Đọc ảnh màu và thực hiện hoán đổi thứ tự màu RGB một cách ngẫu nhiên
 - Chọn ngẫu nhiên một phép biến đổi ảnh trong các phương pháp như đảo ngược màu, điều chỉnh gamma, biến đổi log, cân bằng histogram, kéo giãn độ tương phản
 - Lưu ảnh đã biến đổi vào thư mục "output_transformed" và hiển thị ảnh trên màn hình
Giải thích:
có 5 phương pháp biến đổi ảnh gồm :
	Hàm inverse_transform(image) đảo ngược màu của ảnh (ảnh đen thành trắng, ảnh trắng thành đen)
	Hàm gamma_correction(image, gamma=1.5) điều chỉnh độ sáng ảnh bằng phương pháp gamma, gamma > 1 giúp tăng độ sáng, gamma < 1 giúp làm tối ảnh
	Hàm log_transformation(image) biến đổi log để tăng cường chi tiết ở vùng tối của ảnh
	Hàm histogram_equalization(image) cân bằng histogram để tăng độ tương phản, làm ảnh rõ nét hơn
	Hàm contrast_stretching(image) kéo giãn độ tương phản bằng cách chuẩn hóa các pixel giữa khoảng giá trị tối thiểu và tối đa
. Gọi shuffle_rgb(image) để thực hiện hoán đổi màu RGB của ảnh ngẫu nhiên(shuffle)
. Gọi process_images(output_folder) với đầu vào input là folder 'exercise' sau đó tạo thư mục đầu ra nếu chưa có. Dùng for in để duyệt các ảnh trong folder, thay đổi thứ tự màu = shuffled_image, chọn phép biến đổi ảnh ngẫu nhiên = hàm random.choice và áp dụng phép biến đổi sau khi chuyển sang ảnh grayscale. Lưu các ảnh đã biến đổi với cv2.imwrite và hiển thị ảnh đã biến đổi trong 1 giây với cv2.waitKey(1000), sau đó đóng tất cả ảnh khi hết thời gian hiển thị. Các ảnh đã biến đổi được lưu vào folder output_transformed để xem lại nếu cần.
. Gọi hàm process_images("output_transformed") để chạy chương trình code
2.4
Chương trình code thực hiện ba nhiệm vụ chính:
1. Thay đổi màu RGB của ảnh ngẫu nhiên ( nếu ảnh có thứ tự R, G, B thì sau khi đổi sẽ thành G,  R , B hoặc B, R, G v.v ) dùng numpy.random.permutation(3)
2. Chọn một phép biến đổi ảnh ngẫu nhiên từ ba phương pháp:
	. Fast Fourier Transform (FFT) – Biến đổi ảnh để hiển thị phổ tần số
	. Butterworth Lowpass Filter – Lọc tần số thấp để làm mịn ảnh
	. Butterworth Highpass Filter – Lọc tần số cao để tăng cường chi tiết ảnh
3. Nếu ngẫu nhiên là Butterworth Lowpass, áp dụng thêm Min Filter để làm mịn ảnh. Nếu ngẫu nhiên là Butterworth Highpass, áp dụng thêm Max Filter để tăng cường chi tiết. Còn lại sẽ là Fast Fourier
Sau khi chạy code sẽ hiển thị ảnh (người dùng nhấn phím bất kì để hiển thị ảnh tiếp theo) và ảnh được lưu lại ở folder output_random
Giải thích :
- Gọi hàm shuffle_rgb(image) và sử dụng numpy.random.permutation(3) để hoán đổi thứ tự màu (R,G,B) ngẫu nhiên.
- Gọi hàm fast_fourier_transform(image), trước hết ta chuyển đổi ảnh sang dạng Fourier dùng (cv2.dft)
dịch chuyển trung tâm tần số = numpy.fft.fftshift
tính toán biên độ phổ tần số = cv2.magnitude. Sau đó chuyển hóa và chuyển đổi về ảnh hiển thị
magnitude_spectrum = np.log(1 + magnitude_spectrum)  
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
- Gọi hàm butterworth_lowpass_filter(shape, d0=30, n=2) trong đó:
	d0=30 là bán kính vùng tần số thấp
	n= 2 là bậc của bộ lọc
- Gọi hàm butterworth_highpass_filter(shape, d0=30, n=2) trong đó:
	1 - butterworth_highpass_filter(shape, d0=30, n=2) (lí do là ngược lại với lowpass ta sẽ tăng cường chi tiết bằng cách loại bỏ tần số thấp ( 1 - ))
- Gọi hàm apply_butterworth_filter(image, filter_type="lowpass"):
	Biến đổi Fourier rồi áp dụng bộ lọc Butterworth trước khi chuyển ảnh về miền không gian.
	apply_butterworth_filter(image, "lowpass") sẽ làm mịn ảnh, còn "highpass" sẽ tăng độ nét
- min_filter trong đó chọn giá trị pixel nhỏ nhất trong vùng lân cận để làm mịn ảnh, nếu ksize lớn hơn thì mức độ làm mịn sẽ cao hơn
- ngược lại với min thì chính là max_filter sẽ chọn giá trị pixel lớn nhất ở lân cận và tăng cường chi tiết của bức ảnh.
- hàm process_images(): chọn ngẫu nhiên ảnh với đầu vào input là folder 'exercise', output sẽ là 'output_random', os.makedirs để tạo folder . Sau khi đọc ảnh màu (cv2.imread) sẽ dùng shuffled_image để thay đổi màu RGB sau đó chọn ngẫu nhiên ( 3 phương pháp FF, Lowpass, Highpass) để thực hiện biến đổi theo yêu cầu đề bài ( áp dụn min/max filter nếu là low/highpass). Sử dụng cv2.waitKey(0) để người chạy chương trình có thể xem ảnh và nhấn phím bất kì để ảnh tiếp theo hiển thị.
