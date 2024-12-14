from flask import Flask, jsonify
from scraper import *

BASE_URL = 'https://balatrogame.fandom.com/wiki/'
SUB_URLS = {
    'jokers': 'Jokers',
    'decks': 'Decks',
    'tarot': 'Tarot_Cards',
    'spectral': 'Spectral_Cards',
    'planets': 'Planet_Cards',
    'vouchers': 'Vouchers',
    'enhancements': 'Card_Modifiers#Enhancements',
    'editions': 'Card_Modifiers#Editions',
    'seals': 'Card_Modifiers#Seals',
    'stakes': 'Stakes',
    'blinds': 'Blinds_and_Antes',
    'tags': 'Tags'
}


app = Flask(__name__)

# Define routes for each category to pull data for

@app.route('/jokers', methods=['GET'])
def jokers():
    url = BASE_URL + SUB_URLS['jokers']
    joker_data = fetch_joker_data(url, True)
    return joker_data


@app.route('/decks', methods=['GET'])
def decks():
    url = BASE_URL + SUB_URLS['decks']
    deck_data = fetch_deck_data(url, True)
    return deck_data


@app.route('/tarot', methods=['GET'])
def tarot():
    url = BASE_URL + SUB_URLS['tarot']
    tarot_data = fetch_tarot_data(url, True)
    return tarot_data


@app.route('/spectral', methods=['GET'])
def spectral():
    url = BASE_URL + SUB_URLS['spectral']
    spectral_data = fetch_spectral_data(url, True)
    return spectral_data

@app.route('/planets', methods=['GET'])
def planets():
    url = BASE_URL + SUB_URLS['planets']
    planet_data = fetch_planet_data(url, True)
    return planet_data


@app.route('/vouchers', methods=['GET'])
def vouchers():
    url = BASE_URL + SUB_URLS['vouchers']
    voucher_data = fetch_voucher_data(url, True)
    return voucher_data


@app.route('/enhancements', methods=['GET'])
def enhancements():
    url = BASE_URL + SUB_URLS['enhancements']
    enhancement_data = fetch_modifier_data(url, 0, True)
    return enhancement_data


@app.route('/editions', methods=['GET'])
def editions():
    url = BASE_URL + SUB_URLS['editions']
    edition_data = fetch_modifier_data(url, 1, True)
    return edition_data


@app.route('/seals', methods=['GET'])
def seals():
    url = BASE_URL + SUB_URLS['seals']
    seal_data = fetch_modifier_data(url, 2, True)
    return seal_data


@app.route('/stakes', methods=['GET'])
def stakes():
    url = BASE_URL + SUB_URLS['stakes']
    stake_data = fetch_stakes_data(url, True)
    return stake_data

@app.route('/blinds', methods=['GET'])
def blinds():
    url = BASE_URL + SUB_URLS['blinds']
    blind_data = fetch_blinds_data(url, True)
    return blind_data

@app.route('/tags', methods=['GET'])
def tags():
    url = BASE_URL + SUB_URLS['tags']
    tag_data = fetch_tags_data(url, True)
    return tag_data

# Routes to pull individual items for a category

@app.route('/jokers/<int:id>', methods=['GET'])
def jokers_id(id):
    url = BASE_URL + SUB_URLS['jokers']
    joker_data = fetch_joker_data(url)
    joker_info = joker_data[joker_data['id'] == id]
    return joker_info


@app.route('/decks/<int:id>', methods=['GET'])
def decks_id(id):
    url = BASE_URL + SUB_URLS['decks']
    deck_data = fetch_deck_data(url)
    deck_info = deck_data[deck_data['id'] == id]
    return deck_info


@app.route('/tarot/<int:id>', methods=['GET'])
def tarot_id(id):
    url = BASE_URL + SUB_URLS['tarot']
    tarot_data = fetch_tarot_data(url)
    tarot_info = tarot_data[tarot_data['id'] == id]
    return tarot_info


