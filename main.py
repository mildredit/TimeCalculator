from time_calculator import add_time
from unittest import main 


print(add_time("11:43 PM", "24:20", "monday"))

print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("11:59 PM", "24:05"))

main(module='test_module', exit=False)
