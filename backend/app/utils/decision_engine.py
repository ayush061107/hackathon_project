from app import models, schemas


class DecisionEngine:

    def __init__(
        self,
        products: list[models.Product],
        priorities: schemas.PriorityWeights
    ):
        self.products = products
        self.priorities = priorities

    def _normalize_high(self, value, maximum):
        if maximum == 0:
            return 0
        return value / maximum

    def _normalize_low(self, value, minimum):
        if value == 0:
            return 0
        return minimum / value

    def calculate_scores(self):

        if len(self.products) == 0:
            return {}

        max_rating = max(p.rating for p in self.products)
        max_ram = max(p.ram for p in self.products)
        max_storage = max(p.storage for p in self.products)
        max_battery = max(p.battery for p in self.products)

        min_price = min(p.price for p in self.products)
        min_weight = min(p.weight for p in self.products)

        scores = {}

        for product in self.products:

            score = 0

            score += (
                self._normalize_low(product.price, min_price)
                * self.priorities.price
            )

            score += (
                self._normalize_high(product.rating, max_rating)
                * self.priorities.rating
            )

            score += (
                self._normalize_high(product.ram, max_ram)
                * self.priorities.ram
            )

            score += (
                self._normalize_high(product.storage, max_storage)
                * self.priorities.storage
            )

            score += (
                self._normalize_high(product.battery, max_battery)
                * self.priorities.battery
            )

            score += (
                self._normalize_low(product.weight, min_weight)
                * self.priorities.weight
            )

            scores[product.id] = round(score, 2)

        return scores

    def get_winner(self):

        scores = self.calculate_scores()

        if not scores:
            return None

        winner_id = max(scores, key=scores.get)

        winner = next(
            product
            for product in self.products
            if product.id == winner_id
        )

        return winner

    def generate_reasons(self, winner):

        reasons = []

        reasons.append(
            f"{winner.name} achieved the highest weighted score."
        )

        if winner.rating >= 4:
            reasons.append(
                "It has an excellent user rating."
            )

        if winner.battery >= 5000:
            reasons.append(
                "Battery backup is strong."
            )

        if winner.ram >= 8:
            reasons.append(
                "RAM is suitable for multitasking."
            )

        if winner.storage >= 256:
            reasons.append(
                "Storage capacity is sufficient."
            )

        return reasons

    def get_result(self):
        scores = self.calculate_scores()
        winner = self.get_winner()
        reasons = self.generate_reasons(winner)
        return {
            "winner": winner,
            "scores": scores,
            "reasons": reasons
        }