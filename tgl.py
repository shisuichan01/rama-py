from datetime import datetime
now = datetime.now()
dd = str(now.day)
mm = str(now.month)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)
