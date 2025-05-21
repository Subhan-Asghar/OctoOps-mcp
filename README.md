<h1 align="center">🚀 OctoOps: GitHub Automation Agent via MCP Server</h1>

<p align="center">
  <b>OctoOps</b> is a lightweight, prompt-driven <code>MCP</code> server agent that automates GitHub operations such as repository and branch management, cloning, archiving, and file handling — all triggered through natural language tools.
</p>

<hr />

<h2>🧠 Features</h2>

<ul>
  <li>🔐 <strong>Secure GitHub Authentication</strong> using Personal Access Tokens</li>
  <li>📂 <strong>Clone Repositories</strong> to local directories</li>
  <li>📝 <strong>List, Create, and Delete</strong> Repositories</li>
  <li>🌿 <strong>Branch Management:</strong> List, Create, and Delete branches</li>
  <li>📁 <strong>Delete Files</strong> from specific branches</li>
  <li>📦 <strong>Archive or Unarchive</strong> repositories</li>
  <li>🚚 <strong>Transfer Ownership</strong> of repositories</li>
</ul>

<h2>📦 Installation</h2>

```bash
git clone https://github.com/your-username/octoops.git
cd octoops
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

<h2>🔑 Environment Setup</h2>
Create a .env file in the root directory:
<pre> <code> GITHUB_TOKEN=your_personal_access_token_here </code> <pre>
<h2>⚙️ Available MCP Tools</h2>