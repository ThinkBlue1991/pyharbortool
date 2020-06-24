import requests


class HarborClient(object):
    def __init__(self, host, user, password, protocol="http"):
        self._host = host
        self._user = user
        self._password = password
        self._protocol = protocol

        self._session_id = self._login()

    def _login(self):
        try:
            if self._protocol == "https":
                login_data = requests.post("{0}://{1}/c/login".format
                                           (self._protocol, self._host),
                                           data={'principal': self._user,
                                                 'password': self._password})
            else:
                login_data = requests.post("{0}://{1}/login".format
                                           (self._protocol, self._host),
                                           data={'principal': self._user,
                                                 'password': self._password})
            if login_data.status_code == 200:
                session_id = login_data.cookies.get('sid')
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

    def delete_repository(self, repo_name, tag='latest'):
        try:
            url = "{0}://{1}/api/repositories/{2}/tags/{3}".format(
                self._protocol,
                self._host,
                repo_name,
                tag)
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
        try:
            url = "{0}://{1}/api/projects?page={2}&page_size={3}".format(
                self._protocol, self._host, page, page_size)

            response = requests.get(url, cookies={'sid': self._session_id})

            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag

        except Exception as ex:
            print(ex)
            return None

    def get_repositories_by_project_id(self, page, page_size, project_id):
        try:
            url = "{0}://{1}/api/repositories?page={2}&page_size={3}&project_id={4}".format(
                self._protocol, self._host, page, page_size, project_id)

            response = requests.get(url, cookies={'sid': self._session_id})

            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag

        except Exception as ex:
            print(ex)
            return None

    def get_repository_info(self, project_id, repo_name):
        try:
            url = "{0}://{1}/api/repositories?project_id={2}&q={3}".format(
                self._protocol, self._host, project_id, repo_name)

            response = requests.get(url, cookies={'sid': self._session_id})

            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag

        except Exception as ex:
            print(ex)
            return None

    def get_tags(self, repo_name, detail=1):
        try:
            url = "{0}://{1}/api/repositories/{2}/tags?detail={3}".format(
                self._protocol, self._host, repo_name, detail)

            response = requests.get(url, cookies={'sid': self._session_id})

            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag

        except Exception as ex:
            print(ex)
            return None

    def get_tag_info(self, repo_name, tag):
        try:
            url = "{0}://{1}/api/repositories/{2}/tags/{3}".format(
                self._protocol,
                self._host,
                repo_name,
                tag)
            response = requests.get(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag
        except Exception as ex:
            print(ex)
            return None

    def get_manifest(self, repo_name, tag):
        try:
            url = "{0}://{1}/api/repositories/{2}/tags/{3}/manifest".format(
                self._protocol,
                self._host,
                repo_name,
                tag)
            response = requests.get(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag
        except Exception as ex:
            print(ex)
            return None

    def get_users(self):
        try:
            url = "{0}://{1}/api/users".format(self._protocol, self._host)
            response = requests.get(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = response.json()
            else:
                flag = None
            return flag
        except Exception as ex:
            print(ex)
            return None

    def get_logs(self, page, page_size):
        try:
            url = "{0}://{1}/api/logs?page={2}&page_size={3}".format(
                self._protocol, self._host, page, page_size)
            response = requests.get(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = response.json()
            else:
                flag = False
            return flag
        except Exception as ex:
            print(ex)
            return False

    def get_statistics(self):
        try:
            url = "{0}://{1}/api/statistics".format(self._protocol, self._host)
            response = requests.get(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = response.json()
            else:
                flag = False
            return flag
        except Exception as ex:
            print(ex)
            return False

    def create_project(self, project_info: dict):
        try:
            url = "{0}://{1}/api/projects".format(self._protocol, self._host)
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
            url = "{0}://{1}/api/projects/{2}".format(self._protocol,
                                                      self._host, project_id)
            response = requests.delete(url, cookies={'sid': self._session_id})
            if response.status_code == 200:
                flag = True
            else:
                flag = False
            return flag
        except Exception as ex:
            print(ex)
            return False
