import os
from flask import Flask, url_for, render_template, request
from flask import redirect

app = Flask(__name__)
about1 = 0
about2 = 0
about3 = 0
answers1 = 0
answers2 = 0
answers3 = 0
answers4 = 0
answers5 = 0
finalResults = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
results = ""
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
		about1=request.form["day"]
		about2=request.form["mood"]
		about3=request.form["like"]
		return redirect(url_for('page1'))

#first set of questions time alloted for break
@app.route('/page1', methods=['GET', 'POST'])
def renderPage1():
	return render_template('page1.html')

#gets the answer of the first question
def process_q1():
	if request.form.get('Submit', None) == 'POST':
		answers1=request.form["time"]
		return redirect(url_for('page2'))

#question 2
@app.route('/page2',methods=['GET','POST'])
def renderPage2():
	return render_template('page2.html')

#gets the answer of the second question
def process_q2():
	if request.form.get('Submit', None) == 'POST':
		answers2=request.form["energy"]
		return redirect(url_for('page3'))

#question 3
@app.route('/page3',methods=['GET','POST'])
def renderPage3():
	return render_template('page3.html')

#gets the answer for question 3
def process_q3():
	if request.form.get('Submit', None) == 'POST':
		answers3=request.form["hungry"]
		return redirect(url_for('page4'))

#question 4
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
	return render_template('page4.html')

#gets the answer for question 4
def process_q4():
	if request.form.get('Submit', None) == 'POST':
		answers4=request.form["drink"]
		return redirect(url_for('page5'))
   
#question 5
@app.route('/page5', methods=['GET', 'POST'])
def renderPage5():
	return render_template('page5.html')

#gets the answer for question 5
def process_q5():
	if request.form.get('Submit', None) == 'POST':
		answers5=request.form["movie"]
		return redirect(url_for('final'))

#final
@app.route('/final', methods=['GET', 'POST'])
def renderFinal():
	results = final_Results()
	return render_template('final.html', myfunction=results)

#gets the results
def final_Results():
	index = 0
	#about1 - mood - bad
	if about1 == 1:
		for index in range(0, 17):
			if index == 2:
				finalResults[2] += 4
			elif index == 6:
				finalResults[6] += 3
			elif index == 13:
				finalResults[13] += 3
			else:
				finalResults[index] += 1
	
	#mood - ehhh
	elif about1 == 2:
		for index in range(0, 17):
			if index == 6:
				finalResults[6] += 3
			elif index == 13:
				finalResults[13] += 2
			else:
				finalResults[index] += 1

	#mood - great
	else:
		for index in range(0, 17):
			finalResults[index] += 1

#sets day results
	#about2 - day - morning
	index = 0
	if about2 == 1:
		for index in range(0, 17):
			if index == 0:
				finalResults[0] += 2
			else:
				finalResults[index] += 1
	
	#day - mid morning
	elif about2 == 2:
		for index in range(0, 17):
			if index == 0:
				finalResults[0] += 2
			elif index == 6:
				finalResults[6] += 3
			elif index == 16:
				finalResults[16] += 3
			else:
				finalResults[index] += 1

	#day - evening
	else:
		for index in range(0, 17):
			if index == 6:
				finalResults[6] += 3
			elif index == 16:
				finalResults[16] += 3
			else:
				finalResults[index] += 1

#like results
	index = 0

	#about3 - bookworm	
	if about3 == 1:
		for index in range(0, 17):
			if index == 9:
				finalResults[9] += 4
			elif index == 15:
				finalResults[15] += 2
			elif index == 17:
				finalResults[17] += 3
			else:
				finalResults[index] += 1
	
	#lazy
	elif about3 == 2:
		for index in range(0, 17):
			if index == 13:
				finalResults[13] += 4
			elif index == 17:
				finalResults[17] += 2
			else:
				finalResults[index] += 1

	#athletic
	elif about3 == 3:
		for index in range(0, 17):
			if index == 1:
				finalResults[1] += 4
			elif index == 7:
				finalResults[7] += 2
			else:
				finalResults[index] += 1
	
	#shoppaholic
	elif about3 == 4:
		for index in range(0, 17):
			if index == 3:
				finalResults[3] += 4
			elif index == 15:
				finalResults[15] += 2
			elif index == 16:
				finalResults[15] += 5
			else:
				finalResults[index] += 1

	#video game lover
	else:
		for index in range(0, 17):
			if index == 2:
				finalResults[2] += -1
			elif index == 13:
				finalResults[13] += 2
			else:
				finalResults[index] += 1

