from ..utils.logger import get_logger

class RecommendationEngine:
    def __init__(self):
        self.logger = get_logger("RecommendationEngine")
        self.diet_plans = {
            "anemia": ["Spinach", "Lentils", "Beetroot"],
            "pregnancy": ["Millets", "Green vegetables", "Dairy"]
        }
        self.logger.info("RecommendationEngine initialized")

    def get_diet_recommendation(self, risks):
        self.logger.debug(f"Generating recommendations for risks: {risks}")
        recommendations = []
        for risk in risks:
            if risk in self.diet_plans:
                recommendations.extend(self.diet_plans[risk])
        self.logger.debug(f"Recommendations: {recommendations}")
        return recommendations 
