import os
import yaml
import re
import shutil


def read_blog_meta():
    """
    读取blog_meta.yml文件，获取博客目录和中文标题的映射关系
    """
    with open('docs/blog/blog_meta.yml', 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def process_markdown_files(blog_dir):
    """
    读取blog目录下的所有markdown文件，提取元数据，并过滤掉以下划线开头的文件夹
    """
    blog_posts = []
    for root, dirs, files in os.walk(blog_dir):
        # 过滤掉以下划线开头的文件夹
        dirs[:] = [d for d in dirs if not d.startswith('_')]

        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    metadata = extract_metadata(content)
                    if metadata:
                        metadata['file_path'] = os.path.relpath(file_path, blog_dir)
                        metadata['date'] = file[:8]
                        blog_posts.append(metadata)
                        update_markdown_tags(file_path, metadata)
    return sorted(blog_posts, key=lambda x: x['date'], reverse=True)


def extract_metadata(content):
    """
    从markdown文件内容中提取元数据
    """
    metadata = {}
    match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
    if match:
        metadata_text = match.group(1)
        try:
            metadata = yaml.safe_load(metadata_text)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML metadata: {e}")
    return metadata


def update_markdown_tags(file_path, metadata):
    """
    更新markdown文件中的标签信息
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 检查是否存在标签行
    tag_line = f"标签：{', '.join([f'[{tag}](../../_tags/{tag})' for tag in metadata['tag']])}"
    tag_pattern = r'标签：.*'

    if re.search(tag_pattern, content):
        # 如果存在标签行，更新它
        content = re.sub(tag_pattern, tag_line, content)
    else:
        # 如果不存在标签行，在元数据后面添加
        content = re.sub(r'---\n(.*?)\n---', f'---\n\1\n---\n\n{tag_line}', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def generate_tag_pages(blog_posts):
    """
    生成标签索引页面
    """
    tags_dir = 'docs/blog/_tags'
    if os.path.exists(tags_dir):
        shutil.rmtree(tags_dir)
    os.makedirs(tags_dir, exist_ok=True)

    tag2posts = {}
    for post in blog_posts:
        if 'tag' in post:
            for tag in post['tag']:
                tag = tag.strip()
                if not tag:
                    continue
                if tag not in tag2posts:
                    tag2posts[tag] = []
                tag2posts[tag].append(post)

    for tag, posts in tag2posts.items():
        with open(f'docs/blog/_tags/{tag}.md', 'w', encoding='utf-8') as f:
            f.write(f'# {tag}\n\n')
            for post in posts:
                f.write(f"## [{post['title']}]({os.path.relpath(post['file_path'], '_tags')})\n\n")
                if 'summary' in post:
                    f.write(f"> {post['summary']}\n\n")
                f.write('----\n\n')


def update_mkdocs_nav(title_map, blog_posts):
    """
    更新mkdocs.yml文件中的nav部分
    """
    with open('mkdocs.yml', 'r', encoding='utf-8') as file:
        mkdocs_config = yaml.safe_load(file)

    nav = mkdocs_config['nav']
    blog_index = next(i for i, item in enumerate(nav) if '笔记' in item)

    new_nav = {category: [] for category in title_map.keys()}
    for post in blog_posts:
        category = os.path.dirname(post['file_path'])
        if category in new_nav:
            new_nav[category].append({post['title']: os.path.join("blog", post['file_path'])})

    nav[blog_index]['笔记'] = [{title_map[category]: items} for category, items in new_nav.items() if items]

    with open('mkdocs.yml', 'w', encoding='utf-8') as file:
        yaml.dump(mkdocs_config, file, allow_unicode=True)


def main():
    """
    主函数，协调整个脚本的执行
    """
    blog_meta = read_blog_meta()
    blog_posts = process_markdown_files('docs/blog')
    generate_tag_pages(blog_posts)
    update_mkdocs_nav(blog_meta['TITLE'], blog_posts)


if __name__ == "__main__":
    main()
