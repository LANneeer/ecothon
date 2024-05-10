car_brands_by_country = {
    "JAPAN": ['TOYOTA', 'HONDA', 'NISSAN', 'MAZDA', 'SUBARU'],
    "USA": ['FORD', 'CHEVROLET', 'TESLA', 'CADILLAC', 'DODGE'],
    "SOUTH KOREA": ['HYUNDAI', 'KIA', 'GENESIS'],
    "CIS": ['LADA', 'GAZ', 'UAZ', 'BELAZ'],
    "CHINA": ['GEELY', 'BYD', 'GREAT WALL', 'HAVAL', 'CHERY', 'NIO'],
    "EU": ['VOLKSWAGEN', 'MERCEDES-BENZ', 'BMW', 'AUDI', 'PORSCHE', 'FERRARI', 'LAMBORGHINI', 'FIAT', 'MASERATI',
           'ALFA ROMEO', 'RENAULT', 'PEUGEOT', 'CITROËN', 'BUGATTI', 'ASTON MARTIN', 'ROLLS ROYCE', 'BENTLEY', 'MINI',
           'JAGUAR']
}


def brand_to_country(model: str, car_brands_by_country: dict) -> str:
    brand = model.split()[0].upper()
    for country, brands in car_brands_by_country.items():
        if brand in brands:
            return country
    return "Brand not found"


def get_eco_class(year_of_release: int, country: str) -> int:
    eco_classes = {
        "CIS": {
            "years": [(0, 2005), (2006, 2007), (2008, 2012), (2013, 2015), (2016, 2025)],
            "classes": [0, 2, 3, 4, 5]
        },
        "EU": {
            "years": [(1996, 1999), (2000, 2004), (2005, 2009), (2010, 2025)],
            "classes": [2, 3, 4, 5]
        },
        "JAPAN": {
            "years": [(0, 1997), (1998, 2004), (2005, 2009), (2010, 2025)],
            "classes": [1, 2, 3, 4]
        },
        "SOUTH KOREA": {
            "years": [(0, 2000), (2001, 2002), (2003, 2005), (2006, 2009), (2010, 2025)],
            "classes": [1, 2, 3, 4, 5]
        },
        "USA": {
            "years": [(1990, 1995), (1996, 2000), (2001, 2003), (2004, 2009), (2010, 2025)],
            "classes": [1, 2, 3, 4, 5]
        },
        "CHINA": {
            "years": [(0 - 2003), (2004, 2007), (2008, 2010), (2011, 2013), (2013, 2025)],
            "classes": [1, 2, 3, 4, 5]
        }
    }

    region_info = eco_classes.get(country)
    if region_info:
        for index, (start, end) in enumerate(region_info["years"]):
            if start <= year_of_release <= end:
                return region_info["classes"][index]

    return 0


def get_emission_standards(mq9: float, mq135: float, PM25: float, ecoclass: int) -> str:
    eco_standart = {
        0: {
            "CO": 0.5,
            "NO": 3.5,
            "PM25": 64.67,
        },
        1: {
            "CO": 0.5,
            "NO": 3.5,
            "PM25": 64.67,
        },
        2: {
            "CO": 0.5,
            "NO": 3.5,
            "PM25": 64.67,
        },
        3: {
            "CO": 0.3,
            "NO": 3.5,
            "PM25": 64.67,
        },
        4: {
            "CO": 0.3,
            "NO": 3.5,
            "PM25": 64.67,
        },
        5: {
            "CO": 0.3,
            "NO": 3.5,
            "PM25": 64.67,
        },
    }
    eco_info = eco_standart.get(ecoclass)
    if eco_info:
        if eco_info["CO"] >= mq9 and eco_info["NO"] >= mq135 and eco_info["PM25"] >= PM25:
            result = "OK"
        else:
            result = "BAD"
    return {"eco_info": eco_info, "result": result}


if __name__ == "__main__":
    year_of_release = 2005
    model = "LADA OUTBACK"
    mq9 = 0.5
    mq135 = 0.3
    PM25 = 21

    country = brand_to_country(model, car_brands_by_country)
    eco_class = get_eco_class(year_of_release, country)
    status = get_emission_standards(mq9, mq135, PM25, eco_class)

    print(f"The eco class for a car from {country} released in {year_of_release} is: {eco_class}, status: {status}")
