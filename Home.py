import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
content1 = """Lorem ipsum odor amet, consectetuer adipiscing elit. Dapibus dapibus conubia sollicitudin; tempus ante dapibus. Luctus iaculis in pharetra laoreet pulvinar sagittis? Gravida posuere adipiscing nisl finibus justo nullam. Conubia luctus vulputate pellentesque ornare hendrerit mattis neque; morbi ultrices. Arcu ante facilisis per malesuada inceptos congue tristique condimentum. Integer ad interdum ullamcorper magna scelerisque morbi mi massa? Urna inceptos est tincidunt malesuada; primis fusce justo. Hendrerit ligula fusce sapien pellentesque congue fringilla viverra. Venenatis sem convallis scelerisque sapien nisl primis. Urna venenatis mi quam litora habitant. Phasellus vehicula diam tincidunt fames elementum volutpat aliquet. Dolor blandit eros sem tellus nam tortor fames tortor. Maximus porttitor maximus cursus fames aliquam; imperdiet non. Ullamcorper varius eros ullamcorper blandit est nisi bibendum. Metus class sagittis morbi mus taciti platea."""
st.write(content1)
st.subheader("Our Team", divider="red")

column1, empty1, column2, empty2, column3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")

with column1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.text(row["role"])
        st.image(f"images/{row['image']}")\

with column2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.text(row["role"])
        st.image(f"images/{row['image']}")

with column3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first_name"].title()} {row["last_name"].title()}')
        st.text(row["role"])
        st.image(f"images/{row['image']}")