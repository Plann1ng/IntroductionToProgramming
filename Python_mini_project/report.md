# Mini-project report
Members: Ryustem ShabanProgram: Network Security
Course: 1DV501
Date of submission: 2021-11-03

## Introduction
The mini project is about understanding BST map and Hashing. In this project we will use the two large word files from 100k sentences and holy grail from assignment 3 and implement to both BST map and hash set. The first exercise is to use set and dictionary to identify top 10 frequent words and unique word. The second exercise is to implement words from the two large file into BST map and hash set. The third exercise is two use BST map to find the top 10 frequent words and use hash set to fine unique words. By the end of this project we should understand how BST map and Hashing work.
## Part 1:
The word count for holy_grail that we used in our mini project was ```11267``` (This was the output from previous the assignment) and
for the eng_news_100k-sentences it is ```1931072```

Counting the unique words in each file was done using the ```count_unique()``` function.
The idea of this function was to simply read the text file and split each word in it. The function will return the set length of the text, while duplicates will be automatically ignored, as it is a set.

To get the most frequent words the ```count_occurencies()``` function was used.
The function provides an empty dictionary. The same as in the previous function, the text is read and split into separate words. The for loop checks whether each word in has a length of more than four. If that is the case, the word is added to the dictionary as key with a value of zero. If the word already exists in the dictionary, its value will be increased by one.
(Idea was taken from the exercise 8 from assignment 3)

Finally, the ```main()``` function was added which provides an automated way to run both files and fill the arguments required for the functions.


### 100k sentences
The 100k sentences text file had ```94980``` unique words.
The ten most frequent words are: 
```py
their	6121
about	4593
would	3866
people	3684
there	3665
which	3566
after	2969
first	2872
years	2777
other	2729

```
### Holy grail
The holy grail text file had ```1879``` unique words. The ten most frequent words are:
```py
arthur	    261
launcelot   102
knight	    84
galahad	    81
father	    76
bedevere    68
knights	    65
robin	    58
guard	    58
right	    57
```
## Part 2: Implementing data structures
### Binary Search Tree
The first function of the ```BstMap``` adds values to the tree after comparing the value attached to the key.
The ```put()``` function was implemented in the following way.
The first comparison done, is always with the root. Depending on the values and the order of the element, each node is compared with the leaf. If the value of the element is less, then the element will go to the left side, otherwise it will go to the right side.
To automate and continue this process, recursion is used to call the function once more, so it will continue this process until it finds an empty spot to put the new node.

On ```to_string()``` function provides an empty string under the variable "s" and adds the nodes starting from left to the right using recursion of the function for each depth level until it gets to the level where LHS and the RHS of the tree is empty.

The ```count``` function starts from default value 1 and checks and adds value from left to right side by using recursion.

After that follows the ```get()``` function.
The function will check for the given key and will return the key value attached to that key accordingly.
Default value ```'v'``` is set to be None. First, the if statement checks whether the tree has no leaves and only the root. If the tree is not empty, the value of the element is compared to the leaves. Recursion is used until the function reaches the point where it finds the key that is in the Tree and returns it.
if key is not in the tree function, it will return ```None```.

The ```max_depth()``` function starts from the default case where tree has only a root and no leaves, default depth for the root only is 1. If the Tree has nodes attached, the two default value pairs for left and right side will be set.
Starting from the left side to the bottom and then from the right side all the way to the bottom. 
In the end, the max value of the side is returned to see which has the biggest depth value.

Finally, we have the ```as_list()``` function, which basically returns a list of key and value pairs.
Starting from the left and to check if the LHS is empty, if that is not the case then recursion is used until all the way through the tree and everything is added to the empty list, that was provided by the user. Exactly the same is done for the right side.
The reason behind starting from left side is to sort the values from smaller to greater and afterwards return the list which is filled with the elements of the tree.

All output for the ```bst_main.py``` file shows the results that are given as solutions in the comments. 

### Hash Set
The ```get_hash()``` function was implemented in the following way.
The ```get_hash()``` function takes word as user input and loops for each character in the word. We have the default hash value 'hv' with a start value of 0. For each letter we take the ascii value, sum it up as a hash value by adding it to the empty 'hv' variable and returning it for each word.

