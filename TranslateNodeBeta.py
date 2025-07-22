import requests
import time
import json

class TranslateNodeBeta:

    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True, 
                    "default": "", 
                    "placeholder": "Please enter text to translate..."
                }),
                "source_language": (["Auto Detect", "Chinese", "English", "Russian"], {
                    "default": "Auto Detect"
                }),
                "target_language": (["Chinese", "English", "Russian", "Chat/Общение"], {
                    "default": "English"
                }),
                "model": (["openai", "mistral", "qwen-coder", "llama"], {
                    "default": "openai"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translation_result",)
    FUNCTION = "translate_text"
    CATEGORY = "utils"
    
    def detect_language(self, text):
        chinese_chars = sum(1 for char in text if '\u4e00' <= char <= '\u9fff')
        russian_chars = sum(1 for char in text if '\u0400' <= char <= '\u04ff')
        total_chars = len(text.strip())
        
        if total_chars == 0:
            return "unknown"
        
        chinese_ratio = chinese_chars / total_chars
        russian_ratio = russian_chars / total_chars
        
        if chinese_ratio > 0.3:
            return "chinese"
        elif russian_ratio > 0.3:
            return "russian"
        else:
            return "english"
    
    def build_translate_prompt(self, text, source_language, target_language):
        if source_language == "Auto Detect":
            detected_lang = self.detect_language(text)
            if detected_lang == "chinese":
                actual_source = "Chinese"
            elif detected_lang == "russian":
                actual_source = "Russian"
            else:
                actual_source = "English"
        else:
            actual_source = source_language
        
        if actual_source == "Chinese" and target_language == "English":
            prompt = f"""Please translate the following Chinese text to English, requirements:
1. Accurate, natural, and fluent translation
2. Maintain the tone and style of the original text
3. Use accurate English expressions for technical terms
4. Only output the translation result, do not add any explanations

Chinese text to translate:
{text}"""
        elif actual_source == "English" and target_language == "Chinese":
            prompt = f"""Please translate the following English text to Chinese, requirements:
1. Accurate, natural, and fluent translation
2. Maintain the tone and style of the original text
3. Use language that conforms to Chinese expression habits
4. Only output the translation result, do not add any explanations

English text to translate:
{text}"""
        elif actual_source == "Russian" and target_language == "English":
            prompt = f"""Please translate the following Russian text to English, requirements:
1. Accurate, natural, and fluent translation
2. Maintain the tone and style of the original text
3. Use accurate English expressions for technical terms
4. Only output the translation result, do not add any explanations

Russian text to translate:
{text}"""
        elif actual_source == "English" and target_language == "Russian":
            prompt = f"""Please translate the following English text to Russian, requirements:
1. Accurate, natural, and fluent translation
2. Maintain the tone and style of the original text
3. Use language that conforms to Russian expression habits
4. Only output the translation result, do not add any explanations

English text to translate:
{text}"""
        elif target_language == "Chat/Общение":
            if actual_source == "Russian":
                prompt = f"""Ответь на русском языке на следующий текст или вопрос. Будь полезным и дружелюбным:

{text}"""
            elif actual_source == "Chinese":
                prompt = f"""请用中文回答以下文本或问题。请友好和有帮助：

{text}"""
            else:
                prompt = f"""Please respond to the following text or question in English. Be helpful and friendly:

{text}"""
        else:
            prompt = f"""Please translate the following {actual_source} text to {target_language}, requirements:
1. Accurate, natural, and fluent translation
2. Maintain the tone and style of the original text
3. Only output the translation result, do not add any explanations

Text to translate:
{text}"""
        
        return prompt
    
    def _handle_error(self, error_type, error_msg, model):
        print(f"❌ {error_msg} | Model: {model}")
        return f"[{error_type}] {error_msg}"
    
    def call_translate_api(self, prompt, model="openai"):
        try:
            api_url = "https://text.pollinations.ai/"
            print(f"🌐 Translation API call | Model: {model}")
            
            payload = {
                "messages": [{"role": "user", "content": prompt}],
                "model": model,
                "timestamp": int(time.time())
            }
            
            response = requests.post(
                api_url, 
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=45
            )
            
            if response.status_code == 200:
                result = response.text.strip()
                print(f"✅ Translation successful | Model: {model}")
                return result
            else:
                error_messages = {
                    400: "Request parameter error", 401: "API authentication failed", 403: "Access denied",
                    404: "API endpoint not found", 429: "Too many requests", 500: "Internal server error",
                    502: "Gateway error", 503: "Service unavailable", 504: "Gateway timeout"
                }
                error_msg = error_messages.get(response.status_code, f"HTTP error: {response.status_code}")
                return self._handle_error("API Error", error_msg, model)
                
        except requests.exceptions.Timeout:
            return self._handle_error("Timeout Error", "Request timeout", model)
        except requests.exceptions.ConnectionError:
            return self._handle_error("Connection Error", "Network connection failed", model)
        except requests.exceptions.RequestException as e:
            return self._handle_error("Network Error", f"Request exception: {str(e)}", model)
        except json.JSONDecodeError:
            return self._handle_error("Format Error", "Response data format error", model)
        except Exception as e:
            return self._handle_error("System Error", f"Unknown exception: {str(e)}", model)
    
    def translate_text(self, text, source_language, target_language, model):
        if not text.strip():
            return ("Please enter text to translate",)
        
        prompt = self.build_translate_prompt(text, source_language, target_language)
        
        translated_text = self.call_translate_api(prompt, model)
        
        return (translated_text,)