target = 6700000
bank = 0
days = 1
for days in range(1, 31):
	while True:
		try:
			desposit = float(str(input(f"Enter the deposit amount for day {days}: ")))
			if desposit == 0:
				print("วันนี้ไม่ได้ออมเงิน ข้ามไปยังวันถัดไป")
				continue
			bank += desposit
			break
		except:
			print("Error")
	print(f"Bank: {bank} Baht")
	if bank >= target:
		print(f"บรรลุเลุป้าป้หมายการออมแล้ว")
		break
else:
		print(f"ไม่สามารถบรรลุเป้าหมายการออมได้")