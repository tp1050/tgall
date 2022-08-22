from helper import tprint, disp



# class Flask_Config:
#     sandogh={}
#     def __init__(self,**kwargs):
#         self._sandogh = {}
#         self.sandogh.update(kwargs)
#     def __str__(self):
#         return str(self.sandogh)

class Flask_Config:
    def __init__(self,**kwargs):
        # self._sandogh = {}
        print(kwargs)
        self.__dict__.update(kwargs)
    def __getattr__(self, name):
        return self.__dict__.get(name,None)
    def __setattr__(self, name, value):
        self.__dict__[name]=value



class Conf1(Flask_Config):
    def __init__(self,**kwargs):
        from koon import lan_ip
        super().__init__(INSTANCE_RELATIVE_CONFIG = True, IMAGE_EXTS = ["*.png", "*.jpg", "*.jpeg","*.gif", "*.tiff"],SERVER_IP=lan_ip(),SERVER_NAME="7270.dool.dool:8989",SECRET_KEY='12345678')
        self.__dict__.update(kwargs)
#
# class Flask_Config2:
#     def __init__(self,**kwargs):
#
#         self.__dict__.update(kwargs)
#     def __str__(self):
#         return ""
#
#
# class Flask_conf12(Flask_Config):
#     def __init__(self):
#         from koon import lan_ip
#         super().__init__(instance_relative_config = True, IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".gif", ".tiff"],
#         SERVER_NAME=f"{lan_ip()}:8456")
#     def sandoghech(self):
#         return ""
# #
# #
# #
# # class Flask_conf11(Flask_Config):
# #     def __init__(self):
# #         from koon import lan_ip
# #         super().__init__(instance_relative_config = True, IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".gif", ".tiff"],
# #         SERVER_NAME=f"{lan_ip()}:8456")
# #     def sandoghech(self):
# #         return self.sandogh
# #
# # # class Flask_conf2(Flask_Config):
# # #     from koon import lan_ip
# # #     def __init__(self):
# # #         Flask_Config.__init__(self)
# # #
# # #     # @property
# # #     def get_attrr(self):
# # #         return self._sandogh
# #
# #     # @get_attrr.setter
# #     # def get_attrr(self, **kwargs):
# #     #     self._sandogh.update(kwargs)
# #     #
# #     # @get_attrr.deleter
# #     # def get_attrr(self, keys_to_remove: dict):
# #     #     for k in keys_to_remove:
# #     #         self._sandogh.pop(k)
# #
# # class Flask_conf3(Flask_Config):
# #     from koon import lan_ip
# #     def __init__(self):
# #         Flask_Config.__init__(self)
# #
# #     def getter(self, *args):
# #         l=list()
# #         for i in args:
# #             l.append(self._sandogh[i])
# #         return l
# #
# #     def setter(self, **kwargs):
# #         ret = self._sandogh.update(kwargs)
# #         return self._sandogh
# #
# #     def deleter(self, keys_to_remove):
# #         for k in keys_to_remove:
# #             self._sandogh.pop(k)
# #
# #
# # # instance_relative_config = True,
# # # IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".gif", ".tiff"],
# # # SERVER_NAME=f"{lan_ip()}:8456")
# # print('--------------------------------------------')
# # f=Flask_conf3()
# # print(f.setter(instance_relative_config = True,IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".gif", ".tiff"]))
# # f.deleter(keys_to_remove=['instance_relative_config'])
# # f.getter('instance_relative_config')
# # # print(f._sandogh)
# # # print(f)
