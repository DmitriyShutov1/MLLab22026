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

queries = [
    "Что такое принципы SOLID в программировании?",
    "What is OOP? Explain main concepts like inheritance, encapsulation, polymorphism.",
    "Какой язык программирования чаще всего используется для машинного обучения и почему?",
    "What is the difference between supervised and unsupervised learning?",
    "Что такое DDD (Domain-Driven Design) простыми словами?",
    "Explain what is Git and why it is important for developers.",
    "Что такое переобучение (overfitting) в ML и как с ним бороться?",
    "What is the difference between Python list and tuple?",
    "Что такое REST API? Как он работает?",
    "Explain what is Docker and why it is used."
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
