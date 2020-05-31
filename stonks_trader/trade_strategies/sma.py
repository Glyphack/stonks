from typing import List
from .strategy import TradingStrategy


class SmaStrategy(TradingStrategy):
    def analyze(self):
        self.df["buy_signal"] = (
            (
                    (self.df['sma_10'] > self.df['sma_20']) &
                    (self.df['sma_20'].shift(1) < self.df['sma_10'].shift(1))
            )
        )

    @property
    def plot_lines(self) -> List[List[str]]:
        return [["close", "sma_10", "sma_20"], ["close"]]
