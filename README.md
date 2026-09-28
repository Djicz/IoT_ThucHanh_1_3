# BÀI 3: MÔ PHỎNG HỆ THỐNG ĐIỀU KHIỂN ĐÈN THÔNG MINH QUA MQTT

## 1. Broker sử dụng
- **Tên Broker:** Local Eclipse Mosquitto Broker
- **Host / IP:** `localhost`
- **Port:** `1883`
- **Giao thức:** MQTT TCP
- **Topics:**
  - Topic nhận lệnh điều khiển: `iot/lab/light01/cmd`
  - Topic phản hồi trạng thái: `iot/lab/light01/status`

---

## 2. Cách chạy từng chương trình

Mở **2 cửa sổ Terminal**:

1. **Terminal 1 - Khởi động thiết bị Đèn thông minh (Smart Light Device):**
   ```bash
   python device_bai3.py
   ```
   *Thiết bị sẽ kết nối Broker, gửi trạng thái khởi tạo (`OFF`) lên `iot/lab/light01/status` và lắng nghe lệnh điều khiển tại `iot/lab/light01/cmd`.*

2. **Terminal 2 - Khởi động Ứng dụng điều khiển (Controller App):**
   ```bash
   python controller_bai3.py
   ```
   *Controller kết nối Broker, lắng nghe topic trạng thái và chờ người dùng nhập lệnh từ bàn phím (`ON`, `OFF`, `EXIT`).*

---

## 3. Kết quả đạt được

### Thao tác điều khiển tại Terminal Controller:
```text
Dang ket noi controller toi MQTT Broker...
[*] Controller da ket noi toi Broker: localhost:1883
[*] Da subscribe topic trang thai: 'iot/lab/light01/status'
=============================================

--- HE THONG DIEU KHIEN DEN THONG MINH ---
Cac lenh hop le: ON, OFF, EXIT

Nhap lenh: ON
[>] Da gui lenh ON toi light01

[<] Trang thai nhan duoc tu [iot/lab/light01/status]:
    {"device_id": "light01", "status": "ON"}
-----------------------------------

Nhap lenh: OFF
[>] Da gui lenh OFF toi light01

[<] Trang thai nhan duoc tu [iot/lab/light01/status]:
    {"device_id": "light01", "status": "OFF"}
-----------------------------------

Nhap lenh: ABC
[!] Lenh khong hop le! Vui long chi nhap 'ON', 'OFF' hoac 'EXIT'.

Nhap lenh: EXIT
[*] Dang thoat chuong trinh...
[*] Da ngat ket noi.
```

### Output tương ứng tại Terminal Device:
```text
Dang khoi dong thiet bi den thong minh...
[*] Thiet bi 'light01' da ket noi toi Broker: localhost:1883
[*] Dang lang nghe lenh tren topic: 'iot/lab/light01/cmd'
[*] Trang thai hien tai: OFF
[*] Nhan Ctrl+C de dung thiet bi.
=============================================
[+] Da phan hoi trang thai: {"device_id": "light01", "status": "OFF"}

[!] Nhan duoc lenh: 'ON' tu topic 'iot/lab/light01/cmd'
[*] Chuyen trang thai den thanh: [ON]
[+] Da phan hoi trang thai: {"device_id": "light01", "status": "ON"}

[!] Nhan duoc lenh: 'OFF' tu topic 'iot/lab/light01/cmd'
[*] Chuyen trang thai den thanh: [OFF]
[+] Da phan hoi trang thai: {"device_id": "light01", "status": "OFF"}
```

### Đánh giá:
- Xây dựng thành công mô hình giao tiếp 2 chiều hoàn chỉnh: Giám sát trạng thái + Điều khiển thiết bị.
- Phản hồi trạng thái tức thời dưới dạng JSON chuẩn.
- Xử lý tốt các trường hợp nhập sai lệnh và cung cấp lệnh `EXIT` thoát chương trình mượt mà.
