# pip install rich
from rich.console import Console
from rich.table import Table
from rich import box

data = [
    ["Alice", "24", "New York", "🟢 Active"],
    ["Bob", "19", "Los Angeles", "🔴 Offline"],
    ["Charlie", "32", "Chicago", "🟡 Away"]
]
headers = ["Name", "Age", "City", "Status"]

console = Console()

# Create a table with rounded corners and a vibrant border color
table = Table(box=box.ROUNDED, show_lines=True)

# Add columns with distinct alignment and styling
table.add_column("Name", style="bold white")
table.add_column("Age", justify="center", style="magenta")
table.add_column("City", style="green")
table.add_column("Status", style="italic")

# Unpack and add rows
for row in data:
    print(*row)
    table.add_row(*row)

console.print(table) 

