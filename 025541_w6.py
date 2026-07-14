target = 6700000
bank = 0
days = 1
while bank < target or days > 30:
    days += 1
    while True:
        try:
            bank = float(str(input(f"Enter the deposit amount for day {days}: ")))
            break
        except:
            print("Error")
    print(f"Bank: {bank} Baht")
if bank >= target:
    print(f"บรรลุเลุป้าป้หมายการออมแล้ว")
else:
    print(f"ไม่สามารถบรรลุเป้าหมายการออมได้")