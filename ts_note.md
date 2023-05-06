./main2 -m ./vicuna-13B-1.1-GPTQ-4bit-128g.GGML.bin -c 512 -b 1024 -n 256 --keep 48 --repeat_penalty 1.0 --color -i -r "User:" -f ./chat.txt


../llama.cpp/models/main -m ../llama.cpp/models/gpt4all-lora-quantized-ggml.bin -c 512 -b 1024 -n 256 --keep 48 --repeat_penalty 1.0 --color -i -r "User:" -f ../llama.cpp/models/chat.txt


npm start ../llama.cpp/models/main -m ../llama.cpp/models/gpt4all-lora-quantized-ggml.bin -c 512 -b 1024 -n 256 keep 48 repeat_penalty 1.0 --color -i -r "User:" -f ../llama.cpp/models/chat.txt
