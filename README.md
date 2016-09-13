## Plans(Ordered by urgency) ##
1. adding undergraduate courses.(done)
2. custom index page.(done)
3. attracting users.
4. bg font bugs.

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
Installing all the packages. 
Run it in root directory.
```
#!bash

pip install -r requirements.txt
```

### Step3: ###

In rango directory:   

```
#!python

python manage.py runserver 8001
```

### Done ###
Open this url in your browser
[http://127.0.0.1:8001/](http://127.0.0.1:8001/)

###  ###
###  ###
If it does not work, sending email to me:
**me@changchen.me**