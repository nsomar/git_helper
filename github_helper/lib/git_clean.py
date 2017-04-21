import subprocess
from typing import List
from git import Repo, Head
import click
import arrow
from .print_helpers import print_error, print_success, print_warning
from .git_branch import GitBranch, BranchStatus
from .common import exec_command

Branches = List[Head]

def execute(path: str, branch_name: str):
    repo = Repo(path)
    base_branch = get_branch(repo, branch_name)

    if base_branch is None:
        print_error("Branch not found")
        exit(1)

    branches = GitBranch.branches_to_clean(base_branch, repo)
    delete_branches(branches)

def delete_branches(branches: List[Head]):
    if branches == []:
        print_success("No branches to delete")
        return

    click.echo(f"👀  ({len(branches)}) branches that can be deleted:")
    [print_branch_info(x) for x in branches]

    if click.confirm(delte_branch_message(branches)):
        print_warning('Deleting branches')
        execute_delete(branches)

def print_branch_info(branch: Head):
    click.echo(f"\n- {branch.name}")
    print("  " + branch.commit.message.strip())
    date = arrow.get(branch.commit.committed_date)
    print("  " + date.format("YYYY-MMM-DD HH:mm"))

def delte_branch_message(branches: List[Head]):
    return "\n".join([
        "\n🔥  Deleting the branches?",
        "",
        "This will execute:"
    ] + [
        f"git branch -d {branch.name}"
        for branch in branches
    ] + [
        "",
        "Proceed?"
    ])

def execute_delete(branches: List[Head]):
    for branch in branches:
        exec_command([
            "git", "branch", "-d", branch.name
        ])

def get_branch(repo, name) -> Head:
    branch = local_branch(repo, name)
    if branch is None:
        branch = remote_branch(repo, name)
    return branch

def local_branch(repo, name) -> Head:
    for branch in repo.branches:
        if branch.name == name:
            return branch
    return None

def remote_branch(repo, name) -> Head:
    for remote in repo.remotes:
        for branch in remote.refs:
            if branch.name == name:
                return branch
    return None


def branches_status(repo: Repo, base_branch: Head) -> Branches:
    return [
        GitBranch(branch, base_branch, repo)
        for branch in repo.branches
    ]

def branches_to_delete(branches: Branches) -> Branches:
    return [
        branch
        for branch in branches
        if (
            branches == BranchStatus.Behind or
            branches == BranchStatus.Sync
        )
    ]

