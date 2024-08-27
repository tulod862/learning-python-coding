from bs4 import BeautifulSoup

def extract_accounts_from_html(following_file, followers_file):
    """
    Extracts the lists of followers, following, and blocked accounts from an HTML file.

    Parameters:
    - html_file (str): Path to the HTML file.

    Returns:
    - Tuple containing three sets: followers, following, and blocked.
    """
    try:
        with open(followers_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        followers = {item.text.strip() for item in soup.select('a')}
        with open(following_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        following = {item.text.strip() for item in soup.select('a')}
        
        blocked = set()
        return followers, following, blocked

    except FileNotFoundError:
        print(f"Error: The file does not exist.")
        return set(), set(), set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set(), set(), set()

def analyze_relationships(followers, following, blocked):
    """
    Analyzes relationships between followers, following, and blocked accounts.

    Parameters:
    - followers (set): Set of followers.
    - following (set): Set of following accounts.
    - blocked (set): Set of blocked accounts.

    Returns:
    - Tuple containing five sets:
        Accounts followed but not following back.
        Accounts that follow back.
        Accounts that follow but are not followed back.
        Accounts that block me (if known).
        Accounts I have blocked.
    """
    followers_set = set(followers)
    following_set = set(following)
    blocked_set = set(blocked)

    not_following_back = following_set - followers_set
    mutual_followers = following_set & followers_set
    not_following_back_me = followers_set - following_set
    blocked_me = blocked_set - following_set
    
    return not_following_back, mutual_followers, not_following_back_me, blocked_me, blocked_set

#following_path = r'C:\Users\Rhea Tulod\Downloads\start_here.html\connections\followers_and_following\following.html'
followers_path= r'C:\Users\Rhea Tulod\Downloads\start_here.html\connections\followers_and_following\followers_1.html'
following_path= "my_html_file.html"

"C:\Users\Rhea Tulod\Downloads\start_here.html\connections\followers_and_following"
followers, following, blocked = extract_accounts_from_html(following_path, followers_path)

print("Followers:", followers)
print("Following:", following)
print("Blocked accounts:", blocked)
not_following_back, mutual_followers, not_following_back_me, blocked_me, blocked_set = analyze_relationships(followers, following, blocked)

print("Accounts I follow but they don't follow me back:", not_following_back)
print("Accounts I follow and they also follow me back:", mutual_followers)
print("Accounts follow me but I don't follow them:", not_following_back_me)
print("Accounts that block me:", blocked_me)
print("Accounts that I have blocked:",blocked_set)