
# 📊 Automated Platform Surveillance System

## 📌 Overview

The **Automated Platform Surveillance System** is a Python-based monitoring tool that tracks system resources such as CPU, RAM, Disk usage, and running processes.
It automatically generates detailed log files at regular intervals for analysis and monitoring.

---

## 🚀 Features

* Monitors CPU usage
* Tracks RAM (Memory) statistics
* Analyzes Disk usage
* Lists running processes with memory usage
* Generates timestamp-based log files
* Supports automatic scheduling
* Command-line based execution

---

## 🛠️ Technologies Used

* Python
* psutil – System monitoring
* schedule – Task scheduling
* os, sys, time – Core Python modules

---

## 📂 Project Structure

```
Automated-Platform-Surveillance-System/
│
├── surveillance.py
├── Logs/
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Install required libraries

```
pip install psutil schedule
```

---

## ▶️ Usage

### Help Command

```
python surveillance.py --h
```

### Usage Instructions

```
python surveillance.py --u
```

### Run the Script

```
python surveillance.py <TimeInterval> <DirectoryName>
```

### Example

```
python surveillance.py 5 Logs
```

This will generate a log file every 5 minutes inside the Logs folder.

---

## 📝 Log File Details

Each log file contains:

* Timestamp of log creation
* CPU Usage
* RAM Details (Total, Used, Available)
* Disk Usage
* Running Processes (PID, Name, Memory Usage)

---

## ⚠️ Error Handling

* Handles invalid command-line arguments
* Skips inaccessible processes
* Validates directory creation

---

## 📈 Future Enhancements

* Email alerts for high resource usage
* Web dashboard for real-time monitoring
* Graphical visualization of logs
* Database storage instead of log files

---

## 👨‍💻 Author

Varad Muley

---

## 📜 License

This project is open-source and free to use for educational purposes.
