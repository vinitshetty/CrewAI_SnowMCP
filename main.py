from crew import run_analysis


def main():
    """Main entry point for the Customer Support Analysis Crew."""
    
    # Product name to analyze
    product_name = 'jackets'
    
    # User's custom analysis prompt
    user_prompt = 'Only summarize total number of cases and summarize issues and resolutions'

    print("\n" + "="*60)
    print(f"Customer Support Analysis: {product_name}")
    print(f"Request: {user_prompt}")
    print("="*60 + "\n")
    
    result = run_analysis(product_name, user_prompt)
    
    print("\n" + "="*60)
    print("Analysis Complete")
    print("="*60)
    print(result)


if __name__ == "__main__":
    main()
