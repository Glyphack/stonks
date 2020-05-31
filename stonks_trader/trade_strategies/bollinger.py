from typing import List

from ta.volatility import BollingerBands
from .strategy import TradingStrategy
from stonks_trader.helpers.indicator_utils import is_crossover


class BollingerBandsStrategy(TradingStrategy):
    def analyze(self):
        bollinger_bands = BollingerBands(
            self.df.close,
        )
        self.df["bb_h2"] = bollinger_bands.bollinger_hband()
        self.df["bb_l2"] = bollinger_bands.bollinger_lband()
        bollinger_bands2 = BollingerBands(
            self.df.close,
            ndev=1
        )
        self.df["bb_h1"] = bollinger_bands2.bollinger_hband()
        self.df["bb_l1"] = bollinger_bands2.bollinger_lband()
        self.df[f"buy_signal"] = (
            is_crossover(self.df.close, self.df.bb_h1)
        )
        self.df[f"sell_signal"] = (
            is_crossover(self.df.bb_l1, self.df.close)
        )

    @property
    def _plot_lines(self) -> List[List[str]]:
        return [["close", "bb_h1", "bb_l1", "bb_l2", "bb_h2"]]

    @property
    def strategy_name(self):
        return "trend_bollinger"
