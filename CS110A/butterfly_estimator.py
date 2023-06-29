
'''
Instructions:
 write a program that takes an input of male and female butterflies.
 calculate their population estimates.
 Find Total butterflies, their sex ratio, variance, gender difference, and mating pairs.
 '''

print("Butterfly Estimator\n")

# takes in input form the user.
males = int(input("Enter the estimated number of male butterflies: "))
females = int(input("Enter the estimated number of female butterflies: "))

# calculations
total_butterflies = males + females

sex_ratio = males / females

# use of absolute method so that we donot get a negative value
gender_difference = abs(males - females)

# using min so we dont over estimate the amount of mating pairs at one instance
# for total mating pairs we could multiply males and females
mating_pairs = min(males , females)

# variance is the measure of spread between the numbers in a dataset.
mean = (males + females) / 2
variance = (((males - mean) ** 2) + ((females - mean) ** 2)) / 2

# prints the necessary outputs.
print ("\nTotal Butterflies : ", total_butterflies)

print ("Sex Ratio : ", sex_ratio)

print ("Gender Difference : ", gender_difference)

print ("Mating Pairs : ", mating_pairs)

print ("Variance : ", variance)


'''
The variance is calculated as the average of the squared differences from the mean.
The formula for variance is (Xi - mean)^2 / n where Xi is the value of ith data point and n is the total number of data points.
In this case, we have two data points and we used the mean of these two data points as the average for variance calculation.
'''
'''
This activity is to get familiar with the math operators in python.
The operators I didnot use are the floor division operator '//', modulo operator '%'
The floor division operator rounds the result down to the nearest integer/whole number
and the modulus operator returns the remainder after division.
'''