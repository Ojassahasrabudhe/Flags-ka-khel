from PIL import Image

group_of_countries = ['India','Bangladesh','Pakistan', 'Srilanka', 'Bermuda' ]
score = 0.0

for questions in range(len(group_of_countries)):

	flagImage = group_of_countries[questions].replace(' ', '+') + '.jpg'

	image = Image.open(flagImage)
	image.show()

	answer = raw_input("\nWhich country's flag is this?\n")

	if answer== group_of_countries[questions]:
		print 'you are correct'
		score = score+1
		print 'your new score is below'
		print score

	else:
		print 'You loose half point, you loser!'
		score = score-0.5
		print 'your new score is below'
		print score
