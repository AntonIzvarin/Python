import requests


class YougileProjectsClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def create_project(self, payload: dict) -> requests.Response:
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id: str) -> requests.Response:
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )

    def update_project(
        self, project_id: str, payload: dict
    ) -> requests.Response:
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json=payload,
            headers=self.headers
        )
