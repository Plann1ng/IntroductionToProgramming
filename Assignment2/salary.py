
user_input = input("Provide Salaries with a gap between:")
salaries = user_input.split()
num = [int(n) for n in salaries]
num = sorted(num)
maximum_salary = max(num)
minimum_salary = min(num)
gap = maximum_salary - minimum_salary
average = sum(num)/len(num)
average = round(average)
median = num[int(len(num)/2)]
reverse = num[::-1]
rvrs_median = reverse[int(len(reverse)/2)]
even = (median - rvrs_median)*0.5
even_median = rvrs_median + even
if len(num) % 2 ==0:
    median = even_median
print(gap,average,median)
