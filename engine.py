import openai
import tiktoken
import newspaper

openai.api_key = "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"

current_model = "gpt-3.5-turbo"


#GENERATE
def generate_text_with_openai(user_prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # you can replace this with your preferred model
        messages=[{"role": "user", "content": user_prompt}],
    )
    return completion.choices[0].message.content




#COUNT
def count_tokens(text, current_model):
    encoding = tiktoken.encoding_for_model(current_model)
    num_tokens = encoding.encode(text)
    return len(num_tokens)

#num_token = count_tokens(prompt, gen_prompt.current_model)




#COST
def estimate_input_cost(model_name, token_count):
    model_costs = {
        "gpt-3.5-turbo-0613": 0.0015,
        "gpt-3.5-turbo-16k-0613": 0.003,
        "gpt-4-0613": 0.03,
        "gpt-4-32k-0613": 0.06
    }

    cost_per_1000_tokens = model_costs.get(model_name, 0.0)  # Default to 0.0 if model_name not found
    estimated_cost = (token_count / 1000) * cost_per_1000_tokens
    return estimated_cost




def get_article_from_url(url):
    try:
        article = newspaper.article(url)
        article.download()
        if article.download_state == 2:
            article.parse()
            article_text = article.text
            return article_text
        else:
            print("Error: Uable to download article from URL:", url)
            return None
    except Exception as c:
        print("An error occured while processing the URL", url)
        print(str(c))
        return None