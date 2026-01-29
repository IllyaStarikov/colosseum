import sys

_input = sys.stdin.read()
_input = _input.split('\n')

for pairs in _input:
	if pairs != "":
		pairs = [int(i) for i in pairs.split(' ')]
		print(abs(pairs[0] - pairs[1]))