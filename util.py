import pandas as pd
import api
import Levenshtein


RARITY_COLORS = {
    'common': 0x0093ff,
    'uncommon': 0x35bc86,
    'rare': 0xff4c40,
    'legendary': 0xaa5ab4,
    'spectral': 0x2e76fd,
    'planets': 0x00a8ca,
    'tarot': 0x7b559c
}

def fetch_data(key, args = None):
    func = getattr(api, f"{key}")
    if func:
        if args:
            return func(args)
        else:
            return func()
    else:
        return None

# TODO: 'Soul' returns 'Sigil' as the closest match but it should return 'The Soul'. Check algorithm for partial matches.
# TODO: Check distances for all 3 cases: lower, upper and title. Edge case: DNA when converted to title case does not give the correct result.
def find_closest_match(category, search_term):
    data = fetch_data(category)
    data['category'] = category
    # Convert search term to title case
    search_term = search_term.title()
    # Calculate the Levenshtein distance for each item name
    distances = [(id, item, Levenshtein.distance(search_term, item), category) for id, item, category in data.values]

    # Find the minimum distance
    min_distance = min(distances, key=lambda x: x[2])[2]

    # Return all items with the minimum distance
    closest_matches = [(id, item, distance, category) for id, item, distance, category in distances if distance == min_distance]
    return closest_matches