#page1 results - time
	index = 0

	#answers1 - 10 min	
	if answers1 == 1:
		for index in range(0, 17):
			if index == 1:
				finalResults[1] += 2
			elif index == 2:
				finalResults[2] += 3
			elif index == 4:
				finalResults[4] += 3
			elif index == 7:
				finalResults[7] += 3
			elif index == 8:
				finalResults[8] += 2
			elif index == 14:
				finalResult[14] += 2
			else:
				finalResults[index] += 1
	
	#15 min
	elif answers1 == 2:
		for index in range(0, 17):
			if index == 0:
				finalResults[0] += 2
			elif index == 3:
				finalResults[3] += 2
			elif index == 4:
				finalResults[4] += 3
			elif index == 8:
				finalResults[8] += 2
			elif index == 10:
				finalResults[10] += 2
			elif index == 12:
				finalResults[12] += 2
			else:
				finalResults[index] += 1

	#20 min
	elif answers1 == 3:
		for index in range(0, 17):
			if index == 1:
				finalResults[1] += 4
			elif index == 3:
				finalResults[3] += 2
			elif index == 5:
				finalResults[5] += 3
			elif index == 6:
				finalResults[6] += 3
			elif index == 9:
				finalResults[9] += 4
			elif index == 10:
				finalResults[10] += 2
			elif index == 11:
				finalResults[11] += 4
			elif index == 12:
				finalResults[12] += 2
			elif index == 15:
				finalResults[15] += 2
			else:
				finalResults[index] += 1
	
	#30 min
	else:
		for index in range(0, 17):
			if index == 1:
				finalResults[2] += 4
			elif index == 3:
				finalResults[3] += 2
			elif index == 5:
				finalResults[5] += 3
			elif index == 6:
				finalResults[6] += 3
			elif index == 9:
				finalResults[9] += 4
			elif index == 10:
				finalResults[10] += 2
			elif index == 11:
				finalResults[11] += 4
			elif index == 15:
				finalResults[15] += 2
			elif index == 16:
				finalResults[16] += 4
			else:
				finalResults[index] += 1

#energy results			
	index = 0
	#answers2 - energy - low
	if answers2 == 1:
		for index in range(0, 17):
			if index == 0:
				finalResults[0] += 5
			elif index == 2:
				finalResults[2] += 2
			elif index == 11:
				finalResults[11] += 4
			else:
				finalResults[index] += 1
	
	#energy - mid
	elif answers2 == 2:
		for index in range(0, 17):
			if index == 0:
				finalResults[0] += 3
			elif index == 1:
				finalResults[1] += 3
			elif index == 2:
				finalResults[2] += 2
			elif index == 7:
				finalResults[7] += 3
			elif index == 17:
				finalResults[17] += 2
			else:
				finalResults[index] += 1

	#energy - high
	else:
		for index in range(0, 17):
			if index == 1:
				finalResults[1] += 4
			elif index == 7:
				finalResults[7] += 3
			elif index == 17:
				finalResults[17] += 2
			else:
				finalResults[index] += 1

#hungry results			
	index = 0
	#answers3 - hunger - low
	if answers3 == 1:
		for index in range(0, 17):
			if index == 1:
				finalResults[1] += 3
			elif index == 7:
				finalResults[7] += 2
			else:
				finalResults[index] += 1
	
	#hunger - mid
	elif answers3 == 2:
		for index in range(0, 17):
			if index == 1:
				finalResults[1] += 3
			elif index == 4:
				finalResults[4] += 3
			elif index == 7:
				finalResults[7] += 2
			elif index == 10:
				finalResults[10] += 2
			else:
				finalResults[index] += 1

	#hunger - high
	else:
		for index in range(0, 17):
			if index == 4:
				finalResults[4] == 4
			elif index == 5:
				finalResults[5] == 4
			else:
				finalResults[index] += 1


