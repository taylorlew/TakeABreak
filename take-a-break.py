import os
from flask import Flask, url_for, render_template, request
from flask import redirect

app = Flask(__name__)
class takeABreak():
  
	about1 = 0
	about2 = 0
	about3 = 0
	answers1 = 0
	answers2 = 0
	answers3 = 0
	answers4 = 0
	answers5 = 0
	results = ""
	finalResults = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	#Home page
	@app.route('/')
	def renderMain():
		return render_template('home.html')

	#start over
	@app.route('/startOver')
	def startOver():
		return redirect(url_for('renderMain'))

	#about page
	@app.route('/about')
	def renderAbout():
		return render_template('about.html')

	#gets the answer of the first question
	def process_about():
		if request.form.get('Submit', None) == 'POST':
			return redirect(url_for('page1'))

	#first set of questions time alloted for break
	@app.route('/page1', methods=['GET', 'POST'])
	def renderPage1():
		takeABreak.about1 = request.form['mood']
		takeABreak.about2 = request.form['day']
		takeABreak.about3 = request.form['like']
		return render_template('page1.html')

	#gets the answer of the first question
	def process_q1():
		if request.form.get('Submit', None) == 'POST':
			return redirect(url_for('page2'))

	#question 2
	@app.route('/page2',methods=['GET','POST'])
	def renderPage2():
		takeABreak.answers1 = request.form['time']
		return render_template('page2.html')

	#gets the answer of the second question
	def process_q2():
		if request.form.get('Submit', None) == 'POST':
			return redirect(url_for('page3'))

	#question 3
	@app.route('/page3',methods=['GET','POST'])
	def renderPage3():
		takeABreak.answers2 = request.form['energy']
		return render_template('page3.html')

	#gets the answer for question 3
	def process_q3():
		if request.form.get('Submit', None) == 'POST':
			return redirect(url_for('page4'))

	#question 4
	@app.route('/page4',methods=['GET','POST'])
	def renderPage4():
		takeABreak.answers3 = request.form['hungry']
		return render_template('page4.html')

	#gets the answer for question 4
	def process_q4():
		if request.form.get('Submit', None) == 'POST':
			return redirect(url_for('page5'))
   
	#question 5
	@app.route('/page5', methods=['GET', 'POST'])
	def renderPage5():
		takeABreak.answers4 = request.form['drink']
		return render_template('page5.html')

	#gets the answer for question 5
	def process_q5():
		if request.form.get('Submit', None) == 'POST':
			return redirect(url_for('final'))

	#final
	@app.route('/final', methods=['GET', 'POST'])
	def renderFinal():
		takeABreak.answers5 = request.form['movie']
		#results = takeABreak.final_Results()
	#gets the results
		index = 0
		#about1 - mood - bad
		if (int)(takeABreak.about1) == 1:
			for index in range(0, 17):
				if (int)(index) == 2:
					takeABreak.finalResults[2] += 4
				elif (int)(index) == 6:
					takeABreak.finalResults[6] += 3
				elif (int)(index) == 13:
					takeABreak.finalResults[13] += 3
	
		#mood - ehhh
		elif (int)(takeABreak.about1) == 2:
			for index in range(0, 17):
				if (int)(index) == 6:
					takeABreak.finalResults[6] += 3
				elif (int)(index) == 13:
					takeABreak.finalResults[13] += 2

	#sets day results
		#about2 - day - morning
		index = 0
		if (int)(takeABreak.about2) == 1:
			for index in range(0, 17):
				if (int)(index) == 0:
					takeABreak.finalResults[0] += 2
	
		#day - mid morning
		elif (int)(takeABreak.about2) == 2:
			for index in range(0, 17):
				if (int)(index) == 0:
					takeABreak.finalResults[0] += 2
				elif (int)(index) == 6:
					takeABreak.finalResults[6] += 3
				elif (int)(index) == 16:
					takeABreak.finalResults[16] += 2

		#day - evening
		elif (int)(takeABreak.about2) == 3:
			for index in range(0, 17):
				if (int)(index) == 6:
					takeABreak.finalResults[6] += 3
				elif (int)(index) == 16:
					takeABreak.finalResults[16] += 2

		#like results
		index = 0
	
		#about3 - bookworm	
		if (int)(takeABreak.about3) == 1:
			for index in range(0, 17):
				if (int)(index) == 2:
					takeABreak.finalResults[2] += 3
				elif (int)(index) == 9:
					takeABreak.finalResults[9] += 4
				elif (int)(index) == 15:
					takeABreak.finalResults[15] += 2
				elif (int)(index) == 17:
					takeABreak.finalResults[17] += 3
	
		#lazy
		elif (int)(takeABreak.about3) == 2:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += -3
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += -3
				elif (int)(index) == 13:
					takeABreak.finalResults[13] += 4
				elif (int)(index) == 17:
					takeABreak.finalResults[17] += 2

		#athletic
		elif (int)(takeABreak.about3) == 3:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += 4
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += 3
	
		#shoppaholic
		elif (int)(takeABreak.about3) == 4:
			for index in range(0, 17):
				if (int)(index) == 3:
					takeABreak.finalResults[3] += 4
				elif (int)(index) == 15:
					takeABreak.finalResults[15] += 2
				elif (int)(index) == 16:
					takeABreak.finalResults[16] += 4

		#video game lover
		elif (int)(takeABreak.about3) == 5:
			for index in range(0, 17):
				if (int)(index) == 2:
					takeABreak.finalResults[2] += -1
				elif (int)(index) == 13:
					takeABreak.finalResults[13] += 2

		#page1 results - time
		index = 0

		#answers1 - 10 min	
		if (int)(takeABreak.answers1) == 1:
			for index in range(0, 17):
				if (int)(index) == 0:
					takeABreak.finalResults[0] += 2
				elif (int)(index) == 2:
					takeABreak.finalResults[2] += 2
				elif (int)(index) == 4:
					takeABreak.finalResults[4] += 2
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += 3
				elif (int)(index) == 8:
					takeABreak.finalResults[8] += 2
				elif (int)(index) == 14:
					takeABreak.finalResults[14] += 2
	
		#15 min
		elif (int)(takeABreak.answers1) == 2:
			for index in range(0, 17):
				if (int)(index) == 0:
					takeABreak.finalResults[0] += 2
				elif (int)(index) == 3:
					takeABreak.finalResults[3] += 2
				elif (int)(index) == 4:
					takeABreak.finalResults[4] += 2
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += 2
				elif (int)(index) == 8:
					takeABreak.finalResults[8] += 2
				elif (int)(index) == 10:
					takeABreak.finalResults[10] += 2
				elif (int)(index) == 12:
					takeABreak.finalResults[12] += 2

		#20 min
		elif (int)(takeABreak.answers1) == 3:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += 3
				elif (int)(index) == 3:
					takeABreak.finalResults[3] += 2
				elif (int)(index) == 5:
					takeABreak.finalResults[5] += 3
				elif (int)(index) == 6:
					takeABreak.finalResults[6] += 3
				elif (int)(index) == 9:
					takeABreak.finalResults[9] += 3
				elif (int)(index) == 10:
					takeABreak.finalResults[10] += 2
				elif (int)(index) == 11:
					takeABreak.finalResults[11] += 4
				elif (int)(index) == 12:
					takeABreak.finalResults[12] += 2
				elif (int)(index) == 15:
					takeABreak.finalResults[15] += 2
	
		#30 min
		elif (int)(takeABreak.answers1) == 4:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[2] += 3
				elif (int)(index) == 3:
					takeABreak.finalResults[3] += 2
				elif (int)(index) == 5:
					takeABreak.finalResults[5] += 3
				elif (int)(index) == 6:
					takeABreak.finalResults[6] += 3
				elif (int)(index) == 9:
					takeABreak.finalResults[9] += 3
				elif (int)(index) == 10:
					takeABreak.finalResults[10] += 2
				elif (int)(index) == 11:
					takeABreak.finalResults[11] += 3
				elif (int)(index) == 15:
					takeABreak.finalResults[15] += 2
				elif (int)(index) == 16:
					takeABreak.finalResults[16] += 3

		#energy results			
		index = 0
		#answers2 - energy - low
		if (int)(takeABreak.answers2) == 1:
			for index in range(0, 17):
				if (int)(index) == 0:
					takeABreak.finalResults[0] += 5
				elif (int)(index) == 2:
					takeABreak.finalResults[2] += 2
				elif (int)(index) == 11:
					takeABreak.finalResults[11] += 4
	
		#energy - mid
		elif (int)(takeABreak.answers2) == 2:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += 3
				elif (int)(index) == 2:
					takeABreak.finalResults[2] += 2
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += 2
				elif (int)(index) == 17:
					takeABreak.finalResults[17] += 2

		#energy - high
		elif (int)(takeABreak.answers2) == 3:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += 3
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += 2
				elif (int)(index) == 17:
					takeABreak.finalResults[17] += 2

		#hungry results			
		index = 0
		#answers3 - hunger - low
		if (int)(takeABreak.answers3) == 1:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += 2
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += 2
	
		#hunger - mid
		elif (int)(takeABreak.answers3) == 2:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += 2
				elif (int)(index) == 4:
					takeABreak.finalResults[4] += 2
				elif (int)(index) == 10:
					takeABreak.finalResults[10] += 2

		#hunger - high
		elif (int)(takeABreak.answers3) == 3:
			for index in range(0, 17):
				if (int)(index) == 4:
					takeABreak.finalResults[4] == 4
				elif (int)(index) == 5:
					takeABreak.finalResults[5] == 4

		#drink results			
		index = 0
		#answers4 - coffee
		if (int)(takeABreak.answers4) == 1:
			for index in range(0, 17):
				if (int)(index) == 0:
					takeABreak.finalResults[0] += 5
				elif (int)(index) == 9:
					takeABreak.finalResults[9] += 3
	
		#tea
		elif (int)(takeABreak.answers4) == 2:
			for index in range(0, 17):
				if (int)(index) == 9:
					takeABreak.finalResults[9] += 3
				elif (int)(index) == 14:
					takeABreak.finalResults[14] += 4

		#smoothie
		elif (int)(takeABreak.answers4) == 3:
			for index in range(0, 17):
				if (int)(index) == 10:
					takeABreak.finalResults[10] += 4

		#water
		elif (int)(takeABreak.answers4) == 4:
			for index in range(0, 17):
				if (int)(index) == 1:
					takeABreak.finalResults[1] += 3
				elif (int)(index) == 7:
					takeABreak.finalResults[7] += 2

		#movie results			
		index = 0
		#answers5- romantic
		if (int)(takeABreak.answers5) == 1:
			for index in range(0, 17):
				if (int)(index) == 2:
					takeABreak.finalResults[2] += 2
				elif (int)(index) == 3:
					takeABreak.finalResults[3] += 3
				elif (int)(index) == 16:
					takeABreak.finalResults[16] += 3
	
		#action
		elif (int)(takeABreak.answers5) == 2:
			for index in range(0, 17):
				if (int)(index) == 2:
					takeABreak.finalResults[2] += -3

		#Scary
		elif (int)(takeABreak.answers5) == 3:
			for index in range(0, 17):
				if (int)(index) == 2:
					takeABreak.finalResults[2] += -3

		#comedy
		elif (int)(takeABreak.answers5) == 4:
			for index in range(0, 17):
				if (int)(index) == 3:
					takeABreak.finalResults[3] += 2
				elif (int)(index) == 13:
					takeABreak.finalResults[13] += 3

		#figure out the results
		tracker = 0
		index = 0
		for index in range(0, 17):
			print takeABreak.finalResults[index]
			if takeABreak.finalResults[index] > takeABreak.finalResults[tracker]:
				tracker = index
		if (int)(tracker) == 0:
			results = "You need a pick-me-up!  Grab a cup of coffee to get you more energized and awake!"
		elif (int)(tracker) == 1:
			results = "Take some time to relieve that stress and go for a walk or run to clear your head.  It will make you feel better!"
		elif (int)(tracker) == 2:
			results = "Look up some inspirational quotes to cheer you up!  It won't take long and will make you in a better mood :)"
		elif (int)(tracker) == 3:
			results = "Window shop online!  You can search for cute clothes, new boots, or cool new gadgets!  But choose wisely, you only have time to look at one or two stores max!"
		elif (int)(tracker) == 4:
			results = "Grab a snack!  It can be fruit, chips, or crackers!  It will satisfy your hungry stomach."
		elif (int)(tracker) == 5:
			results = "Take a break and grab a meal.  Your stomach will thank you for feeding it and you will be able to focus better without your stomach growling."
		elif (int)(tracker) == 6:
			results = "Call a friend or family member you haven't talked to in awhile!  It will be a nice break to catch up."
		elif (int)(tracker) == 7:
			results = "Stretch!  Your body will thank you after sitting for such a long time studying!"
		elif (int)(tracker) == 8:
			results = "Catch up on the news!  Read some yahoo news.  They are short and a perfect study break."
		elif (int)(tracker) == 9:
			results = "You love reading, so read a chapter in a book for fun!  You will keep your mind active and enjoy it more than that boring history book."
		elif (int)(tracker) == 10:
			results = "Make a smoothie!  Add some strawberries, maybe bananas, or even kale if you want to be healthy!"
		elif (int)(tracker) == 11:
			results = "Take a nap!  But your nap should be short and only 20-30 minutes or else you won't feel refreshed quickly to finish your work."
		elif (int)(tracker) == 12:
			results = "Find some new music to listen to!  Try new artists, genres, or bands!"
		elif (int)(tracker) == 13:
			results = "Laugh your heart out and watch some funny youtube videos!  It will be nice to laugh a little after you've been in the gloomy library."
		elif (int)(tracker) == 14:
			results = "Make yourself a cup of tea!  It could be pumpkin, passion, green, chai; there are so many to choose from!"
		elif (int)(tracker) == 15:
			results = "Read a magazine or newspaper article.  There is so much to read about it! Fashion, sports, current events, you name it!"
		elif (int)(tracker) == 16:
			results = "Paint your nails!  It's so relaxing and gives you an excuse not to do work because you have to let them dry."
		elif (int)(tracker) == 17:
			results = "Do a puzzle.  It could be a crossword puzzle, sudoku, or even a word search!  You will keep your brain stimulated on your break!"
		return render_template('final.html', myfunction=results)

#runs program
if __name__=="__main__":
	app.run()
