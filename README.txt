========================================================================
BÀI 3: MÔ PHỎNG HỆ THỐNG ĐIỀU KHIỂN ĐÈN THÔNG MINH QUA MQTT
========================================================================

1. THÔNG TIN SINH VIÊN:
- Họ và tên: Họ tên
- Mã sinh viên: Mã SV

2. BROKER SỬ DỤNG:
- Tên Broker: Local Eclipse Mosquitto Broker
- Host / IP: localhost
- Cổng (Port): 1883
- Topics:
  + Topic nhận lệnh điều khiển: iot/lab/light01/cmd
  + Topic phản hồi trạng thái:  iot/lab/light01/status

3. CÁCH CHẠY TỪNG CHƯƠNG TRÌNH:
(Mở 2 cửa sổ Terminal)

- Terminal 1: Khởi động thiết bị đèn thông minh (Smart Light Device)
  Lệnh chạy: python device_bai3.py

- Terminal 2: Khởi động ứng dụng điều khiển (Controller App)
  Lệnh chạy: python controller_bai3.py
  (Nhập lệnh: ON, OFF hoặc EXIT trên bàn phím)

4. KẾT QUẢ ĐẠT ĐƯỢC:
- Xây dựng thành công cơ chế giao tiếp 2 chiều (Giám sát & Điều khiển) đồng bộ qua MQTT.
- Ứng dụng Controller gửi lệnh ON/OFF lên topic 'iot/lab/light01/cmd'.
- Thiết bị đèn tiếp nhận lệnh, chuyển đổi trạng thái (bật/tắt) và tự động phản hồi chuỗi JSON lên topic 'iot/lab/light01/status':
  {"device_id": "light01", "status": "ON"} (hoặc "OFF")
- Controller nhận được phản hồi trạng thái mới nhất từ thiết bị và in ra màn hình.
- Xử lý kiểm soát lỗi khi nhập sai lệnh và hỗ trợ lệnh EXIT để thoát chương trình an toàn.
===============================================================================
