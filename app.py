import gradio as gr
from API_Project_2.get_city_temperature import get_city_temperature

def get_temperature_for_web(city_name):
    try:
        result = get_city_temperature(city_name)
        return result
    except Exception as e:
        return f"Error: {e}"

# Create the Gradio interface
iface = gr.Interface(
    fn=get_temperature_for_web,   # your function
    inputs="text",                # text input for city name
    outputs="text",               # show the temperature result
    title="City Temperature API",
    description="Enter a city name to get its current temperature."
)

# Launch the web app
iface.launch(share=True)