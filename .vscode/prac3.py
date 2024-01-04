text="Using AI"
openai_results="Openai"
msg="What is the reason behind the current global recession"
with open(f"Myprojects/openai/{msg[0:30]}.txt",'w') as f:
    f.write(text+openai_results)