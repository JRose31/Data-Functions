# Data Functions
### Script containing Functions that manipulate data
This is a python script, containing functions of code that I found myself using
regularly when dealing with data in one way or another

## Functions
#### *sort_list()*
Takes the argument of multiple list, sorts all list with the first list being set as the sort rule.
Returns a tuple of list for multiple variable assignments.
###### ex: sort_list(x, y)

#### *avgna()*
Takes the argument of a single list (currently), reassigns empty or NaN values in that list with
the mean number of that dataset. Takes an additonal argument of number of decimals user wants
returned in that mean value.
###### ex: avgna(list, 3)
####### If available, the mean value (value taking the empty values place, will return a number up to 3 decimal places)

#### *delna()*
Takes the argument of multiple list, deletes entire rows that contain empty or NaN values.
###### ex: x, y = sort_list(x, y)
