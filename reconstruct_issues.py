import json
import os
import re
import glob

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text[:50]

def process_data():
    issue_files = glob.glob("data/raw/issues_*.json")
    comment_files = glob.glob("data/raw/comments_*.json")

    all_issues = []
    for f_path in issue_files:
        with open(f_path, "r") as f:
            all_issues.extend(json.load(f))

    all_comments = []
    for f_path in comment_files:
        with open(f_path, "r") as f:
            all_comments.extend(json.load(f))

    # Group comments by issue_url
    comments_by_issue = {}
    for comment in all_comments:
        issue_url = comment['issue_url']
        if issue_url not in comments_by_issue:
            comments_by_issue[issue_url] = []
        comments_by_issue[issue_url].append(comment)

    for issue in all_issues:
        number = issue['number']
        title = issue['title']
        slug = slugify(title)
        dir_name = f"{number}-{slug}"
        dir_path = os.path.join("issues", dir_name)
        os.makedirs(dir_path, exist_ok=True)

        # README.md (Issue Body)
        readme_content = f"# #{number} {title}\n\n"
        readme_content += f"**State:** {issue['state']}\n"
        readme_content += f"**Created at:** {issue['created_at']}\n"
        readme_content += f"**User:** {issue['user']['login']}\n\n"
        readme_content += issue['body'] or ""

        with open(os.path.join(dir_path, "README.md"), "w") as f:
            f.write(readme_content)

        # comments.md
        issue_comments = comments_by_issue.get(issue['url'], [])
        issue_comments.sort(key=lambda x: x['created_at'])

        if issue_comments:
            comments_content = f"# Comments for #{number} {title}\n\n"
            for comment in issue_comments:
                comments_content += f"## Comment by {comment['user']['login']} at {comment['created_at']}\n\n"
                comments_content += comment['body'] or ""
                comments_content += "\n\n---\n\n"

            with open(os.path.join(dir_path, "comments.md"), "w") as f:
                f.write(comments_content)

    print(f"Reconstructed {len(all_issues)} issues using {len(issue_files)} issue files and {len(comment_files)} comment files.")

if __name__ == "__main__":
    process_data()