#drink results			
	index = 0
	#answers4 - coffee
	if answers4 == 1:
		for index in range(0, 17):
			if index == 0:
				finalResults[0] += 5
			elif index == 9:
				finalResults[9] += 2
			else:
				finalResults[index] += 1
	
	#tea
	elif answers4 == 2:
		for index in range(0, 17):
			if index == 9:
				finalResults[9] += 2
			elif index == 14:
				finalResults[14] += 5
			else:
				finalResults[index] += 1

	#smoothie
	elif answers4 == 3:
		for index in range(0, 17):
			if index == 10:
				finalResults[10] += 4
			else:
				finalResults[index] += 1

	#water
	elif answers4 == 4:
		for index in range(0, 17):
			if index == 1:
				finalResults[1] += 3
			elif index == 7:
				finalResults[7] += 2
			else:
				finalResults[index] += 1

	#fruit juice
	else:
		for index in range(0, 17):
			finalResults[index] += 1

#movie results			
	index = 0
	#answers5- romantic
	if answers5 == 1:
		for index in range(0, 17):
			if index == 3:
				finalResults[3] += 4
			elif index == 16:
				finalResults[16] += 5
			else:
				finalResults[index] += 1
	
	#action
	elif answers5 == 2:
		for index in range(0, 17):
			if index == 2:
				finalResults[2] += -3
			else:
				finalResults[index] += 1

	#Scary
	elif answers5 == 3:
		for index in range(0, 17):
			if index == 2:
				finalResults[2] += -3
			else:
				finalResults[index] += 1

	#comedy
	else:
		for index in range(0, 17):
			if index == 3:
				finalResults[3] += 2
			elif index == 13:
				finalResults[13] += 3
			else:
				finalResults[index] += 1

#figure out the results
	tracker = 0
	index = 0
	for index in range(0, 17):
		if finalResults[index] > finalResults[tracker]:
			tracker = index
	if tracker == 0:
		results = "You need a pick-me-up!  Grab a cup of coffee to get you more energized and awake!"
	elif tracker == 1:
		results = "Take some time to relieve that stress and go for a walk or run to clear your head.  It will make you feel better!"
	elif tracker == 2:
		results = "Look up some inspirational quotes to cheer you up!  It won't take long and will make you in a better mood :)"
	elif tracker == 3:
		results = "Window shop online!  You can search for cute clothes, new boots, or cool new gadgets!  But choose wisely, you only have time to look at one or two stores max!"
	elif tracker == 4:
		results = "Grab a snack!  It can be fruit, chips, or crackers!  It will satisfy your hungry stomach."
	elif tracker == 5:
		results = "Take a break and grab a meal.  Your stomach will thank you for feeding it and you will be able to focus better without your stomach growling."
	elif tracker == 6:
		results = "Call a friend of family member you haven't talked to in awhile!  It will be a nice break to catch up."
	elif tracker == 7:
		results = "Stretch!  Your body will thank you after sitting for such a long time studying!"
	elif tracker == 8:
		results = "Catch up on the news!  Read some yahoo news.  They are short and a perfect study break."
	elif tracker == 9:
		results = "You love reading, so read a chapter in a book for fun!  You will keep your mind active and enjoy it more than that boring history book."
	elif tracker == 10:
		results = "Make a smoothie!  Add some strawberries, maybe bananas, or even kale if you want to be healthy!"
	elif tracker == 11:
		results = "Take a nap!  But your nap should be short and only 20-30 minutes or else you won't feel refreshed quickly to finish your work."
	elif tracker == 12:
		results = "Find some new music to listen to!  Try new artists, genres, or bands!"
	elif tracker == 13:
		results = "Laugh your heart out and watch some funny youtube videos!  It will be nice to laugh a little after you've been in the gloomy library."
	elif tracker == 14:
		results = "Make yourself a cup of tea!  It could be pumpkin, passion, green, chai; there are so many to choose from!"
	elif tracker == 15:
		results = "Read a magazine or newspaper article.  There is so much to read about it! Fashion, sports, current events, you name it!"
	elif tracker == 16:
		results = "Paint your nails!  It's so relaxing and gives you an excuse not to do work because you have to let them dry."
	elif tracker == 17:
		results = "Do a puzzle.  It could be a crossword puzzle, sudoku, or even a word search!  You will keep your brain stimulated on your break!"
	return results

#runs program
if __name__=="__main__":
	app.run()
