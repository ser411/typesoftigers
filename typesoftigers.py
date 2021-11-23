import streamlit as st
import pandas as pd
import PIL
from PIL import Image

st.title("9 Types of Tigers")
st.header("Lets learn about all 9 types of tigers, including population size, weight, range, and unique features.")

st.subheader("**Endangered Status**")
st.write("**1.Siberian Tiger**")

st.write(pd.DataFrame({
       'List': ['Endangered Status','Common name','Latin name','Also known as','Range','Weight','Size','Unique Features'],
       'Description':['Endangered','Siberian tiger','Panthera tigris altaica','Korean tiger, Amur tiger, Manchurian tiger, Ussurian tiger','North Asia (Russia, China, Korea)','389 – 475 lbs (males), 260 – 303 lbs (females)','70 – 82 inches (males), 66 – 72 inches (females)','Big size, pale fur']
       }))
image = Image.open('siberian.jpg')
st.image(image, caption='Siberian Tiger')


st.write("**2.Bengal Tiger**")

st.write(pd.DataFrame({
    'List': ['Endangered Status','Common name','Latin name','Also known as','Range','Weight','Size','Unique Features'],
    'Description':['Endangered','Bengal tiger','Panthera tigris tigris','Royal Bengal tiger, Indian tiger','Indian subcontinent (India, Nepal, Bhutan, Bangladesh)','397 – 569 lbs (males), 220 – 350 lbs (females)','110 – 120 inches (males), 94 – 104 inches (females)','Large bodies, white mutation']
}))

image = Image.open('bengal.jpg')

st.image(image, caption='Bengal Tiger')


st.write("**3.Indochinese Tiger**")

st.write(pd.DataFrame({
    'List': ['Endangered Status','Common name','Latin name','Also known as','Range','Weight','Size','Unique Features'],
    'Description':['Near critically endangered','Indochinese tiger','Panthera tigris corbetti','Corbett’s tiger','Southeast Asia (Thailand, Vietnam, Laos, Burma, China, formerly Cambodia)','331 to 430 lbs (males), 220 – 290 lbs (females)','100 – 112 inches (males), 91 – 100 inches (females)','Short, narrow, single stripes']
}))

image = Image.open('indochinese.jpg')

st.image(image, caption='Indochinese Tiger')


st.write("**4.Malayan Tiger**")

st.write(pd.DataFrame({
    'List': ['Endangered Status','Common name','Latin name','Also known as','Range','Weight','Size','Unique Features'],
    'Description':['Critically endangered','Malayan tiger','Panthera tigris jacksoni and occasionally Panthera tigris malayensis','Southern Indochinese tiger','Southeast Asia (Malaysia, Thailand, Burma)','220 – 308 lbs (males), 165 – 245 lbs (females)','75 – 112 inches (males), 70 – 103 inches (females)','Small and endangered. No notable physical difference between the Indochinese and Malayan tigers.']
}))

image = Image.open('malayan.jpg')

st.image(image, caption='Malayan Tiger')


st.write("**5.South China Tiger**")

st.write(pd.DataFrame({
    'List': ['Endangered Status','Common name','Latin name','Also known as','Range','Weight','Size','Unique Features'],
    'Description':['Critically endangered and near extinction','South China tiger','Panthera tigris amoyensis','Amoy tiger, Xiamen tiger, Chinese tiger','Central and eastern China (Hunan, Fukien, Guangdong and Jiangxi provinces)','287 – 386 lbs (males), 220 – 254 lbs (females)','91 – 104 inches (males), 87 – 94 inches (females)','Small, rare, possible blue mutation.']
}))

st.write("The South China tiger is an extremely rare species. In fact, it might even be functionally extinct. There are only 30 – 40 of them left, and they’re all in zoos. The South China tiger hasn’t been spotted in the wild in decades.")


st.write("**6.Sumatran Tiger**")

st.write(pd.DataFrame({
    'List': ['Endangered Status','Common name','Latin name','Range','Weight','Size','Unique Features'],
    'Description':['Critically endangered','Sumatran tiger','Panthera tigris sumatrae','Indonesia','220 – 310 lbs (males), 165 – 243 lbs (females)','87 – 100 inches (males), 85 – 91 inches (females)','Smallest breed, genetically isolated, the only surviving tiger species in the Sudra Islands.']
}))

image = Image.open('sumatran.jpg')

st.image(image, caption='Sumatran Tiger')

st.subheader("**Extinct**")
st.write("(3 Subspecies Extinct tiger)")

st.write("**7.Caspian Tiger**")
st.write(pd.DataFrame({
    'List': ['Common name','Latin name','Also known as','Range','Weight','Size','Unique Features'],
    'Description':['Caspian tiger','Originally Felis virgata, later Panthera tigris virgata','Hyrcanian tiger, Hyrcan tiger, Turan tiger','Central Asia and the Middle East (China, Turkey, Iran, Afghanistan)','370 – 530 lbs (males), 187 – 298 lbs (females)','106 – 116 inches (males), 94 – 102 inches (females)','Large bodies, muted colors.']
}))


st.write("**8.Bali Tiger**")
st.write(pd.DataFrame({
    'List': ['Common name','Latin name','Range','Weight','Size','Unique Features'],
    'Description':['Bali tiger','Panthera tigris balica','Indonesia','200 – 220 lbs (males), 143 – 176 lbs (females)','87 – 91 inches (males), 75 – 83 inches (females)','Formerly smallest tiger species']
}))


st.write("**9.Javan Tiger**")
st.write(pd.DataFrame({
    'List': ['Common name','Latin name','Range','Weight','Size','Unique Features'],
    'Description':['Javan tiger','Panthera tigris sondaica','Indonesia','220 – 311 lbs (males), 165 – 254 lbs (females)','Around 90 – 100 inches','Extinct but possibly in hiding']
}))
st.write("Source")
st.write("https://storyteller.travel/types-of-tigers/")
