import socket
import concurrent.futures
from rich.console import Console
from rich.text import Text
from rich.table import Table

console = Console()

# Fancy banner
console.print(Text("PORT SCANNER ", style="bold red"), style="on green")
console.print(Text("By ZENTRIX", style="bold red"), style="on violet")

# Get domain
while True:
    try:
        domain = input("Enter the domain name: ")
        target = socket.gethostbyname(domain)
        break
    except socket.gaierror:
        console.print("[bold red]Invalid domain! Please enter a valid domain.[/bold red]")

# Get port range
while True:
    try:
        port_range = input("Enter the range of ports to scan (format: start - end): ")
        start_port, end_port = map(int, port_range.split('-'))
        if start_port < 0 or end_port > 65535 or start_port >= end_port:
            raise ValueError
        break
    except ValueError:
        console.print("[bold red]Invalid port range! Please enter a valid range (e.g., 20-1000).[/bold red]")

# User-defined timeout
timeout = float(input("Enter timeout in seconds (default is 1s): ") or 1)

# Rich table for output
table = Table(title=f"Open Ports on {target}")
table.add_column("Port", style="cyan", justify="center")
table.add_column("Status", style="green")

def port_scanner(port):
    """Scan a single port"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((target, port))
            return port  # Return open port
        except:
            return None  # Return None if closed

# Use ThreadPoolExecutor for efficient scanning
open_ports = []
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(port_scanner, range(start_port, end_port + 1))

# Display results
for port in results:
    if port:
        table.add_row(str(port), "Open")
        open_ports.append(port)

console.print(table)

if not open_ports:
    console.print("[bold red]No open ports found![/bold red]")
else:
    console.print(f"[bold green]Scan complete! Found {len(open_ports)} open ports.[/bold green]")