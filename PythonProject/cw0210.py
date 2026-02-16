class sportsteam:

    level = "professional"

    def __init__(self, sport, name, city, year, country = "United States"):
        self.sport = sport
        self.name = name
        self.city = city
        self.year = year
        self.country = country

    def teaminfo(self):
        print(f"{self.name}, located in {self.city}, {self.country} who "
              f"plays {sportsteam.level} {self.sport}. Establised in {self.year}")

team1= sportsteam("basketball", "Boston Celtics", "Boston", "1946")
team2= sportsteam("soccer", "Liverpool F.C", "Liverpool", "1892", "England")
team1.teaminfo()
team2.teaminfo()