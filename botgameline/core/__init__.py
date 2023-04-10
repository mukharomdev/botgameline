class BotGameLine:
	def __init__(self,instance):
		self._instance = instance

	def get(self):
	    try:
	      	return self._only
	    except AttributeError:
	      self._only = self._instance()
	      return self._only

	def __call__(self):
    		raise TypeError("Using method get..")

@BotGameLine
class botgameline:
	def execute(self,cmd):
		print("dispatch bot with command =>",cmd)



