from typing import List
from git import Head
from enum import Enum

class BranchStatus(Enum):
    Sync = 1
    NotSync = 2
    Behind = 4
    MergedAndDeleted = 5

class GitBranch:

    @staticmethod
    def branches_to_clean(base_branch, repo) -> List[Head]:
        return [
            branch
            for branch in repo.branches
            if (
                GitBranch.has_commit_in_base(base_branch, branch) and
                not GitBranch.is_base_remote(base_branch, branch, repo) and
                not GitBranch.is_current_branch(branch, repo)
            )
        ]

    @staticmethod
    def is_base_remote(base_branch, branch, repo):
        for remote in repo.remotes:
            name = f"{remote.name}/{branch.name}"
            if name == base_branch.name:
                return True
        return False

    @staticmethod
    def is_current_branch(branch, repo):
        return GitBranch.branch_name(repo.head) == branch.name

    @staticmethod
    def has_commit_in_base(base_branch, branch):
        commit = branch.commit
        tree = base_branch.commit
        for item in tree.traverse():
            if item.hexsha == commit.hexsha:
                return True

        return False

    @staticmethod
    def branch_name(branch):
        try:
            return branch.reference.name
        except:
            return "Detached Head"
