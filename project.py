"""Simple prototype for the Smart Umrah Package Matcher.

This is an illustrative prototype using fictional demo packages.
It ranks packages by weighted distance from a traveler's preferences.
"""

packages = [
    {
        "name": "Package A",
        "price": 240000,
        "days": 21,
        "makkah_distance": 800,
        "madinah_distance": 800,
    },
    {
        "name": "Package B",
        "price": 270000,
        "days": 21,
        "makkah_distance": 300,
        "madinah_distance": 500,
    },
    {
        "name": "Package C",
        "price": 310000,
        "days": 28,
        "makkah_distance": 200,
        "madinah_distance": 300,
    },
]

preferences = {
    "price": 260000,
    "days": 21,
    "makkah_distance": 500,
    "madinah_distance": 500,
}

weights = {
    "price": 0.45,
    "days": 0.15,
    "makkah_distance": 0.25,
    "madinah_distance": 0.15,
}


def min_max(values):
    low = min(values)
    high = max(values)
    if high == low:
        return {value: 0.0 for value in values}
    return {value: (value - low) / (high - low) for value in values}


def rank_packages(packages, preferences, weights):
    all_fields = list(preferences.keys())
    normalized = {}

    for field in all_fields:
        values = [package[field] for package in packages] + [preferences[field]]
        scaled = min_max(values)
        normalized[field] = {
            "packages": [scaled[package[field]] for package in packages],
            "preference": scaled[preferences[field]],
        }

    ranked = []
    for index, package in enumerate(packages):
        distance = 0.0
        for field in all_fields:
            difference = abs(
                normalized[field]["packages"][index]
                - normalized[field]["preference"]
            )
            distance += weights[field] * difference
        ranked.append((distance, package["name"]))

    return sorted(ranked)


if __name__ == "__main__":
    print("Recommended packages:")
    for position, (distance, name) in enumerate(
        rank_packages(packages, preferences, weights), start=1
    ):
        print(f"{position}. {name} (distance: {distance:.3f})")
