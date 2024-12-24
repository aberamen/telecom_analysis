from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def perform_kmeans(data, n_clusters):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = model.fit_predict(data)
    return clusters, model

def elbow_method(data, max_k):
    sse = []
    for k in range(1, max_k):
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(data)
        sse.append(model.inertia_)
    plt.plot(range(1, max_k), sse)
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE")
    plt.show()
