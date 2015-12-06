from ConfigParser import SafeConfigParser
import os

parser = SafeConfigParser()

class Config:
	def get_config(self,filename,section,key):
		parser.read(os.path.abspath(filename))
		config_value = parser.get(section,key)
		return config_value
