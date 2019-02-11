# Chapter 14 Question 10
# Rewrite Exercise 11.40 using a dictionary to store the pairs
# of states and capitals so that the questions are randomly displayed.


import random


def main():
    capitals = {
        "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock",
        "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover",
        "Florida": "Tallahasse", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
        "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka",
        "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
        "Massachusettes": "Boston", "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
        "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
        "New Jersey": "Trenton", "New York": "Albany", "New Mexico": "Santa Fe", "North Carolina": "Raleigh",
        "North Dakota": "Bismark", "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem",
        "Pennslyvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia",
        "South Dakota": "Pierre", "New Hampshire": "Concord", "Wyoming": "Cheyenne", "Wisconsin": "Madison",
        "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier",
        "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston"
    }

    keyList = list(capitals.keys())
    correct = 0
    for i in range(52):
        state = random.randint(0, 51)
        inputCapital = input("What is the capital of " + keyList[state] + "? ")
        if inputCapital.lower() == capitals.get(keyList[state]).lower():
            print("Correct answer")
            correct += 1
        else:
            print("The Correct answer is ", capitals.get(state))


if __name__ == "__main__":
    main()
