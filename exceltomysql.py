# Author : Kethu Harikishan Reddy
# Email: kishanreddy.kethu@gmail.com
# Description: This is the file for extracting data from an excel file and connect to a running MySQL server to build a database as it is exactly in the excel file.
# 			   The first row of the excel file will be taken as the column names of the table.
# 			   Presently, the data is actually getting stored as strings in the database. Hopefully, I'll have a workaround in the future.
# 			   Tested on MySQLdb version 1.2.5 and xlrd 0.9.3 and MySQL Version 5.6.17 on Windows 8 64-bit machine with Python 2.7.6 AMD64 installed.
import xlrd # Module for reading excel files
import MySQLdb as ms # Module for MySQL-Python api
def main():
	# The following line selects sheet 1 of the given Excel file.
	# Make sure there's only one sheet in it. Else, it takes first one.
	x = raw_input("\nIs everything ready?\n(Type y/n and press enter)\n")
	if x == 'y' or x =='Y':
		filename = raw_input("Please Enter the file name to export(with .xlsx or .xls etc.):\n")
	else:
		main()
		return
	try:
		book = xlrd.open_workbook(filename,'utf8')	# The file to convert.
	except Exception, e:
		print "\n\nThe file with the given name was not found!\n Restarting......\n"
		main()
		return
	sheet = book.sheet_by_index(0)	# The sheet we're working on.
	# The following line is the one which connects to the running instance of MySQL server.
	# Change the values accordingly.
	con = ms.connect(host="localhost", port=3306, user="root",passwd="NO")
	cu = con.cursor()	# The handle for the connection.
	row_num = sheet.nrows 	# No. of rows in file.
	col_num = sheet.ncols 	# No. of columns in file.
	if "xls" in filename:
		if "xlsx" in filename:
			name = filename.replace(".xlsx","")
		else:
			name = filename.replace(".xlsx","")
	cu.execute("create database ",+name)
	cu.execute("use "+name)
	tab_str = "create table data" # Initial part of string while creating a table.
	col = [] # List that gets all field names.
	cols="(" # String that has all field names while using "insert into" statement,
	fields = "(" # The string used with values of size of input while creating the table.
	for y in xrange(0,col_num):
		col.append(str(sheet.cell(0,y).value).replace(" ","").replace("'",""))
		if y != (col_num - 1):
			fields = fields + str(col[y])+" varchar(255)," # Data gets truncated automatically if more than 200 characters.
			cols += str(col[y])+","		
		else:
			fields = fields + str(col[y])+" varchar(255))"
			cols += str(col[y])+")"
	# print "Trying ",str(tab_str+fields)
	cu.execute(str(tab_str+fields))
	ins_str = "insert into data "+cols+" values (" # Initial part of the insert command.
	for x in xrange(1,row_num):
		value = ""
		print "In row ",x+1
		for y in xrange(0,col_num):
			cell = sheet.cell(x,y)
			if cell.ctype == 3: # xldate type.
				# 3 means 'xldate' , 1 means 'text' , 2 means 'number'
				# converting date from the  excel file in float format to proper dd-mm-yyy format.
				year, month, day, hour, minute, second = xlrd.xldate_as_tuple(cell.value, book.datemode)
				date = str(day)+"-"+str(month)+"-"+str(year)
				if y==(col_num - 1):
					value += "'"+str(date)+"'"+")"
				else:
					value += "'"+str(date)+"'"+","
			else:
				if cell.ctype == 2: # Number type.
					if y==(col_num - 1):
						value += "'"+str(int(cell.value)).replace("'","")+"'"+")" # Removing the "'"s in the data because they mess up the "'"s already being used to create tables and store data as strings.
					else:
						value += "'"+str(int(cell.value)).replace("'","")+"'"+","
				else: # Text or anything other than number and date
					if y==(col_num - 1):
						value += "'"+cell.value.replace("'","").encode('utf8')+"'"+")"
					else:
						value += "'"+cell.value.replace("'","").encode('utf8')+"'"+"," # The encoding is in case there is a weird character in the text like /xc2 or /xbf. It actually happens!
			# print "In row ",x+1," column ",y+1,":"
			# print "Trying ", str(ins_str+str(value))
		cu.execute(str(ins_str+value))
		# print value
	con.commit() # This is the most important line. It commits all the insert commands to the server like git. Else, you'll have to use autocommit feature of MySQLdb which I don't suggest because you either need the "whole" database or you don't.
	cu.close() # Closing the handle.
	con.close() # Closing the connection. Else, some free connections might interfere with ongoing connections.

if __name__ == '__main__':
	main()