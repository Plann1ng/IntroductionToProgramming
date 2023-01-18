~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                                         											   |
|									Ryustem Duran Shaban									   |
|																				   |
|									   LNU ID:rs223fx                                                                          |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|																				   |
|                                                                         Exercise 3 (VG)                                                                          |
|                                                                                                                                                                  |
|                                                                             Task                                                                                 |
|                                                                                                                                                                  |
|  The output in Exercise 2 is not very pretty. Write a program pretty_print_subdirectories.py that works like print_subdirectories(dir_path) in Exercise 2 but    |
|  gives an indented print where the directory depth is given by the indentation (see example below) and avoids printing hidden directories (names starting with   |
|  . (dot) or _ (underscore)).     																   |
|                                                                                                                                                                  |
|                                                                           Solution                                                                               |
|                                                                                                                                                                  |
|  Import os, give path and run for loop with 3 variables, because path itself is with 3 layers which are directories, subdirectories and files in them. Secondly  |
|  use basename and startswith method to get rid of files starting with dots and underscores. Give variable to keep on track directory depth. Firstly replace the  |
|  whole path with empty string and then use count method to count out the separators we are getting, which are indicators for depth. Bigger the count(os.sep)     |
|  bigger the indent will be. Adittionally set variable indent which will be string with 4 empty spaces. Lastly print formatted string first curly brackets for    |
|  the directory depth (indent* dir_level[seperator value]) and second brackets are to be filled with basename of the directory paths. Extra information sources   |
|  for <os.walk> , <os.path.basename>, <os.sep> are given on the bottom of the program as comment.                                                                 |
|																				   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|																				   |
|                                                                          Exercise 7 (VG)                                                                         |
|																				   |
|                                                                               Task                                                                               |
|																				   |
|  It has been a lot of programming in this course. But how many lines of Python code have you actually written? Write a program count_lines.py containing a       |
|  function count_py_lines(dir_path) returning a count (an integer) of all the non-empty lines in all Python files (ending with .py) in the directory specified by |
|  dir_path and all its subdirectories (transitively).                                                                                                             |
|																				   |
|                                                                             Solution                                                                             |
|																				   |
|  Name the function and start with setting up a counter. Os.walk for each file and we give 3 variables again for the 3 layers of walking method. Accesing files   |
|  layer and setting up a for loop "names" . Setting up a if statement to collect python programs. Give a new path which is basically the main root and formatted  |
|  separator followed with python file name. The program does this for every program. Open the programs with the new path. One more for loop to ignore the empty   |
|  empty lines and add 1 each time the whole program executes                                                                                                      |
|																				   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|																				   |
|                                                                           Exercise 9 (VG)                                                                        |
|																				   |
|                                                                                Task                                                                              |
|																				   |
|  In this exercise we will once again use the two text files eng_news_100K-sentences.txt and holy_grail.txt that we used in Exercise 6.                           |
|  Knowing the character frequencies for a language has many important applications in cryptoanalysis.                                                             |
|  Write a program letter_count.py that: Reads a text file. Windows users having a problem reading these files can try to use open(..., encoding='utf-8') when     |
|  reading the files. Feel free to use the output from Exercise 6 if you like to. Use a dictionary to count the numbers of times each letter (a-z, upper case      |
|  as lower case letters) is occurring in the files. Notice: Upper case letter are turned into lower case letters and you.                                         |
|  only need to count occurrences of the English letters abcdefghijklmnopqrstuvwxyz. Letters with accents and non-English letters can be ignored.                  |
|																				   |
|                                                                             Solution                                                                             |
|																				   |
|  Give both paths inside a list attached to a variable. Open them under for loop. One more for loop for lines. Strip lines to manipulate each word.               |
|  Another loop for characters to add characters to our dictionary or increase their value. Print statement that includes os.basename. Setting up star value as    |
|  the minimum coefficient of the values in the dictionary in order to not get an letter wtih empty star. Last loop to iterate the keys in the dictionary          |
|  formatted printing letters and stars times dictitionary value(count of letters) divided by the minimum character occurance.                                     |
|																				   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~