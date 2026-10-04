destination=input("Enter your destination: ")
distance=float(input("Enter the distance in kilometers: "))
average_speed=float(input("Enter the average speed in km/h: "))

time=distance/average_speed
minutes=time*60

print("Destination: ", destination)
print("Distance: ", distance,"km")
print("Average Speed: ", average_speed,"km/h")
print("Estimated Time: ", time,"hours","and ",minutes,"minutes")

