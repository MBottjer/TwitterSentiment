def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))

removeNonAscii("回比は")