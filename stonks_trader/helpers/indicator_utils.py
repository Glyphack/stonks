def is_crossover(series1, series2):
    return (
            (series1 > series2) &
            (series1.shift(1) < series2.shift(1))
    )
