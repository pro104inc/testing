import openai

# Define your OpenAI API key
api_key = "[YOUR_API_KEY]"

# Define the cryptocurrency project details
project_name = "Crypto Project Full Name"
token_name = "Token Name"

# Define the questions for the analysis
questions = [
    "Project Overview: Provide a brief summary of the project and its goals for {}.".format(project_name),
    "Project Overview: What problem does the project aim to solve?",
    "Project Overview: Who are the key team members, and what is their experience in the industry for {}?".format(project_name),
    "Project Overview: What partnerships, collaborations, or endorsements does the project have?",
    "Technology: Describe the technology behind {}.".format(project_name),
    "Technology: How is the technology different from other similar projects in the market?",
    "Technology: What is the potential impact of the technology on the industry?",
    "Market Potential: Who is the target audience of {}?".format(project_name),
    "Market Potential: How large is the market opportunity, and what is the projected growth rate?",
    "Market Potential: Are there any regulatory, legal, or competitive barriers to entry?",
    "Tokenomics: What is the token's utility, and how is it used within {}?".format(project_name),
    "Tokenomics: How is the token supply structured, and what is the maximum supply cap?",
    "Tokenomics: What is the token distribution, and what percentage of tokens are held by the team, investors, or the community?",
    "Investment Considerations: What are the risks associated with investing in {}?".format(project_name),
    "Investment Considerations: What is the team's roadmap and timeline for achieving their goals?",
    "Investment Considerations: How does {}'s valuation compare to other similar projects in the market?",
    "Based on the above analysis, what is your overall assessment of {}'s trustworthiness and potential?".format(project_name)
]

# Create a function to analyze the project
def analyze_project():
    results = []
    for question in questions:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=150,
            api_key=api_key
        )
        results.append(response.choices[0].text)

    return results

# Call the function to analyze the project
analysis_results = analyze_project()

# Print the analysis results
for i, question in enumerate(questions):
    print(f"{question}\n{analysis_results[i]}\n")

# Save the analysis results to a file
with open("crypto_project_analysis.txt", "w") as file:
    for i, question in enumerate(questions):
        file.write(f"{question}\n{analysis_results[i]}\n\n")
