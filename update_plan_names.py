import pandas as pd
import numpy as np

def update_plan_names():
    """
    Update plan names in filtered_plan2.csv to use realistic insurance plan names
    """
    try:
        # Load the current filtered plan data
        df = pd.read_csv("filtered_plan2.csv")
        
        # Create realistic insurance plan names based on metal levels and plan types
        plan_names = []
        
        # Insurance company names
        companies = [
            "Blue Cross", "Aetna", "Cigna", "UnitedHealth", "Kaiser", "Humana", 
            "Anthem", "Molina", "Centene", "WellCare", "Ambetter", "Oscar",
            "Bright Health", "Friday Health", "Sidecar Health", "Clover Health"
        ]
        
        # Plan name suffixes
        suffixes = [
            "Select", "Premier", "Advantage", "Complete", "Essential", "Basic",
            "Standard", "Premium", "Plus", "Choice", "Flex", "Smart", "Value",
            "Care", "Health", "Wellness", "Secure", "Protect", "Guard"
        ]
        
        # Metal level specific names
        metal_names = {
            "Bronze": ["Bronze", "Basic", "Essential", "Value"],
            "Silver": ["Silver", "Standard", "Select", "Advantage"],
            "Gold": ["Gold", "Premier", "Complete", "Plus"],
            "Platinum": ["Platinum", "Premium", "Elite", "Ultimate"]
        }
        
        for idx, row in df.iterrows():
            metal_level = row.get('MetalLevel', 'Silver')
            plan_type = row.get('PlanType', 'PPO')
            
            # Select company
            company = np.random.choice(companies)
            
            # Select metal-specific name
            metal_name = np.random.choice(metal_names.get(metal_level, metal_names["Silver"]))
            
            # Select suffix
            suffix = np.random.choice(suffixes)
            
            # Create plan name
            plan_name = f"{company} {metal_name} {suffix}"
            
            # Add plan type if it's not PPO (most common)
            if plan_type != 'PPO':
                plan_name += f" {plan_type}"
            
            plan_names.append(plan_name)
        
        # Update the dataframe
        df['PlanMarketingName'] = plan_names
        
        # Save the updated data
        df.to_csv("filtered_plan2.csv", index=False)
        
        print(f"✅ Successfully updated {len(plan_names)} plan names")
        print("Sample plan names:")
        for i in range(min(10, len(plan_names))):
            print(f"  {i+1}. {plan_names[i]}")
            
        return True
        
    except Exception as e:
        print(f"❌ Error updating plan names: {e}")
        return False

if __name__ == "__main__":
    update_plan_names() 