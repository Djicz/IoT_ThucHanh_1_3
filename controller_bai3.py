import time
import json
import paho.mqtt.client as mqtt

# Cau hinh broker & topic
BROKER = "localhost"
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"
TARGET_DEVICE = "light01"

# Tao Client
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Controller_App_Bai3")
except AttributeError:
    client = mqtt.Client(client_id="Controller_App_Bai3")

def on_connect(client, userdata, flags, rc, *args, **kwargs):
    if rc == 0:
        print(f"[*] Controller da ket noi toi Broker: {BROKER}:{PORT}")
        # Subscribe trang thai thiet bi
        client.subscribe(TOPIC_STATUS, qos=1)
        print(f"[*] Da subscribe topic trang thai: '{TOPIC_STATUS}'\n" + "="*45)
    else:
        print(f"[!] Ket noi that bai, ma loi: {rc}")

def on_message(client, userdata, msg):
    payload_str = msg.payload.decode("utf-8")
    print(f"\n[<] Trang thai nhan duoc tu [{msg.topic}]:")
    print(f"    {payload_str}")
    print("-" * 35)

client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi controller toi MQTT Broker...")
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

time.sleep(1) # Cho ket noi on dinh

print("\n--- HE THONG DIEU KHIEN DEN THONG MINH ---")
print("Cac lenh hop le: ON, OFF, EXIT")

try:
    while True:
        cmd = input("\nNhap lenh: ").strip()
        cmd_upper = cmd.upper()

        if not cmd:
            continue

        if cmd_upper == "EXIT":
            print("[*] Dang thoat chuong trinh...")
            break
        elif cmd_upper in ["ON", "OFF"]:
            client.publish(TOPIC_CMD, cmd_upper, qos=1)
            print(f"[>] Da gui lenh {cmd_upper} toi {TARGET_DEVICE}")
            time.sleep(0.5) # Cho thoi gian de nhan phan hoi truoc khi nhap lenh tiep
        else:
            print("[!] Lenh khong hop le! Vui long chi nhap 'ON', 'OFF' hoac 'EXIT'.")

except KeyboardInterrupt:
    print("\n[*] Nguoi dung dung chuong trinh.")

finally:
    client.loop_stop()
    client.disconnect()
    print("[*] Da ngat ket noi.")
