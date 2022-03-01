import base64

data = "Tier 2 Support Software Engineer (Backend)"
encoded = base64.b64encode(data.encode("utf-8"))
encoded_str = str(encoded, "utf-8")

print(encoded_str)
