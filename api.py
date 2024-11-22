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

@app.route('/jokers/<int:id>', methods=['GET'])
def jokers():
    url = BASE_URL + SUB_URLS['jokers']
    joker_data = fetch_joker_data(url, True)
    joker_json = joker_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(joker_json)


@app.route('/decks/<int:id>', methods=['GET'])
def decks():
    url = BASE_URL + SUB_URLS['decks']
    deck_data = fetch_deck_data(url, True)
    deck_json = deck_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(deck_json)


@app.route('/tarot/<int:id>', methods=['GET'])
def tarot():
    url = BASE_URL + SUB_URLS['tarot']
    tarot_data = fetch_tarot_data(url, True)
    tarot_json = tarot_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(tarot_json)


@app.route('/spectral', methods=['GET'])
def spectral():
    url = BASE_URL + SUB_URLS['spectral']
    spectral_data = fetch_spectral_data(url, True)
    spectral_json = spectral_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(spectral_json)


@app.route('/planets', methods=['GET'])
def planets():
    url = BASE_URL + SUB_URLS['planets']
    planet_data = fetch_planet_data(url, True)
    planet_json = planet_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(planet_json)


@app.route('/vouchers', methods=['GET'])
def vouchers():
    url = BASE_URL + SUB_URLS['vouchers']
    voucher_data = fetch_voucher_data(url, True)
    voucher_json = voucher_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(voucher_json)


@app.route('/enhancements', methods=['GET'])
def enhancements():
    url = BASE_URL + SUB_URLS['enhancements']
    enhancement_data = fetch_modifier_data(url, True, 0)
    enhancement_json = enhancement_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(enhancement_json)


@app.route('/editions', methods=['GET'])
def editions():
    url = BASE_URL + SUB_URLS['editions']
    edition_data = fetch_modifier_data(url, True, 1)
    edition_json = edition_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(edition_json)


@app.route('/seals', methods=['GET'])
def seals():
    url = BASE_URL + SUB_URLS['seals']
    seal_data = fetch_modifier_data(url, True, 2)
    seal_json = seal_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(seal_json)


@app.route('/stakes', methods=['GET'])
def stakes():
    url = BASE_URL + SUB_URLS['stakes']
    stake_data = fetch_stakes_data(url, True)
    stake_data.reset_index().rename(columns={'index': 'id'}, inplace=True)
    stake_json = stake_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(stake_json)


@app.route('/blinds', methods=['GET'])
def blinds():
    url = BASE_URL + SUB_URLS['blinds']
    blind_data = fetch_blinds_data(url, True)
    blind_data.reset_index().rename(columns={'index': 'id'}, inplace=True)
    blind_json = blind_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(blind_json)


@app.route('/tags', methods=['GET'])
def tags():
    url = BASE_URL + SUB_URLS['tags']
    tag_data = fetch_tags_data(url, True)
    tag_json = tag_data.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(tag_json)

# Routes to pull individual items for a category

@app.route('/jokers/<int:id>', methods=['GET'])
def jokers(id):
    url = BASE_URL + SUB_URLS['jokers']
    joker_data = fetch_joker_data(url)
    joker_info = joker_data[joker_data['id'] == id]
    joker_json = joker_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(joker_json)


@app.route('/decks/<int:id>', methods=['GET'])
def decks(id):
    url = BASE_URL + SUB_URLS['decks']
    deck_data = fetch_deck_data(url)
    deck_info = deck_data[deck_data['id'] == id]
    deck_json = deck_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(deck_json)


@app.route('/tarot/<int:id>', methods=['GET'])
def tarot(id):
    url = BASE_URL + SUB_URLS['tarot']
    tarot_data = fetch_tarot_data(url)
    tarot_info = tarot_data[tarot_data['id'] == id]
    tarot_json = tarot_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(tarot_json)


@app.route('/spectral/<int:id>', methods=['GET'])
def spectral(id):
    url = BASE_URL + SUB_URLS['spectral']
    spectral_data = fetch_spectral_data(url)
    spectral_info = spectral_data[spectral_data['id'] == id]
    spectral_json = spectral_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(spectral_json)


@app.route('/planets/<int:id>', methods=['GET'])
def planets(id):
    url = BASE_URL + SUB_URLS['planets']
    planet_data = fetch_planet_data(url)
    planet_info = planet_data[planet_data['id'] == id]
    planet_json = planet_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(planet_json)


@app.route('/vouchers/<int:id>', methods=['GET'])
def vouchers(id):
    url = BASE_URL + SUB_URLS['vouchers']
    voucher_data = fetch_voucher_data(url)
    voucher_info = voucher_data[voucher_data['id'] == id]
    voucher_json = voucher_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(voucher_json)


@app.route('/enhancements/<int:id>', methods=['GET'])
def enhancements(id):
    url = BASE_URL + SUB_URLS['enhancements']
    enhancement_data = fetch_modifier_data(url, 0)
    enhancement_info = enhancement_data[enhancement_data['id'] == id]
    enhancement_json = enhancement_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(enhancement_json)


@app.route('/editions/<int:id>', methods=['GET'])
def editions(id):
    url = BASE_URL + SUB_URLS['editions']
    edition_data = fetch_modifier_data(url, 1)
    edition_info = edition_data[edition_data['id'] == id]
    edition_json = edition_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(edition_json)


@app.route('/seals/<int:id>', methods=['GET'])
def seals(id):
    url = BASE_URL + SUB_URLS['seals']
    seal_data = fetch_modifier_data(url, 2)
    seal_info = seal_data[seal_data['id'] == id]
    seal_json = seal_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(seal_json)


@app.route('/stakes/<int:id>', methods=['GET'])
def stakes(id):
    url = BASE_URL + SUB_URLS['stakes']
    stake_data = fetch_stakes_data(url)
    stake_info = stake_data[stake_data['id'] == id]
    stake_json = stake_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(stake_json)


@app.route('/blinds/<int:id>', methods=['GET'])
def blinds(id):
    url = BASE_URL + SUB_URLS['blinds']
    blind_data = fetch_blinds_data(url)
    blind_info = blind_data[blind_data['id'] == id]
    blind_json = blind_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(blind_json)


@app.route('/tags/<int:id>', methods=['GET'])
def tags(id):
    url = BASE_URL + SUB_URLS['tags']
    tag_data = fetch_tags_data(url)
    tag_info = tag_data[tag_data['id'] == id]
    tag_json = tag_info.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(tag_json)

# Run the app
if __name__ == '__main__':
    app.run(debug=False)