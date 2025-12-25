import pandas as pd
import numpy as np
from scipy.stats import beta
import os

# --- 1. CONFIGURATION & PRIORS (The "Ground Truth") ---
np.random.seed(42)  # Ensures your portfolio results are consistent every time
N_PATIENTS = 2000
MONTHS = 12

# Economic Assumptions (2025 Market Rates)
COST_HIGH_DOSE = 1200  # List Price (Standard Care)
COST_LOW_DOSE = 800    # List Price (Precision Maintenance)
COST_APP = 45          # Digital Support PMPM
REBATE_CLIFF_MONTH = 6 # Rebates only kick in after Month 6
REBATE_RATE = 0.40     # 40% Rebate after cliff

def run_simulation():
    print(f"--- Starting GLP-1 Precision Simulation (N={N_PATIENTS}) ---")
    
    # Initialize Patient IDs and assign 50/50 split to strategies
    ids = np.arange(N_PATIENTS)
    strategies = np.random.choice(['Standard Care', 'Precision Maintenance'], size=N_PATIENTS)
    
    # --- 2. GENERATE PATIENT ATTRIBUTES ---
    # Engagement Score: Beta Distribution (Most people try moderately hard)
    engagement = np.random.beta(5, 2, size=N_PATIENTS)
    
    # Biology Resistance: 20% of people are "Non-Responders"
    # This adds intellectual honesty: The app works, but genetics still matter.
    resistance = np.random.choice([0, 1], size=N_PATIENTS, p=[0.8, 0.2]) 
    
    # --- 3. SURVIVAL LOGIC (The Titration Cliff) ---
    # Global retention is ~63% (Prime Therapeutics 2025). 
    # We roll the dice to see who churns.
    retention_prob = 0.63
    is_churned = np.random.rand(N_PATIENTS) > retention_prob
    
    # If they churn, WHEN do they churn? 
    # Use Beta(2,5) to skew dropouts heavily towards Months 2-3 (Side effects).
    churn_months = beta.rvs(2, 5, size=N_PATIENTS) * 12
    churn_months = np.maximum(churn_months, 1.0) # Minimum 1 month
    
    # Set final duration: Churners get dropout time; Survivors get 12 months.
    duration = np.where(is_churned, churn_months, 12.0)
    
    # --- 4. EFFICACY LOGIC (Weight Loss %) ---
    # Standard Care: Simple Bell Curve (Mean 7.7%, SD 3.0%)
    wl_std = np.random.normal(7.7, 3.0, size=N_PATIENTS)
    
    # Precision Maintenance: Dependent on Engagement & Biology
    # Formula: (Base + Slope * Engagement) * (Resistance Factor)
    # This models that "High Engagement" = "High Weight Loss"
    wl_prec_raw = (5.0 + (13.0 * engagement)) 
    
    # If Resistant (1), efficacy drops by 50%. Add some random noise.
    wl_prec = wl_prec_raw * (1 - (resistance * 0.5)) + np.random.normal(0, 1.5, size=N_PATIENTS)
    
    # Assign the correct WL based on their strategy
    final_wl = np.where(strategies == 'Standard Care', wl_std, wl_prec)
    final_wl = np.clip(final_wl, 0, 25) # Cap at 0% and 25%

    # --- 5. FINANCIAL LOGIC (The P&L) ---
    net_costs = []
    
    for i in range(N_PATIENTS):
        months_active = int(np.ceil(duration[i]))
        strat = strategies[i]
        
        # Determine Monthly Unit Cost
        drug_cost = COST_HIGH_DOSE if strat == 'Standard Care' else COST_LOW_DOSE
        app_cost = COST_APP if strat == 'Precision Maintenance' else 0
        
        total_patient_spend = 0
        
        for m in range(1, months_active + 1):
            # The Rebate Cliff: Full price until Month 6
            current_drug_cost = drug_cost
            if m > REBATE_CLIFF_MONTH:
                current_drug_cost = drug_cost * (1 - REBATE_RATE)
            
            total_patient_spend += (current_drug_cost + app_cost)
            
        net_costs.append(total_patient_spend)

    # --- 6. EXPORT ---
    df = pd.DataFrame({
        'Patient_ID': ids,
        'Strategy': strategies,
        'Engagement_Score': engagement,
        'Biology_Resistance': resistance,
        'Duration_Months': duration,
        'Churned': is_churned,
        'Weight_Loss_Pct': final_wl,
        'Net_Payer_Cost': net_costs
    })
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    output_path = 'data/glp1_simulation_results.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✓ Success! Generated {N_PATIENTS} patient journeys.")
    print(f"✓ Data saved to: {output_path}")
    
    # Quick sanity check for the user
    print("\n--- Quick Validation ---")
    print(df.groupby('Strategy')[['Weight_Loss_Pct', 'Net_Payer_Cost']].mean())

if __name__ == "__main__":
    run_simulation()