def packets_arrived(T, M):
    ##########   Base Case ###########################################
    if T == 1:                              #if T=1, all the packets will arrive in same time slot
        return [[M]]
    
    ########## Recursive Case #######################################
    patterns = []                           #initiating empty array
    for i in range(M+1):
        remaining_patterns = packets_arrived(T-1, M-i)          #Generate every other arrival sequence possible for the remaining time slots.
        # insert current slot's arrival count to the beginning of each pattern
        for pattern in remaining_patterns:                      #for loop to append time slot as vectors
            patterns.append([i] + pattern)
    return patterns

# prompt for the values of T and M 
T = int(input("Enter the number/value of time slots (T): "))
M = int(input("Enter the number/value of packets (M): "))

patterns = packets_arrived(T, M)           #pushing the patterns into array patterns

# printing the arrival patterns 
for count, pattern in enumerate(patterns, 1):   #used enumerate to count the number of potential outcomes
    print(pattern)
 
print("number of potential outcomes : ",count)
