import re

def alphanumeric(password):
    return bool(re.match('^[a-zA-Z0-9]+$', password))

print(alphanumeric("g_jus91pz123HgswL0IHoz"))