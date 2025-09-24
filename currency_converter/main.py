from logging import root
import sys
import os
import json

# Add the root directory to the pyhton path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)

import logger  # type: ignore



def load_json(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float: # type: ignore
    base: str = base.lower()
    to: str = to.lower()

    source_currency: dict | None = rates.get(base)
    target_currency: dict | None = rates.get(to)

    if target_currency is not None and (source_currency is not None or base=='eur'):
        if base == "eur":
            return amount * target_currency['rate']
        else:
            return amount * (source_currency['rate'] / target_currency['rate']) # type: ignore
    else:
        logger.logging.info("Invalid currency type")
        return 0.00
    

def main() -> None:
    rates: dict[str, dict] = load_json("currency_converter/rates.json")
    result: float = convert(amount=100, base='eur', to="clp", rates=rates)
    print(result)

    
if __name__ == "__main__":
    main()











"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro. 
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""


# Free API article

# https://medium.com/@apilayer/best-free-exchange-rate-apis-for-accurate-currency-conversion-891505a17da7#:~:text=CurrencyLayer%20is%20a%20popular%20foreign,focus%20on%20accuracy%20and%20reliability.