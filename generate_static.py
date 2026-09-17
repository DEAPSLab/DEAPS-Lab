import os, re

NAV = """    <div class="bg-gray-800 text-white text-xs py-2">
        <div class="max-w-7xl mx-auto px-4 flex justify-between items-center">
            <div>Welcome to DEAPS Lab - Distributed, Edge, AI, Parallel, and Scheduling Systems Lab</div>
            <div class="flex space-x-4">
                <a href="contact.html" class="bg-sky-500 text-white px-2 py-1 rounded hover:bg-sky-600">Contact Us</a>
                <a href="opportunities.html" class="bg-sky-500 text-white px-2 py-1 rounded hover:bg-sky-600">Join Our Team</a>
            </div>
        </div>
    </div>
    <nav class="bg-sky-400 shadow-lg sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex items-center justify-between h-16">
                <a href="index.html" class="flex items-center space-x-3">
                    <img src="static/images/deaps-logo.svg" alt="DEAPS Lab Logo" class="w-8 h-8" />
                    <span class="font-bold text-xl text-white">DEAPSLab</span>
                </a>
                <div class="flex-1 max-w-2xl mx-8">
                    <div class="relative">
                        <input type="text" placeholder="Search research, publications, members..." class="w-full py-2 px-4 rounded-md border-2 border-yellow-400 focus:outline-none focus:border-yellow-500">
                        <button class="absolute right-0 top-0 h-full px-4 bg-yellow-400 hover:bg-yellow-500 rounded-r-md">
                            <svg class="w-5 h-5 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                        </button>
                    </div>
                </div>
                <div class="flex items-center space-x-4 flex-wrap">
                    <a href="publications.html" class="nav-link">Publications</a>
                    <a href="research.html" class="nav-link">Research</a>
                    <a href="members.html" class="nav-link">Team</a>
                    <a href="https://www.google.com/maps/place/Indian+Institute+Of+Technology-Ropar" target="_blank" class="nav-link flex items-center">Location</a>
                </div>
            </div>
        </div>
        <div class="bg-sky-400 border-t border-sky-300">
            <div class="max-w-7xl mx-auto px-4">
                <div class="flex items-center space-x-4 py-2 flex-wrap">
                    <a href="about.html" class="nav-link">About</a>
                    <a href="nitin-auluck.html" class="nav-link">Prof. Nitin Auluck</a>
                    <a href="opportunities.html" class="nav-link">Opportunities</a>
                    <a href="news-events.html" class="nav-link">News &amp; Events</a>
                    <a href="resources.html" class="nav-link">Resources</a>
                    <a href="gallery.html" class="nav-link">Gallery</a>
                    <a href="alumni.html" class="nav-link">Alumni</a>
                </div>
            </div>
        </div>
    </nav>"""

