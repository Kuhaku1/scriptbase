from {{cookiecutter.package_name}}.services import user_service


class TestUserService:

    def test_get_user_by_id(self):
        user = user_service.get_user_by_id(5)
        assert user.get("id") == 5
