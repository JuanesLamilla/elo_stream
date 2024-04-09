"""
""" 

# Import libraries
import streamlit as st
import random

def wide_space_default():
    st.set_page_config(layout="wide")

wide_space_default()

data = {
    "Apple": "An apple is a round, often :red[red], edible :red[fruit] produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica). Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found. Apples have been grown for thousands of years in Asia and Europe and were introduced to North America by European colonists. Apples have religious and mythological significance in many cultures, including Norse, Greek, and European Christian tradition.",
    "Firetruck": "A fire engine (also known in some places as a fire truck or fire ambulance) is a (often :red[red]) vehicle, usually a specially-designed or modified truck, that functions as a firefighting apparatus. The primary purposes of a fire engine include transporting firefighters and water to an :red[emergency] as well as carrying equipment for firefighting operations in a fire drill. Some fire engines have specialized functions, such as wildfire suppression and aircraft rescue and firefighting, and may also carry equipment for technical rescue.",
    "Orange": "An orange, also called sweet orange to distinguish it from the bitter orange Citrus × aurantium, is the (typically :red[orange] coloured) :red[fruit] of a tree in the family Rutaceae. Botanically, this is the hybrid Citrus × sinensis, between the pomelo (Citrus maxima) and the mandarin orange (Citrus reticulata). The chloroplast genome, and therefore the maternal line, is that of pomelo. The sweet orange has had its full genome sequenced.",
    "Traffic Cone": "Traffic cones, also called pylons, witches hats,[1][2] road cones, highway cones, safety cones, caution cones, channelizing devices,[3] construction cones, roadworks cones, or just cones, are usually cone-shaped (and typically :red[orange] coloured) markers that are placed on roads or footpaths to temporarily redirect traffic in a safe manner. They are often used to create separation or merge lanes during road construction projects or automobile :red[emergencies], although heavier, more permanent markers or signs are used if the diversion is to stay in place for a long period of time.",
}

key_words = {
    "Apple": ["fruit", "red"],
    "Firetruck": ["emergency", "red"],
    "Orange": ["fruit", "orange"],
    "Traffic Cone": ["orange", "emergency"],
}

key_word_info = {
    "fruit": "A fruit is the seed-bearing structure in flowering plants formed from the ovary after flowering. Fruits are the means by which flowering plants disseminate seeds. Edible fruits, in particular, have propagated with the movements of humans and animals in a symbiotic relationship as a means for seed dispersal and nutrition.",
    "red": "Red is the color at the long wavelength end of the visible spectrum of light, next to orange and opposite violet. It has a dominant wavelength of approximately 625–740 nanometres. It is a primary color in the RGB color model and the CMYK color model, and is the complementary color of cyan.",
    "orange": "Orange is the colour between yellow and red on the spectrum of visible light. Human eyes perceive orange when observing light with a dominant wavelength between roughly 585 and 620 nanometres. In painting and traditional colour theory, it is a secondary colour of pigments, created by mixing yellow and red.",
    "emergency": "An emergency is a situation that poses an immediate risk to health, life, property, or environment. Most emergencies require urgent intervention to prevent a worsening of the situation, although in some situations, mitigation may not be possible and agencies may only be able to offer palliative care for the aftermath.",

}

st.title("Choose your preferred option")

choice_1, choice_2 = st.columns(2)

# Randomly pick 2 options from data
options = random.sample(list(data.keys()), 2)

# Get the keys (titles) and values (text) of the selected options
option_1_key = options[0]
option_1_value = data[option_1_key]

option_2_key = options[1]
option_2_value = data[option_2_key]

with choice_1:
    st.header("Option 1: " + option_1_key)
    st.markdown(option_1_value)
    st.button('Vote option 1')

with choice_2:
    st.header("Option 2: " + option_2_key)
    st.markdown(option_2_value)
    st.button('Vote option 2')

st.button('Skip')

st.markdown("""---""")

st.header("Additional info:")

# Get the key words for the selected options (if they share a key word, it will only be displayed once)
key_words_combined = list(set(key_words[option_1_key] + key_words[option_2_key]))

for key_word in key_words_combined:
    st.subheader(":red[" + key_word + "]")
    st.markdown(key_word_info[key_word])
