

class OrderTransforms():

    def get_order_item(self, data, item, item_root='result', symbol='BTCUSD'):
        rtn_val = None
        try :
            if item_root is not None:
                rtn_val = data[item_root][item]
            else :
                rtn_val = data[item]
        except : 
            rtn_val = None

        return rtn_val


    def get_active_order_item(self, data, item, item_root="result", symbol='BTCUSD', index_overide=None):
        rtn_val = None

        if item_root == "result" and index_overide is None:
            try :
                loop_data = data[item_root]['data']
                ind = [i for i in range(0, len(loop_data)) if loop_data[i]['symbol'] == symbol]
                ind = ind[0]

                rtn_val = loop_data[ind][item]   
            except : 
                rtn_val = None
        elif item_root == "result" and index_overide is not None:
            rtn_val = data[item_root]['data'][index_overide][item]

        else :
            try :
                rtn_val = data[item]
            except : 
                rtn_val = None

        return rtn_val
