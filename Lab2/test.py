import time

print("--------------------------------------")
#return วินาที ตั้งแต่ 1 มกราคม, 1970, 00:00:00
seconds = time.time()
print("Seconds since epoch =", seconds)	
# seconds passed since epoch
seconds = 1545925769.9618232
time_since_epoch = time.ctime(seconds)
print("Time since epoch:", time_since_epoch)	
print("--------------------------------------")
print(time.asctime())
print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime()))
time_structure = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
print("Result:", time.asctime(time_structure))
print("--------------------------------------")
named_tuple = time.localtime() 
time_string = time.strftime("%d/%ฉm/%Y, %H:%M:%S", named_tuple)
print(time_string)
print("--------------------------------------")