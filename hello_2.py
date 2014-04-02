import sys

def hello_world(s):
	print 'Hello World',s,'!'

def main(s):
	hello_world(s)

if __name__ == "__main__":
	try:
		main(sys.argv[1])
	except:
		print 'Unable to properly initiate this process!!!'
