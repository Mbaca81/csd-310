def city_country(city, country, population=None, language=None):
    """Return a formatted City, Country string including population and language."""
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, language {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"


print(city_country("santiago", "chile", 5000000, "spanish"))


