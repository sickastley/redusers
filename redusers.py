"""
The MIT License (MIT)
Copyright (c) 2022-present sickastley && CyanCipher
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import csv
import praw
import time
from credentials import credentials
from datetime import datetime

class Redusers():

	def __init__(self):

		client_id = credentials['client_id']
		client_secret = credentials['client_secret']
		username = credentials['username']
		password = credentials['password']

		reddit = praw.Reddit(client_id = client_id, 
			client_secret = client_secret,
			user_agent = "For INDIA",
			username = username,
			password = password)

		self.reddit = reddit

		self.title = 'la ilah illa modiji. ass on the roof rasul allah modiji'
		self.msg = 'future belongs to those who trust in clean energy and water management, not those who run behind packages of cse and havent written of single line of true code in their life.' 

	def loadcsv(self, userFile):

		readFile = []

		try: 
			with open(userFile, 'r') as file:

				csv1 = csv.reader(file)

				for item in csv1:
					readFile.append(item)

			return readFile

		except:
			with open(userFile, 'w') as file:
				pass
			self.loadcsv(userFile)

	def savecsv(self, data, userFile):

		with open(userFile, "a", newline = '') as file:

			writer = csv.writer(file)
			for item in data:
				writer.writerow(item)

	def userInCsv(self, user, userFile):

		readFile = self.loadcsv(userFile)

		userList = []

		for item in readFile:
			userList.append(item[0])

		return user in userList

	def stateInCsv(self, user, userFile, value):

		readFile = self.loadcsv(userFile)

		for item in readFile:
			if item[0] == user:
				if item[1] == value:

					return True

			else: return False

	def addUser(self, user, userFile, Bool):

		temp = [[user, Bool]]
		self.savecsv(temp, userFile)

	def changeBool(self, user, userFile, Bool):

		readFile = self.loadcsv(userFile)

		for item in readFile:
			if item[0] == user:
				item[1] = Bool

		with open(userFile, 'w', newline = '') as file:
			writer = csv.writer(file)

			for item in readFile:
				writer.writerow(item)

	def ratelim(self, string):
		lst = string.split(" ")
		kek = int(lst[13])

		return kek

	def bulk(self, subreddit, userFile, limit):

		self.loadcsv(userFile)

		reddit = self.reddit

		comments = reddit.subreddit(subreddit).comments(limit=limit)

		for comment in comments:
			user = str(comment.author)
			print(user)
			if not self.userInCsv(user, userFile):
				self.addUser(user, userFile, 'False')

	def invite(self, userFile):

		reddit = self.reddit
		data = self.loadcsv(userFile)
		title = self.title
		msg = self.msg

		for item in data:

			if item[1] == "False":
				user = item[0]

				try:
					reddit.redditor(user).message(title, msg)
					t = str(datetime.now())
					t = t[:-6]
					print(f"{t} User: {user}, Status: Success")

					self.changeBool(user, userFile, 'True')

				except praw.exceptions.RedditAPIException as exception:

					for subexception in exception.items:
						t = str(datetime.now())
						t = t[:-6]

						if subexception.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
							self.changeBool(user, userFile, 'True')
							print(f"{t} User: {user}, Status: Failed, Reason: Not Whitelisted.")

						elif subexception.error_type == "RATELIMIT":
							kek = self.ratelim(str(subexception))
							kekinsecs = (kek * 60) + 15
							print(f"{t} Ratelimited for {kek} minutes, sleeping for {kekinsecs} seconds...")
							time.sleep(kekinsecs)

						elif subexception.error_type == "USER_DOESNT_EXIST":
							self.changeBool(user, userFile, 'True')
							print(f"{t} User: {user}, Status: Failed, Reason: User Dead.")

						elif subexception.error_type == "INVALID_USER":
							self.changeBool(user, userFile, 'True')
							print(f"{t} User: {user}, Status: Failed, Reason: User Invalid.")

						elif subexception.error_type == "NO_USER":
							self.changeBool(user, userFile, 'True')
							print(f"{t} User: {user}, Status: Failed, Reason: No user named this.")

						else:
							print(subexception.error_type)

				time.sleep(29)

	def oldToNew(self, old, new, value):

		oldFile = self.loadcsv(old)
		newFile = self.loadcsv(new)

		for item in oldFile:
			user = item[0]

			if not self.userInCsv(user, new):
				self.addUser(user, new, value)

			else:
				self.changeBool(user, new, value)





		