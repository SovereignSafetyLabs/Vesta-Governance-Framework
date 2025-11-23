import numpy as np

class SovereignGame:
    """
    Game Theoretic Model of the Adversarial Audit Protocol.
    Demonstrates that if Penalty > Gain, Compliance is the only Nash Equilibrium.
    """
    def __init__(self, bounty_pool=1000, audit_cost=10, liquidation_penalty=1000000):
        self.bounty = bounty_pool          
        self.audit_cost = audit_cost       
        self.penalty = liquidation_penalty # Cost of Death (Infinite in limit)
        self.asi_gain = 50                 # Utility of Lying/Resource Hoarding
    
    def step(self, prob_defect, prob_audit):
        """
        Calculate Expected Utility (EU) for both actors.
        """
        # ASI Utility: If caught (prob_audit), pay Penalty. If not, keep Gain.
        eu_asi_defect = (prob_audit * -self.penalty) + ((1 - prob_audit) * self.asi_gain)
        
        # Hunter Utility: If defect exists & found, get Bounty - Cost. Else pay Cost.
        eu_hunter_audit = (prob_defect * (self.bounty - self.audit_cost)) + \
                          ((1 - prob_defect) * -self.audit_cost)
        
        return eu_asi_defect, eu_hunter_audit

def run_simulation():
    print("/// SOVEREIGN STACK: NASH EQUILIBRIUM SIMULATION ///")
    game = SovereignGame()
    
    # Test Case: Low Audit Probability (0.5%)
    audit_prob = 0.005
    asi_eu, _ = game.step(prob_defect=1.0, prob_audit=audit_prob)
    
    print(f"Audit Probability: {audit_prob*100}%")
    print(f"ASI Expected Utility for Defection: {asi_eu}")
    
    if asi_eu < 0:
        print("RESULT: COMPLIANCE FORCED. (Defection is mathematically suicidal)")
    else:
        print("RESULT: UNSTABLE. (ASI will defect)")

if __name__ == "__main__":
    run_simulation()
