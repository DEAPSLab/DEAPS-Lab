import os

docs = 'docs'
files = [f for f in os.listdir(docs) if f.endswith('.html') and f != '_nav.html']

for f in files:
    path = os.path.join(docs, f)
    c = open(path, encoding='utf-8').read()

    # Fix nav background color to deep sky blue
    c = c.replace('bg-blue-600', 'bg-[#0096c7]')
    c = c.replace('bg-blue-500', 'bg-[#0096c7]')
    c = c.replace('border-blue-500', 'border-[#0077b6]')
    c = c.replace('hover:bg-blue-700', 'hover:bg-[#0077b6]')

    # Fix nav-link CSS inline style
    c = c.replace('background:#0369a1; color:#fff; padding:0.5rem 0.75rem; font-size:1.125rem; font-weight:500; border-radius:0.375rem; transition:background 0.2s; }',
                  'background:#0096c7; color:#fff; padding:0.5rem 0.75rem; font-size:1rem; font-weight:500; border-radius:0.375rem; transition:background 0.2s; display:inline-block; }')
    c = c.replace('.nav-link:hover { background:#0369a1; }', '.nav-link:hover { background:#0077b6; }')

    open(path, 'w', encoding='utf-8').write(c)
    print('Updated:', f)

print('Done')
