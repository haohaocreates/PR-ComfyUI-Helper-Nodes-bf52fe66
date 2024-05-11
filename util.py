from .base import GLOBAL_CATEGORY, BaseNode

import comfy
import comfy.samplers

MODULE_CATEGORY = f"{GLOBAL_CATEGORY}/util"


class HelperNodes_WidthHeight(BaseNode):
    """
    Simple integer values node that allows definition of the
    image height and width for passing into empty latents
    as Integers.

    Permits custom values between 8 and 4096, in steps of 8.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {
                    "default": 1024,
                    "min": 8,
                    "max": 4096,
                    "step": 8,
                    "display": "number"
                }),
                "height": ("INT", {
                    "default": 1024,
                    "min": 8,
                    "max": 4096,
                    "step": 8,
                    "display": "number"
                }),
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("width", "height")

    CATEGORY = f"{MODULE_CATEGORY}"

    FUNCTION = "process"

    def process(self, width, height):
        return width, height


class HelperNodes_CfgScale(BaseNode):
    """
    Simple integer value node that allows you to specify the CFG scale
    for how strictly to the prompt the AI is.

    Permits values between 0 and 10, defaults at 8.0, and permits
    revisions as small as 0.25 on CFG scale selection.  Rounds to two
    decimal points.
    """
    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "scale": ("FLOAT", {
                    "default": 8.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.25,
                    "round": 0.00,
                    "display": "number"
                }),
            }
        }

    RETURN_TYPES = ("INT", )
    RETURN_NAMES = ("CFG",)

    CATEGORY = f"{MODULE_CATEGORY}"

    FUNCTION = "process"

    def process(self, scale) -> tuple:
        return (scale,)


class HelperNodes_Steps(BaseNode):
    """
    Simple integer value node that allows you to specify the number of
    sample steps to make in KSampler.

    Permits you to select between 1 and 100, but defaults at 25.
    """
    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "steps": ("INT", {
                    "default": 25,
                    "min": 1,
                    "max": 100,
                    "step": 1,
                    "display": "number"
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("steps",)

    CATEGORY = f"{MODULE_CATEGORY}"

    def process(self, steps) -> tuple:
        return (steps,)


class HelperNodes_StringLiteral(BaseNode):
    """
    Simple String value node that allows you to specify a string to pass
    into other nodes.

    Does not permit multiline text. See HelperNodes_MultilineStringLiteral
    for multiline text values.
    """
    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "string": ("STRING", {"multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    CATEGORY = f"{MODULE_CATEGORY}"

    def process(self, string) -> tuple:
        return (string,)


class HelperNodes_MultilineStringLiteral(BaseNode):
    """
    Simple String value node that allows you to specify a string to pass
    into other nodes.

    This node permits multiline text.
    """
    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "string": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    CATEGORY = f"{MODULE_CATEGORY}"

    def process(self, string) -> tuple:
        return (string,)
