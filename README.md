# 🗑️ Smart Trash Bin System

An IoT-based Smart Trash Bin built using Raspberry Pi, ultrasonic sensor, and a servo motor. This system automatically detects when a person is near and opens the lid, promoting contactless and hygienic waste disposal.

---

## 🚀 Features

- 🤖 **Automatic lid opening/closing** using distance sensing  
- 📡 **Ultrasonic sensor-based object detection**  
- 🧠 **Simple and modular Python code**  
- 💰 **Low-cost components** (can be built at home)  
- 🏥 **Ideal for smart homes, hospitals, schools, and public places**  

---

## 🛠️ Components Used

| Component         | Description                              |
|------------------|------------------------------------------|
| Raspberry Pi      | Main controller                          |
| Ultrasonic Sensor | Distance measurement (e.g., HC-SR04)     |
| Servo Motor       | Lid movement                             |
| Jumper Wires      | For connections                          |
| Breadboard        | Circuit assembly                         |

---

## 📷 Circuit Diagram

![Smart Trash Bin Circuit] 
(./A_schematic_diagram_of_a_Smart_Trash_Bin_circuit_i.png)



## ▶️ How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script**:
   ```bash
   python smart_trash_bin.py
   ```

> ⚠️ **Note:** Make sure to run this on a Raspberry Pi or similar board with GPIO support.

