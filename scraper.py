from bs4 import BeautifulSoup
import requests
import pandas as pd

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

def fetch_joker_data(url, asList=False):
    """
        Fetches and parses table data for Jokers from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    joker_table = tables[1]

    rows = []
    names = []
    # Iterate over the rows in the table
    for tr in joker_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 7:  # Ensure there are enough cells to process
            continue

        # Extract the data from the cells
        name_tag = cells[1].find_all("a")[1]
        image_url = cells[1].find_all("a")[0].find('img').get('data-src') or cells[1].find_all("a")[0].find('img').get('src')

        joker_data = {
            "Name": name_tag.text.strip() if name_tag else None,
            "Image_URL": image_url,
            "Effect": cells[2].text.strip(),
            "Cost": cells[3].text.strip(),
            "Rarity": cells[4].text.strip(),
            "Type": cells[6].text.strip(),
        }
        names.append(name_tag.text.strip())
        rows.append(joker_data)
    rows = pd.DataFrame(rows)
    # Replace the type abbreviations with full names
    type_dict = {
        '+m': 'Additive Mult',
        '+c': 'Chips',
        'Xm': 'Multiplicative Mult',
        '++': 'Chips & Additive Mult ',
        '!!': 'Effect',
        '...': 'Retrigger',
        '+$': 'Economy'
    }
    rows['Type'] = rows['Type'].map(type_dict)
    if asList:
        return names
    return rows.reset_index().rename(columns={'index': 'id'})

def fetch_deck_data(url, asList=False):
    """
        Fetches and parses table data for Decks from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    deck_table = tables[0]

    rows = []
    names = []
    for tr in deck_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 3:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag = cells[1].find('a')
        desc = cells[2]

        deck_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'description': desc.text.strip(),
        }
        rows.append(deck_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_tarot_data(url, asList=False):
    """
        Fetches and parses table data for Tarot Cards from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    tarot_table = tables[0]

    rows = []
    names = []
    for tr in tarot_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 2:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag = cells[1].find('a')
        desc = cells[2]

        tarot_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'description': desc.text.strip(),
        }
        rows.append(tarot_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_planet_data(url, asList=False):
    """
        Fetches and parses table data for Planet Cards from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    planet_table = tables[0]

    rows = []
    names = []
    for tr in planet_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 4:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag = cells[1].find('span')
        addition = cells[2]
        hand = cells[3].find('a').text
        hand_base_score = cells[4].text

        planet_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'addition': addition.text.strip(),
            'hand': hand.strip(),
            'hand_base_score': hand_base_score.strip(),
        }
        rows.append(planet_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_spectral_data(url, asList=False):
    """
        Fetches and parses table data for Spectral Cards from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    spectral_table = tables[0]

    rows = []
    names = []
    for tr in spectral_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 3:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag = cells[1].find('span')
        desc = cells[2]

        spectral_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'description': desc.text.strip(),
        }
        rows.append(spectral_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_voucher_data(url, asList=False):
    """
        Fetches and parses table data for Vouchers from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    voucher_table = tables

    rows = []
    names = []
    for tr in voucher_table.find("tbody").find_all("tr")[2:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 4:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image_base = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag_base = cells[0]
        desc_base = cells[1]
        image_upg = cells[2].find('a').find('img').get('data-src') or cells[2].find('a').find('img').get('src')
        name_tag_upg = cells[2] 
        desc_upg = cells[3]

        voucher_data = {
            'image_base': image_base,
            'name_base': name_tag_base.text.strip(),
            'description_base': desc_base.text.strip(),
            'image_upg': image_upg,
            'name_upg': name_tag_upg.text.strip(),
            'description_upg': desc_upg.text.strip(),
        }
        rows.append(voucher_data)
        names.append(name_tag_base.text.strip())
        names.append(name_tag_upg.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_modifier_data(url, idx, asList=False):
    """
        Fetches and parses table data for all card modifiers from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
            idx (int): Index number indicating which modifier to fetch. 0- Enhancements, 1- Editions, 2- Seals
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    mod_table = tables[idx]

    rows = []
    names = []
    for tr in mod_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 2:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag = cells[1].find('a')
        desc = cells[2]
        cost = cells[3].text.strip()

        enhancement_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'description': desc.text.strip(),
            'cost': cost,
        }
        rows.append(enhancement_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_stakes_data(url, asList=False):
    """
        Fetches and parses table data for Stakes from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    stake_table = tables[0]

    rows = []
    names = []
    for tr in stake_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 3:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[1].find('a').find('img').get('data-src') or cells[1].find('a').find('img').get('src')
        name_tag = cells[2]
        desc = cells[3]
        unlocks_deck = cells[4]

        stake_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'description': desc.text.strip(),
            'unlocks_deck': unlocks_deck.text.strip(),
        }
        rows.append(stake_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_blinds_data(url, asList=False):
    """
        Fetches and parses table data for Blinds and Antes from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    blind_table = tables[0]

    rows = []
    names = []
    for tr in blind_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 5:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag = cells[1]
        desc = cells[2]
        min_ante = cells[3]
        min_score = cells[4]
        reward = cells[5]

        blind_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'description': desc.text.strip(),
            'min_ante': min_ante.text.strip(),
            'min_score': min_score.text.strip(),
            'reward': reward.text.strip()
        }
        rows.append(blind_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

def fetch_tags_data(url, asList=False):
    """
        Fetches and parses table data for Tags from the Balatro fandom Wiki.
        Args:
            url (str): URL to fetch data from.
            asList (bool): Whether to return only the list of elements or the descriptions as well.
        Returns:
            pd.DataFrame: DataFrame containing the table data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to fetch data from {url}')
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables in the page
    tables = soup.find_all('table', {'class': 'fandom-table'})
    if not tables:
        raise Exception(f'No tables found in {url}')
    
    tag_table = tables[0]

    rows = []
    names = []
    for tr in tag_table.find("tbody").find_all("tr")[1:]:  # Skip the header row
        cells = tr.find_all("td")
        if len(cells) < 3:  # Ensure there are enough cells to process
            continue

        # Extract the data
        image = cells[0].find('a').find('img').get('data-src') or cells[0].find('a').find('img').get('src')
        name_tag = cells[1]
        desc = cells[2]
        ante = cells[4]

        tag_data = {
            'image': image,
            'name': name_tag.text.strip(),
            'description': desc.text.strip(),
            'ante': ante.text.strip(),
        }
        rows.append(tag_data)
        names.append(name_tag.text.strip())
    if asList:
        return names
    return (pd.DataFrame(rows)).reset_index().rename(columns={'index': 'id'})

