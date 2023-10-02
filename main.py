import re

def count_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

        # Count total messages
        messages = data.split('\n')
        total_messages = len(messages)

        # Count media messages
        media_messages = len([msg for msg in messages if '<Media omitted>' in msg])

        # Count links
        link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        links = re.findall(link_pattern, data)
        total_links = len(links)

        return total_messages, media_messages, total_links

# Usage example
file_path = '_chat.txt'  # Replace with the actual file path
total_messages, media_messages, total_links = count_messages(file_path)

print(f'Total Messages: {total_messages}')
print(f'Media Messages: {media_messages}')
print(f'Total Links: {total_links}')


    