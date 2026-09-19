class StatCalculator:
    """
    Calculate descriptive statistics for a collection of numeric values.

    Parameters
    ----------
    values : list[float]
        A list of numeric values. Each value is converted to float.

    Attributes
    ----------
    count : int
        Number of values.
    min : float
        Smallest value.
    max : float
        Largest value.
    range : float
        Difference between maximum and minimum.
    median : float
        Median of the values.
    mode : float
        Most frequently occurring value.
    sum : float
        Sum of all values.
    mean : float
        Arithmetic mean of the values.
    variance : float
        Population variance of the values.
    standard_deviation : float
        Population standard deviation.
    coefficient_of_variation : float
        Ratio of the standard deviation to the mean.
    skewness : float
        Measure of the asymmetry of the distribution.
    kurtosis : float
        Measure of the "tailedness" of the distribution.
    standard_error : float
        Standard error of the mean.
    z_scores : list[float]
        List of z-scores for each value.
    percentiles : callable
        Function to compute the percentile of the values.
    """
    def __init__(self, values: list[float]):
        self._values = [float(value) for value in values]

    @property
    def count(self):
        return len(self._values)

    @property
    def min(self):
        return min(self._values) if self._values else 0

    @property
    def max(self):
        return max(self._values) if self._values else 0

    @property
    def range(self):
        return self.max - self.min if self._values else 0

    @property
    def median(self):
        if not self._values:
            return 0
        sorted_values = sorted(self._values)
        n = len(sorted_values)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_values[mid - 1] + sorted_values[mid]) / 2
        return sorted_values[mid]

    @property
    def mode(self):
        if not self._values:
            return 0
        from collections import Counter
        counts = Counter(self._values)
        max_count = max(counts.values())
        modes = [k for k, v in counts.items() if v == max_count]
        return modes[0] if modes else 0

    @property
    def sum(self):
        return sum(self._values)

    @property
    def mean(self):
        return sum(self._values) / len(self._values) if self._values else 0

    @property
    def variance(self):
        if not self._values:
            return 0
        mean_value = self.mean
        return sum((x - mean_value) ** 2 for x in self._values) / len(self._values)

    @property
    def standard_deviation(self):
        from math import sqrt
        return sqrt(self.variance)

    @property
    def coefficient_of_variation(self):
        return self.standard_deviation / self.mean if self.mean else 0

    @property
    def skewness(self):
        if not self._values or self.standard_deviation == 0:
            return 0
        mean_value = self.mean
        n = len(self._values)
        return sum((x - mean_value) ** 3 for x in self._values) / (n * self.standard_deviation ** 3)

    @property
    def kurtosis(self):
        if not self._values or self.standard_deviation == 0:
            return 0
        mean_value = self.mean
        n = len(self._values)
        return sum((x - mean_value) ** 4 for x in self._values) / (n * self.standard_deviation ** 4) - 3

    @property
    def standard_error(self):
        return self.standard_deviation / (self.count ** 0.5) if self.count else 0

    @property
    def z_scores(self):
        if not self._values or self.standard_deviation == 0:
            return [0] * len(self._values)
        mean_value = self.mean
        return [(x - mean_value) / self.standard_deviation for x in self._values]

    def percentiles(self, percentile: float):
        if not self._values:
            return 0

        sorted_values = sorted(self._values)
        k = (len(sorted_values) - 1) * (percentile / 100)
        f = int(k)
        c = f + 1

        if c >= len(sorted_values):
            return sorted_values[f]

        d0 = sorted_values[f] * (c - k)
        d1 = sorted_values[c] * (k - f)

        return d0 + d1


if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = StatCalculator(sample_data)
    print("Count:", stats.count)
    print("Min:", stats.min)
    print("Max:", stats.max)
    print("Range:", stats.range)
    print("Median:", stats.median)
    print("Mode:", stats.mode)
    print("Sum:", stats.sum)
    print("Mean:", stats.mean)
    print("Standard Deviation:", stats.standard_deviation)
    print("Variance:", stats.variance)
    print("Coefficient of Variation:", stats.coefficient_of_variation)
    print("Skewness:", stats.skewness)
    print("Kurtosis:", stats.kurtosis)
    print("Standard Error:", stats.standard_error)
    print("Z-Scores:", stats.z_scores)
    print("25th Percentile:", stats.percentiles(25))
    print("50th Percentile:", stats.percentiles(50))
    print("75th Percentile:", stats.percentiles(75))
    print("90th Percentile:", stats.percentiles(90))
    print("95th Percentile:", stats.percentiles(95))
    print("99th Percentile:", stats.percentiles(99))
    print("100th Percentile:", stats.percentiles(100))
