import json
import os
import re
import glob

def slugify(text):
    text = (text or "no-title").lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text[:50] or "issue"

def reconstruct():
    issue_files = sorted(glob.glob("data/raw/issues_page_*.json"))
    all_issues = []
    for f_path in issue_files:
        with open(f_path, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                all_issues.extend(data)

    # Sort by number
    all_issues.sort(key=lambda x: x['number'])

    for issue in all_issues:
        number = issue['number']
        title = issue['title']
        slug = slugify(title)
        dir_name = f"{number}-{slug}"
        dir_path = os.path.join("issues", dir_name)
        os.makedirs(dir_path, exist_ok=True)

        filename = f"{slug}.md"
        filepath = os.path.join(dir_path, filename)

        # Build content with metadata
        content = "---\n"
        content += f"title: \"{title}\"\n"
        content += f"number: {number}\n"
        content += f"author: {issue['user']['login']}\n"
        content += f"created_at: {issue['created_at']}\n"
        content += f"updated_at: {issue['updated_at']}\n"
        labels = [l['name'] for l in issue.get('labels', [])]
        content += f"labels: {labels}\n"
        content += "---\n\n"

        content += (issue['body'] or "") + "\n"

        # Add comments if available
        comments_file = f"data/raw/comments_issue_{number}.json"
        if os.path.exists(comments_file):
            try:
                with open(comments_file, "r") as f:
                    comments = json.load(f)
                for comment in comments:
                    content += "\n---\n"
                    content += f"### Comment by {comment['user']['login']} at {comment['created_at']}\n\n"
                    content += (comment['body'] or "") + "\n"
            except:
                pass

        with open(filepath, "w") as f:
            f.write(content)

    print(f"Reconstructed {len(all_issues)} issues.")

if __name__ == "__main__":
    reconstruct()
