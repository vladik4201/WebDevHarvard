individuals = [
    {"his/her_name": "Greg", "Game":"fourth"},
    {"his/her_name":"Draco", "Game":"fifth"},
    {"his/her_name":"Hagrid", "Game":"sixth"}
]

# def x(individuals):
#     return individuals["his/her_name"]
#with lambda, you don't need the function above which to call out would need individuals.sort(key=x)
 

individuals.sort(key=lambda individuals: individuals["Game"])

#sorts all the individuals and to sort them, use x as the key by their name
# if you change to Game, it will sort everyone by game in alphabetical order  
print(individuals)
