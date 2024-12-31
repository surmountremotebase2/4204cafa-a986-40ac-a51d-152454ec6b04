#Type code here
from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.technical_indicators import RSI, EMA, SMA, MACD, MFI, BB

class TradingStrategy(Strategy):

    @property
    def assets(self):
        return ["SPY"]

    @property
    def interval(self):
        return "1hour"

    def run(self, data_functions):
        data = data_functions["ohlcv"]

        spy_50_ma = SMA("SPY", data, 50)
        spy_200_ma = SMA("SPY", data, 200)

        if None in [spy_50_ma, spy_200_ma]:
            return None

        spy_stake = 0
        if spy_50_ma[-2] < spy_200_ma[-2] and spy_50_ma[-1] >= spy_200_ma[-1]:
            spy_stake = 1 

        return TargetAllocation({"SPY": spy_stake})