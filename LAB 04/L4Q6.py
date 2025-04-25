print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
def print_day_with_suffixes():
    for hour in range(24):  
        if hour == 0:
            print(f"12:00 AM - Midnight")
        elif hour == 12:
            print(f"12:00 PM - Noon")
        elif hour < 12:
            print(f"{hour}:00 AM")
        else:
            print(f"{hour - 12}:00 PM")


print_day_with_suffixes()

