import gradio as gr
import os
import keras_nlp
from transformers import AutoModelForCausalLM

# Set Kaggle API credentials using values from environment variables
os.environ["KAGGLE_USERNAME"] = os.environ.get("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.environ.get("KAGGLE_KEY")


# Load LoRA weights if you have them
LoRA_weights_path = "fined-tuned-model.lora.h5"
gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma_2b_en")
gemma_lm.backbone.enable_lora(rank=4)  # Enable LoRA with rank 4
gemma_lm.preprocessor.sequence_length = 512  # Limit sequence length
gemma_lm.backbone.load_lora_weights(LoRA_weights_path)  # Load LoRA weights

# Define the response generation function
def generate_response(message):
    # Create a prompt template
    template = "Instruction:\n{instruction}\n\nResponse:\n{response}"

    # Create the prompt with the current message
    prompt = template.format(instruction=message, response="")
    print("Prompt:\n", prompt)

    # Generate response from the model
    response = gemma_lm.generate(prompt, max_length=256)
    # Only keep the generated response
    response = response.split("Response:")[-1].strip()

    print("Generated Response:\n", response)

    # Extract and return the generated response text
    return response  # Adjust this if your model's output structure differs

# Create the Gradio chat interface
interface = gr.Interface(
    fn=generate_response,  # Function that generates responses
    inputs=gr.Textbox(placeholder="Hello, I am Sage, your mental health advisor", lines=2, scale=7),
    outputs=gr.Textbox(),
    title="Sage, your Mental Health Advisor",
#     description="Chat with Sage, your mental health advisor.",
#     live=True
)
proxy_prefix = os.environ.get("PROXY_PREFIX")
# Launch the Gradio app
interface.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix, share=True)
