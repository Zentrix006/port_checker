

# 🔍 Port Scanner  

A **multi-threaded port scanner** built with Python that quickly scans a target domain for open ports using `socket` and `concurrent.futures`. Uses `rich` for a beautiful CLI output!  

## ⚡ Features  
✅ Fast, multi-threaded scanning  
✅ Custom port range selection  
✅ User-defined timeout for flexibility  
✅ Clean & stylish output with `rich`  

## 🚀 Installation  
```bash
pip install rich
```

## 🛠️ Usage  
```bash
python port_scanner.py
```
- Enter the **target domain**  
- Specify the **port range** (e.g., `20-1000`)  
- Set **timeout** (default: `1s`)  

## 📌 Example Output  
```plaintext
PORT SCANNER  
By ZENTRIX  

Enter the domain name: example.com  
Enter the range of ports to scan (format: start - end): 20-1000  
Enter timeout in seconds (default is 1s): 1  

┌──────────┬──────────┐
│   Port   │ Status   │
├──────────┼──────────┤
│   22     │ Open     │
│   443    │ Open     │
└──────────┴──────────┘  

Scan complete! Found 2 open ports.  
```

## 🎯 Why Use This?  
🔹 Ideal for **pentesters** and **network security analysts**  
🔹 Quick & efficient **reconnaissance tool**  
🔹 Simple yet effective for **open port enumeration**  

💻 **Contributions & feedback are welcome!** 🚀  

