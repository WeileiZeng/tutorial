# Ex_7_6_14.py	
def main():				
				# return list (like [mm,dd,yy])
			import string
			date = input("enter a date like\'month/day/year\': ")
			date = string.split("date","/")
			mm = eval(date[0])
			dd = eval(date[1])
			yy = eval(date[2])
			datelist = [mm,dd,yy]
			
				# return True or False
			yy % 4 == 0
			
			
			
			# return True or False
			a = [4,6,9,11]
			if dd > 31 :
				print "false"
			elif mm in a and dd > 30:
				print "false"
			elif mm > 1 and mm < 3 and dd > 28:
				print "flase"
			else:
				print "ture"
			
				
			
		
		
main()