from typing import List

from ta.momentum import StochasticOscillator

from .strategy import TradingStrategy


class StochasticStrategy(TradingStrategy):
    def analyze(self):
        stochastic_df = StochasticOscillator(
            self.df.high,
            self.df.low,
            self.df.close,
            n=5
        )
        self.df["stoch_k"] = stochastic_df.stoch()
        self.df["stoch_d"] = stochastic_df.stoch_signal()
        self.df["high_close"] = ((self.df.high - self.df.close) / (
                self.df.high + self.df.close / 2) * 100)
        self.df["buy_signal"] = (
                (
                        (self.df['stoch_k'] > self.df['stoch_d']) &
                        (self.df['stoch_k'].shift(1) < self.df[
                            'stoch_d'].shift(1))
                ) &
                (self.df['stoch_d'] < 26)
        )
        self.df["stoch_buy_signal_early"] = (
                (self.df['stoch_k'] < self.df['stoch_d']) &
                ((self.df["stoch_d"]) - self.df["stoch_k"] < 3) &
                (self.df['stoch_d'] < 26)
        )

    @property
    def _plot_lines(self) -> List[List[str]]:
        return [["close"], ["stoch_d", "stoch_k"]]

    @property
    def strategy_name(self):
        return "stochastic oscillator"
