import streamlit as st

# Set up session state variables
if "ten_x" not in st.session_state:
    # ten_x mode changes our buttons to increment and decrement by 10 instead of by 1
    st.session_state.ten_x = 0

if "hundred_x" not in st.session_state:
    st.session_state.hundred_x = False
    # hundred_x mode changes our buttons to increment and decrement by 100 instead of by 1

if "count" not in st.session_state:
    st.session_state.count = 0

# Helper function to determine the current increment/decrement step
def get_step():
    if st.session_state.hundred_x:
        return 100
    if st.session_state.ten_x:
        return 10
    return 1

# Set up callbacks for inputs
def increment():
    st.session_state.count += get_step()


def decrement():
    st.session_state.count -= get_step()
    if st.session_state.count < 0:
        # Minimum count value is zero
        st.session_state.count = 0


# Write to page
with st.expander("Options") as options:
    # The key of the checkbox (ten_x) will automatically be added to the session state
    st.checkbox("10x mode", key="ten_x", value=st.session_state.ten_x)
    st.checkbox("100x mode", key="hundred_x", value=st.session_state.hundred_x)

st.write(f"Total count is {st.session_state.count}")

# Get the current step for the button labels
step = get_step()

st.button(
    f"plus {step}",
    key="increment",
    on_click=increment,
)
st.button(
    f"minus {step}",
    key="decrement",
    on_click=decrement,
)
