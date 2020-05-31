from typing import List

from ta.volatility import BollingerBands
from .strategy import TradingStrategy


class CompressionStrategy(TradingStrategy):
    def analyze(self):
        bollinger_bands = BollingerBands(
            self.df.close,
        )
        self.df["bb_h2"] = bollinger_bands.bollinger_hband()
        self.df["bb_l2"] = bollinger_bands.bollinger_lband()
        self.df[f"buy_signal"] = (
                self.df.bb_h2 - self.df.bb_l2 <= 200
        )

    @property
    def _plot_lines(self) -> List[List[str]]:
        return [["close", "bb_l2", "bb_h2"]]

    @property
    def strategy_name(self):
        return "compression"
