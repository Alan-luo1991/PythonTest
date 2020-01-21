import json
import token

from ws4py.client.threadedclient import WebSocketClient


class CG_Client(WebSocketClient):

    def opened(self):
        req = '{"token":"918e482c2d8524867615f735b8abc4f840675638d140898f8631ab63a2ca2e22", "length": "1"}'
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        data = resp['data']
        if type(data) is dict:
            ask = data['asks'][0]
            print('Ask:', ask)
            bid = data['bids'][0]
            print('Bid:', bid)


if __name__ == '__main__':
    ws = None
    try:
        ws = CG_Client('wss://test-game.bblgmm.com/connector11')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()