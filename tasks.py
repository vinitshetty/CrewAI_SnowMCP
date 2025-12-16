from crewai import Task
from agents import support_agent


def create_support_task(product_name, user_prompt):
    """Create a support analysis task for a specific product with custom analysis."""
    return Task(
        description=(
            f"Analyze customer support cases for the product: {product_name}\n\n"
            f"User Request: {user_prompt}\n\n"
            "Search through the support tickets file and provide the requested analysis."
        ),
        expected_output=(
            f"Provide analysis based on the user's request:\n{user_prompt}"
        ),
        agent=support_agent,
    )
