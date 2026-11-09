import re
with open('lessons/0001-context-and-memory.html') as f:
    html = f.read()
html = re.sub(r'<script.*?</script>', '', html, flags=re.S)
html = re.sub(r'<style.*?</style>', '', html, flags=re.S)
text = re.sub(r'<[^>]+>', ' ', html)
words = text.split()
print('word count:', len(words))
print('estimated minutes:', len(words)/150)
