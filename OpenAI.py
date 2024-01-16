import openai

# Set the API key
openai.api_key = "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"

def OPAI(yo):
    try:
        # Set up the model
        model_engine = "gpt-3.5-turbo-instruct"
        s = True
        while s:
            # yo = input("Ask me : ")
            prompt = yo

            # Generate a response
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.7,
            )

            message = completions['choices'][0]['text']
            if yo.lower() == "bye" or yo.lower() == "bye!" or yo.lower() == "byee" or yo.lower() == "bye":
                s = False
                return "Bye :)"
            elif yo.lower() == "hi" or yo.lower() == "hey" or yo.lower() == "hello" or yo.lower() == "hie" or yo.lower() == "hix":
                s = False
                return "Hi, You can ask me anything..."
            else:
                s = False
                return message
    except Exception as e:
        return '⚠️ 𝗔𝗜 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗼𝘃𝗲𝗿𝗹𝗼𝗮𝗱𝗲𝗱 !! \n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗹𝗮𝘁𝗲𝗿!!' + str(e)