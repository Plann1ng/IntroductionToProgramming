|                                                    COMMENT SECTION FOR VG EXERCISES                                                                         
|
|                                                            ASSIGNMENT 2
|
|                                                           SHABAN RYUSTEM
|
|                                                          NGDNS-EN / 1DV501
|
|                                                          LNU code: rs223fx
|
| P.S  I use larger font thats why the .md file can have some inaccurencies with the stylistic characters I used such as " | " , "~" if so happens, I can
| either submit next time without the special characters or you decide I'll be glad to hear your opinion about this. Just "Ctrl" + "-" for bigger font
| I am so sorry about this, but I cant see everything when the font is too close. Have a nice time reading the comments. Hope you will like it.
| Thanks for your attention. Hope you will enjoy reading it.
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| 
|                                                        COMMENT OF THE PROCCESS
|
|                                                            Exercise 9 (VG)
|
|   Write a program countdigits.py, which for any given positive number N (read from the keyboard) prints the number of zeros, odd digits and even digits of
|   an integer.
|
|
|   Line 3,4,5 > Defining variables so we can use them in the loop
|
|   Line 6 > For statement to check for each character from the user input
|
|   Line 7 - 12 > If statements to check if characters were mentioned before in the
|   input and adding +1 for each of them to our variables that we defined before the loop
|
|   Line 13 > Result
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|
|                                                             Exercise 10 (VG)
|  
|   Write a program birthday_candles.py that computes how many boxes of candles a person needs to buy each year for her/his birthday cake.
|   You can assume that the person reaches an age of 100, the number of candles used each year is the same as the age, that you save non-used candles 
|   from one year to another, and that each box contains 24 candles. Also, at the end, we want you to print the total number of boxesone has to buy,
|   and how many candles are available after having celebrated the 100th birthday.
|   
|   Line 4 > Giving range for our first loop under the name "age"
|
|   Line 6 > Another comparison for the case in Line 5 when age substracted with candles are less than 1 box
|
|   Line 9 > Nested comparison for the statement we gave in Line 5. While age - candles are divisable by 24 without remainder
|   our boxes automatically will be equal to difference between age and the candles divided by the box.
|   we use int fucntion here, because otherwise it will return us a float number which will affect the final value of the boxes and the candles.
|
|   Line 12 > One more time division of the difference, but there is one more thing to state and it is the number that we are adding.
|   We do so, because otherwise remaining candles are being negative value.
|
|   Line 13 > Our final value after all calculations will be the number of candles respecting the condition stated on Line 5 which is
|   basic mathematical computing.
|
|   Line 14 > If conditions doesnt met in the previous comparison boxes will be 0 and we basically substract candles with current age value we have
|   to get the remaining candle value.
|
|   Line 18 > While boxes are different than 0 we give print statement to be printed every time the loop executes to execute the statement
|   also to keep track and fulfill requirements stated in the exercise
|
|   Line 20 > Total number of boxes.
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|
|                                                             Exercise 14 (VG)
|
|  There are four different digits A, B, C, and D such that the number DCBA is equal to 4 times ABCD. 
|  What are the four digits? Note: to make ABCD and DCBA a proper four digit integer, neither A nor D
|  can be zero. The name of the program computing A, B, C, and D should be named abcd.py.
|   
|  Line 2 > First loop for variable A which cant be zero
|
|  Line 3 - 4 > loops for B, C which can be 0 as well
|
|  Line 5 > D loop, which cant be 0 again.
|
|  Line 6 > Multiplying the numbers of thousands hundreds tens by our variables and with 4 as well..
|
|  Line 7 > Reversing it and doing the same procedure.
|
|  Line 8 > Formatting the print statement.
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                              
|                                                                     Exercise 15 (VG)
| Assume a unit circle centred around origin inside a square with sides 2 like in the figure above. Assume also that we randomly generate N points
| (x,y) where both x and y are within the range [-1,1]  The proportion of points inside the circle should then approximately be the same as the ratio between
| between the circle area pi*R*R (which equals pi since R=1) and the square area 4. This relation can be used to compute an approximation of
| pi. Write a program pi_approx.py that computes (and prints) a pi approximation for N=100, N=10000, and 
| N=1000000. Print also the error (i.e. the absolut value of pi_actual - pi_approx).
|
|  Line 4 - 10 >  Computes the path length of the points (x0,y0), (x1,y1), ..., (xn,yn), range is starting from 1 till The value we have for 
|  N and we use the distance formula to add the sum each time the loop runs.
| 
|  Line 15 > We raise Variable N to the power of from 2 to 4 which gives us desired values.
|
|  Line 16 - 17 >The formula's ressourch https://www.mathway.com/popular-problems/Trigonometry/350117
|
|  Line 19 > Format the print statement.
|   https://www.informit.com/articles/article.aspx?p=28790&seqNum=2, abs stands for absolute value and it was necesarry for the last calculations
|
|
|
|                                                         Honest info about this exercises
| There is no way I can do it alone even tho it is easy I would not be able to figure it out. We discussed it with friends I checked on google formual and so
| on. To format adittionally also checked from Google. The link is above. So if u think i dont deserve, just take it off its totally fine for me. I putten it 
| because I wasted a lot of nerves and time.
|
|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|
|                                                                    Exercise 21 (VG)
|
|  When the union is reporting about the latest salary negotiations they are presenting the average salary, the median salary, and the salary gap
|  for the workers that they represent. Write a salary_revision.py that reads an arbitary number of salaries (integers)
|  and then reports the median and average salaries, and the salary gap. All of them should be integers (correctly rounded off).
| 
|  By salary gap we mean the difference between the highest and lowest saleries. The median salary is the middle.
|  salary (or average of the two middle salaries) when all saleries have been sorted. The easiest way to sort a list is to use the sort method in the 
|  list class.
|  
|  Line 2 > Taking user input
|
|  Line 3 > Splitting the string so we can reach each number
|
|  Line 4 - 5 > Turning them to an integer list to sort (LEcture slides 6 was on my help for arbitary numbers)
|
|  Line 6 - 7 > Maximum and minimum salary 
| 
|  Line 8 > Substarcting minimum from maximum for the gap
|
|  Line 9 > Dividing the sum of the integers from the list to the lenght 
|
|  Line 11 > Dividing the lenght of our list with 2 to get desired integer by us after sorting the list
|  
|  Line 12 > Reversing the list for the second case when there is an even number
|
|  Line 13 > Firstly we do the same procedure as for odd input 
|
|  Line 14 > Taking the difference between two mid numbers from sorted and reverse and multyplying by 0.5 to get the half of the value
|
|  Line 15 > Getting the final value for even median by adding the value  of reverse list's median value with the leftover from the calculation
|
|  Line 16 > If statement before printing for even character input.
|
|  Addittional information > https://www.wallstreetmojo.com/median-formula/ From here comes my idea to multiply by 0.5.
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                 
|                                                                 Exercise 22 (VG)
|
|  A random walk is basically a sequence of steps in some enclosed plane, where the direction of each step is random. The walk teminates when a maximal
|  number of steps have been taken or when a step goes outside the given boundary of the plane. For this task, assume a plane given by a grid, with the point
|  (0, 0) at the center. The size of the plane is given by an integer; if the given integer is k, then the values of the x and y coordinates can vary from
|  -k to k. Each step will be one unit up, one unit down, one unit to the right or one unit to the left (no diagonal movements).
|
|  Line 4 > Setting up the function
|
|  Line 6 > Resetting value of horizontal and vertical steps each time the loop runs
|
|  Line 10 > Setting up the range to -size and size since steps can be backwards as well.
|
|  Line 11 > Including range for steps inside the size loop
|
|  Line 12 - 20 > Basic comparison for direction to check if the sailor will fall with the given step range and size 
|  1 = Up , 2 = Right, 3 = Down, 4 = Left
|  
|  Line 21 > Comparison each time program being executed to check if there is something fulfilling the conditions
|
|  Line 29 > Computing the percentages to include them to the print statement
|
|  Line 34 > Formatting print statement to get smoother output 
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
