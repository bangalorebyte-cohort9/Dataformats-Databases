import model

def initdatabase():
	model.createsql()


def inittables():
	model.cretetables()

def insertintotest(arg1,arg2):
	model.insertvalues(arg1,arg2)

def gettablevalues():
	return model.getallvalues()