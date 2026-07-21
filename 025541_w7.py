##variable
tax_payers = ()
tax_goal = ()
balance = int()
leftover_credit = ()
horse = r"""
  .  ,
  |\/|
  bd "n.
 /   _,"n.___.,--x.
<co>'\             Y
 ~~   \       L   7|
       H l--'~\\ (||
       H l     H |`'    -Juan (horse accountant)
       H [     H [			
  ____//,]____//,]___
		  	"""
##func
def dash(value):
	print("-" * value)
def dash2(value):
	print("=" * value)
def under_dash(value):
	print("_" * value)
def upper_dash(value):
	print("‾" * value)
def jackson_dash(value):
	print("\\" * value)
def reverse_jackson_dash(value):
	print("/" * value)
def star(value):
	print("*" * value)
def hash(value):
	print("#" * value)
def sixseven(value):
	print("67" * value)
##code
under_dash(50)
dash(50)
print(horse)
dash2(50)
while True:
	dash(50)
	try:
		tax_payers = int(input("Enter the number of people: "))
		under_dash(50)
		dash2(50)
		upper_dash(50)
		tax_goal = int(input("Enter the tax goal: "))
		dash2(50)
		upper_dash(50)
		break
	except:
		print("Error")
while balance < tax_goal:
	reverse_jackson_dash(50)
	jackson_dash(50)
	for i in range(0, tax_payers):
		dash2(50)
		while True:
			try:
				balance += int(input(f"Enter tax amount for person number {i+1}: "))
				under_dash(50)
				dash(50)
				print(f"Total tax collected: {balance}")
				upper_dash(50)
				print(f"Tax goal: {tax_goal}")
				upper_dash(50)
				break
			except:
				print("Error")
if balance >= tax_goal:
	star(50)
	dash2(50)
	print(f"Tax goal achieved with a total of {balance} collected.")
	dash2(50)
	leftover_credit = balance - tax_goal
	dash(50)
	print(f"Leftover credit: {leftover_credit}")
	dash(50)
	upper_dash(50)