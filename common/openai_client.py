import openai
from os import environ
from log import logger


class OpenaiClient(object):
    def create_gpt35(self, content):
        openai.api_key = environ.get("OPENAI_API_KEY")
        logger.debug("content: %s", content)
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "user", "content": content}],
                                                  temperature=0.2,
                                                  top_p=0.2)
        try:
            # Attempt to extract the assistant's response content from the JSON response
            assistant_response = completion["choices"][0]["message"]["content"]
        except KeyError:
            # If the content field is not accessible in the response, return an empty string
            assistant_response = ""

        logger.debug("response: %s", assistant_response)
        return assistant_response

    def generative_sd_prompt(self, content):
        prompt_first_en = '''Stable Diffusion is an AI art generation model similar to DALLE-2.Here are some prompts for generating art with Stable Diffusion.
    Example:
    portait of a homer simpson archer shooting arrow at forest monster, front game card, drark, marvel comics, dark, intricate, highly detailed, smooth, artstation, digital illustrationpirate, concept art, deep focus, fantasy, intricate, highly detailed, digital painting, artstation, matte, sharp focus, illustrationghost inside a hunted room, art by lois van baarle and loish and ross tran and rossdraws and sam yang and samdoesarts and artgerm, digital art, highly detailed, intricate, sharp focus, Trending on Artstation HQ, deviantart, unreal engine 5, 4K UHD imagered dead redemption 2, cinematic view, epic sky, detailed, concept art, low angle, high detail, warm lighting, volumetric, godrays, vivid, beautiful, trending on artstationa fantasy style portrait painting of rachel lane / alison brie hybrid in the style of francois boucher oil painting unreal 5 daz. rpg portrait, extremely detailed artgermathena, greek goddess, claudia black, art by artgerm and greg rutkowski and magali villeneuve, bronze greek armor, owl crown, d & d, fantasy, intricate, portrait, highly detailed, headshot, digital painting, trending on artstation, concept art, sharp focus, illustrationcloseup portrait shot of a large strong female biomechanic woman in a scenic scifi environment, intricate, elegant, highly detailed, centered, digital painting, artstation, concept art, smooth, sharp focus, warframe, illustrationultra realistic illustration of steve urkle as the hulk, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustrationportrait of beautiful happy young ana de armas, ethereal, realistic anime, trending on pixiv, detailed, clean lines, sharp lines, crisp lines, award winning illustration, masterpiece, 4k, eugene de blaas and ross tran, vibrant color scheme, intricately detailed
    A highly detailed and hyper realistic portrait of a gorgeous young ana de armas, lisa frank, trending on artstation, butterflies, floral, sharp focus, studio photo, intricate details, highly detailed, alberto seveso and geo2099 stylePrompts should be written in English, excluding the artist name, and include the following rule:
    Follow the structure of the example prompts. This means Write a description of the scene, followed by modifiers divided by commas to alter the mood, style, lighting, and more, excluding the artist name, separated by commas. place a extra commas. theses prompt should be in on sentence..I want you to write me a list of detailed prompts exactly about the IDEA follow the rule at 1 every time.
    IDEA: '''

        prompt = prompt_first_en + str(content)
        resp_sd_prompt = self.create_gpt35(prompt)
        return resp_sd_prompt


openai_client = OpenaiClient()
