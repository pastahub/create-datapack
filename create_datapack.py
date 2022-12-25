import json, os, sys

if __name__ == "__main__":
	os.chdir(sys.path[0])
	settings_file = open('settings.json')

	settings = json.load(settings_file)
	name = settings['name']
	pack_format = settings['pack_format']
	description = settings['description']

	cwd = os.getcwd()
	os.makedirs(os.path.join(cwd, name + '/data/minecraft/tags/functions'))
	os.makedirs(os.path.join(cwd, name + '/data/' + name + '/functions'))

	with open(name + '/pack.mcmeta', 'w') as f:
		f.write('{\"pack\":{\"pack_format\":' + str(pack_format) + ',\"description\":\"' + description + "\"}}")

	with open(name + '/data/minecraft/tags/functions/tick.json', 'w') as f: 
		f.write('{\"values\": [\"' + name +':tick\"]}')

	open(name + '/data/' + name + '/functions/tick.mcfunction', 'w')
