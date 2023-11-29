import streamlit as st
import app_info


#Helper Functions
def isinstr(num, string):
    for i in num:
        if i not in string:
            return False
    return True
def isbin(num):
    return isinstr(num, "01")
def ishex(num):
    return isinstr(num, "0123456789abcdefABCDEF")

def bin_to_dec(num):
    d_num = 0
    pow2 = 1
    for i in num[::-1]:
        d_num += int(i)*pow2
        pow2 *= 2
    return d_num
def dec_to_bin(num):
    num = int(num)
    b_num = 0
    pow10 = 1
    while num > 0:
        b_num += (num%2)*pow10
        pow10 *= 10
        num //= 2
    return str(b_num)
def dec_to_hex(num):
    num = int(num)
    h_num_list = []
    h_num = ""
    pow10 = 1
    while num > 0:
        h_num_list.append(num%16)
        num //= 16
    for i in h_num_list[::-1]:
        if i >= 10:
            h_num += chr(ord('A') + i - 10)
        else:
            h_num += str(i)
    return h_num
def hex_to_dec(num):
    d_num = 0
    pow16 = 1
    for i in num[::-1]:
        if ord(i) >= ord('a') and ord(i) <= ord('f'):
            d_num += (10 + ord(i) - ord('a'))*pow16
            pow16 *= 16
        elif ord(i) >= ord('A') and ord(i) <= ord('F'):
            d_num += (10 + ord(i) - ord('A'))*pow16
            pow16 *= 16
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            d_num += (ord(i) - ord('0'))*pow16
            pow16 *= 16
    return d_num

def convert(text, mode, config):
    converted_text = ""
    try:
        if mode == 0:
            for i in range(len(text[0])):
                if i > 0:
                    converted_text += ' '
                if config['mode'] == "Binary":
                    converted_text += dec_to_bin(str(ord(text[0][i])))
                elif config['mode'] == "Decimal":
                    converted_text += str(ord(text[0][i]))
                elif config['mode'] == "Hexadecimal":
                    converted_text += dec_to_hex(str(ord(text[0][i])))
        elif mode == 1:
            text = text[1].split()
            for ch in text:
                if config['mode'] == "Binary":
                    if isbin(ch):
                        converted_text += chr(bin_to_dec(ch))
                elif config['mode'] == "Decimal":
                    if ch.isdigit():
                        converted_text += chr(int(ch))
                elif config['mode'] == "Hexadecimal":
                    if ishex(ch):
                        converted_text += chr(hex_to_dec(ch))
    except:
        text = f"<p style='font-size: 16px; color: red;'>[ Error ] - Invalid input was given!</p>"
        st.markdown(text, unsafe_allow_html=True)
        text = f"<p style='font-size: 16px; color: red;'>Try typing other characters or smaller values</p>"
        st.markdown(text, unsafe_allow_html=True)
    return converted_text


#Sidebar
def sidebar_section(config):
    st.sidebar.header("⚙️Options")
    config['mode'] = st.sidebar.radio("Convertion Mode", ["Binary", "Decimal", "Hexadecimal"]) #NEW
    config['font'] = st.sidebar.slider("Font Size", 1, 100, 16) #NEW
    
    st.sidebar.divider() #NEW
    
    st.sidebar.write("Hello, my name is ~*HAL*~")
    st.sidebar.write("...")
    st.sidebar.write("I mean, Convert.io, and I am here simply to assist you, so don't worry about me")
    st.sidebar.image(app_info.sidebar_image)
sidebar_section(app_info.config)


#Header
def header_section():
    st.title("Convert.io") #NEW
    st.write("Quickly convert your texts from *and* into **binary**, **decimal**, *and* **hexadecimal** form!")
    st.image(app_info.title_image)
    
    st.divider() #NEW
header_section() #NEW


#Functionality
def functionality_section(instructions, config):
    converted_text = ["", "", ""]
    
    expander = st.expander("Instructions")
    expander.divider()
    for instruction in instructions:
        expander.write(instruction)
    st.divider() #NEW
    
    st.subheader("Convert mode:")
    tab0, tab1 = st.tabs(["Text - Number", "Number - Text"])
    tab = 0
    with tab0:
        converted_text[0] = st.text_area(f"Type below the text you want converted into {config['mode']} form", "Example Text") #NEW
        if st.button("Submit"): #NEW
            converted_text[2] = convert(converted_text, 0, config)
    with tab1:
        converted_text[1] = st.text_area(f"Type below the text in {config['mode']} form you want converted into characters", "Example Text") #NEW
        if st.button("Submit "): #NEW
            converted_text[2] = convert(converted_text, 1, config)
    
    st.divider() #NEW
    
    st.subheader("Converted Text:")
    text = f"<p style='font-size: {config['font']}px;'>{converted_text[2]}</p>"
    st.markdown(text, unsafe_allow_html=True)
functionality_section(app_info.instructions, app_info.config)
