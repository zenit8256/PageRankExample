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
    (1, 2, {"weight": 0.26}),
    (1, 3, {"weight": 0.33}),
    (1, 4, {"weight": 0.12}),
    (1, 5, {"weight": 0.25}),
    (1, 6, {"weight": 0.15}),
    (2, 7, {"weight": 0.21}),
    (2, 8, {"weight": 0.28}),
    (2, 9, {"weight": 0.43}),
    (2, 10, {"weight": 0.25}),
    (3, 11, {"weight": 0.33}),
    (3, 12, {"weight": 0.29}),
    (3, 13, {"weight": 0.12}),
    (4, 14, {"weight": 0.01}),
    (4, 15, {"weight": 0.13}),
    (5, 16, {"weight": 0.56}),
    (6, 17, {"weight": 0.17}),
    (7, 18, {"weight": 0.78}),
    (8, 19, {"weight": 0.31}),
    (9, 20, {"weight": 0.5}),
    (10, 11, {"weight": 0.25}),
    (11, 12, {"weight": 0.18}),
    (12, 13, {"weight": 0.76}),
    (13, 14, {"weight": 0.23}),
    (14, 15, {"weight": 0.11}),
    (15, 16, {"weight": 0.1}),
    (16, 17, {"weight": 0.2}),
    (17, 18, {"weight": 0.3}),
    (18, 19, {"weight": 0.35}),
    (19, 20, {"weight": 0.27}),
    (20, 1, {"weight": 0.18})
]

G.add_edges_from(links)

pagerank = nx.pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight="weight")

sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
for page, rank in sorted_pagerank:
    print(f"{websites[page]}: PageRank = {rank:.4f}")
