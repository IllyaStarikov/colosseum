size = int(input())

for _ in range(size):
	string = input()
	remaining = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	for char in string.lower():
		remaining = list(filter(lambda x: x != char, remaining))
	
	if not remaining:
		print("pangram")
	else:
		print("missing {0}".format("".join(str(x) for x in remaining)))