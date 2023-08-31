# PostgreSQL and Django

This  project for getting the brief knowledege of the WORKING WITH Djando and PostgreSQL

> If we have used POSTGRESQL for the project you will need to update seeting.py 
> Under the setting.py file which contain DATABASES and you should modify it as following

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD' : "admin",
        'HOST' : 'localhost',
        'POSRT' : '5432',
    }
}
```