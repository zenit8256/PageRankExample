import networkx as nx

G = nx.DiGraph()

websites = {
    1: "Bamazon",
    2: "Foogle",
    3: "Microsnack",
    4: "BookHub",
    5: "TubeYou",
    6: "Twizzler",
    7: "Instaglam",
    8: "Zoomify",
    9: "Facepad",
    10: "Linkr",
    11: "SnappyBook",
    12: "Pintastic",
    13: "Flickroo",
    14: "Snapster",
    15: "Tweeter",
    16: "Googlr",
    17: "Whatsup",
    18: "Futub",
    19: "Meedle",
    20: "Quokka"
}

links = [
    (1, 2, {"weight": 5.0}),
    (1, 3, {"weight": 5.0}),
    (1, 4, {"weight": 5.0}),
    (1, 5, {"weight": 5.0}),
    (1, 6, {"weight": 2.0}),
    (2, 7, {"weight": 2.0}),
    (2, 8, {"weight": 2.0}),
    (2, 9, {"weight": 2.0}),
    (2, 10, {"weight": 2.0}),
    (3, 11, {"weight": 2.0}),
    (3, 12, {"weight": 2.0}),
    (3, 13, {"weight": 2.0}),
    (4, 14, {"weight": 2.0}),
    (4, 15, {"weight": 2.0}),
    (5, 16, {"weight": 2.0}),
    (6, 17, {"weight": 2.0}),
    (7, 18, {"weight": 2.0}),
    (8, 19, {"weight": 2.0}),
    (9, 20, {"weight": 2.0}),
    (10, 11, {"weight": 2.0}),
    (11, 12, {"weight": 2.0}),
    (12, 13, {"weight": 2.0}),
    (13, 14, {"weight": 2.0}),
    (14, 15, {"weight": 2.0}),
    (15, 16, {"weight": 2.0}),
    (16, 17, {"weight": 2.0}),
    (17, 18, {"weight": 2.0}),
    (18, 19, {"weight": 2.0}),
    (19, 20, {"weight": 2.0}),
    (20, 1, {"weight": 2.0})
]

G.add_edges_from(links)

pagerank = nx.pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight="weight")

sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
for page, rank in sorted_pagerank:
    print(f"{websites[page]}: PageRank = {rank:.4f}")
