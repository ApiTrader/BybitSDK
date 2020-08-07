
class MarketDataTransforms():

    def get_symbol_item(self, data, item, symbol='BTCUSD'):
        """
        Returns an element from the market data json. Searches for the symbol before returning the data point. 

        Data is from "https://api-testnet.bybit.com/v2/public/tickers" endpoint on bybit. 
        """
        data = data.get('result')

        ind = 0
        for i in range(0, len(data)):
            if data[i].get('symbol') == symbol:
                ind = i
                break

        return data[ind].get(item)
        
        