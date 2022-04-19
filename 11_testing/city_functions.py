"""A collection of functions for working with cities."""


def format_city_country(city, country, population=0):
    """Return a string like 'Zacatecas, Mexico - population 200000'."""

    formatted_city = f'{city.title()}, {country.title()}'

    if population:
        return formatted_city + f' - population {population}'
    else:
        return formatted_city


print(format_city_country('zacatecas', 'mexico', 200_000))
