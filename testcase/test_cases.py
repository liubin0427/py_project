import pytest


class Test:

    age=16

    def test_login(self, aaa):
        print('-----'+str(aaa))

    @pytest.mark.moke
    def test_logout(self, aaa):
        print('logout')

    @pytest.mark.skip(reason="太好看-跳过")
    def test_operate(self):
        print("被跳过")
    @pytest.mark.skipif(age>18,reason="有条件")
    def test_operate1(self):
        print("被执行")
    def test_fail_rerun(self):
        assert 1==2