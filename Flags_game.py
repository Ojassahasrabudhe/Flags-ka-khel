from PIL import Image
import random 
# I have imported Image library from PIL in onder to use images in my code. I have not completely understood what work a library does, but I read I need to do this on Stackexchange.
# I have imported random to facilitate the random shuffle command which is used to give options randomly.

group_of_countries = ['India','Bangladesh','Pakistan', 'Srilanka', 'Bermuda', 'Argentina', 'Brazil', 'Peru', 'Mexico', 'Canada' ]
score = 0.0

#I have written score outside the for loop because we want the score to be added with every answer. I had previoulsy written the score in the for loop and this lead to score becoming zero with every new question.

#I have created list of 10 countries for my game. The code lifts a country as per the written sequence, and then adds .jpg to the name of the element and picks up the image.

print 'Your options are'
print("\n".join(map(str, group_of_countries)))
print random.shuffle(group_of_countries)

#The above commands were written entirely by trial and error method. But they work!!
#I am essentially printing out the entire list such that every element prints on a new line.
# Then I shuffle the list and the program picks it up below! woah. I don't know how it decides which list to choose. The randomised one or the original one!?

for questions in range(len(group_of_countries)):

	flagImage = group_of_countries[questions].replace(' ', '+') + '.jpg'

	image = Image.open(flagImage)
	image.show()

	#print ' Your options are'
	#random.shuffle(group_of_countries)
	#print (group_of_countries) 
	#print("\n".join(map(str, group_of_countries)))

	#Here I print'your options are' and in the next line I print the list of all the countries on the quiz in a random fasion.
	# I need to figure out how to print only four random elements which also includes the answer element.
	



	answer = raw_input("\nWhich country's flag is this?\n")
	#here if the answer matches the element of the list, then it will consider answer to be correct and add a point.

	#Below, is just the algebra for checking the answer and then adding or subtracting points from the score.

	if answer== group_of_countries[questions]:
		print 'you are correct'
		score = score+1
		print 'your new score is below'
		print score

	else:
                #print 'Incorrect answer '
		print 'The correct answer is below'
		print group_of_countries[questions]
		#Now the latest edit done above makes the code show the correct answer when answered incorrectly.


		print 'But you loose half point, you loser!'
		score = score-0.5
		print 'your new score is below'
		print score

	if score >= 9.0:
		print 'you have played too much'
		break
# I have added this feature just to make the code bit longer and funny.
