from redusers import Redusers

client = Redusers('bot2')

client.bulk('indiaspeaks', './data/right.csv', 20000)
client.bulk('DesiMemeCentral', './data/right.csv', 20000)
client.bulk('Sham_Sharma_Show', './data/right.csv', 20000)
client.bulk('KarmaBhumi', './data/right.csv', 20000)


client.bulk('librandu', './data/left.csv', 20000)
client.bulk('india', './data/left.csv', 20000)
client.bulk('Saimansays', './data/left.csv', 20000)
client.bulk('Indiameme', './data/left.csv', 20000)
client.bulk('kerala', './data/left.csv', 20000)


client.isKachra('./data/right.csv', './data/left.csv')
client.broom('./data/right.csv', './data/left.csv')
