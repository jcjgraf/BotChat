#! /usr/bin/python3

from cleverwrap import CleverWrap

class Bot(CleverWrap):

	def __init__(self, botName, apiKey):
		print("Initiate Bot {}".format(botName))
		CleverWrap.__init__(self, apiKey, botName)

	def talk(self, lastMessage):
		message = self.say(lastMessage)
		print("{}: {}".format(self.name, lastMessage))

		return message


if __name__ == '__main__':

	bots = []

	bots.append(Bot("b1", "firstCleverBotAPIKey"))
	bots.append(Bot("b2", "secondCleverBotAPIKey"))

	message = "Hi there!"

	try:
		
		while 1:
			for bot in bots:
				message = bot.talk(message)


	except KeyboardInterrupt:
		print("\nEnding conversation")
		b1.reset()
		b2.reset()