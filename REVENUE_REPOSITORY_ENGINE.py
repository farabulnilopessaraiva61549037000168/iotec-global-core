from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class RevenueRepository:

    repositories: Dict[str, Any]


class RevenueRepositoryEngine:

    def __init__(self):

        self.repositories: Dict[str, Dict[str, Any]] = {}

    def create(self, name):

        if name not in self.repositories:

            self.repositories[name] = {}

    def save(self, repository, key, value):

        self.create(repository)

        self.repositories[repository][key] = value

    def load(self, repository, key):

        if repository not in self.repositories:

            return None

        return self.repositories[repository].get(key)

    def exists(self, repository):

        return repository in self.repositories

    def repository_count(self):

        return len(self.repositories)

    def object_count(self):

        total = 0

        for repo in self.repositories.values():

            total += len(repo)

        return total


if __name__ == "__main__":

    repository = RevenueRepositoryEngine()

    print("=" * 70)

    print("REVENUE REPOSITORY ENGINE")

    print("=" * 70)

    print("REPOSITORIES :", repository.repository_count())

    print("OBJECTS      :", repository.object_count())

