from utils import fetch_symbol
from typing import Dict
import yfinance as yf

def company_profile(comapny_name: str)-> Dict[str,str|float]:
    """
    Returns a dict containing:
        - Current Price 
        - PE Ratio
        - Sector 
        - Industry
        - Business Summary
    """
    symbol = fetch_symbol(comapny_name)
    ticker = yf.Ticker(symbol)
    price_attrs : list = ['regularMarketPrice', 'currentPrice', 'price']

    try:
        result: dict = {
            'current_price': None,
            'pe_ratio': None,
            'sector': None,
            'industry': None,
            'desc': None,
        }
        for attr in price_attrs:
            if result['current_price'] is None and attr in ticker.info and ticker.info[attr] is not None:
                result['current_price'] = ticker.info[attr]

        current_price = ticker.fast_info.get('last_price')
        if current_price is not None:
            result['current_price'] = current_price

        if 'trailingPE' in ticker.info and ticker.info['trailingPE'] is not None:
            result['pe_ratio'] = ticker.info['trailingPE']

        if 'sector' in ticker.info and ticker.info['sector'] is not None:
            result['sector'] = ticker.info['sector']

        if 'industry' in ticker.info and ticker.info['industry'] is not None:
            result['industry'] = ticker.info['industry']

        if 'longBusinessSummary' in ticker.info and ticker.info['longBusinessSummary'] is not None:
            result['desc'] = ticker.info['longBusinessSummary']

    except Exception as e:
        raise ValueError(f"Error fetching data for '{symbol}': {e}")
    

    return result


if __name__ == '__main__':
    data = company_profile('Bharat Dynamics')
    print(data)




