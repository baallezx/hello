import sys

def welcome(username):
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome User:<',username,'>\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n',';)\n\n'*28

def main(arg1):
	welcome(arg1)

if __name__ == "__main__":
	main(sys.argv[1])

