#!/usr/local/bin/python3

import os
import time
from selenium import webdriver
from getpass import getpass

# profile = webdriver.FirefoxProfile()
# profile.default_preferences['webdriver_assume_untrusted_issuer'] = False
# profile.update_preferences()
# profile.accept_untrusted_certs = True
# driver = webdriver.Firefox(firefox_profile=profile, executable_path='.\geckodriver.exe')

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(chrome_options=options)


class Ruckus:
    logon_url = 'https://wifi.cvl.com.tw/admin/login.jsp'
    dashboard_url = 'https://wifi.cvl.com.tw/admin/dashboard.jsp'
    conf_acl_url = 'https://wifi.cvl.com.tw/admin/conf_acls.jsp'
    data_sync_time = 4

    def __init__(self, username, password):
        self.macs = {}
        self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1024, 768)

        self.driver.get(self.__class__.logon_url)
        self.driver.find_element_by_css_selector('[name="username"]').send_keys(username)
        self.driver.find_element_by_css_selector('[name="password"]').send_keys(password)
        self.driver.find_element_by_css_selector('[name="ok"]').click()
        time.sleep(self.__class__.data_sync_time)  # wait for the authentication page to be loaded.

    def add_mac(self, mac, acl_list=None):
        if acl_list is None:
            acl_list = self.get_acls()[-1]
        else:
            acl_list = acl_list

        if not self.exist_mac(mac):
            self.driver.get(self.__class__.conf_acl_url)  # go to configuration page.
            self.driver.find_element_by_css_selector(f'[id="{acl_list}"]').click()
            self.driver.find_element_by_css_selector(f'[id="mac"]').send_keys(mac)
            self.driver.find_element_by_css_selector('[id="create-new-station"]').click()
            self.driver.find_element_by_css_selector('[id="ok-acl"]').click()
            time.sleep(self.__class__.data_sync_time)  # wait for the data to be synced.
            return True
        else:
            return False

    def add_macs(self, macs, acl_list=None):
        acl_list = acl_list or self.get_acls()[-1]
        macs = self.exist_macs(macs)
        added_macs = ()
        not_added_macs = ()
        add_mac_condition = True

        for mac, v in macs.items():
            add_mac_condition = add_mac_condition and v
            if v:
                not_added_macs += mac,
            else:
                added_macs += mac,

        if not add_mac_condition:
            self.driver.get(self.__class__.conf_acl_url)  # go to configuration page
            self.driver.find_element_by_css_selector(f'[id="{acl_list}"]').click()  # the last acl list
            for mac in added_macs:
                self.driver.find_element_by_css_selector(f'[id="mac"]').send_keys(mac)  # fill out mac
                self.driver.find_element_by_css_selector('[id="create-new-station"]').click()  # 'create button'
            self.driver.find_element_by_css_selector('[id="ok-acl"]').click()
            time.sleep(self.__class__.data_sync_time)  # wait for the data to be synced.
        else:
            pass
        return {'added_macs': added_macs, 'not_added_macs': not_added_macs}

    def _remove_mac(self, mac):
        acl_list = self.exist_mac(mac)
        if acl_list:
            self.driver.get(self.__class__.conf_acl_url)  # go to configuration page.
            self.driver.find_element_by_css_selector(f'[id="{acl_list}"]').click()
            macs_location = self.driver.find_element_by_css_selector('#staTable').find_elements_by_tag_name('td')
            for location in macs_location:
                if location.text == mac:
                    delete_index = macs_location.index(location) + 1
                    macs_location[delete_index].find_element_by_css_selector('span#delete').click()
                    break
            else:
                pass
            self.driver.find_element_by_css_selector('[id="ok-acl"]').click()
            time.sleep(self.__class__.data_sync_time)  # wait for the data to be synced.
            return True
        else:
            return False

    def get_macs(self):
        self.driver.get(self.__class__.conf_acl_url)  # go to configuration page.
        for acl in self.get_acls():  # loop through acl list.
            self.driver.find_element_by_css_selector(f'[id="{acl}"]').click()  # click "EDIT" button.
            macs = self.driver.find_element_by_css_selector('#staTable').text  # get MACs.
            filtered_macs = tuple(macs.replace(' delete', '').replace('\n', ' ').lower().split(' '))  # filter out unwanted charactors.
            self.macs.setdefault(acl, filtered_macs)  # put MACs into dictionary with acl as key.
        return self.macs

    def exist_mac(self, mac):
        self.macs = self.macs or self.get_macs()
        for k, v in self.macs.items():  # loop through MAC list.
            if mac.lower() in v:  # if target mac in the MAC list.
                return k  # return acl.
        return None

    def exist_macs(self, macs):
        exist_macs_ = {}  # use dict so it supports de-duplicated macs.
        for mac in self.clean_macs(macs):
            exist_mac_ = self.exist_mac(mac)
            if exist_mac_:
                exist_macs_.setdefault(mac, exist_mac_)
            else:
                exist_macs_.setdefault(mac, False)
        return exist_macs_

    def get_acls(self):
        self.driver.get(self.__class__.conf_acl_url)  # go to configuration page.
        acl_objs = self.driver.find_element_by_css_selector('table#acl.listTable > tbody').find_elements_by_css_selector('td.action > span')  # get acl lists.
        return tuple([i.get_attribute('id') for i in acl_objs if 'edit' in i.get_attribute('id')])  # filter out unwanted charactors.

    @staticmethod
    def clean_macs(macs):
        macs = (type(macs) == str) and [macs] or macs  # support single MAC.
        return tuple([mac.lower() for mac in macs])  # lowering MACs.

    def __repr__(self):
        # todo: return something.
        return f'{self.driver.title}'

    def __del__(self):
        return self.driver.quit()

    # todo: when acl list is full.

    # todo: check if received mac is legal


def timing(origin_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = origin_func(*args, **kwargs)
        print(f'{round(time.time() - start_time)} seconds.')
        return f
    return wrapper


@timing
def main():
    RUCKUS_USER = os.environ.get('RUCKUS_USER') or input('ruckus username: ')
    RUCKUS_PASS = os.environ.get('RUCKUS_PASS') or getpass('ruckus passowrd: ')
    mac = 'ff:ff:ff:ff:ff:ff', 'bb:bb:bb:bb:bb:bb', 'E0:AA:96:11:21:08', 'E0:AA:96:11:21:08','aa:aa:aa:aa:aa:aa', 'cc:cc:cc:cc:cc:cc', 'E0:AA:96:11:21:01', 'E0:AA:96:11:21:02', 'E0:AA:96:11:21:08'


if __name__ == '__main__':
    main()

