# === Stage 26: Аномальные значения ===
# Project: BookSwap
import statistics


class StatisticalAnomalyDetector:
    """Detects anomalous numeric values in a book collection using simple statistics."""

    def __init__(self, values):
        self.values = list(values)

    def detect(self, threshold_multiplier=3.0):
        anomalies = []
        if len(self.values) < 3:
            return anomalies
        mean = statistics.mean(self.values)
        std_dev = statistics.pstdev(self.values)
        if std_dev == 0:
            return anomalies
        lower = mean - threshold_multiplier * std_dev
        upper = mean + threshold_multiplier * std_dev
        for index, value in enumerate(self.values):
            if value < lower or value > upper:
                anomalies.append(index)
        return anomalies


def find_outlier_pages(books, numeric_field):
    field_values = [book[numeric_field] for book in books]
    detector = StatisticalAnomalyDetector(field_values)
    return detector.detect()
