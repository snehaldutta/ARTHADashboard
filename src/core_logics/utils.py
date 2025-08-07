from ticker import fetch_ticker

def fetch_symbol(company_name: str) -> str:
    """
    Returns the ticker symbol for a given company name.
    If the company_name already looks like a ticker, it's returned as-is.
    """
    if '.' in company_name:
        return company_name

    ticker = fetch_ticker(company_name)

    if not ticker or not isinstance(ticker, str):
        raise ValueError(f"Unable to resolve ticker for company: {company_name}")

    return ticker


