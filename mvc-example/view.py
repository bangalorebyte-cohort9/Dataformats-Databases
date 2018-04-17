import controller


if __name__ == '__main__':

	testid = int(input('Enter a test id'))
	testtext = input('Enter the text ')

	controller.initdatabase()
	controller.inittables()
	controller.insertintotest(testid,testtext)

	print(controller.gettablevalues())
