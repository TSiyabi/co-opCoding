import os
import subprocess
import shutil
import random
from pathlib import Path

BASE_DIR = Path("git_issues_lab")
ISSUES = []

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"[ERROR] {cmd}\n{result.stderr.decode()}")
    return result.stdout.decode()

def create_base():
    if BASE_DIR.exists():
        shutil.rmtree(BASE_DIR)
    BASE_DIR.mkdir()
    print(f"Created base directory: {BASE_DIR}")

def create_git_repo(name):
    repo_path = BASE_DIR / name
    repo_path.mkdir()
    run("git init", cwd=repo_path)
    Path(repo_path / ".gitignore").write_text("*.log\n")
    Path(repo_path / "README.md").write_text(f"# {name}\n")
    run("git add .", cwd=repo_path)
    run('git commit -m "Initial commit"', cwd=repo_path)
    return repo_path

def issue_committing_multiple_projects_same_branch(repo):
    Path(repo / "project1").mkdir()
    Path(repo / "project2").mkdir()
    Path(repo / "project1" / "app1.py").write_text("print('Project 1')")
    Path(repo / "project2" / "app2.py").write_text("print('Project 2')")
    run("git add .", cwd=repo)
    run('git commit -m "Committing two projects in one branch"', cwd=repo)
    ISSUES.append("Multiple projects committed in same branch")

def issue_committing_in_main_directly(repo):
    Path(repo / "hotfix.py").write_text("print('Hotfix in main')")
    run("git add .", cwd=repo)
    run('git commit -m "Hotfix committed on main"', cwd=repo)
    ISSUES.append("Commits made directly on main branch")

def issue_nested_git_folder(repo):
    nested_repo = repo / "subproject"
    nested_repo.mkdir()
    run("git init", cwd=nested_repo)
    Path(nested_repo / "nested.py").write_text("print('Nested git')")
    run("git add .", cwd=nested_repo)
    run('git commit -m "Nested repo commit"', cwd=nested_repo)
    run("git add .", cwd=repo)
    run('git commit -m "Added nested git repo"', cwd=repo)
    ISSUES.append(".git folder inside another .git")

def issue_branching_from_wrong_branch(repo):
    run("git checkout -b feature1", cwd=repo)
    Path(repo / "feature1.py").write_text("print('Feature 1')")
    run("git add .", cwd=repo)
    run('git commit -m "Add feature 1"', cwd=repo)
    run("git checkout -b feature2", cwd=repo)  # wrongly from feature1
    Path(repo / "feature2.py").write_text("print('Feature 2')")
    run("git add .", cwd=repo)
    run('git commit -m "Add feature 2 from wrong base"', cwd=repo)
    ISSUES.append("Branch created from wrong feature branch instead of main")

def issue_conflicting_changes(repo):
    run("git checkout -b conflictA", cwd=repo)
    Path(repo / "conflict.txt").write_text("Version A\n")
    run("git add .", cwd=repo)
    run('git commit -m "conflict A version"', cwd=repo)

    run("git checkout main", cwd=repo)
    run("git checkout -b conflictB", cwd=repo)
    Path(repo / "conflict.txt").write_text("Version B\n")
    run("git add .", cwd=repo)
    run('git commit -m "conflict B version"', cwd=repo)

    ISSUES.append("Conflicting file changes in different branches")

def issue_committing_ignored_file(repo):
    Path(repo / "debug.log").write_text("log stuff")
    run("git add debug.log", cwd=repo)
    run('git commit -m "Added ignored file"', cwd=repo)
    ISSUES.append("Committed ignored file")

def issue_unmerged_branches(repo):
    run("git checkout -b unmerged", cwd=repo)
    Path(repo / "unmerged.txt").write_text("Unmerged changes")
    run("git add .", cwd=repo)
    run('git commit -m "Unmerged branch changes"', cwd=repo)
    run("git checkout main", cwd=repo)
    ISSUES.append("Created unmerged branch")

def issue_detached_head(repo):
    commit_hash = run("git rev-parse HEAD", cwd=repo).strip()
    run(f"git checkout {commit_hash}", cwd=repo)
    Path(repo / "detached.txt").write_text("In detached state")
    ISSUES.append("HEAD detached from any branch")

def issue_untracked_files(repo):
    Path(repo / "tempfile.tmp").write_text("Temporary file")
    ISSUES.append("Untracked temp file present")

def issue_force_push(repo):
    run("git checkout -b rewrite-history", cwd=repo)
    Path(repo / "rewrite.txt").write_text("First commit")
    run("git add .", cwd=repo)
    run('git commit -m "Rewrite this"', cwd=repo)
    run("git reset --hard HEAD~1", cwd=repo)
    ISSUES.append("Used git reset to rewrite history")

def simulate_issues():
    create_base()
    repo = create_git_repo("broken-repo")
    issue_committing_multiple_projects_same_branch(repo)
    issue_committing_in_main_directly(repo)
    issue_nested_git_folder(repo)
    issue_branching_from_wrong_branch(repo)
    issue_conflicting_changes(repo)
    issue_committing_ignored_file(repo)
    issue_unmerged_branches(repo)
    issue_detached_head(repo)
    issue_untracked_files(repo)
    issue_force_push(repo)

    # Add more simulated issues here as needed...

    print("\n✅ Git issue simulation complete.")
    print("Issues introduced:")
    for i, issue in enumerate(ISSUES, 1):
        print(f"{i:02d}: {issue}")

if __name__ == "__main__":
    simulate_issues()
