# ByBit Integration

The code in this directory is an sdk for interacting with the bybit platform.

## Getting started

The following is a code snippet to create the client object and make a Get request. Please note that our client class has access to all of the subclass functions in our sdk library.  
```python
from bybit_sdk.bybit_client import ByBitClient

# set required variables
base_url = 'https://api-testnet.bybit.com/'
api_key = '<YOUR API KEY>'
api_secret = '<YOUR API SECRET>'
web_socket_url = '<WEB_SOCKET_URL>' # Websocket Url is an optional parameter only needed for web socket data. 

# create platform client
client = ByBitClient(base_url=base_url, api_key=api_key, api_secret=api_secret, web_socket_url=web_socket_url)


client.get_symbol_data()
```



## REST API Docs

Link: https://bybit-exchange.github.io/docs/inverse/

Common:
- [Server time](bybit_client.py)
    - Gets the current server time in seconds with trailing decimals.

Active Order
- [Place active order](bybit_active_orders.py)
    - Places an order the bybit exchange.
- [Place active order-V2](bybit_active_orders.py)
- [Get active order](bybit_active_orders.py)
    - Gets an active order.
- [Cancel active order](bybit_active_orders.py)
    - Cancels an active order.
- [Cancel active order-V2](bybit_active_orders.py)
- [Edit active order](bybit_active_orders.py)
- [Cancel all active orders](bybit_active_orders.py)
- [Query active order (real-time)](bybit_active_orders.py)


Conditional Order
- [Place conditional order](bybit_conditional_orders.py)
    - Places a conditional order on the bybit exchange.
- [Get conditional order](bybit_conditional_orders.py)
    - Gets a conditional order on the bybit exchange
- [Cancel conditional order](bybit_conditional_orders.py)
    - Cancels a conditional order on the bybit exchange
- [Cancel all conditional orders](bybit_conditional_orders.py)
- [Edit conditional order](bybit_conditional_orders.py)
- Query stop order (real-time)
    - Not yet implemented. 

Positions
- [User leverage](bybit_positions.py)
- [Change leverage](bybit_positions.py)
- [My position](bybit_positions.py)
    - Gets position list including wallet information. 
- [Change margin](bybit_positions.py)
- [My position-V2 (real-time)](bybit_positions.py)
- [Change margin](bybit_positions.py)
- [Set Trading-Stop](bybit_positions.py)


### Wallet

- [Get Wallet fund records](bybit_wallet.py)
- [Get Withdraw records](bybit_wallet.py)
- [Get Account Balance](bybit_wallet.py)
- Set risk limit
    - Not yet implemented.
- Get risk limit list
    - Not yet implemented.

Funding
- [Funding rate](bybit_funding.py)
    - Funding rate is generated every 8 hours at 00:00 UTC, 08:00 UTC and 16:00 UTC. If it's 12:00 UTC now, what you will get is the funding rate generated at 08:00 UTC.
- [My funding fee](bybit_funding.py)
    - Users last funding fee. The current interval's fund fee settlement is based on the previous interval's fund rate. For example, at 16:00, the settlement is based on the fund rate generated at 8:00. The fund rate generated at 16:00 will be used at 0:00 on the next day.
- [Predicted funding](bybit_funding.py)
    - Gets the predicted funding rate for the next settlement period. 
    - When the funding rate is positive, long positions pay short positions and if it is negative, the short position holders have to pay the long position holders. If you close your position before the Funding interval, you will not be charged. This means it may be good to exit before this funding fee. 
    - funding fee = position value*funding rate. Position value = quantity of contract/mark price.

Execution
- [Get the trade records of a order](bybit_executions.py)

Market data
- [Get the orderbook](bybit_market_data.py)
- [Get latest information for symbol](bybit_market_data.py)
    - i.e. get tickers
- [Get public trading records](bybit_market_data.py)
- [Get symbols](bybit_market_data.py)
    - Different from the symbol bullet above. 