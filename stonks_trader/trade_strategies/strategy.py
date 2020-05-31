import abc
from typing import List

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')


class TradingStrategy(metaclass=abc.ABCMeta):
    def __init__(self, df: pd.DataFrame, config=None):
        self.df: pd.DataFrame = df.copy()
        self.config = config or None

    @abc.abstractmethod
    def analyze(self):
        pass

    def plot(self, name: str = "", n: int = 60):
        count_of_subplots = len(self._plot_lines)
        fig, axes = plt.subplots(nrows=count_of_subplots)
        if count_of_subplots > 1:
            plt.grid()
            for i, lines in enumerate(self._plot_lines):
                self.df.tail(n).plot(
                    ax=axes[i], y=lines, x="date", title=name
                )
                plt.show()
        else:
            self.df.tail(n).plot(
                y=self._plot_lines[0], x="date", title=name
            )
            plt.show()

    def is_buy_signal(self, day: int = -1):
        return self.df["buy_signal"].iat[day]

    def is_sell_signal(self, day: int = -1):
        return self.df["sell_signal"].iat[day]

    def dump(self, n, path):
        self.df.tail(n).to_csv(path)

    @property
    @abc.abstractmethod
    def _plot_lines(self) -> List[List[str]]:
        pass

    @property
    @abc.abstractmethod
    def strategy_name(self):
        pass
