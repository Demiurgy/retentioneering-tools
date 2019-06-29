from sklearn.cluster import KMeans

__KMEANS_FILTER__ = [
    'n_clusters',
    'init',
    'n_init',
    'max_iter',
    'tol',
    'precompute_distances',
    'verbose',
    'random_state',
    'copy_x',
    'n_jobs',
    'algorithm'
]


def simple_cluster(data, **kwargs):
    """
    Finds cluster of users in data.

    :param data: feature matrix for clustering
    :param kwargs: keyword arguments for sklearn.cluster.KMeans
    :return: np.array of clusters
    """
    km = KMeans(random_state=0, **{i: j for i, j in kwargs.items() if i in __KMEANS_FILTER__})
    return km.fit_predict(data.values)
