from redusers import Redusers

client = Redusers()

# to get userlist from existing subs
# client.bulk('indiaspeaks', 'demo.csv', 1000)

# to invite  from the given file
# client.invite('demo.csv')

# to merge old csv to new type.
# last value tells whether the file has userbase which has been invited or not.
# True for invited and False for not invited.

client.oldToNew('pholder_indiaspeaks.csv', 'demo.csv', 'False')
client.oldToNew('test.csv', 'demo.csv', 'False')
client.oldToNew('chodi.csv', 'demo.csv', 'False')
client.oldToNew('users.csv', 'demo.csv', 'False')

client.oldToNew('sent.csv', 'demo.csv', 'True')