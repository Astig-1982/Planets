from planets import Planets

def get_started():
    # this function retrieves the requested information about specific plantes
    message = ''
    while message != 'N':
        # it takes the user input and based on it, it creates an object based on Plants class
        planet = input('Choose a planet: ').lower()
        if planet == 'mercury':
            planet = Planets("Mercury", "2,439.7", "3.285 × 10^23", "5.43", ".38")
        elif planet == 'venus':
            planet = Planets("Venus", "6,051.8", "4.867 × 10^24", "5.24", ".9")
        elif planet == 'earth':
            planet = Planets("Earth", "6,371", "5.972 × 10^24", "5.51", "1")
        elif planet == 'mars':
            planet = Planets("Mars", "3,389.5", "6.39 × 10^23", "3.93", ".378")
        elif planet == 'jupiter':
            planet = Planets("Jupiter", "69,911", "1.898 × 10^27", "1.33", "2.36")
        elif planet == 'saturn':
            planet = Planets("Saturn", "58,232", "5.683 × 10^26", "687", ".9")
        elif planet == 'uranus':
            planet = Planets("Uranus", "25,362", "8.681 × 10^25", "1.27", ".88")
        elif planet == 'neptune':
            planet = Planets("Neptune", "24,622", "1.024 × 10^26", "1.64", "1.12")

        # it takes the user input and based on it, it calls the relevant method created in Planets class
        spec = input('Choose the spec: size, weight, density, my weight: ')
        if spec == 'size':
            print(planet.planet_size())
        elif spec == 'weight':
            print(planet.planet_weight())
        elif spec == 'density':
            print(planet.planet_density())
        elif spec == 'my weight':
            your_weight = input('What is your weight in kg? ')
            print(planet.calculate_your_weight(your_weight))

        message = input('Play again? ').upper()

# executing the function
get_started()