
class WalletDataTransforms():

    def get_wallet_item(self, data, item, item_root='result', data_index=0, symbol='BTCUSD'):
        """
        Given a data point in the json, it returns values from the tickers api.
        """     

        if item_root is not None: 

            return data.get(item_root).get('data')[data_index].get(item)
        else :
            return data.get(item)

        
        