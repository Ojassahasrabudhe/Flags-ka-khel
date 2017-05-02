from PIL import Image

pool = ['India','Bangladesh','Pakistan', 'Sri Lanka', 'Bermuda' ]
score = 0.0

for questions in range(len(pool)):

	flagImage = pool[questions].replace(' ', '+') + '.jpg'

	image = Image.open(flagImage)
	image.show()

	answer = raw_input("\nWhich country's flag is this?\n")

	if answer== pool[questions]:
		print 'you are correct'
		score = score+1
		print 'your new score is below'
		print score

	else:
		print 'You loose half point, you loser!'
		score = score-0.5
		print 'your new score is below'
		print score 


