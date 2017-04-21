from git import Repo, Remote, RemoteProgress
from .common import exec_command
from .print_helpers import print_warning


def execute(path: str):
    repo = Repo(path)
    for remote in repo.remotes:
        clean_remote(remote)

def clean_remote(remote: Remote):
    print_warning(f"Fetching {remote.name}, {remote.url}")
    remote.fetch()
    for branch in remote.refs:
        print(branch)
