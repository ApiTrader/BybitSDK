
class PositionTransforms():

    def get_position_list_item(self, data, item, item_root='result', symbol='BTCUSD'):
        
        try : 
            if item_root is not None: 
                loop_data = data[item_root]
                ind = 0 

                ind = [i for i in range(0, len(loop_data)) if loop_data[i]['symbol'] == symbol]
                ind = ind[0]

                return loop_data[ind][item]
            else :
                return data[item]

        except Exception as e:
            return str(e)

    def get_leverage_item(self, data, symbol='BTCUSD', item='leverage'):

        try:

            if symbol is None:
                return data[item] 
            else : 
                return data['result'][symbol][item]
        except Exception as e:
            return str(e)