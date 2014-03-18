import os
import networkx as nx

def get_client():

    from doubao_client import DoubanClient
    API_KEY = os.environ.get('DOUBAN_API_KEY')
    API_SECRET = os.environ.get('DOUBAN_API_SECRET')
    your_redirect_uri = ''
    SCOPE = 'bouban_basic_common, community_basic_user'

    your_password = ''

    client = DoubanClient(API_KEY, API_SECRET, your_redirect_uri, SCOPE)

    client.auth_with_code(your_password)

    return client

def get_user_info(id, client):
    user = client.user.get(id)

def get_followers(id, client):
    followers = client.user.followers(id, start, count)

    return followers

def get_following(id, client):
    following = client.user.following(id, start, count)

    return followings

def generate_graph(id, client):
    graph = nx.DiGraph()
    # user = get_user_info(id, client)

    visited = []
    to_visite = [id]
    edges = []

    while to_visite and len(visited) < 10000:
        id = to_visite.pop(0)
        followers = get_followers(id, client)
        followings = get_following(id, client)

        for follower in followers:
            if follower in visited:
                pass
            else:
                to_visit.append(follower)
                edge = (follower, id)
                edges.append(edge)

        for following in followings:
            if following in visited:
                pass
            else:
                to_visite.append(following)
                edge = (id, following)
                edges.append(edge)

        visited.append(id)

    graph.add_edges_from(edges)

    return graph

if __name__ == '__main__':
    sys.exit(generate_graph())
