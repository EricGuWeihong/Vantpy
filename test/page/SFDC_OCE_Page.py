#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage
from utils.logger import Logger
import sys

sys.path.append('../')
logger = Logger(logger='SFDC_OCE_Page').getlog()


class SFDC_OCE_Page(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    username_loc = (By.ID, "username")  # 定位用户名
    password_loc = (By.ID, "password")  # 定位密码
    errmsg_loc = (By.ID, "error")  # 定位错误信息
    login_btn = (By.ID, "Login")  # 定位登录按钮
    cancel_chgpsw_btn = (By.ID, "cancel-button")  # 定位取消更改密码按钮
    news_loc = (By.ID, "MessageTitle0")  # 定位消息栏
    menus_loc = (By.XPATH, "//span[@class='slds-truncate']")  # 定位菜单栏
    components_loc = (By.XPATH, "//h2[@class='title']")  # 定位标准组件
    dashboard_loc = (By.XPATH, "//div[@class='slds-page-header__name-title']/h1/span")  # 定位仪表板
    project_loc = (By.XPATH, "//div[@class='gridHeader truncation'][@title='Pilot项目状态']")  # 定位项目状态
    frame_loc = (By.TAG_NAME, "iframe")  # 定位iframe子框架
    tab_acct_loc = (By.XPATH, "//a[@title='客户']")  # 定位客户菜单
    all_acct_loc = (By.XPATH, "//span[@class='slds-truncate'][@title='所有客户']")  # 定位所有客户标题
    acct_type_p_loc = (By.XPATH,
                       "//lightning-base-combobox[@lightning-combobox_combobox=''][@class='slds-combobox_container']")  # 定位客户类型父级下拉框
    acct_type_c_loc = (By.XPATH, "//lightning-base-combobox-item[@role='option']/span/span")  # 定位客户类型子级下拉选项
    acct_view_p_loc = all_acct_loc
    acct_view_c_loc = (By.XPATH, "//li[@class='uiMenuItem'][@role='presentation']/a/div")  # 定位客户视图子级下拉选项
    hco_list_p_loc = (By.TAG_NAME, "tbody")
    hco_list_c_loc = (By.XPATH, "//td[@class='slds-cell-wrap']/a[@dir='ltr']")
    more_opt_btn = (By.XPATH, "//button[@class='slds-button slds-button_icon-border']")  # 定位更多操作按钮
    # loading_spinner_loc = (By.XPATH, "//lightning-spinner[@class='slds-spinner_container']")  # 定位加载图标
    loaded_spinner_loc = (By.XPATH, "//lightning-spinner[@class='slds-spinner_container slds-hide']")  # 定位加载完成
    hco_name_loc = (By.XPATH,
                    "//div[@class='testonly-outputNameWithHierarchyIcon slds-grid sfaOutputNameWithHierarchyIcon']/span[@class='custom-truncate uiOutputText']")
    hco_tab_p_loc = (By.XPATH, "//lightning-tab-bar/ul[@role='tablist'][@class='slds-tabs_default__nav']")
    hco_tab_c_loc = (By.XPATH, "//li[@role='presentation']")
    hco_detail_p_loc = (By.XPATH, "//div[@force-recordlayoutsection_recordlayoutsection=''][@class='slds-form']")
    hco_detail_c_loc = (By.XPATH, "//span[@force-recordlayoutitem_recordlayoutitem=''][@class='test-id__field-label']")

    hco_subtab_asso_loc = (By.XPATH, "//a[@id='customTab2__item']")  # HCO关联信息subtab
    hco_subtab_history_loc = (By.XPATH, "//a[@id='customTab3__item']")  # HCO互动历史
    hco_subtab_relatedObj_loc = (By.XPATH, "//a[@id='customTab4__item']")  # 相关对象列表

    associated_hco_p_loc = (By.TAG_NAME, "tbody")
    associated_hco_c_loc = (By.XPATH, "//td[@scope='row']/div/span/span[3]")


    def input_username(self, text):
        self.send_key(self.username_loc, text)

    def input_password(self, text):
        self.send_key(self.password_loc, text)

    def click_login_btn(self):
        self.click(self.login_btn)

    def click_cancel_chgpsw_btn(self):
        self.click(self.cancel_chgpsw_btn)

    def get_errmsg(self):
        return self.get_text(self.errmsg_loc)

    def find_news(self):
        return self.get_text(self.news_loc)

    def get_menus(self):
        menu_list = []
        for element in self.find_elements(*self.menus_loc):
            if element.text != "OCE":
                menu_list.append(element.text)
        logger.info("获取菜单栏列表")
        # print(menu_list)
        return menu_list

    def get_components(self):
        component_list = []
        for element in self.find_elements(*self.components_loc):
            component_list.append(element.text.split(" ")[0])  # 截断标题中的数字
        self.driver.switch_to.frame(self.find_element(*self.frame_loc))
        component_list.append(self.find_element(*self.dashboard_loc).text)
        component_list.append(self.find_element(*self.project_loc).text)
        logger.info("获取页面组件列表")
        # print(component_list)
        return component_list

    def open_acct_tab(self):
        url = self.get_attribute(self.tab_acct_loc, "href")
        logger.info("打开并跳转 - 客户 URL: %s" % url)
        self.driver.get(url)
        return self.get_text(self.all_acct_loc)

    def get_picklist_values(self, parent_loc, child_loc, select_value=None, select_numb=None, extend_required=True):
        if extend_required:
            self.click(parent_loc)  # 点击展开下拉框
            # logger.info("点击并展开下拉框")
        select = self.find_element(*parent_loc)
        options_list = select.find_elements(*child_loc)
        # print(self.get_text(child_loc))
        if select_value is None and select_numb is None:
            value_list = []
            for option in options_list:
                # print("Option: ", option.text)
                if len(option.text) > 0:
                    value_list.append(option.text)
            logger.info("获取列表中的全部值")
            # print(value_list)
            return value_list
        else:
            seq_no = 0
            option = None
            for option in options_list:
                if select_value == option.text or select_numb == seq_no:
                    break
                seq_no += 1
            if select_value is not None:
                logger.info("返回列表中指定值 %s 的对象" % select_value)
            else:
                logger.info("返回列表中指定序列 %d 的对象" % select_numb)
            return option

    def get_acct_types(self):
        acct_type_list = self.get_picklist_values(self.acct_type_p_loc, self.acct_type_c_loc)
        logger.info("获取客户类型列表")
        # print(acct_type_list)
        return acct_type_list

    def get_acct_view(self):
        acct_view_list = self.get_picklist_values(self.acct_view_p_loc, self.acct_view_c_loc)
        logger.info("获取客户视图列表")
        # print(acct_view_list)
        return acct_view_list

    def switch_to_hco(self):
        selected = self.get_picklist_values(self.acct_type_p_loc, self.acct_type_c_loc, "HCO")
        selected.click()
        self.wait_for_loading()
        hco_list = self.get_picklist_values(self.hco_list_p_loc, self.hco_list_c_loc, extend_required=False)
        logger.info("切换客户类型至 HCO")

    def wait_for_loading(self):
        self.sleep(2)
        self.is_located(self.loaded_spinner_loc)
        logger.info("等待Loading画面结束")

    def click_hco_name(self, hco):
        if str(hco).isdigit:
            logger.info("选择并点击列表中 序列为 %s 的HCO" % hco)
            selected = self.get_picklist_values(self.hco_list_p_loc, self.hco_list_c_loc, select_numb=hco,
                                                extend_required=False)
        else:
            logger.info("选择并点击列表中 名称为 %s 的HCO" % hco)
            selected = self.get_picklist_values(self.hco_list_p_loc, self.hco_list_c_loc, select_value=hco,
                                                extend_required=False)
        selected_hco_name = selected.text
        selected.click()
        self.wait_for_loading()
        return selected_hco_name

    def get_hco_tab_list(self):
        hco_tab_list = self.get_picklist_values(self.hco_tab_p_loc, self.hco_tab_c_loc, extend_required=False)
        logger.info("获取客户选项卡列表")
        return hco_tab_list

    def switch_to_default(self):
        pass

    def get_detail_field(self):
        detail_field_list = self.get_picklist_values(self.hco_detail_p_loc, self.hco_detail_c_loc,
                                                     extend_required=False)
        logger.info("获取客户详情页面字段列表")
        return detail_field_list

    def switch_to_associate(self):
        self.click(self.hco_subtab_asso_loc)

    def switch_to_history(self):
        self.click(self.hco_subtab_history_loc)

    def switch_to_related(self):
        self.click(self.hco_subtab_relatedObj_loc)

