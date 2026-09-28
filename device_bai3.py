import json
import paho.mqtt.client as mqtt

# Cau hinh broker & topic
BROKER = "localhost"
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"
DEVICE_ID = "light01"

# Trang thai mac dinh ban dau
current_status = "OFF"

# Tao Client
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Device_Light01")
except AttributeError:
    client = mqtt.Client(client_id="Device_Light01")

def publish_status():
    global current_status
    status_payload = {
        "device_id": DEVICE_ID,
        "status": current_status
    }
    payload_json = json.dumps(status_payload)
    client.publish(TOPIC_STATUS, payload_json, qos=1)
    print(f"[+] Da phan hoi trang thai: {payload_json}")

def on_connect(client, userdata, flags, rc, *args, **kwargs):
    if rc == 0:
        print(f"[*] Thiet bi '{DEVICE_ID}' da ket noi toi Broker: {BROKER}:{PORT}")
        print(f"[*] Dang lang nghe lenh tren topic: '{TOPIC_CMD}'")
        print(f"[*] Trang thai hien tai: {current_status}")
        print("[*] Nhan Ctrl+C de dung thiet bi.\n" + "="*45)
        client.subscribe(TOPIC_CMD, qos=1)
        # Publish trang thai ban dau
        publish_status()
    else:
        print(f"[!] Ket noi that bai, ma loi: {rc}")

def on_message(client, userdata, msg):
    global current_status
    cmd = msg.payload.decode("utf-8").strip().upper()
    print(f"\n[!] Nhan duoc lenh: '{cmd}' tu topic '{msg.topic}'")

    if cmd in ["ON", "OFF"]:
        current_status = cmd
        print(f"[*] Chuyen trang thai den thanh: [{current_status}]")
        publish_status()
    else:
        print(f"[?] Lenh khong hop le: '{cmd}'. Chi chap nhan 'ON' hoac 'OFF'.")

client.on_connect = on_connect
client.on_message = on_message

print("Dang khoi dong thiet bi den thong minh...")
client.connect(BROKER, PORT, keepalive=60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\n[*] Thiet bi da tat.")
    client.disconnect()
    print("[*] Da ngat ket noi.")
