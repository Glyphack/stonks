from typing import List

from ta.trend import MACD

from .strategy import TradingStrategy
from ..helpers.indicator_utils import is_crossover


class MACDStrategy(TradingStrategy):
    @property
    def _plot_lines(self) -> List[List[str]]:
        return [["macd", "signal"]]

    @property
    def strategy_name(self):
        return "macd"

    def analyze(self):
        macd = MACD(self.df.close, n_fast=12, n_slow=26, n_sign=9)
        self.df["macd"] = macd.macd()
        self.df["signal"] = macd.macd_signal()
        self.df["buy_signal_macd"] = (
            is_crossover(self.df['macd'], self.df['signal'])
        )
        self.df["sell_signal_macd"] = (
            is_crossover(self.df['signal'], self.df['macd'])
        )
        self.df["buy_signal"] = (
            self.df["buy_signal_macd"]
        )
