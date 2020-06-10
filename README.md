 
i have used following libraries/framework and modules
1. **DRF** : django rest framework to design rest application
in the application 

       write the following command : python manage.py add_users 3
       this will add three users to database and aslo display them in json format in the console like this:
       {'ppid': 'UOYAV4', 'real_name': 'Tina Gutierrez', 'tz': "('Canada/Eastern', 'Canada/Eastern')", 'Members_periods': [{'start_time': '2020-06-03T20:05:53.166812Z', 'end_time': '2020-06-03T20:05:53.166837Z'}, {'start_time': '2020-06-03T20:05:53.197825Z', 'end_time': '2020-06-03T20:05:53.197844Z'}]}
{'ppid': 'IF94CV', 'real_name': 'Michelle Wilson', 'tz': "('America/Tijuana', 'America/Tijuana')", 'Members_periods': [{'start_time': '2020-06-03T20:05:53.368127Z', 'end_time': '2020-06-03T20:05:53.368145Z'}, {'start_time': '2020-06-03T20:05:53.399020Z', 'end_time': '2020-06-03T20:05:53.399044Z'}]}
{'ppid': '68YHX7', 'real_name': 'Timothy Arias', 'tz': "('America/Montreal', 'America/Montreal')", 'Members_periods': [{'start_time': '2020-06-03T20:05:53.536882Z', 'end_time': '2020-06-03T20:05:53.536895Z'}, {'start_time': '2020-06-03T20:05:53.576466Z', 'end_time': '2020-06-03T20:05:53.576480Z'}]}


    you can get the list of users or single user from this api
    **/api/v1/members/HJT785/**
    here, HJT785 is the id 
    the output is 
    {
    "ppid": "HJT785",
    "real_name": "kishu chauhan",
    "tz": "Pacific/Yap",
    "Members_periods": [
        {
            "start_time": "2020-06-08T14:56:59Z",
            "end_time": "2020-06-08T14:57:02Z"
        },
        {
            "start_time": "2020-06-08T14:58:15Z",
            "end_time": "2020-06-08T14:58:18Z"
        }
    ]
}

2. **Docker**
 i have used docker to containerize my application

3. **AWS , Nginx and gunicorn** to make the application live on  https://18.220.254.196

