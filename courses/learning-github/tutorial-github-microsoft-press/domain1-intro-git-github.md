# Domain 1: Introduction to Git and GitHub (22%)
---
# Lesson 1: Git Basics
---
## Describe version control and distributed version control
- Version control allows developers or collaborators to track changes to plain text or source code files
- Facilitates collaboration in development
- Distributed version control, (Git), everyone can have a copy or clone of a repo, Rapid and asynchronous
## Describe Git
- Open source version control software, VCS, created by Linus Torvalds 
## Describe GitHub
- Comprehensive hybrid cloud development platform, facilitating project management, issue tracking, code review, and CI/CD
- Users enjoy a robust AI-enhanced SDLC
- Access methods: REST API, web UI, mobile app, gh CLI
## Compare Git and GitHub
- Git is distributed system for handling version control, 100% free and open-source
- GitHub is platform that enhances Git with collaboration features
- Proprietary, closed-source software 
- Free open source software (GitHub CLI)
# Lesson 2: GitHub Basics
---
## Describe a Git repository
- A repo is a storage space for project files and version history
- Supports collaboration by tracking every text change
- 3 repo visibilities: public, internal, private
## Describe a commit
- A commit is a snapshot of your project at a specific point in time
- Includes a message describing what has changed and why
- Commits help with tracking history, enabling devs to roll back in time
- Every commit has a unique hash to track specific changes
- Standard is to use present tense
## Describe branching
- Allow developers to work on different features, bug fixes, or experiments independently from the main codebase
- Default branch is called main or master
- Create a new branch to isolate changes and prevent overwrites
- Helps avoid disruption in the main branch while allowing expermimentation
## Define a remote
- A remote is your version of your project hosted on GitHub
- Local repo is your copy on your machine, and remotes help synchronize with other team members
- **origin**: the default name for your GitHub remote when you clone a repo
- **upstream**: Used when your repository is a fork. It refers to the original repo from which your fork was made
- Common operations, git push, git pull, best practice; allows pull before you push
- Add a remote repo, git remote add https://github.com/user-name/repo.git
## Describe the GitHub flow
- A lightweight, branch-based workflow to streamline collaboration
- Key steps: Create a branch, Commit, changes, Open a pull request (PR), team members can review and discuss PR
- After approval, the branch is merged into the main branch
- The main branch is ready for deployment
# Lesson 3: GitHub Entities
---
## Describe the different GitHub acounts
- **Personal Accounts**: Individual users, free and paid plans, access to public and private repos
- **Organizations**: Teams and companies, Shared account by a separate GitHub entity, centralized management, advanced security features, billing and invoicing
## Describe GitHub's products for personal accounts
- **GitHub Free**: Public repos, limited private repos, basic collab tools
- **GitHub Pro**: Unlimited private repos, advanced collab tools, code review features
- **GitHub Team**: All feats of pro, plus team management tools and organization insights
## Describe GitHub's products for organization accounts
- **GitHub Team**: Same feats as personal plan, plus organization-wide management
- **GitHub Enterprise Cloud**: Advanced security and compliance, self-hosted runners, dedicated support
- **GitHub Enterprise Server**: On-premises deployment, full control over data and infrastructure
## Describe user profile features
- **Profile picture and bio**: Personalize your profile
- **Pinned Repositories**: Showcase your best work
- **Contributions graph**: Visualize your activity
- **Achievements**: Highlight your accomplishments
## Describe GitHub enterprise's deployment options
- **GitHub Enterprise** is the overall product name
- **GitHub Enterprise Cloud**: Hosted on GitHub's infrastructure, easy setup and maintanence, Called GHEC
- **GitHub Enterprise Server**: Deployed on your own servers, full control over data and security, Called GHES, you can deploy in a cloud
# Lesson 4: GitHub Markdown
---
## Describe markdown
- Lightweight markup language
- Plain-text formatting syntax
- Easy to read and write
- Renders to HTML
- Extends standard Markdown with a few key features thaht enhance its functionality with the GH ecosystem
- Ex. @, autoconvert URLs and email addrs into links
- `code` fencing
## Identify GitHub basic formatting syntax
- **Headers**: #, ##, ###
- **Emphasis**: _italics_, **bold**
- **Lists**: -, 1
- **Links**: [link text](URL)
- **Images**: ![alt text](image URL)
## Identify the text formatting toolbar on issue and pull request comments
- Located in **Issue** and **Pull Request**comment boxes
- Provides visual buttons for common formatting
- Can toggle between visual editor and Markdown code
## Explain where to find and use slash commands
- Type / to trigger
- Quick access to formatting and actions
- Available in issues, PRs, and discussion
- /label
- /assign
- /close
# Lesson 5: GitHub Desktop
---
## Explain the difference between GitHub desktop and GitHub.com
- **GitHub Desktop**: A local client for managing repos on your machine
- FOSS, cross-platform desktop app written in TypeScript and Electron - Collaboration only
- **GitHub.com**: Cloud-hosted platform for sharing repositories and collaborating with others
- Proprietary with FOSS components, written in Ruby on Rails, TypeScript, Golang, React - Collaboration and development
## Describe the available features with GitHub desktop
- **Branching and merging**: Visualize and merge branches easily
- **Conflict resolution**: Resolve merge conflicts using simple UI
- **Pull Requests and Issues**: Seamless integration with GitHub for creating and managing PRs
## Describe the available features with GitHub mobile
- Closed-source, proprietary GitHub client available for iOS and Android
- **Pull requests and issues**: Review, comment on, and merge pull requests, track and manage issues across projects
- **Real-time notifications**: Stay updated with alerts for new commits, PR reviews, and more
- **Repository browsing**: Navigate through files, code, and commit histories withing any repo
- **Copilot chat**: Ask questions about code, generate solutions, and review suggestions from more than 100,000 repos
## Explain how to manage notifications through the GitHub Mobile app
- **Customizable notifications**: Adjust preferences for specific repos or threads
- **Inbox management**: Organize and act on notifications efficiently
- **In-app actions**: Reply to comments or close issues directly from the notification center
