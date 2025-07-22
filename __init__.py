from .PromptPreset.PromptPresetMultipleChoice import PromptPresetMultipleChoice
from .PromptPreset.PromptPresetOneChoice import PromptPresetOneChoice
from .TriggerWordMerger import TriggerWordMerger
from .ImageScaler import ImageScaler
from .MultiLineTextNode import MultiLineTextNode
from .TextCombinerNode import TextCombinerNode
from .TextModifier import TextModifier
from .PhotographPromptGen.PhotographPromptGenerator import PhotographPromptGenerator
from .TextSwitch import TextSwitch
from .ImgSwitch.ImageSwitch2way import ImageSwitch2way
from .ImgSwitch.ImageSwitch4way import ImageSwitch4way
from .ExtraOptions import ExtraOptions
from .PromptOptimizer import PromptOptimizer
from .SystemPrompt.SystemPromptLoader import SystemPromptLoader
from .ColorRemoval import ColorRemoval
from .BaiduTranslate.BaiduTranslateNode import BaiduTranslateNode
from .ImgSwitch.AutoImageSwitch import AutoImageSwitch
from .TextExtractor import TextExtractor
from .KontextPresets.KontextPresetsPlus.KontextPresetsPlus import KontextPresetsPlus
from .KontextPresets.KontextPresetsBasic import LoadKontextPresetsBasic
from .TranslateNodeBeta import TranslateNodeBeta


NODE_CLASS_MAPPINGS = {
    "ColorRemoval": ColorRemoval,
    "PromptPresetOneChoice": PromptPresetOneChoice,
    "PromptPresetMultipleChoice": PromptPresetMultipleChoice,
    "TriggerWordMerger": TriggerWordMerger,
    "ImageScaler": ImageScaler,
    "MultiLineTextNode": MultiLineTextNode,
    "TextCombinerNode": TextCombinerNode,
    "TextModifier": TextModifier,
    "PhotographPromptGenerator": PhotographPromptGenerator,
    "TextSwitch": TextSwitch,
    "ImageSwitch2way": ImageSwitch2way,
    "ExtraOptions": ExtraOptions,
    "ImageSwitch4way": ImageSwitch4way,
    "PromptOptimizer": PromptOptimizer,
    "SystemPromptLoader": SystemPromptLoader,
    "BaiduTranslateNode": BaiduTranslateNode,
    "AutoImageSwitch": AutoImageSwitch,
    "TextExtractor": TextExtractor,
    "KontextPresetsPlus": KontextPresetsPlus,
    "LoadKontextPresetsBasic": LoadKontextPresetsBasic,
    "TranslateNodeBeta": TranslateNodeBeta,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptPresetOneChoice": "Single Choice Prompt Preset (Commentable)",
    "PromptPresetMultipleChoice": "Multiple Choice Prompt Preset (Commentable)",
    "TriggerWordMerger": "Trigger Word Merger",
    "ImageScaler": "Image Scaler",
    "MultiLineTextNode": "Multi-line Text (Commentable)",
    "TextCombinerNode": "Prompt Combiner (Commentable)",
    "TextModifier": "Text Modifier",
    "PhotographPromptGenerator": "Photography Prompt Generator",
    "TextSwitch": "Text Switch (Commentable)",
    "ImageSwitch2way": "Image Switch - 2-way (Commentable)",
    "ImageSwitch4way": "Image Switch - 4-way (Commentable)",
    "ExtraOptions": "Extra Guidance Options (Universal)",
    "BaiduTranslateNode": "Baidu Translate",
    "PromptOptimizer": "Prompt Optimizer",
    "SystemPromptLoader": "System Prompt Loader",
    "ColorRemoval": "Color Removal",
    "AutoImageSwitch": "Auto Image Switch",
    "TextExtractor": "Chinese-English Text Extractor",
    "KontextPresetsPlus": "Kontext Presets (Enhanced)",
    "LoadKontextPresetsBasic": "Kontext Presets (Basic)",
    "TranslateNodeBeta": "Chinese-English Translator [beta]",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']