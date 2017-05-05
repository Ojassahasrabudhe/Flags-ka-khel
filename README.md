# flags-ka-khel

CS101 End Term Project. Flag quiz game in python.
Program submitted on the 5th of May, 2017.


## Contact Information

This code was written by Ojas S, a student of Ashoka University, India as an intro to programming assignment.
voice: 7744054856
email: ojas.sahasrabudhe_ug19(@)ashoka.edu.in

This program was written `Python` programming language version 2.7.3.
You will need to inctall the `PIL` library to run this program. It also uses the `random` library which is pre-installed with Python.


## Objective

To show the user a flag of a country and ask to identify the country from four options.
If the user identifies correctly, then give one point. If not, deduct half a point and show the correct answer.


## Functioning

The program has a `list` of ten countries called `group_of_countries`. More countries can be added to this list.
This `list` is shuffled everytime the program runs the for loop.
Thus some countries might get repeated.
Then there is a second `list` called `options`. This list has the zero element of the most recently shuffled `group_of_countries` list.
It adds the next three elements to the list options and then prints the list options which the user sees as his/her options to chose from.
The program then searches for the `.jpg` files of each country from the folder and displays the image.

Here the user is prompted to type the name of the country by looking at the options.
WARNING: Spelling and proper capitalization are crucial. The program does not recognise any input other than what is displayed in the options as a valid answer.

There is a point system in place.
