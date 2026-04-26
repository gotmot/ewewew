import requests


class GitHubAPI:
    def __init__(self):
        self.base_url = "https://github.com"
        self.headers = {"Accept": "application/vnd.github.v3+json"}

    def _make_request(self, endpoint):
        """Базовый метод для выполнения HTTP-запросов."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers)

            if response.status_code == 404:
                print(f"Ошибка 404: Ресурс не найден по адресу {url} не найден.")
                return None
            elif response.status_code == 403:
                print("Ошибка 403: Превышен лимит запросов (Rate Limit).")
                return None

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при запросе: {e}")
            return None

    def get_user_info(self, username):
        return self._make_request(f"/users/{username}")

    def get_repo_info(self, owner, repo):
        return self._make_request(f"/repos/{owner}/{repo}")

if __name__ == "__main__":
    gh = GitHubAPI()

    print("Запрос информации о пользователе...")
    user_info = gh.get_user_info("torvalds")
    if user_info:
        print(f"Пользователь: {user_info['login']}, Имя: {user_info.get('name', 'не указано')}")

    print("-" * 20)

    print("Запрос информации о репозитории...")
    repo_info = gh.get_repo_info("torvalds", "linux")
    if repo_info:
        print(f"Репозиторий: {repo_info['name']}, Описание: {repo_info.get('description', 'нет описания')}")

    print("-" * 20)
    print("Тест ошибки 404:")
    gh.get_user_info("this_user_does_not_exist_123456789")
