﻿# VeracityAds-hw
This is a project as part of my appliction process for VeracityAds.


## Runing 
on windowns run:
```py manage.py runserver```
and on linux and macOS
```python manage.py runserver```


## Testing 
on windowns run:
```py manage.py Test```
and on linux and macOS
```python manage.py Test```

## Entrypoints

### POST /recipes/
Use to create new recipes in the system.
```JSON
{
  "title": "Spaghetti Carbonara",
  "description": "A classic Italian pasta dish with a creamy egg sauce.",
  "ingredients": [
    "200g spaghetti",
    "100g pancetta",
    "2 large eggs",
    "50g grated Parmesan cheese",
    "Salt",
    "Black pepper"
  ],
  "instructions": [
    "do A",
    "now do B"
  ],
  "category": "Pasta"
}
```
Use this json format. 

### GET /recipes/
Use to list all the recipes.


### GET /recipes/{id}
Use to get a recipe.

### PUT /recipes/{id}
Use to update a recipe.
To change the title for example add this json in the body
```JSON 
{"title":"Not Spaghetti Carbonara"}
```

### DELETE /recipes/{id}
Use to delete a recipe.

### GET /recipes/search/?q={query}
Use to find recipes base on the name or the catagory.
