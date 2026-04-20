from hangman import choose_word, update_guessed, display_guessed, is_word_guessed



cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
    "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus",
    "San Francisco", "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington", "Boston",
    "El Paso", "Nashville", "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis",
    "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento",
    "Kansas City", "Long Beach", "Mesa", "Atlanta", "Colorado Springs", "Virginia Beach",
    "Raleigh", "Omaha", "Miami", "Oakland", "Minneapolis", "Tulsa", "Wichita", "New Orleans",
    "Arlington", "London", "Birmingham", "Glasgow", "Liverpool", "Manchester", "Leeds",
    "Sheffield", "Edinburgh", "Bristol", "Cardiff", "Paris", "Marseille", "Lyon", "Toulouse",
    "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rome", "Milan",
    "Naples", "Turin", "Palermo", "Genoa", "Bologna", "Florence", "Venice", "Berlin", "Hamburg",
    "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig",
    "Bremen", "Prague", "Brno", "Ostrava", "Plzen", "Liberec", "Warsaw", "Krakow", "Lodz",
    "Wroclaw", "Poznan", "Gdansk", "Budapest", "Debrecen", "Szeged", "Miskolc", "Pecs",
    "Sofia", "Plovdiv", "Varna", "Burgas", "Ruse", "Athens", "Thessaloniki", "Patras",
    "Heraklion", "Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Oslo", "Bergen", "Trondheim",
    "Stavanger", "Stockholm", "Gothenburg", "Malmö", "Uppsala", "Copenhagen", "Aarhus", "Odense",
    "Aalborg", "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Fukuoka", "Kobe", "Kyoto",
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Beijing", "Shanghai", "Guangzhou",
    "Shenzhen", "Chengdu", "Wuhan", "Hangzhou", "Chongqing", "Nanjing", "Tianjin", "Hong Kong",
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat",
    "Pune", "Jaipur", "Jakarta", "Surabaya", "Bandung", "Medan", "Bekasi", "Depok", "Tangerang",
    "Makassar", "Manila", "Quezon City", "Caloocan", "Davao", "Cebu", "Hanoi", "Ho Chi Minh City",
    "Can Tho", "Da Nang", "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast",
    "Newcastle", "Wollongong", "Auckland", "Wellington", "Christchurch", "Hamilton", "Tauranga",
    "Cape Town", "Johannesburg", "Durban", "Pretoria", "Port Elizabeth", "Bloemfontein", "Lagos",
    "Kano", "Ibadan", "Abuja", "Port Harcourt", "Benin City", "Nairobi", "Mombasa", "Kisumu",
    "Thika", "Eldoret", "Cairo", "Alexandria", "Giza", "Shubra El-Kheima", "Port Said",
    "Casablanca", "Rabat", "Fes", "Marrakech", "Tangier", "Salé", "Mexico City", "Guadalajara",
    "Monterrey", "Puebla", "Tijuana", "León", "Zapopan", "Ciudad Juárez", "Buenos Aires",
    "Córdoba", "Rosario", "Mendoza", "La Plata", "Santiago", "Valparaíso", "Concepción",
    "Viña del Mar", "Antofagasta", "São Paulo", "Rio de Janeiro", "Brasilia", "Salvador",
    "Fortaleza", "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Toronto", "Montreal",
    "Vancouver", "Calgary", "Ottawa", "Edmonton", "Quebec City", "Winnipeg", "Hamilton",
    "Kitchener", "London", "Halifax", "Barcelona", "Valencia", "Seville", "Zaragoza", "Málaga",
    "Murcia", "Palma", "Bilbao", "Athens", "Thessaloniki", "Patras", "Heraklion", "Dubai",
    "Abu Dhabi", "Doha", "Kuwait City", "Riyadh", "Jeddah", "Tehran", "Baghdad", "Amman",
    "Beirut", "Damascus", "Istanbul", "Ankara", "Izmir", "Bucharest", "Cluj-Napoca", "Timișoara",
    "Sibiu", "Constanța", "Belgrade", "Novi Sad", "Niš", "Zagreb", "Split", "Ljubljana",
    "Sarajevo", "Skopje", "Tirana", "Minsk", "Moscow", "Saint Petersburg", "Novosibirsk",
    "Yekaterinburg", "Kazan", "Nizhny Novgorod", "Chelyabinsk", "Samara", "Ufa", "Omsk",
    "Riyadh", "Jeddah", "Mecca", "Medina", "Dammam", "Khobar", "Bahrain", "Manama", "Doha",
    "Muscat", "Salalah", "Sohar", "Kuwait City", "Al Ahmadi", "Hawalli", "Seoul", "Incheon",
    "Busan", "Daegu", "Daejeon", "Gwangju", "Ulsan", "Jeju", "Tokyo", "Osaka", "Nagoya",
    "Sapporo", "Fukuoka", "Kobe", "Kyoto", "Hiroshima", "Sendai", "Kitakyushu", "Chiba",
    "Yokohama", "Nagasaki", "Kanazawa", "Toyama", "Hakodate", "Niigata"
]

def main():

    print("Welcome to Hangman gameeeeee!!!!")
    print("Please guess the word below!! P.S it is a city! and spaces allowed")
    
    word = choose_word(cities).casefold()

    # Letter placeholder
    for _ in word:
        print('_', end=" ")

    print()

    guessed = set()
    chances = len(word) + 4

    while chances > 0:
        print()
        chances -= 1
        
        guess = input("Enter a letter! ").casefold()

        if not guess.isalpha() or guess == " ":
            print("Enter only a letter!!")
            continue

        elif (len(guess)) >1:
            print("Enter only A letter")
            continue
        elif guess in guessed:
            print("oops! You already guessed that letter!")
        else:
            guessed = update_guessed(guessed, guess)
            print("guessed:", guessed)
            print(display_guessed(word, guessed))

            print()
            print("Your chance(s) left: ", chances)

        if is_word_guessed(word, guessed):
            print("Congrats")
    print('Boo !! You are dead. The word is: ', word)

if __name__ == "__main__":
    main()
        

