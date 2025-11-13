from datetime import datetime

# The Moscow Times
date_str1 = "Wednesday, October 2, 2002"
dt1 = datetime.strptime(date_str1, "%A, %B %d, %Y")
print(dt1)  # 2002-10-02 00:00:00

# The Guardian
date_str2 = "Friday, 11.10.13"
dt2 = datetime.strptime(date_str2, "%A, %d.%m.%y")
print(dt2)  # 2013-10-11 00:00:00

# Daily News
date_str3 = "Thursday, 18 August 1977"
dt3 = datetime.strptime(date_str3, "%A, %d %B %Y")
print(dt3)  # 1977-08-18 00:00:00
