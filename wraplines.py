def wrapline(text, char_count=100):
    a = text.split()
    breakpoint()
    ret = ''
    for i in range(0, len(text), char_count):
        ret += text[i:i+char_count]


text = "We are a small breakfast and lunch cafe and bakery.  Most of our food is dine in or wedding venues.  We have lost our business revenue.  Wedding venues have been cancelled."
wrapline(text)
