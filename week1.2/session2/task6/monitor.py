# Week 1.2, Session 2: Task 6
temperature=int(input("enter the machine's temperature in celsius"))
pressure=int(input("enter the pressure in PSI"))
operational_status=int(input("""enter the machine's operating status: 
(1)=operating, (0)=stopped"""))

#temperature
if temperature > 80:
    print("temp too high, maybe shut down")
elif temperature >50 and temperature <80:
    print("temp within safe limits")
else:
    print("temp is low, no action needed")

#pressure
if pressure > 100:
    print("high pressure detected, call maintenance")
elif pressure >70 and pressure <100:
    print("pressure is stable")
else:
    print("pressure is low, system operating normally")

#operation status
if operational_status == 1:
