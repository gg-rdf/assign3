import requests
import pandas as pd
import json

#call api
response = requests.get(
        'http://alethea-support-training-bt.lab.up:8888/metadata/search?aql=SELECT%20hostname,Project,SYSID,Service,TLC%20FROM%20vm%20WHERE%20Product=CURRY%20AND%20Service=TOMCAT%20ORDER%20BY%20SYSID')

# load json
json_data = json.loads(response.text)

# Normalize data
#df = pd.json_normalize(json_data, record_path=['content'], meta=['Project', 'SYSID', 'Service', 'TLC', 'hostname'])
df = pd.json_normalize(json_data['result'])


# Keep required columns
df = df[['content.Project', 'content.SYSID', 'content.Service','content.TLC','content.hostname']]

# rename columns
df= df.set_axis(['Project', 'SYSID', 'Service', 'TLC', 'hostname'], axis=1, inplace=False)

# create csv
df.to_csv('out.csv',index=False)

print(df)