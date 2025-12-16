from crewai import Crew
from agents import support_agent
from tasks import create_support_task


def run_analysis(product_name, user_prompt):
    """Execute the customer support analysis crew for a specific product with custom prompt."""
    
    # Create task with product name and user prompt
    support_task = create_support_task(product_name, user_prompt)
    
    # Create crew
    crew = Crew(
        agents=[support_agent],
        tasks=[support_task],
        verbose=True,
    )
    
    return crew.kickoff()
