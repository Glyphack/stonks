from typing import List

from ta.momentum import RSIIndicator

from .strategy import TradingStrategy


class RsiStrategy(TradingStrategy):
    @property
    def _plot_lines(self) -> List[List[str]]:
        return [["close"], ["rsi"]]

    @property
    def strategy_name(self):
        return "RSI"

    def analyze(self):
        self.df["rsi"] = RSIIndicator(close=self.df.close).rsi()  #
        self.df["buy_signal"] = (self.df["rsi"] < 20)
