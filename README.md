# GIS YELP API EXAMPLE

### General Info
***
This is an example to use GIS + Django using Yelp dataset to get existing coordinates on earth.
This example has CRUD methods for the entities: user, business, reviews
This example has an endpoint /api/business/get_business_from_distance that fetches businesses within a radius determined by the user, just send their latitude and longitude [Radius optional] as query string parameters.


<p align="center">
  <img width="600" height="350" src="https://www.endpointdev.com/blog/2014/01/using-google-maps-and-jquery-for/image-0.png">
</p>
<small>*Note:  This image is taken from the internet and thanks to the author as it is only used for illustrative purposes.  </small>

***


## Requirements
* [Python](https://www.python.org/): Version 3.8
* [Django](https://www.djangoproject.com/) Version 3.2.16
* [GDAL](https://gdal.org/api/python_bindings.html) Version 3.2.2.1
* [Docker](https://docs.docker.com/get-docker/) version 20.10.11
* [docker-compose](https://docs.docker.com/compose/install/) version 1.29.2
* [Yelp subset](https://drive.google.com/file/d/1rPjOdKXggrs3QYcEk8MQ9yyAD_dPZPG9/view?usp=sharing)


<small> 
*Note:  The data we provide to you is a subset of that available at https://www.yelp.com/dataset  
</small>

## Pre install
Download and copy the 'business10k.json' file to the path: yelp -> business -> scripts

```
                           _____ load_business.py
                          /
morgana -> business-> scripts
                          \_____ business10k.json
                                    
```

Download and copy the 'user100k.json' file to the path: yelp -> user -> scripts

```
                       _____ load_users.py
                      /
morgana -> user-> scripts
                      \_____ user100k.json
                                    
```

Download and copy the 'review1M.json' file to the path: yelp -> review -> scripts

```
                           _____ load_reviews.py
                          /
morgana -> review-> scripts
                          \_____ review1M.json
                                    
```


## Install

Create the containers:
```bash
  docker-compose up --build
```

Create all migrations:
```bash
  docker-compose run web python manage.py migrate
```

To load the dataset, it is necessary to execute the commands in order according to the E/R diagram.  
*Note: `load_reviews` took around 25-30 minutes. since it has a lot of information. It is recommended to delete a few records if you only want to do basic tests.

```bash
  docker-compose run web python manage.py runscript load_business
  docker-compose run web python manage.py runscript load_users
  docker-compose run web python manage.py runscript load_reviews
```

Create super user with django In order to use path `/admin` correctly
```bash
  docker-compose run web python manage.py createsuperuser
```

Run API:
```bash
  docker-compose up
```

## Running Tests

```bash
  docker-compose run web python manage.py test
```

## Documentation
I managed to integrate Swagger with django to see all endpoints once I ran the API successfully.  

[http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)  
[http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)


## Author
[@omar_gc](https://github.com/OmarGC)

