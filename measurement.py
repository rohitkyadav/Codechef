total_measurements = int(input("Enter the total no. of inputs: "));
measurements = [];

for x in range(total_measurements):
	x = int(input("Enter the measurement: "));
	measurements.append(x);
measurements.sort();
measurements.pop(0);
measurements.pop();
print(sum(measurements)/len(measurements));