@app.route('/spectral/<int:id>', methods=['GET'])
def spectral_id(id):
    url = BASE_URL + SUB_URLS['spectral']
    spectral_data = fetch_spectral_data(url)
    spectral_info = spectral_data[spectral_data['id'] == id]
    return spectral_info


@app.route('/planets/<int:id>', methods=['GET'])
def planets_id(id):
    url = BASE_URL + SUB_URLS['planets']
    planet_data = fetch_planet_data(url)
    planet_info = planet_data[planet_data['id'] == id]
    return planet_info


@app.route('/vouchers/<int:id>', methods=['GET'])
def vouchers_id(id):
    url = BASE_URL + SUB_URLS['vouchers']
    voucher_data = fetch_voucher_data(url)
    voucher_info = voucher_data[voucher_data['id'] == id]
    return voucher_info


@app.route('/enhancements/<int:id>', methods=['GET'])
def enhancements_id(id):
    url = BASE_URL + SUB_URLS['enhancements']
    enhancement_data = fetch_modifier_data(url, 0)
    enhancement_info = enhancement_data[enhancement_data['id'] == id]
    return enhancement_info


@app.route('/editions/<int:id>', methods=['GET'])
def editions_id(id):
    url = BASE_URL + SUB_URLS['editions']
    edition_data = fetch_modifier_data(url, 1)
    edition_info = edition_data[edition_data['id'] == id]
    return edition_info


@app.route('/seals/<int:id>', methods=['GET'])
def seals_id(id):
    url = BASE_URL + SUB_URLS['seals']
    seal_data = fetch_modifier_data(url, 2)
    seal_info = seal_data[seal_data['id'] == id]
    return seal_info


@app.route('/stakes/<int:id>', methods=['GET'])
def stakes_id(id):
    url = BASE_URL + SUB_URLS['stakes']
    stake_data = fetch_stakes_data(url)
    stake_info = stake_data[stake_data['id'] == id]
    return stake_info


@app.route('/blinds/<int:id>', methods=['GET'])
def blinds_id(id):
    url = BASE_URL + SUB_URLS['blinds']
    blind_data = fetch_blinds_data(url)
    blind_info = blind_data[blind_data['id'] == id]
    return blind_info


@app.route('/tags/<int:id>', methods=['GET'])
def tags_id(id):
    url = BASE_URL + SUB_URLS['tags']
    tag_data = fetch_tags_data(url)
    tag_info = tag_data[tag_data['id'] == id]
    return tag_info

@app.route('/all', methods=['GET'])
def get_all():
    url = BASE_URL + SUB_URLS['jokers']
    joker_data = fetch_joker_data(url)
    url = BASE_URL + SUB_URLS['decks']
    deck_data = fetch_deck_data(url)
    url = BASE_URL + SUB_URLS['tarot']
    tarot_data = fetch_tarot_data(url)
    url = BASE_URL + SUB_URLS['spectral']
    spectral_data = fetch_spectral_data(url)
    url = BASE_URL + SUB_URLS['planets']
    planet_data = fetch_planet_data(url)
    url = BASE_URL + SUB_URLS['vouchers']
    voucher_data = fetch_voucher_data(url)
    url = BASE_URL + SUB_URLS['enhancements']
    enhancement_data = fetch_modifier_data(url, 0)
    url = BASE_URL + SUB_URLS['editions']
    edition_data = fetch_modifier_data(url, 1)
    url = BASE_URL + SUB_URLS['seals']
    seal_data = fetch_modifier_data(url, 2)
    url = BASE_URL + SUB_URLS['stakes']
    stake_data = fetch_stakes_data(url)
    url = BASE_URL + SUB_URLS['blinds']
    blind_data = fetch_blinds_data(url)
    url = BASE_URL + SUB_URLS['tags']
    tag_data = fetch_tags_data(url)
    return joker_data, deck_data, tarot_data, spectral_data, planet_data, voucher_data, enhancement_data, edition_data, seal_data, stake_data, blind_data, tag_data


# Run the app
if __name__ == '__main__':
    app.run(debug=False)