
data = [
    {
        "id": 123,
        "name": "Dionne",
        "nationality": "Dutch",
        "person_age": 23,
        "duration": "Long",
        "interaction": 7,
        "looks": 7,
        "close": True,
        "reply": True,
        "lay": True,
        "comments": "",
        "created_at": "2020-08-29T22:00:12.833241+02:00",
        "updated_at": "2020-08-30T00:42:10.977761+02:00",
        "created_by": 1
    },
    {
        "id": 125,
        "name": "Lourrane Francisss",
        "nationality": "English",
        "person_age": 22,
        "duration": "Medium",
        "interaction": 8,
        "looks": 7,
        "close": True,
        "reply": True,
        "lay": True,
        "comments": "",
        "created_at": "2020-08-29T23:13:03.367344+02:00",
        "updated_at": "2020-08-29T23:21:16.549419+02:00",
        "created_by": 1
    },
    {
        "id": 126,
        "name": "Roger Brown",
        "nationality": "English",
        "person_age": 27,
        "duration": "Medium",
        "interaction": 7,
        "looks": 7,
        "close": True,
        "reply": True,
        "lay": True,
        "comments": "",
        "created_at": "2020-08-29T23:19:49.560620+02:00",
        "updated_at": "2020-08-29T23:20:30.490062+02:00",
        "created_by": 1
    },
    {
        "id": 127,
        "name": "Lourrane",
        "nationality": "Brazil",
        "person_age": 29,
        "duration": "Medium",
        "interaction": 7,
        "looks": 7,
        "close": True,
        "reply": True,
        "lay": True,
        "comments": "",
        "created_at": "2020-08-29T23:41:51.602276+02:00",
        "updated_at": "2020-08-29T23:41:59.831016+02:00",
        "created_by": 1
    },
    {
        "id": 129,
        "name": "Moore",
        "nationality": "Belgian",
        "person_age": 22,
        "duration": "Medium",
        "interaction": 7,
        "looks": 7,
        "close": True,
        "reply": False,
        "lay": False,
        "comments": "",
        "created_at": "2020-08-30T00:37:18.585982+02:00",
        "updated_at": "2020-08-30T00:37:18.586016+02:00",
        "created_by": 1
    }
]

import pandas
from pandas.io.json import json_normalize
from datetime import date, datetime

df = pandas.json_normalize(data)

my_string = '2019-10-31'
my_string = '2020-08-30T00:37:18.586016+02:00'

# Create date object in given time format yyyy-mm-dd
my_date = datetime.strptime(my_string, "%Y-%m-%d")

print(my_date)
print('Type: ',type(my_date))



# df['approach_at'] = df['created_at'].month

# print(df['approach_at'])


