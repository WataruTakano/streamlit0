import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit introduction")

st.write("DataFrame")

df=pd.DataFrame({
	"1": [1,2,3,4],
    "2": [10,20,30,40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)

st.table(df)

"""
# 章
## 節
### 項

```python
streamlit st
```
"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ["a","b","c"]
)
st.write(df)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df=pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=["lat","lon"]
)
st.map(df)

st.write("DisplayImage")

if st.checkbox("Show image") :
	img = Image.open("sample.png")
	st.image(img, caption="sample", use_column_width =True)

option = st.selectbox(
	"answer your favorite number",
	list(range(1,11))
)

"your favorite number", option


#st.sidebar.write("interactive widgets")
#text = st.sidebar.text_input("answer your hobby")
#"your hobby is ", text

#condition = st.sidebar.slider("answer your condition", 0, 100, 50)
#"condition is ",condition

left_column, right_column = st.beta_columns(2)
button = left_column.button("display the right column")
if button:
	right_column.write("this is right")

expander = st.beta_expander("question")
expander.write("answer")

st.sidebar.write("interactive widgets")
text = st.sidebar.text_input("answer your hobby")
"your hobby is ", text

condition = st.sidebar.slider("answer your condition", 0, 100, 50)
"condition is ",condition

st.write("progress bar")
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100) :
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i+1)
	time.sleep(0.1)

"Done"