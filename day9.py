# programming_dictionary = {
#     "bug": "An error in a program that prevents the program from running as expected",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again"
#
# }
# print(programming_dictionary["bug"])
#
# # adding new items to dic
# programming_dictionary["Loop"] = " The action of doing something over and over again"
# print(programming_dictionary)
#
# # create and empty dic
# empty_dictionary = {}
#
# # edit an item in a dic
# programming_dictionary["bug"] = "2342342"
#
# # loop dic
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     elif score <= 70:
#         student_grades[student] = "Fail"
# # 🚨 Don't change the code below 👇
#
# print(student_grades)

# nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# # nesting dictionary in a dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "Total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Suttgart"], "Total_visits": 5},
# }
# # nesting dictionary in a list
# travel_log = [
#     {
#         "Country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "Total_visits": 12},
#     {
#         "Country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Suttgart"],
#         "Total_visits": 5},
# ]

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
#
#
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#





#🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
#
