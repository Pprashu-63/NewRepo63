
def isPalindrome(B):
	return B == B[::-1]

B = input("enter the string name ")
ans = isPalindrome(B)

if ans:
	print("Yes")
else:
	print("No")


