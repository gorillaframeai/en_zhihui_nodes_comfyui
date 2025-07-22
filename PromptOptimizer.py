import requests

class PromptOptimizer:
    def __init__(self):
        self.expansion_mode = ""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_prompt": ("STRING", {"multiline": True, "default": ""}), 
                "node_switch": ("BOOLEAN", {"default": True}),
                "expansion_mode": (["Standard (Chinese)", "Standard (English)", "Detailed (Chinese)", "Detailed (English)", "Custom"], {"default": "Standard (Chinese)"}),
                "model_selection": (["gemini", "openai", "deepseek", "mistral", "qwen-coder", "llama", "sur", "unity", "searchgpt", "evil",], {"default": "openai"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 9999999999})
            },
            "optional": {
                "custom_rules": ("STRING", {"multiline": True, "default": ""})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("optimization_output",)
    FUNCTION = "optimize_prompt"
    CATEGORY = "zhihui/generator"

    def optimize_prompt(self, user_prompt, seed, expansion_mode, node_switch, model_selection, custom_rules=""):  
        if not node_switch:
            return ("") 

        if not user_prompt or not user_prompt.strip():
            raise ValueError("Error: User prompt cannot be empty, please enter content and try again.")
        
        api_system_prompt = ""
        if expansion_mode == "Standard (Chinese)":
            api_system_prompt = "Please expand the basic prompt I provide into a short prompt for text-to-image generation, providing Chinese text without titles and excessive explanations."
        elif expansion_mode == "Detailed (Chinese)":
            api_system_prompt = "Please expand the basic prompt I provide into an extremely detailed prompt for text-to-image generation, adding more rich details of various kinds, providing Chinese text without titles."
        elif expansion_mode == "Standard (English)":
            api_system_prompt = "Please expand the basic prompt I provide into a short prompt for text-to-image generation, providing English text without titles and excessive explanations."
        elif expansion_mode == "Detailed (English)":
            api_system_prompt = "Please expand the basic prompt I provide into an extremely detailed prompt for text-to-image generation, adding more rich details of various kinds, providing English text without titles."

        elif expansion_mode == "Custom":
            if not custom_rules or not custom_rules.strip():
                raise ValueError("Error: Custom mode must have input content, please enter custom expansion rules and try again.")
            api_system_prompt = custom_rules

        url = "https://text.pollinations.ai/"
        payload = {
            "messages": [
                {"role": "system", "content": api_system_prompt},
                {"role": "user", "content": "Prompt: " + user_prompt}
            ],
            "seed": seed,
            "model": model_selection,
        }
        headers = {
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            optimized_prompt = response.text
        except requests.exceptions.RequestException as e:
            optimized_prompt = "Server request failed, please try again later"
            print(f"Request error occurred: {type(e).__name__}")

        import re
        if expansion_mode != "Custom":
            optimized_prompt = optimized_prompt
            
        return (optimized_prompt,)