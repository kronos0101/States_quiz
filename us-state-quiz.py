import random
def states_capitals_quiz():

    states_and_capitals = {
        "Alabama": {"Capital": "Montgomery", "Flower": "Camellia", "Bird": "Yellowhammer", "Date Added": "1819", "Electoral Votes": 9, "Statehood Rank": 22},
        "Alaska": {"Capital": "Juneau", "Flower": "Forget-me-not", "Bird": "Willow Ptarmigan", "Date Added": "1959", "Electoral Votes": 3, "Statehood Rank": 49},
        "Arizona": {"Capital": "Phoenix", "Flower": "Saguaro Cactus Blossom", "Bird": "Cactus Wren", "Date Added": "1912", "Electoral Votes": 11, "Statehood Rank": 48},
        "Arkansas": {"Capital": "Little Rock", "Flower": "Apple Blossom", "Bird": "Northern Mockingbird", "Date Added": "1836", "Electoral Votes": 6, "Statehood Rank": 25},
        "California": {"Capital": "Sacramento", "Flower": "California Poppy", "Bird": "California Quail", "Date Added": "1850", "Electoral Votes": 54, "Statehood Rank": 31},
        "Colorado": {"Capital": "Denver", "Flower": "Rocky Mountain Columbine", "Bird": "Lark Bunting", "Date Added": "1876", "Electoral Votes": 10, "Statehood Rank": 38},
        "Connecticut": {"Capital": "Hartford", "Flower": "Mountain Laurel", "Bird": "American Robin", "Date Added": "1788", "Electoral Votes": 7, "Statehood Rank": 5},
        "Delaware": {"Capital": "Dover", "Flower": "Peach Blossom", "Bird": "Delaware Blue Hen", "Date Added": "1787", "Electoral Votes": 3, "Statehood Rank": 1},
        "Florida": {"Capital": "Tallahassee", "Flower": "Orange Blossom", "Bird": "Northern Mockingbird", "Date Added": "1845", "Electoral Votes": 30, "Statehood Rank": 27},
        "Georgia": {"Capital": "Atlanta", "Flower": "Cherokee Rose", "Bird": "Brown Thrasher", "Date Added": "1788", "Electoral Votes": 16, "Statehood Rank": 4},
        "Hawaii": {"Capital": "Honolulu", "Flower": "Hibiscus", "Bird": "Nene", "Date Added": "1959", "Electoral Votes": 4, "Statehood Rank": 50},
        "Idaho": {"Capital": "Boise", "Flower": "Syringa", "Bird": "Mountain Bluebird", "Date Added": "1890", "Electoral Votes": 4, "Statehood Rank": 43},
        "Illinois": {"Capital": "Springfield", "Flower": "Violet", "Bird": "Northern Cardinal", "Date Added": "1818", "Electoral Votes": 19, "Statehood Rank": 21},
        "Indiana": {"Capital": "Indianapolis", "Flower": "Peony", "Bird": "Northern Cardinal", "Date Added": "1816", "Electoral Votes": 11, "Statehood Rank": 19},
        "Iowa": {"Capital": "Des Moines", "Flower": "Wild Prairie Rose", "Bird": "Eastern Goldfinch", "Date Added": "1846", "Electoral Votes": 6, "Statehood Rank": 29},
        "Kansas": {"Capital": "Topeka", "Flower": "Sunflower", "Bird": "Western Meadowlark", "Date Added": "1861", "Electoral Votes": 6, "Statehood Rank": 34},
        "Kentucky": {"Capital": "Frankfort", "Flower": "Goldenrod", "Bird": "Northern Cardinal", "Date Added": "1792", "Electoral Votes": 8, "Statehood Rank": 15},
        "Louisiana": {"Capital": "Baton Rouge", "Flower": "Magnolia", "Bird": "Brown Pelican", "Date Added": "1812", "Electoral Votes": 8, "Statehood Rank": 18},
        "Maine": {"Capital": "Augusta", "Flower": "White Pine Cone and Tassel", "Bird": "Chickadee", "Date Added": "1820", "Electoral Votes": 4, "Statehood Rank": 23},
        "Maryland": {"Capital": "Annapolis", "Flower": "Black-Eyed Susan", "Bird": "Baltimore Oriole", "Date Added": "1788", "Electoral Votes": 10, "Statehood Rank": 7},
        "Massachusetts": {"Capital": "Boston", "Flower": "Mayflower", "Bird": "Black-Capped Chickadee", "Date Added": "1788", "Electoral Votes": 11, "Statehood Rank": 6},
        "Michigan": {"Capital": "Lansing", "Flower": "Apple Blossom", "Bird": "American Robin", "Date Added": "1837", "Electoral Votes": 15, "Statehood Rank": 26},
        "Minnesota": {"Capital": "Saint Paul", "Flower": "Pink and White Lady's Slipper", "Bird": "Common Loon", "Date Added": "1858", "Electoral Votes": 10, "Statehood Rank": 32},
        "Mississippi": {"Capital": "Jackson", "Flower": "Magnolia", "Bird": "Northern Mockingbird", "Date Added": "1817", "Electoral Votes": 6, "Statehood Rank": 20},
        "Missouri": {"Capital": "Jefferson City", "Flower": "Hawthorn", "Bird": "Eastern Bluebird", "Date Added": "1821", "Electoral Votes": 10, "Statehood Rank": 24},
        "Montana": {"Capital": "Helena", "Flower": "Bitterroot", "Bird": "Western Meadowlark", "Date Added": "1889", "Electoral Votes": 3, "Statehood Rank": 41},
        "Nebraska": {"Capital": "Lincoln", "Flower": "Goldenrod", "Bird": "Western Meadowlark", "Date Added": "1867", "Electoral Votes": 5, "Statehood Rank": 37},
        "Nevada": {"Capital": "Carson City", "Flower": "Sagebrush", "Bird": "Mountain Bluebird", "Date Added": "1864", "Electoral Votes": 6, "Statehood Rank": 36},
        "New Hampshire": {"Capital": "Concord", "Flower": "Purple Lilac", "Bird": "Purple Finch", "Date Added": "1788", "Electoral Votes": 4, "Statehood Rank": 9},
        "New Jersey": {"Capital": "Trenton", "Flower": "Violet", "Bird": "Eastern Goldfinch", "Date Added": "1787", "Electoral Votes": 14, "Statehood Rank": 3},
        "New Mexico": {"Capital": "Santa Fe", "Flower": "Yucca Flower", "Bird": "Greater Roadrunner", "Date Added": "1912", "Electoral Votes": 5, "Statehood Rank": 47},
        "New York": {"Capital": "Albany", "Flower": "Rose", "Bird": "Eastern Bluebird", "Date Added": "1788", "Electoral Votes": 28, "Statehood Rank": 11},
        "North Carolina": {"Capital": "Raleigh", "Flower": "Flowering Dogwood", "Bird": "Northern Cardinal", "Date Added": "1789", "Electoral Votes": 16, "Statehood Rank": 12},
        "North Dakota": {"Capital": "Bismarck", "Flower": "Wild Prairie Rose", "Bird": "Western Meadowlark", "Date Added": "1889", "Electoral Votes": 3, "Statehood Rank": 39},
        "Ohio": {"Capital": "Columbus", "Flower": "Scarlet Carnation", "Bird": "Northern Cardinal", "Date Added": "1803", "Electoral Votes": 17, "Statehood Rank": 17},
        "Oklahoma": {"Capital": "Oklahoma City", "Flower": "Mistletoe", "Bird": "Scissor-tailed Flycatcher", "Date Added": "1907", "Electoral Votes": 7, "Statehood Rank": 46},
        "Oregon": {"Capital": "Salem", "Flower": "Oregon Grape", "Bird": "Western Meadowlark", "Date Added": "1859", "Electoral Votes": 8, "Statehood Rank": 33},
        "Pennsylvania": {"Capital": "Harrisburg", "Flower": "Mountain Laurel", "Bird": "Ruffed Grouse", "Date Added": "1787", "Electoral Votes": 19, "Statehood Rank": 2},
        "Rhode Island": {"Capital": "Providence", "Flower": "Violet", "Bird": "Rhode Island Red", "Date Added": "1790", "Electoral Votes": 4, "Statehood Rank": 13},
        "South Carolina": {"Capital": "Columbia", "Flower": "Yellow Jessamine", "Bird": "Carolina Wren", "Date Added": "1788", "Electoral Votes": 9, "Statehood Rank": 8},
        "South Dakota": {"Capital": "Pierre", "Flower": "Pasque Flower", "Bird": "Ring-necked Pheasant", "Date Added": "1889", "Electoral Votes": 3, "Statehood Rank": 40},
        "Tennessee": {"Capital": "Nashville", "Flower": "Iris", "Bird": "Northern Mockingbird", "Date Added": "1796", "Electoral Votes": 11, "Statehood Rank": 16},
        "Texas": {"Capital": "Austin", "Flower": "Bluebonnet", "Bird": "Northern Mockingbird", "Date Added": "1845", "Electoral Votes": 40, "Statehood Rank": 28},
        "Utah": {"Capital": "Salt Lake City", "Flower": "Sego Lily", "Bird": "California Gull", "Date Added": "1896", "Electoral Votes": 6, "Statehood Rank": 45},
        "Vermont": {"Capital": "Montpelier", "Flower": "Red Clover", "Bird": "Hermit Thrush", "Date Added": "1791", "Electoral Votes": 3, "Statehood Rank": 14},
        "Virginia": {"Capital": "Richmond", "Flower": "American Dogwood", "Bird": "Northern Cardinal", "Date Added": "1788", "Electoral Votes": 13, "Statehood Rank": 10},
        "Washington": {"Capital": "Olympia", "Flower": "Rhododendron", "Bird": "Willow Goldfinch", "Date Added": "1889", "Electoral Votes": 12, "Statehood Rank": 42},
        "West Virginia": {"Capital": "Charleston", "Flower": "Rhododendron", "Bird": "Northern Cardinal", "Date Added": "1863", "Electoral Votes": 4, "Statehood Rank": 35},
        "Wisconsin": {"Capital": "Madison", "Flower": "Wood Violet", "Bird": "American Robin", "Date Added": "1848", "Electoral Votes": 10, "Statehood Rank": 30},
        "Wyoming": {"Capital": "Cheyenne", "Flower": "Indian Paintbrush", "Bird": "Western Meadowlark", "Date Added": "1890", "Electoral Votes": 3, "Statehood Rank": 44}
    }

    score = 0
    print("\nWelcome to the States and Capitals Quiz!")
    print("You will be given 10 questions. Try to match states with their capitals or vice versa.\n")
    
    for _ in range(10):  # Ask 10 random questions
        state, info = random.choice(list(states_and_capitals.items()))
        capital = info["Capital"]

        if random.choice([True, False]):
            # Ask for the capital of a state
            answer = input(f"What is the capital of {state}? ").strip().title()
            if answer == capital:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The capital of {state} is {capital}.")
        else:
            # Ask for the state corresponding to a capital
            answer = input(f"{capital} is the capital of which state? ").strip().title()
            if answer == state:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! {capital} is the capital of {state}.")

        # Show detailed information about the state
        print(f"State: {state}")
        print(f"  ~ Capital: {info['Capital']}")
        print(f"  ~ Flower: {info['Flower']}")
        print(f"  ~ Bird: {info['Bird']}")
        print(f"  ~ Date Added: {info['Date Added']}")
        print(f"  ~ Electoral Votes: {info['Electoral Votes']}")
        print(f"  ~ Statehood Rank: {info['Statehood Rank']}\n")

    # Final score
    print(f"\nYour final score: {score}/10")
    if score == 10:
        print("Excellent! You know your states and capitals!")
    elif score >= 7:
        print("Good job! A little more practice and you'll master it.")
    else:
        print("Keep practicing! You'll get there.")

# Call the function to run the quiz
states_capitals_quiz()
