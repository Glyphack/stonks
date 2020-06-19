from stonks_trader.trade_strategies.bollinger import BollingerBandsStrategy
from stonks_trader.trade_strategies.compression import CompressionStrategy
from stonks_trader.trade_strategies.macd import MACDStrategy
from stonks_trader.trade_strategies.rsi import RsiStrategy
from stonks_trader.trade_strategies.sma import SmaStrategy
from stonks_trader.trade_strategies.stochastic import StochasticStrategy

trade_strategies = {
    "bollinger": BollingerBandsStrategy,
    "compression": CompressionStrategy,
    "macd": MACDStrategy,
    "rsi": RsiStrategy,
    "sma": SmaStrategy,
    "stochastic": StochasticStrategy
}