FOOTER = """    <footer class="bg-gray-900 text-white py-12 mt-16">
        <div class="max-w-7xl mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8">
                <div>
                    <h3 class="font-bold text-lg mb-4">Research Areas</h3>
                    <ul class="space-y-2 text-sm text-gray-300">
                        <li><a href="research.html" class="hover:text-yellow-400">Distributed Systems</a></li>
                        <li><a href="research.html" class="hover:text-yellow-400">Edge Computing</a></li>
                        <li><a href="research.html" class="hover:text-yellow-400">Real-Time Systems</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold text-lg mb-4">Quick Links</h3>
                    <ul class="space-y-2 text-sm text-gray-300">
                        <li><a href="publications.html" class="hover:text-yellow-400">Publications</a></li>
                        <li><a href="opportunities.html" class="hover:text-yellow-400">Join Us</a></li>
                        <li><a href="contact.html" class="hover:text-yellow-400">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold text-lg mb-4">IIT Ropar</h3>
                    <ul class="space-y-2 text-sm text-gray-300">
                        <li><a href="https://www.iitrpr.ac.in/" target="_blank" class="hover:text-yellow-400">Main Website</a></li>
                        <li><a href="https://cse.iitrpr.ac.in/" target="_blank" class="hover:text-yellow-400">CSE Department</a></li>
                        <li><a href="https://www.iitrpr.ac.in/admissions" target="_blank" class="hover:text-yellow-400">Admissions</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold text-lg mb-4">DEAPS Lab</h3>
                    <p class="text-sm text-gray-300">Distributed, Edge, AI, Parallel, and Scheduling Systems Lab — leading research in distributed systems, edge computing, and real-time technologies.</p>
                </div>
            </div>
            <div class="border-t border-gray-700 mt-8 pt-8 text-center text-sm text-gray-400">
                <p>&copy; 2024 DEAPS Lab. All rights reserved.</p>
            </div>
        </div>
    </footer>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .amazon-btn {{ display:inline-block; background:#facc15; color:#000; font-weight:600; padding:0.5rem 1.5rem; border-radius:0.375rem; transition:background 0.2s; box-shadow:0 2px 4px rgba(0,0,0,0.15); }}
        .amazon-btn:hover {{ background:#eab308; }}
        .amazon-btn-secondary {{ display:inline-block; background:#e5e7eb; color:#1f2937; font-weight:600; padding:0.5rem 1.5rem; border-radius:0.375rem; border:1px solid #d1d5db; transition:background 0.2s; }}
        .amazon-btn-secondary:hover {{ background:#d1d5db; }}
        .nav-link {{ background:#0ea5e9; color:#fff; padding:0.5rem 0.75rem; font-size:1rem; font-weight:500; border-radius:0.375rem; transition:background 0.2s; display:inline-block; }}
        .nav-link:hover {{ background:#0284c7; }}
    </style>
</head>
<body class="bg-gray-50">"""

TAIL = "</body>\n</html>"

templates_dir = "deapslab/templates"
docs_dir = "docs"

# Map template filename -> output filename, title
pages = {
    "about.html":       ("about.html",       "About - DEAPS Lab"),
    "nitin_auluck.html":("nitin-auluck.html", "Dr. Nitin Auluck - DEAPS Lab"),
    "members.html":     ("members.html",      "Team Members - DEAPS Lab"),
    "research.html":    ("research.html",     "Research - DEAPS Lab"),
    "publications.html":("publications.html", "Publications - DEAPS Lab"),
    "opportunities.html":("opportunities.html","Opportunities - DEAPS Lab"),
    "news_events.html": ("news-events.html",  "News & Events - DEAPS Lab"),
    "resources.html":   ("resources.html",    "Resources - DEAPS Lab"),
    "gallery.html":     ("gallery.html",      "Gallery - DEAPS Lab"),
    "alumni.html":      ("alumni.html",       "Alumni - DEAPS Lab"),
    "contact.html":     ("contact.html",      "Contact - DEAPS Lab"),
}

url_map = {
    "/contact/":      "contact.html",
    "/opportunities/":"opportunities.html",
    "/publications/": "publications.html",
    "/research/":     "research.html",
    "/members/":      "members.html",
    "/about/":        "about.html",
    "/nitin-auluck/": "nitin-auluck.html",
    "/news-events/":  "news-events.html",
    "/resources/":    "resources.html",
    "/gallery/":      "gallery.html",
    "/alumni/":       "alumni.html",
    "/static/images/":"static/images/",
    '"/":':           '"index.html":',
    'href="/"':       'href="index.html"',
}

for tmpl, (out, title) in pages.items():
    path = os.path.join(templates_dir, tmpl)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Extract content block
    m = re.search(r'\{%\s*block content\s*%\}(.*?)\{%\s*endblock\s*%\}', content, re.DOTALL)
    body = m.group(1).strip() if m else content

    # Fix Django template tags leftover
    body = re.sub(r'\{%.*?%\}', '', body)
    body = re.sub(r'\{\{.*?\}\}', '', body)

    # Fix URLs
    for old, new in url_map.items():
        body = body.replace(old, new)

    html = HEAD.format(title=title) + "\n" + NAV + "\n    <main>\n" + body + "\n    </main>\n" + FOOTER + "\n" + TAIL
    out_path = os.path.join(docs_dir, out)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {out_path}")

print("Done!")
