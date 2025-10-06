# Domain 2: Working with GitHub Repositories (8%)
---
# Lesson 6: Maintain GitHub Repositories
---
## Explain how to create a new repository
- **On GitHub.com**:
  - Click the + in the top-right corner and select **New Repository**
  - Enter a repo name and description
  - Choose between **public** (visible to everyone) **internal** (org access), or **private** (limited access)
  - Optionally, inlcude README.md, .gitignore, or LICENSE
  - Click **Create repository**
- **Using GitHub CLI**:
  - `gh repo create [repo name]`
## Describe the components of a good README and the recommended repository files
- Community health files available at the repo, org, and enterprise level
- Can be centralized at the org level using a .github repo
- Enterprise admins can apply governance across all orgs
- Repo-specific files override org-level defaults
- No centralized health files for personal user accounts; managed per repo
- **Project title and description**: Clearly explain what the project about
- **Installation instructions**: Guide users on how to set up and run the project
- **Usage examples**: Demonstrate how to use the project with code snippets or screenshots
- **Contributing guidelines**: Explain how others can contribute to the project
- **License information**: Specify the open-source license used
## Explain basic repository navigation
- Tab structure - Code - Issues - PR - Actions - Projects - Wiki - Security - Insights - Settings
## Describe repository templates
- Pre-configured repos that provide a starting point for new projects
- Saves time by providing a structure for new projects
- Ensures consistency across projects
- Includes essential files like authorized repo metadata files and a solid README.md
- Creating and using
  - Create a template repo and mark it as template
  - When creating a new repo, select the template from the list
## Describe the different features to maintaining a repository
- **Managing issues and PRs**:
  - Review, comment, label, assign, and merge/close issues and PRs
- **Updating Project Boards and Milestones**:
  - Use project boards to visually track and manage tasks
  - Set milestones to organize work into phases or releases
- **Keeping the repo current**:
  - make regular commits
  - Merge conflicts from collaborators
  - Resolve conflicts when they occur
- **Archiving or deleting**:
  - Archive repos that are no longer actively deployed but need to be preserved
# Lesson 7: Manage GitHub Repositories
---
## Describe how to clone a repository
- Click code tab and under local, clone with HTTPS, SSH, GH CLI
## Describe how to create a new branch
- Click the main branch tab
- `git branch <branch-name>`
- `git checkout -b <branch-name>`
## Explain how to add files to a repository
- Create a new file, stage, commit, push
## Explain how to save a repository with stars
- Starring a repo on GitHub is a way to:
  - Bookmark repos you find interesting or helpful
  - Let the repo owner know that their project is appreciated
  - `gh repo star <repo>`
## Explain feature previews
- **Alpha**: Product or feature under active development
  - No SLAs or tech support
- **Beta**: Product or feature is ready for wider distribution
  - Public or private
  - No SLAs or tech support
- **General availability**: Product or feature is fully tested and available publicly
  - SLA and support
## Identify how to view repository insights
- Insights help repo owners and contributers understand the health and activity of a project
- Insights are available directly in the repo interface
- Include metrics such as traffic, commits, code frequency, and more
