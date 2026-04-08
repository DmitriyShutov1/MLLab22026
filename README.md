# ML Labs - Dmitriy Shutov

# Лабораторная работа 2: NLP (оценка 3)

## Установка и запуск (Windows 11)

1. Установить WSL:
wsl --install

2. Запустить Ubuntu:
wsl.exe -d Ubuntu

3. Установить Ollama:
curl -fsSL https://ollama.com/install.sh | sh

4. Запустить Ollama сервер:
ollama serve &

5. Скачать модель (в новом терминале WSL):
ollama pull qwen2.5:0.5b

6. Создать файл скрипта в WSL:
nano inference.py
(вставить код скрипта и сохранить)

7. Проверить работу Ollama:
curl -X POST http://localhost:11434/api/generate -d '{"model": "qwen2.5:0.5b", "prompt": "Hello", "stream": false}' -H "Content-Type: application/json"

8. Запустить скрипт:
python3 inference.py
