def add_time(start,duration,*day):
	weekDays={"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
	key_list = list(weekDays.keys()) 
	val_list = list(weekDays.values()) 
	a=start.split(":")
	b=a[1].split(" ")
	x=[a[0],b[0],b[1]]

	sHour=int(x[0])+(12 if x[2].upper()=="PM" else 0)
	sMinute=sHour*60+int(x[1])

	y=duration.split(":")
	z=sMinute+int(y[0])*60+int(y[1])
	
	eMinute=z%60
	eDay=int(int((z/60))/24)
	eHour=int((z/60))%24

	p=str((eHour-1)%12+1)+":"+str(eMinute).zfill(2)+" "+("AM","PM")[eHour>=12]

	if(len(day)>0):
		p=p+", "+key_list[val_list.index(int(weekDays[day[0].capitalize()]+eDay)%7)]

	if(eDay>0):
		if(eDay==1):
			p=p+" (next day)"
		else:
			p=p+" ("+str(eDay)+" days later)"
	return p