The ```add()``` function was implemented the following way. 
Before putting the element in the hash set, the first ```if``` statement checks whether the element is already in the hash table. This way, the set contains every element only once and duplicates are discarded.
If the element does not exist in the set yet, its hash value is calculated by calling the ```get_hash()``` function. This hash value is needed, so it can be decided in which bucket the element needs to be stored. The hash value is divided by the current amount of buckets and the integer result gives the bucket index.
When the bucket index is found, the element can be stored at the correct location and the total element size will be increased by one.
Lastly the second ```if``` statement checks whether rehashing is necessary by comparing the bucket size to the total amount of elements in all buckets.

When adding elements to the hash table, the hash table needs to rehash, once it fills up. As it is not known how big the hash table needs to be when initiating it, the rehashing doubles the size of the hash table every time the total amount of elements exceeds the amount of buckets.
To achieve this, the ```rehash()``` function was implemented. It was implemented according to the explanation in the lecture slides.
First, all previous data needs to be saved by copying each element in a new list. All elements in the hash set will be deleted, so the size of the empty hash set can be doubled and the data can be sorted into the correct bucket based on the updated bucket size.

The ```contains()``` functions calculates the location of a certain element by getting its hash value and dividing it by the amount of buckets in hash table, to check if the element already exists in the hash table. This function is often called in previous functions to avoid duplicates in the set.

The ```remove()``` function works similar to the add function with the slight change of the ```.remove(element)``` functionality for the corresponding list in a bucket and decreasing the size of the total element amount by one. As an element is removed and not added, rehashing is not necessary either.

The ```max_bucket_size()``` function goes through each bucket and counts the elements in it. If the element size of one bucket is bigger than the previous one, it is declared the maximum. Every time a bucket size is counted it is compared to the maximum and updated, if the current size exceeds the maximum. If the the current bucket size is smaller or equal to the maximum, the maximum stays the same. Once the size of all buckets is counted and compared, the maximum bucket size is returned.

All output for the ```hash_main.py``` file shows the results that are given as solutions in the comments. 

