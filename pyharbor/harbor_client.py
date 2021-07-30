import requests


class HarborClient(object):
    def __init__(self, host, user, password, protocol="http", api_path="api"):
        self._host = host
        self._user = user
        self._password = password
        self._protocol = protocol
        self._base_path = "{0}://{1}/{2}".format(protocol, host, api_path)

        self._session_id = self._login()

    def _login(self):
        try:
            if self._protocol == "https":
                info = requests.post("{0}://{1}/c/login".format
                                     (self._protocol, self._host),
                                     data={'principal': self._user,
                                           'password': self._password})
            else:
                info = requests.post("{0}://{1}/login".format
                                     (self._protocol, self._host),
                                     data={'principal': self._user,
                                           'password': self._password})
            if info.status_code == 200:
                session_id = info.cookies.get('sid')
                return session_id
            else:
                return None
        except Exception as ex:
            print(ex)
            return None

    def __str__(self):
        return "Harbor Client: Host:{0},User:{1},Password:{2}".format(
            self._host,
            self._user,
            self._password)

    @property
    def host(self) -> str:
        return self._host

    @host.setter
    def host(self, host: str):
        self._host = host

    @property
    def user(self) -> str:
        return self._user

    @user.setter
    def user(self, user: str):
        self._user = user

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def protocol(self) -> str:
        return self._protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self._protocol = protocol

    def _get_request(self, url):
        try:
            response = requests.get(url, cookies={'sid': self._session_id})

            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag

        except Exception as ex:
            print(ex)
            return None

    def delete_repository(self, repo_name, tag='latest'):
        try:
            url = "{0}/repositories/{1}/tags/{2}".format(
                self._base_path, repo_name, tag)

            response = requests.delete(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = True
            else:
                flag = False
            return flag
        except Exception as ex:
            print(ex)
            return False

    def get_projects(self, page, page_size):
        url = "{0}/projects?page={1}&page_size={2}".format(
            self._base_path, page, page_size)

        return self._get_request(url)

    def get_repositories_by_project_id(self, page, page_size, project_id):
        url = "{0}/repositories?page={1}&page_size={2}&project_id={3}".format(
            self._base_path, page, page_size, project_id)

        return self._get_request(url)

    def get_repository_info(self, project_id, repo_name):
        url = "{0}/repositories?project_id={1}&q={2}".format(
            self._base_path, project_id, repo_name)

        return self._get_request(url)

    def get_tags(self, repo_name, detail=1):
        url = "{0}/repositories/{1}/tags?detail={2}".format(
            self._base_path, repo_name, detail)

        return self._get_request(url)

    def get_tag_info(self, repo_name, tag):
        url = "{0}/repositories/{1}/tags/{2}".format(
            self._base_path, repo_name, tag)

        return self._get_request(url)

    def get_manifest(self, repo_name, tag):
        url = "{0}/repositories/{1}/tags/{2}/manifest".format(
            self._base_path, repo_name, tag)

        return self._get_request(url)

    def get_users(self):
        url = "{0}/users".format(self._base_path)

        return self._get_request(url)

    def get_logs(self, page, page_size):
        url = "{0}/logs?page={1}&page_size={2}".format(
            self._base_path, page, page_size)

        return self._get_request(url)

    def get_statistics(self):
        url = "{0}/statistics".format(self._base_path)

        return self._get_request(url)

    def create_project(self, project_info: dict):
        try:
            url = "{0}/projects".format(self._base_path)
            response = requests.post(url, json=project_info,
                                     cookies={'sid': self._session_id})

            if response.status_code == 200:
                flag = True
            else:
                flag = False
            return flag
        except Exception as ex:
            print(ex)
            return False

    def delete_project(self, project_id: int):
        try:
            url = "{0}/projects/{1}".format(self._base_path, project_id)
            response = requests.delete(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = True
            else:
                flag = False
            return flag
        except Exception as ex:
            print(ex)
            return False
