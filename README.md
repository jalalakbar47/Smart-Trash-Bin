# 🗑️ Smart Trash Bin (IoT-Based)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

An IoT-based smart trash bin that opens automatically using an ultrasonic sensor and servo motor controlled by a Raspberry Pi. Designed for touchless, hygienic waste disposal in homes, schools, hospitals, and public places.

---

## 📸 Circuit Diagram

![Smart Trash Bin Circuit](./docs/circuit%20diagram.png)

---

## 🧠 Features

- 🤖 **Automatic lid control** using distance sensing  
- 🔊 **Ultrasonic sensor** to detect hand proximity  
- ⚙️ **Servo motor** to open/close the bin lid  
- 🧾 **Python script** to handle sensor input and motor output  
- 🌐 **IoT concept** – part of smart city and automation systems  

---

## 🛠️ Hardware Required

- Raspberry Pi (any model with GPIO)  
- HC-SR04 Ultrasonic Sensor  
- SG90 Servo Motor  
- Jumper wires  
- Breadboard  
- Power source  
- Dustbin with attachable lid  

---

## 💻 Software / Tools

- Python 3.x  
- GPIO library for Raspberry Pi  
- Tinkercad (for simulation/design)  
- GitHub (version control & documentation)  

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-trash-bin.git
   cd smart-trash-bin
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python script:
   ```bash
   python smart_trash_bin.py
   ```

---

## 📂 File Structure

```
smart-trash-bin/
├── smart_trash_bin.py
├── requirements.txt
├── LICENSE
├── README.md
└── docs/
    ├── circuit diagram.png
    └── notes.md
```

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it for educational purposes.

---

## 🙋‍♂️ Author

**Jalaluddin Khan**  
BSCS Student | Pakistan 🇵🇰  
GitHub: [@jalaluddin-fire](https://github.com/jalaluddin-fire)
