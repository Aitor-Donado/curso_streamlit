from streamlit_marquee import streamlit_marquee

streamlit_marquee(**{
    # the marquee container background color
    'background': "#ffff00",
    # the marquee text size
    'fontSize': '24px',
    # the marquee text color
    "color": "#0000ff",
    # the marquee text content
    'content': '~here is custom marquee component~',
    # the marquee container width
    'width': '600px',
    # the marquee container line height
    'lineHeight': "35px",
    # the marquee duration
    'animationDuration': '5s',
})