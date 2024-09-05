import html

def load_data(file_path):
    """Load HTML data from a file."""
    with open(file_path, 'r') as file:
        return html.load(file)

def analyze_followers(data):
    """Analyze follower and following relationships."""
    following = set(data.get('following', []))
    followers = set(data.get('followers', []))
    blocked = set(data.get('blocked', []))

    not_following_back = following - followers

    mutual_followers = following & followers

    not_following_me_back = followers - following

    blocking_me = blocked

    blocking_me_following = blocking_me & following

    return not_following_back, mutual_followers, not_following_me_back, blocking_me_following

def main():
    
    data = load_data('followers_data.json') 
    not_following_back, mutual_followers, not_following_me_back, blocking_me_following = analyze_followers(data)
    print("Accounts I follow but they don't follow me back:")
    print(not_following_back)
    print("\nAccounts I follow and they also follow me back:")
    print(mutual_followers)
    print("\nAccounts that follow me but I don't follow them:")
    print(not_following_me_back)
    print("\nAccounts who block me and I follow them:")
    print(blocking_me_following)

if __name__ == "__main__":main()    