## Part 3:
All output results for part 3 are the same as the output result for part 1.
Every part of task 3 has a corresponding function which are called in the ```main``` function to display all results for each file.
Each function initiates a new hash set or clears a previous binary search tree and fills it up again, to avoid confusion. This also results in the output being slower. Especially the ```top10()``` function takes some time, but it will display the correct results (the same results that appear in part 1).
The ```read()``` function was implemented to avoid duplicate code, it reads the files once and saves all words in a list. The following functions all take the list of words as parameter to loop through it.
### 3.1
The unique words in each file are counted by using the hash set. To add all words to the hash table, a for loop that goes through each word in the word list and adds them to the hash set by calling the ```add()``` function, was implemented.
Once the hash table is filled up with all words, the ```get_size()``` function is called to display the total number of elements in the set. 
Since the hash table functions like a set, it was implemented in a way that duplicate elements (in this case words, that already exist in the hash table) are ignored and not even added to the hash table. 
The number of unique words in the 100k sentences file is ```94980``` and the unique number of words in the holy grail file is ```1879```
### 3.2
To figure out the top ten most frequent words in each file, the ```top10()``` function was implemented in the following way.
Once more we start with empty string to collect information to it for the output that will be returned from the function.
Used ```continue``` to interact over the loop(Other methods can be used, but continue seemed to be the fastest and best choice).
If the length of the word is less than desired it will stop the loop and go for the next word. The comparison is with '5' since the index starts from 0. 
Using ```get``` from BstMap to get the value for the word(Appearance) and if it is not Empty for each time loop runs we will add to the value + 1 under the name of the variable 'nc' (Stands for new count) and put them to the BstMap with the key(word) and value ('new count'[appearence]) and if the word was not registered already it will add it with default value 1.
To print the top 10 used lambda again as one line function. The rest is just returning the outputs from the functions.
### 3.3
The main part of this task was to call the ```max_bucket()``` function, since the hash tables were already filled up with all words from the previous task 3.1.
The 100k sentences file has a maximum bucket size of ```304``` and the holy grail file has a maximum bucket size of ```17```.
### 3.4
Similar to task 3.3, this task was mainly done by calling the ```max_depth()``` function for the binary search tree.
The 100k sentences file has a max depth of ```13``` and the holy grail file has a max depth of ```9```.
After the presentation, we have been told that this functions must have had some issues, because the numbers cannot be right, so we did some last minute corrections and are now left with the results of ```43``` as the max depth for the 100k sentences file and a max depth of ```25``` for the holy grail.
Apperiently the problem was faced while trying to return the maximum value of the two sides of the tree with the line below
`return 1 + max(left_depth, right_depth)` was not doing what we was expecting. The main idea for it was to take both values into a tuple and just to return the max of them with built in python method. Since had no clue what the correct answer should look like and not exactly same results coming out from everyone we had kept that. But seems like instead of overcomplicating it
we could've just used counter to keep track of the depth while reccursion goes for the both sides, as we do now after Mr.Flygt's question during the presentation.
## Project conclusions and lessons learned
The project was a challenge for everyone in the group. Most of the time was spent trying to understand the concept of both the BST map and the Hashing table. Hence, we spent most of our time on part 2 of the project. To use our time efficiently we decide to assign functions or small parts to different group member. For example we had two people work on BST map and the rest working on Hashing, this way it was possible to work on two parts at the same time. We communicated through discord, exchanging ideas and helping each other, if needed. We had physical group meetings at least twice a week. For this project we spend average of 20 hours per week to work.
As previously mentioned, most communication was done over discord. It was used to schedule group meetings, divide work, compare and discuss small code snippets, as well as have short calls to stay updated on what work needed to be done and was not yet completed.
Whenever necessary, physical meetings were scheduled to work on code together, show progress and explain written code or discuss possible solutions for parts that still needed to be done.

### Technical issues
We were not faced with many technical issues, but working together on git turned out to be harder, because we are not that familiar with it. Everyone was working on their own version of a solution or even multiple ones, which made it hard to figure out which one the final version should be.
Since working on the same file in git can easily cause conflicts, we sometimes ended up sending code snippets back and forth on discord.
Sometimes we would have multiple times the same files on git and ended up picking stuff that was working from some files and used it in other ones.
### Project issues
When working in a group with multiple members, it is always difficult to manage time and make sure that every group member is available for meetings. We tried to avoid that issue as best, as possible by mainly communicating over discord to keep everyone updated.
As we implemented part 3, we stumbled upon the issue that the hashing table takes a long time to show its results, but quickly solved it by chnaging the ```get_size()``` function.

#### Ryustem Shaban's Conclusion
Was working on Part 1, Part 2 BstMap, Part3.
All in all the project was a lot time consuming for someone without previous coding experience and sometimes I was getting lost on the second exercise reasoning some functions and was facing difficulties to use the root and node combination in the BstMap.py. That took me a lot of time and effort to understand. My other issue was the commits that I was making to gitlab, why I say that is because I almost always have at least 3 variants for each problem which are partly working and I keep them to keep the track of my idea, but when my teammates are checking them it is hard and time consuming for them which I can relate since they have to run each one of them and see which one is working (Will work on that to improve.).
Other issue for me was to figure out how to use the combination of the tree and HashSet to fulfill the requirements for Exercise 3. It was not that big deal, got the main idea for the first 20 minutes of thinking, but to implement sometimes can be
times and times harder. Had a lot of typos for the exercise 2 also, i.e ```left.depth = self.right.max_depth(), which were not a big issue, but sometimes can be discouraging.
Last, but not least, the busy schedule. Sometimes was hard for me even to go to meetings or get in touch with the team members since I was bad with math and both exam and the mini project happened to be at the same time. If I had more time I would love to give a try for the VG exercise, but consequences and I feel a little pity that the team is supposed to present that version 
of the program, because I know it could still be faster and more efficient in therms of time complexity.
It was fun to work as a group and try to see other perspectives.
