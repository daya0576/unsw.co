## plans(Ordered by urgency) ##
1. adding undergraduate courses. 
 
2. custom index page.
3. attracting users.


## Configuration ##
### Step1: ###
Adding file **keys.py** to rango directory
keys.py:   
```
#!python

BING_API_KEY = ''
G_EMAIL_KEY = ""
ME_EMAIL_KEY = ""
```

### Step2: ###

```
#!bash

pip install -r /path/to/requirements.txt
```

### Step3: ###

In rango directory:   

```
#!python

python manage.py runserver 8001
```

### Done ###
Open this url in your browser
[http://127.0.0.1:8004/](http://127.0.0.1:8004/)

<br><br>
If it does not work, sending email to me:
**me@changchen.me**