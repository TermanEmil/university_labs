last_sum = infinity

while True:
	for each trolleybus number as nb:
		Add a minute to all given stations for trolleybus nb;
		Get the sum of squared intervals in all given stations;
		Extract the added minute;

	best_option = (Trolleybus number for which the sum was the minimum);

	if (current smallest sum is bigger than last_sum):
		break;
	else:
		last_sum = (current smallest sum);

	Add a minute to the best_option trolleybus;