---
hide:
  - toc
  - navigation
---

<style>
body {
    font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif;
    line-height: 1.5;
    color: #3f4d5a;
    background-color: #ffffff;
}

h1, h2, h3 {
    color: #3f4d5a;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

.header {
    text-align: center;
    padding: 40px 0 20px;
}

.header h1 {
    font-size: 2.8rem;
    margin-bottom: 0.5rem;
    color: #3f4d5a;
}

.header p {
    font-size: 1.1rem;
    color: #6c757d;
}

.projects-section {
    background-color: #f5f5f5;
    padding: 30px;
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.16);
    margin-top: 20px;
}

.projects-section h2 {
    text-align: center;
    margin-bottom: 25px;
    margin-top: 0px;
    color: #3f4d5a;
    font-size: 1.5rem;
    font-weight: 400;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

.feature {
    background-color: #ffffff;
    border-radius: 5px;
    padding: 20px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.06);
}

.feature:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.feature h3 {
    font-size: 1.2rem;
    margin-top: 0;
    margin-bottom: 10px;
    color: #2980b9;
}

.feature p {
    margin-bottom: 0;
    color: #6c757d;
    font-size: 0.95rem;
}

.feature a {
    text-decoration: none;
    color: inherit;
    display: block;
}

@media (max-width: 768px) {
    .feature {
        flex-basis: 100%;
    }
}
</style>

<div class="container">
    <div class="header">
        <h1>欢迎来到 1/2 站台</h1>
        <p>这是一个用于记录一些技术文档的站台，主要包括我的一些笔记和开源项目</p>
    </div>

    <div class="projects-section">
        <h2>我的项目</h2>
        <div class="features">
            <div class="feature">
                <a href="https://inchdance.github.io/">
                    <h3>寸草舞集</h3>
                    <p>上海接触即兴社群活动的主要组织方和上海即兴艺术节的联合主办方，这是一个位于上海致力于后现代剧场的创作与演出，并于日常定期开设接触即兴、肢体开发等课程的艺术团体。</p>
                </a>
            </div>
            <div class="feature">
                <a href="https://github.com/zeropoint5/whisper-api-tool">
                    <h3>Whisper 字幕工具</h3>
                    <p>利用 OpenAI 的 Whisper 模型把音视频转 SRT 字幕的工具</p>
                </a>
            </div>
            <div class="feature">
                <a href="https://github.com/zeropoint5/ai_make_money">
                    <h3>AI 领域的创业公司</h3>
                    <p>一些 AI 领域的创业公司整理</p>
                </a>
            </div>
            <div class="feature">
                <a href="https://zeropoint5.github.io/arxiv_tracker/">
                    <h3>ArXiv Tracker</h3>
                    <p>自动跟踪和总结 arXiv 上特定领域的最新研究论文</p>
                </a>
            </div>
        </div>
    </div>
</div>