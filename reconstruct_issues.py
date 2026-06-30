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
    issue_files = sorted(glob.glob("data/raw/issues_*.json"))
    comment_files = sorted(glob.glob("data/raw/comments_*.json"))

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

    toc_lines = ["# Index of Issues\n\n"]

    # Sort issues by number for consistent TOC and processing
    all_issues.sort(key=lambda x: x['number'])

    for issue in all_issues:
        number = issue['number']
        title = issue['title']
        slug = slugify(title)
        dir_name = f"{number}-{slug}"
        dir_path = os.path.join("issues", dir_name)

        # Remove old directory structure if it exists to clean up README.md/comments.md
        if os.path.exists(dir_path):
            for f in os.listdir(dir_path):
                os.remove(os.path.join(dir_path, f))
        else:
            os.makedirs(dir_path, exist_ok=True)

        filename = f"{slug}.md"
        filepath = os.path.join(dir_path, filename)

        # Lossless content reconstruction: No headers, no metadata.
        content = issue['body'] or ""

        issue_comments = comments_by_issue.get(issue['url'], [])
        issue_comments.sort(key=lambda x: x['created_at'])

        if issue_comments:
            content += "\n\n---\n\n"
            for i, comment in enumerate(issue_comments):
                content += comment['body'] or ""
                if i < len(issue_comments) - 1:
                    content += "\n\n---\n\n"

        with open(filepath, "w") as f:
            f.write(content)

        toc_lines.append(f"- [#{number} {title}](issues/{dir_name}/{filename})\n")

    with open("ISSUES.md", "w") as f:
        f.writelines(toc_lines)

    print(f"Reconstructed {len(all_issues)} issues into lossless format. Updated ISSUES.md.")

if __name__ == "__main__":
    process_data()
