import os
import sys
import networkx as nx

START = 0
COUNT = 20000
def get_client():

    from douban_client import DoubanClient
    API_KEY = os.environ.get('DOUBAN_API_KEY')
    API_SECRET = os.environ.get('DOUBAN_API_SECRET')
    your_redirect_uri = ''
    SCOPE = 'bouban_basic_common, community_basic_user, shuo_basic_r, shuo_basic_w'

    TOKEN_CODE = os.environ.get('DOUBAN_TOKEN_CODE')

    client = DoubanClient(API_KEY, API_SECRET, your_redirect_uri, SCOPE)

    client.auth_with_token(TOKEN_CODE)

    return client

def get_user_info(id, client):
    user = client.user.get(id)

    return user

def get_followers(id, client):
    followers = client.user.followers(id, START, COUNT)
    followers = [follower['id'] for follower in followers]

    return followers

def get_following(id, client):
    followings = client.user.following(id,START, COUNT) 
    followings = [following['id'] for following in followings]

    return followings

def generate_graph(id, client):
    graph = nx.DiGraph()
    # user = get_user_info(id, client)

    visited = []
    to_visite = [id]
    edges = []

    while to_visite and len(visited) < 10:
        id = to_visite.pop(0)
        followers = get_followers(id, client)
        followings = get_following(id, client)

        for follower in followers:
            if follower in visited:
                pass
            else:
                to_visite.append(follower)
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
    # ID = 79102917
    client = get_client()
    ID = client.user.me['id']
    sys.exit(generate_graph(ID, client))
