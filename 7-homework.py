import matplotlib.pyplot as mplot
data = [ 1, 3, 15, 26, 27, 32, 64, 80, 100, 131, 200, 223, 229, 240, 253 ]
mplot.plot( data )

data_str = "\n".join( [ str( item ) for item in data ] )

with open( "data-test.txt", "w" ) as testdatafile:
	testdatafile.write( data_str )

mplot.show()