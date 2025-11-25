from groq import Groq
from dotenv import load_dotenv

import re
import os
from typing import Generator

from config import MODEl_NAME, PROJECT_PATH

load_dotenv()

def read_file(file_path: str) -> str:
	with open(file_path, "r") as file:
		return file.read()


def ask_llm(question: str) -> str:
	client = Groq(api_key=os.environ["GROQ_KEY"])
	chat_completion = client.chat.completions.create(
		messages=[
			{
				"role": "system",
				"content": read_file(file_path=os.path.join(PROJECT_PATH, "context.txt"))
			},
			{
				"role": "user",
				"content": question,
			}
		],
		model=MODEl_NAME,
		stream=False
	)
	answer = format_llm_answer(chat_completion.choices[0].message.content)
	return answer

def format_llm_answer(answer: str) -> str:
	
	ansi_codes = [
	    "033[91m",  # RED
	    "033[92m",  # GREEN
	    "033[93m",  # YELLOW
	    "033[94m",  # BLUE
	    "033[1m",   # BOLD
	    "033[0m",   # RESET
	]

	for code in ansi_codes:
	    # Remplace \\033[...] → \033[...]
	    answer = answer.replace(f"\\\\{code}", f"\033[{code[4:]}")
	    # Remplace \\\\033[...] → \033[...]
	    answer = answer.replace(f"\\\\\\\\{code}", f"\033[{code[4:]}")
	    # Remplace \033[...] échappé une seule fois → \033[...]
	    answer = answer.replace(f"\\{code}", f"\033[{code[4:]}")

	return answer