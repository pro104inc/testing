import engine
import llm
from prompts import Ideas



current_model = "gpt-3.5-turbo"

input_text = "ai trading bot"

prompt = Ideas.domain_brand_names.format(Niche=input_text)




#GENERATE


open_ai_response = llm.llm_generate_text_with_save(prompt, "OpenAI", current_model)
print(open_ai_response)



#COUNT
num_tokens = engine.count_tokens(prompt,current_model)

#print(f"token count {num_tokens}")




#COST
token_count = 1000
costs = engine.estimate_input_cost(current_model, token_count)

#print(f"Cost: {costs}")





