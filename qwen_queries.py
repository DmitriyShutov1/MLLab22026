import requests
import json
import time

def query_llm(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5:0.5b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "max_tokens": 200
        }
    }
    
    response = requests.post(url, json=payload)
    return response.json()["response"]

# 10 запросов
queries = [
    "Explain the concept of 'qualia' in philosophy of mind and why it's considered a hard problem for AI.",
    "What are the ethical implications of using AI for predictive policing? Discuss at least two perspectives.",
    "How does the Chinese Room argument challenge the idea of strong AI? What are its main weaknesses?",
    "Explain the difference between Bayesian and frequentist statistics with a concrete example.",
    "What is the 'alignment problem' in AI safety? Give three potential approaches to solving it.",
    "How does quantum entanglement challenge our classical understanding of causality and locality?",
    "Explain the 'trolley problem' and its variations. Why is it relevant to autonomous vehicle ethics?",
    "What is the difference between weak and strong emergence in complex systems? Provide examples.",
    "How does the concept of 'algorithmic bias' manifest in real-world ML systems? Give specific cases.",
    "Explain the 'measurement problem' in quantum mechanics and the main interpretations that attempt to resolve it."
]

print("=" * 70)
print("LLM INFERENCE REPORT - Qwen2.5:0.5B")
print("=" * 70)
print()

results = []

for i, query in enumerate(queries, 1):
    print(f"[{i}] QUERY: {query}")
    
    try:
        response = query_llm(query)
        print(f"    RESPONSE: {response}")
        results.append({"query": query, "response": response})
    except Exception as e:
        print(f"    ERROR: {e}")
        results.append({"query": query, "response": f"ERROR: {e}"})
    
    print()
    time.sleep(0.5)

# Сохраняем в файл
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("=" * 70)
print("Отчет сохранен в файл: report.json")
print("=" * 70)

# Выводим таблицу
print("\n" + "=" * 70)
print("ИТОГОВАЯ ТАБЛИЦА")
print("=" * 70)
print(f"{'№':<3} | {'ЗАПРОС':<30} | {'ОТВЕТ'}")
print("-" * 70)
for i, r in enumerate(results, 1):
    query_short = r['query'][:28] + ".." if len(r['query']) > 30 else r['query']
    resp_short = r['response'][:50] + ".." if len(r['response']) > 50 else r['response']
    print(f"{i:<3} | {query_short:<30} | {resp_short}")
