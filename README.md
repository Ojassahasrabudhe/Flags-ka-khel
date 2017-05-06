# flags-ka-khel

CS101 End Term Project. Flag quiz game in python.
Program submitted on the 5th of May, 2017.


## Contact Information

This code was written by Ojas S, a student of Ashoka University, India as an intro to programming assignment.
voice: 7744054856
email: ojas.sahasrabudhe_ug19(@)ashoka.edu.in

This program was written in `Python` programming language version 2.7.3.
You will need to install the `PIL` library to run this program. It also uses the `random` library which is pre-installed with Python.


## Objective

To show the user a flag of a country and ask to identify the country from four options.
If the user identifies correctly, then give one point. If not, deduct half a point and show the correct answer.


## Functioning

To run the code, open and run the only .py file in the folder. It is named Flags_game.py

The program has a `list` of ten countries called `group_of_countries`. More countries can be added to this list.
This `list` is shuffled everytime the program runs the for loop.
Thus some countries might get repeated.
Then there is a second `list` called `options`. This list has the zero element of the most recently shuffled `group_of_countries` list.
It adds the next three elements to the list options and then prints the list options which the user sees as his/her options to chose from.
The program then searches for the `.jpg` files of each country from the folder and displays the image.

Here the user is prompted to type the name of the country by looking at the options.
WARNING: Spelling and proper capitalization are crucial. The program does not recognise any input other than what is displayed in the options as a valid answer.

## Licence
MIT License

Copyright (c) [2017] [Ojas Sahasrabudhe]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
