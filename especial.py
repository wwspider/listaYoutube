import re
texto = 'Comunicaçao # interna;'
re_texto = re.sub(r'[^a-zA-Z0-9çÇ]', ' ', texto)

print(re_texto)