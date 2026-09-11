from template import call_openai

prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."

for temperature in [0.0, 0.5, 1.0, 1.5]:
    response, latency = call_openai(
        prompt=prompt,
        temperature=temperature
    )

    print(f"\n===== Temperature: {temperature} =====")
    print(response)