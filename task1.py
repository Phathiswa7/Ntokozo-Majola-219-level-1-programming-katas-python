def multiples(multiples_sum_value):

				sum = 0
    for counter in range(1,multiples_sum_value):
    				if counter % 3 == 0 or counter % 5 == 0 :
        				sum += counter
    print(sum)  
